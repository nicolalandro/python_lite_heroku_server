import unittest

import main


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        """inital test. ensure flask was set up correctly"""
        tester = main.app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
