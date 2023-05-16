import sys
sys.path.append('.')

import unittest

import bigquery_mock
from bigquery_mock import InvalidData

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

def get_sql():
        return """
        SELECT
      name, status, address
    FROM
      `bigquery-public-data.austin_bikeshare.bikeshare_stations`
    LIMIT
      2
        """


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
        client = bigquery_mock.Client(data = DATA1)
        f = items_func_with_result(bq_client = client, sql = get_sql())
        self.assertTrue(f[0], ('name', 'State Capitol @ 14th & Colorado'))
        self.assertTrue(f[1], ('status', 'closed'))
        self.assertTrue(f[2], ('address', '206 W. 14th St.'))

    def test_items_first_result_not_using_result_method_returns_3_correct_name_values(self):
        client = bigquery_mock.Client(data = DATA1)
        f = items_func_not_use_result(bq_client = client, sql = get_sql())
        self.assertTrue(f[0], ('name', 'State Capitol @ 14th & Colorado'))
        self.assertTrue(f[1], ('status', 'closed'))
        self.assertTrue(f[2], ('address', '206 W. 14th St.'))

    def test_items_no_values_returns_empty_list(self):
        client = bigquery_mock.Client()
        f = items_func_with_result(bq_client = client, sql = get_sql())
        self.assertEqual(f, [])

    def test_get_name_returns_2_correct_names(self):
        client = bigquery_mock.Client(data = DATA1)
        f = get_func_no_key(bq_client = client, sql = get_sql())
        self.assertEqual(f, ['State Capitol @ 14th & Colorado', 'Bullock Museum @ Congress & MLK'])
        
    def test_get_name_with_key_word_arg_returns_2_correct_names(self):
        client = bigquery_mock.Client(data = DATA1)
        f = get_func_with_key(bq_client = client, sql = get_sql())
        self.assertEqual(f, ['State Capitol @ 14th & Colorado', 'Bullock Museum @ Congress & MLK'])

    def test_get_name_with_key_word_arg_and_result_method_returns_2_correct_names(self):
        client = bigquery_mock.Client(data = DATA1)
        f = get_func_with_key_with_result(bq_client = client, sql = get_sql())
        self.assertEqual(f, ['State Capitol @ 14th & Colorado', 'Bullock Museum @ Congress & MLK'])

    def test_values_returns_2_correct_values(self):
        client = bigquery_mock.Client(data = DATA1)
        f = values_func_with_key_with_result(bq_client = client, sql = get_sql())
        self.assertEqual(f[0], ('State Capitol @ 14th & Colorado', 'closed', '206 W. 14th St.'))

    def test_keys_returns_correct_keys_first_result(self):
        client = bigquery_mock.Client(data = DATA1)
        f = keys_func_with_key_with_result(bq_client = client, sql = get_sql())
        self.assertTrue(list(f[0]), ['name', 'status', 'address'])

    def test_not_a_list_data_raises_InvalidData(self):
        self.assertRaises(InvalidData, bigquery_mock.Client, data = 1)

    def test_not_a_list_in_list_data_raises_InvalidData(self):
        data = [[('name', 'value',),], 1] 
        self.assertRaises(InvalidData, bigquery_mock.Client, data = data)

    def test_create_table_raises_error(self):
        table_id = 'project.dataset_id.tabele_id'
        schema = [
            bigquery_mock.SchemaField("full_name", "STRING", mode="REQUIRED"),
            bigquery_mock.SchemaField("age", "INTEGER", mode="REQUIRED"),
        ]
        client = bigquery_mock.Client()
        table = bigquery_mock.Table(table_id = table_id, schema=schema)
        print(
            "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
        )
        
if __name__ == '__main__':
    unittest.main()
