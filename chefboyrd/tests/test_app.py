'''Test the flask application with a real server

We use a real client and server to test requests and responses in this unittest file.abs

See methods for examples.

'''
import os
import unittest
import tempfile
import chefboyrd

class ChefBoyRDTest(unittest.TestCase):
    '''Test the flask application'''

    def setUp(self):
        '''Sets up the database file'''
        self.db_fd, self.db_name = tempfile.mkstemp()
        chefboyrd.init_db(self.db_name)
        self.app = chefboyrd.APP.test_client()

    def tearDown(self):
        '''Unlinks and deletes the app database'''
        os.close(self.db_fd)
        os.unlink(self.db_name)

    def test_hello(self):
        '''Sample test for /test/hello route'''
        rv = self.app.get('/test/hello')
        rv.get_data(True)
        self.assertEqual('Hi', rv.get_data(True))
