import data_mock.google.cloud.client

BIKESHARE_NAME_STATUS_ADDRESS = [   [   ('name', '10th & Red River'),
        ('status', 'active'),
        ('address', '699 East 10th Street')],
    [   ('name', '11th & Salina'),
        ('status', 'active'),
        ('address', '1705 E 11th St')]]


class Client(data_mock.google.cloud.client.Client):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.register_mock_data(key = 'bikeshare-name-status-address', mock_data =BIKESHARE_NAME_STATUS_ADDRESS)
        
