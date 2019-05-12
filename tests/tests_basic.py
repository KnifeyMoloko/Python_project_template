import unittest
import os
import main
from app import create_app


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['APP_ENV'] = 'test'

    def tearDown(self):
        os.environ.pop('APP_ENV')

    def test_main_is_running(self):
        self.assertTrue(main.main())

    def test_app_is_not_none(self):
        self.assertTrue(create_app("") is not None)

    def test_logger_is_present(self):
        self.assertLogs()
