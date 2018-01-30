import unittest

import main


class RoutesResponseCorrectlyTestCase(unittest.TestCase):

    def test_index(self):
        tester = main.app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The Artificial Intelligence Of Fish', response.data)

    def test_add_supervisioned_data(self):
        tester = main.app.test_client(self)
        response = tester.get('/add_supervisioned_data', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_show_dataset(self):
        tester = main.app.test_client(self)
        response = tester.get('/show_dataset', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_fish_ai(self):
        tester = main.app.test_client(self)
        response = tester.get('/fish_ai', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_api_load_image_to_cloud(self):
        tester = main.app.test_client(self)
        response = tester.post('/api/load_image_to_cloud', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_api_load_data_from_cloud(self):
        tester = main.app.test_client(self)
        response = tester.post('/api/load_data_from_cloud',
                               data='{"name":"0.json","size":125874}',
                               content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'image', response.data)
        self.assertIn(b'specie', response.data)
        self.assertIn(b'name', response.data)


if __name__ == '__main__':
    unittest.main()
