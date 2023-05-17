import bigquery_mock.bigquery_mock 

BIKESHARE_NAME_STATUS_ADDRESS = [   [   ('name', '10th & Red River'),
        ('status', 'active'),
        ('address', '699 East 10th Street')],
    [   ('name', '11th & Salina'),
        ('status', 'active'),
        ('address', '1705 E 11th St')]]


class Client(bigquery_mock.bigquery_mock.Client):

    def __init__(self):
        super().__init__()
        self.register_data(key = 'bikeshare-name-status-address', data =BIKESHARE_NAME_STATUS_ADDRESS)
        
