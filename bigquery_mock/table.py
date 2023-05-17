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
