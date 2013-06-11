# -*- coding: utf-8 -*-
import unittest
from google.appengine.ext import testbed

from datetime import date
from application.models import *

class MyTestCase(unittest.TestCase):

    def setUp(self):
        # First, create an instance of the Testbed class.
        self.testbed = testbed.Testbed()
        # Then activate the testbed, which prepares the service stubs for use.
        self.testbed.activate()
        # Next, declare which service stubs you want to use.
        self.testbed.init_datastore_v3_stub()
        
    def tearDown(self):
        self.testbed.deactivate()
    
if __name__ == '__main__':
    unittest.main()
