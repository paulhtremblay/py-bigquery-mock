import sys
sys.path.append('.')
import unittest

from data_mock.google.cloud.bigquery import Client
from data_mock.google.cloud.bigquery import InvalidMockData
from data_mock.google.cloud.bigquery import Table
from data_mock.google.cloud.bigquery import SchemaField
from data_mock.google.cloud.bigquery import QueryJobConfig


DATA1= [
        [('name', 'State Capitol @ 14th & Colorado'),
        ('status', 'closed'),
        ('address', '206 W. 14th St.')],
        [('name', 'Bullock Museum @ Congress & MLK'),
        ('status', 'closed'),
        ('address', '1881 Congress Ave.'),
        ]
]

def get_sql():
        return """
        SELECT
      name, status, address
    FROM
      `bigquery-public-data.austin_bikeshare.bikeshare_stations`
    LIMIT
      2
        """

def items_func_with_result_all(bq_client, sql):
    row_iter = bq_client.query(sql).result()
    final = []
    for i in row_iter:
        temp = []
        for j in i.items():
            temp.append(j)
        final.append(temp)
    return final

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

def get_func_no_key(bq_client, sql):
    row_iter = bq_client.query(sql)
    final = []
    for i in row_iter:
        final.append(i.get('name'))
    return final

def get_func_with_key(bq_client, sql):
    row_iter = bq_client.query(sql)
    final = []
    for i in row_iter:
        final.append(i.get('name'))
    return final

def get_func_with_key_with_result(bq_client, sql):
    row_iter = bq_client.query(sql).result()
    final = []
    for i in row_iter:
        final.append(i.get('name'))
    return final

def values_func_with_key_with_result(bq_client, sql):
    row_iter = bq_client.query(sql).result()
    final = []
    for i in row_iter:
        final.append(i.values())
    return final

def keys_func_with_key_with_result(bq_client, sql):
    row_iter = bq_client.query(sql).result()
    final = []
    for i in row_iter:
        final.append(i.keys())
    return final

class TestResults(unittest.TestCase):

    def test_items_first_result_returns_3_correct_name_values(self):
        client = Client(mock_data = DATA1)
        f = items_func_with_result(bq_client = client, sql = get_sql())
        self.assertTrue(f[0], ('name', 'State Capitol @ 14th & Colorado'))
        self.assertTrue(f[1], ('status', 'closed'))
        self.assertTrue(f[2], ('address', '206 W. 14th St.'))

    def test_items_first_result_not_using_result_method_returns_3_correct_name_values(self):
        client = Client(mock_data = DATA1)
        f = items_func_not_use_result(bq_client = client, sql = get_sql())
        self.assertTrue(f[0], ('name', 'State Capitol @ 14th & Colorado'))
        self.assertTrue(f[1], ('status', 'closed'))
        self.assertTrue(f[2], ('address', '206 W. 14th St.'))

    def test_items_no_values_returns_empty_list(self):
        client = Client()
        f = items_func_with_result(bq_client = client, sql = get_sql())
        self.assertEqual(f, [])

    def test_get_name_returns_2_correct_names(self):
        client = Client(mock_data = DATA1)
        f = get_func_no_key(bq_client = client, sql = get_sql())
        self.assertEqual(f, ['State Capitol @ 14th & Colorado', 'Bullock Museum @ Congress & MLK'])
        
    def test_get_name_with_key_word_arg_returns_2_correct_names(self):
        client = Client(mock_data = DATA1)
        f = get_func_with_key(bq_client = client, sql = get_sql())
        self.assertEqual(f, ['State Capitol @ 14th & Colorado', 'Bullock Museum @ Congress & MLK'])

    def test_get_name_with_key_word_arg_and_result_method_returns_2_correct_names(self):
        client = Client(mock_data = DATA1)
        f = get_func_with_key_with_result(bq_client = client, sql = get_sql())
        self.assertEqual(f, ['State Capitol @ 14th & Colorado', 'Bullock Museum @ Congress & MLK'])

    def test_values_returns_2_correct_values(self):
        client = Client(mock_data = DATA1)
        f = values_func_with_key_with_result(bq_client = client, sql = get_sql())
        self.assertEqual(f[0], ('State Capitol @ 14th & Colorado', 'closed', '206 W. 14th St.'))

    def test_keys_returns_correct_keys_first_result(self):
        client = Client(mock_data = DATA1)
        f = keys_func_with_key_with_result(bq_client = client, sql = get_sql())
        self.assertTrue(list(f[0]), ['name', 'status', 'address'])

    def test_not_a_list_data_raises_InvalidData(self):
        self.assertRaises(InvalidMockData, Client, mock_data = 1)

    def test_not_a_list_in_list_data_raises_InvalidData(self):
        data = [[('name', 'value',),], 1] 
        self.assertRaises(InvalidMockData, Client, mock_data = data)

    def test_create_table_succeeds(self):
        table_id = 'project.dataset_id.tabele_id'
        schema = [
            SchemaField("full_name", "STRING", mode="REQUIRED"),
            SchemaField("age", "INTEGER", mode="REQUIRED"),
        ]
        client = Client()
        table = Table(table_ref = table_id, schema=schema)
        client.create_table(table)
        self.assertTrue(hasattr(table, 'project') and hasattr(table, 'table_id') and hasattr(table, 'dataset_id'))
        self.assertTrue(len(table.mock_tables) == 1)

    def test_create_table_as_string_succeeds(self):
        table_id = 'project.dataset_id.table_id'
        client = Client()
        table = client.create_table(table = table_id)
        self.assertTrue(hasattr(table, 'project') and hasattr(table, 'table_id') and hasattr(table, 'dataset_id'))
        self.assertTrue(len(table.mock_tables) == 1)

    def test_register_data_reads_right_data(self):
        client = Client()
        mock_data = [
            [('data1-test', 'found')],
            ]
        client.register_mock_data(key = 'data1', mock_data =mock_data)
        sql = """
            /*
            py-bigquery-mock-register: data1

            */
            SELECT 
            f FROM Table
            """
        f = items_func_with_result_all(bq_client = client, sql = sql)
        self.assertEqual(f, mock_data)

    def test_query_works_with_config(self):
        job_config = QueryJobConfig(destination='mock-table-id')
        client = Client(mock_data = DATA1)
        sql = """
    SELECT corpus
    FROM `bigquery-public-data.samples.shakespeare`
    GROUP BY corpus;
"""

        query_job = client.query(sql, job_config=job_config)  

if __name__ == '__main__':
    unittest.main()
