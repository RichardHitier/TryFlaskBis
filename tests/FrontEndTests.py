import os
import unittest
import urllib

from selenium import webdriver
from flask_testing import LiveServerTestCase
from tryflask import app

_SERVER_PORT = 8943
_ROOT_URL = "http://localhost:{}".format(_SERVER_PORT)


class BaseTestCase(LiveServerTestCase):
    def create_app(self):
        # # remove logging lines on test output
        import logging
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.INFO)
        log.disabled = True
        # os.environ['WERKZEUG_RUN_MAIN'] = 'true'

        # pass in test configurations
        app.config.update(
            # Change the port that the liveserver listens on as we dont want to conflict with running:5000
            LIVESERVER_PORT=_SERVER_PORT
        )

        self.app_context = app.app_context()
        self.app_context.push()
        return app

    def setUp(self):
        # os.environ["PYTHONTRACEMALLOC"] = '1'

        self.driver = self.create_chrome_driver()

    def tearDown(self):
        self.app_context.pop()
        self.driver.close()
        self.driver.quit()

    def create_chrome_driver(self):
        """
        Create then return the chrome driver.

        :return: the chrome driver.
        """
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_argument('--headless')

        return webdriver.Chrome(options=options)


class AccessTestCase(BaseTestCase):
    def test_ping(self):
        self.assertEqual(_ROOT_URL, self.get_server_url())

    def test_selenium_access(self):
        # open browser on servers adress
        self.driver.get(self.get_server_url())
        # L'adresse dans l'url doit être celle que l'on attend.
        self.assertEqual(_ROOT_URL+'/', self.driver.current_url)

    def test_server_is_up_and_running(self):
        response = urllib.request.urlopen(self.get_server_url())
        self.assertEqual(200, response.code)
