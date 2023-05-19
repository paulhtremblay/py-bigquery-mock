from . import exceptions
from .  import table

class Client:

    def __init__(self, project = None, mock_data = [], *args, **kwargs):
        self._test_valid_data(mock_data)
        self.__data = mock_data
        self.project = project
        self.__registered_data = {}

    def register_mock_data(self, key, mock_data):
        self._test_valid_data(mock_data)
        self.__registered_data[key] = mock_data

    def query(self, query, *args, **kwargs):
        key = self._get_sql_key(query)
        if key:
            data = self.__registered_data.get(key)
            if not data:
                raise exceptions.InvalidMockData(f'{key} not found in registered_data')
        else:
            data = self.__data
        return table.RowIterator(data = data)

    def create_table(self, table):
        return table

    def delete_table(self, table_id, not_found_ok=False):
        pass

    def _get_sql_key(self, query):
        for line in query.split('\n'):
            if 'py-bigquery-mock-register:' in line:
                fields = line.split(':')
                if len(fields) != 2:
                    raise exceptions.InvalidMockData('hint should be in format "py-bigquery-mock-register: key"')
                return fields[1].strip()

    def _test_valid_data(self, data):
        if not isinstance(data, list):
            raise exceptions.InvalidMockData(f'{data} is not a list')
        errors = []
        for n, i in enumerate(data):
            if not isinstance(i, list):
                errors.append((n, i, 'not a list'))
        if len(errors) != 0:
            raise exceptions.InvalidMockData(errors)
