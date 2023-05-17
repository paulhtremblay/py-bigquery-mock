import unittest

from google.cloud import bigquery

def get_sql():
        return """
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

def items_func_with_result_all(client, sql):
    row_iter = client.query(sql).result()
    final = []
    for i in row_iter:
        temp = []
        for j in i.items():
            temp.append(j)
        final.append(temp)
    return final

class TestResults(unittest.TestCase):

    def test_items_first_result_returns_3_correct_name_values(self):
        client = bigquery.Client()
        f = items_func_with_result_all(client = client, sql = get_sql())
        needed = [[('name', '10th & Red River'), ('status', 'active'), ('address', '699 East 10th Street')], [('name', '11th & Salina'), ('status', 'active'), ('address', '1705 E 11th St')]]
        self.assertEqual(f, needed)

if __name__ == '__main__':
    unittest.main()
