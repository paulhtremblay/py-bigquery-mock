from . import schema

class Table:

    def _get_table_info(self, table_id):
        if not isinstance(table_id, str):
            raise InvalidData('table id must be str')
        fields = table_id.split('.')
        if len(fields) != 3:
            raise InvalidData('table id must be in format "project_id.dataset_id.table_id"')
        self.project = fields[0]
        self.dataset_id= fields[1]
        self.table_id = fields[2]


    def __init__(self, table_id, schema):
        self._get_table_info(table_id)
        self.schema = schema


class Row():

    def __init__(self, row):
        self.__info = {}
        l = []
        for i in row:
            self.__info[i[0]] = i[1]
            l.append(i[1])
        self.__values = tuple(l)
        self.row = row

    def get(self, *args, **kwargs):
        if args:
            return self.__info.get(args[0])
        return self.__info.get(kwargs['key'])

    def items(self, *args, **kwargs):
        for i in self.row:
            yield i

    def values(self, *args, **kwargs):
        return self.__values

    def keys(self, *args, **kwargs):
        return self.__info.keys()

class RowIterator:

    def __init__(self, data):
        self.__counter = 0
        self.total_rows = len(data)
        self.__data = data
        self.schema = [schema.SchemaField(name = 'todo', field_type='INTEGER')]

    def __iter__(self):
        return self

    def __next__(self):
        if self.__counter< self.total_rows:
            self.__counter += 1
            return Row(row = self.__data[self.__counter -1])
        else:
            raise StopIteration

    def result(self):
        return self

