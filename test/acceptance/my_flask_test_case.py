import time
import unittest

from flask_testing import LiveServerTestCase
from selenium import webdriver

import os

os.environ['test'] = 'test'
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
        # firefox_opt = webdriver.FirefoxOptions()
        # firefox_opt.set_headless(False)
        # self.browser = webdriver.Firefox(firefox_options=firefox_opt)
        self.browser = webdriver.PhantomJS()
        self.app = main.app.test_client(self)

    def tearDown(self):
        self.browser.quit()

    def test_open_add_supervisioned_data_in_second_tab(self):
        self.browser.get(self.get_server_url())
        self.browser.find_elements_by_xpath("//div[@id = 'credits']/p/a")[0].click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.assertEqual(self.browser.current_url, self.get_server_url() + '/add_supervisioned_data')

    def test_open_show_dataset_in_second_tab(self):
        self.browser.get(self.get_server_url())
        self.browser.find_elements_by_xpath("//div[@id = 'credits']/p/a")[1].click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.assertEqual(self.browser.current_url, self.get_server_url() + '/show_dataset')

    def test_open_fish_ai_in_second_tab(self):
        self.browser.get(self.get_server_url())
        self.browser.find_elements_by_xpath("//div[@id = 'credits']/p/a")[2].click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.assertEqual(self.browser.current_url, self.get_server_url() + '/fish_ai')

    def test_add_data_exception_without_image(self):
        self.browser.get(self.get_server_url() + '/add_supervisioned_data')
        self.browser.find_element_by_id('fish_specie').send_keys('test')
        self.browser.find_element_by_id('send_json').click()
        self.browser.find_element_by_id('error')
        self.browser.find_element_by_class_name('close').click()
        time.sleep(2)
        assert len(self.browser.find_elements_by_id('error')) == 0


if __name__ == '__main__':
    unittest.main()
