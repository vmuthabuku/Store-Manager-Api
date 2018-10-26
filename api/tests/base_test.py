import unittest
from flask import json
import json
import psycopg2
from ..Database.connect import conn, cur

from ..app import create_app

class BaseTest(unittest.TestCase):
    """ Class to test Users """
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
       
    def user_auth_register(self, username, email, password, role):
        """ Register a user """
        return self.client().post('/api/v2/auth/signup',
                           content_type="application/json",
                           data=json.dumps({"email": email,
                                            "username": username,
                                            "password": password,
                                            "role": role}))

    def user_auth_login(self, email, password):
        """ Register a user """
        return self.client().post('/api/v2/auth/login',
                           content_type="application/json",
                           data=json.dumps({"email": email,
                                            "password": password}))

    def tear(self):
        """ clear tables """
        conn
        cur.execute('DROP TABLE users')
        conn.commit()
        conn.close()



    



