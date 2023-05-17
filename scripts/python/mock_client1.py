import bigquery_mock.bigquery_mock as Mock

BIKESHARE_NAME_STATUS_ADDRESS = [   [   ('name', '10th & Red River'),
        ('status', 'active'),
        ('address', '699 East 10th Street')],
    [   ('name', '11th & Salina'),
        ('status', 'active'),
        ('address', '1705 E 11th St')]]


class Client(Mock.Client):

    def __init__(self):
        data = [
                [('key', 'value')
                    ]
                ]
        super().__init__(data)
        self.register_data(key = 'bikeshare-name-status-address', data =BIKESHARE_NAME_STATUS_ADDRESS)
        
