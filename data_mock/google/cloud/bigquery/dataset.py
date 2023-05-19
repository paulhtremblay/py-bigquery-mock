class DatasetReference():

    def __init__(self,  project, dataset_id):
        self.project = project
        self.dataset_id = dataset_id

    def table(self, table_id, *args, **kwargs):
        #makes a table_ref
        self.table_id = table_id
        return self
        _table_id = f'{self.project}.{self.dataset_id}.{table_id}'
        return _table_id
