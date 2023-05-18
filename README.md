# py-bigquery-mock
pip install py-bigquery-mock

```python

import data_mock.google.cloud.client

class Client(data_mock.google.cloud.client.Client):

    def __init__(self):
        mock_data = [
                [('key', 'value')
                    ]
                ]
        super().__init__(mock_data = mock_data)


SQL = "Any string, since we are mocking"
bigquery_client = Client()
results = bigquery_client.query(SQL)  
for i in results:
    #i is a generator
    for j in i.items():
        print(j) #('key', 'value')

#other methods work
bigquery_client = Client()
results = bigquery_client.query(SQL)  
for i in results:
    value = i.get('key')
    print(value)#value

#defining data or query
#not the hint in the form: py-bigquery-mock-register: <key>
SQL="""
            /*
            py-bigquery-mock-register: bikeshare-name-status-address

            */
        SELECT
      name, status, address
    FROM
      `bigquery-public-data.austin_bikeshare.bikeshare_stations`
      order by name, status, address
    LIMIT
      2
"""
#now regiseter the data
    
class Client(data_mock.google.cloud.client.Client):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.register_mock_data(key = 'bikeshare-name-status-address', 
        # two rows of data
        mock_data =[   
                    [   ('name', '10th & Red River'),
                        ('status', 'active'),
                        ('address', '699 East 10th Street')],
                    [   ('name', '11th & Salina'),
                        ('status', 'active'),
                        ('address', '1705 E 11th St')]]

                )

bigquery_client = Client()
results = bigquery_client.query(SQL)  
for i in results:
    #i is a generator
    for j in i.items():
        print(j) 
        #('name', '10th & Red River')
        #('status', 'active')
        #('address', '699 East 10th Street')
        #('name', '11th & Salina')
        #('status', 'active')
        #('address', '1705 E 11th St')

```
