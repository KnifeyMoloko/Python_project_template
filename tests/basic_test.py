# basic tests for Evo

import unittest
import os
from .. import main

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['APP_ENV'] = 'test'

    def tearDown(self):
        os.environ.pop('APP_ENV')

    def test_evo_is_working(self):
        self.assertTrue(main.main())


if __name__ == '__main__':
    unittest.main()
