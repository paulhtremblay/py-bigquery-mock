import sys
sys.path.append('.')
import unittest
import bigquery_mock


from google.cloud import bigquery
DATA1= [
        [('name', 'State Capitol @ 14th & Colorado'),
        ('status', 'closed'),
        ('address', '206 W. 14th St.')],
        [('name', 'Bullock Museum @ Congress & MLK'),
        ('status', 'closed'),
        ('address', '1881 Congress Ave.'),
        ]
]

def items_func_with_result(bq_client, sql):
    row_iter = bq_client.query(sql).result()
    final = []
    for i in row_iter:
        for j in i.items():
            final.append(j)
        break
    return final

def items_func_not_use_result(bq_client, sql):
    row_iter = bq_client.query(sql)
    final = []
    for i in row_iter:
        for j in i.items():
            final.append(j)
        break
    return final


class TestResults(unittest.TestCase):

    def test_items1(self):

        sql = """
        SELECT
      name, status, address
    FROM
      `bigquery-public-data.austin_bikeshare.bikeshare_stations`
    LIMIT
      2
        """
        client = bigquery_mock.BigQueryMock(data = DATA1)
        #client = bigquery.Client()
        f = items_func_with_result(bq_client = client, sql = sql)
        self.assertTrue(f[0], ('name', 'State Capitol @ 14th & Colorado'))
        self.assertTrue(f[1], ('status', 'closed'))
        self.assertTrue(f[2], ('address', '206 W. 14th St.'))

    def test_items2(self):

        sql = """
        SELECT
      name, status, address
    FROM
      `bigquery-public-data.austin_bikeshare.bikeshare_stations`
    LIMIT
      2
        """
        client = bigquery_mock.BigQueryMock(data = DATA1)
        #client = bigquery.Client()
        f = items_func_not_use_result(bq_client = client, sql = sql)
        self.assertTrue(f[0], ('name', 'State Capitol @ 14th & Colorado'))
        self.assertTrue(f[1], ('status', 'closed'))
        self.assertTrue(f[2], ('address', '206 W. 14th St.'))
        
if __name__ == '__main__':
    unittest.main()
