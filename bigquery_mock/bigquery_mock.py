class InvalidData(Exception):
    pass

class SchemaField:

    def __init__(self):
        self.field_type = None

class RowIterator:

    def __init__(self, data):
        self.counter = 0
        self.total_rows = len(data)
        self.data = data
        self.schema = [SchemaField()]

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter< self.total_rows:
            self.counter += 1
            return Row(row = self.data[self.counter -1])
        else:
            raise StopIteration

    def result(self):
        return self

class Row():

    def __init__(self, row):
        self.info = {}
        l = []
        for i in row:
            self.info[i[0]] = i[1]
            l.append(i[1])
        self._values = tuple(l)
        self.row = row

    def get(self, *args, **kwargs):
        if args:
            return self.info.get(args[0])
        return self.info.get(kwargs['key'])

    def items(self, *args, **kwargs):
        for i in self.row:
            yield i

    def values(self, *args, **kwargs):
        return self._values

    def keys(self, *args, **kwargs):
        return self.info.keys()

class BigQueryMock:

    def _test_valid_data(self):
        if not isinstance(self.data, list):
            raise InvalidData(f'{self.data} is not a list')
        errors = []
        for n, i in enumerate(self.data):
            if not isinstance(i, list):
                errors.append((n, i, 'not a list'))
        if len(errors) != 0:
            raise InvalidData(errors)


    def __init__(self, data = []):
        self.data = data
        self._test_valid_data()

    def query(self, *args, **kwargs):
        return RowIterator(data = self.data)

