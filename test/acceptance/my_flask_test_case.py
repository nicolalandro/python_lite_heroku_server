import time
from flask_testing import LiveServerTestCase
from selenium import webdriver

import main


class MyFlaskTestCase(LiveServerTestCase):

    def create_app(self):
        app = main.app
        app.config['TESTING'] = True
        # Default port is 5000
        app.config['LIVESERVER_PORT'] = 8943
        # Default timeout is 5 seconds
        app.config['LIVESERVER_TIMEOUT'] = 10
        return app

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.app = main.app.test_client(self)

    def tearDown(self):
        self.browser.quit()

    def test_add_data_exception_without_image(self):
        self.browser.get(self.get_server_url() + '/add_supervisioned_data')
        self.browser.find_element_by_id('fish_specie').send_keys('test')
        self.browser.find_element_by_id('send_json').click()
        self.browser.find_element_by_id('error')
        self.browser.find_element_by_class_name('close').click()
        time.sleep(2)
        assert len(self.browser.find_elements_by_id('error')) == 0
