import json
from .base_test import BaseTest

class TestUser(BaseTest):   
    def test_user_registration(self):
        """Test that a user can register successfully"""
        user_reg = self.client().post('/api/v2/auth/signup',
                               content_type="application/json",
                               data=json.dumps({"email": "email@user.com",
                                                "username":"user",
                                                "password": "password",
                                                 "role": "admin"}))
        self.assertEqual(user_reg.status_code, 201)

    def test_user_login(self):
        """ Test if registered attendant can log in successfully """
        user_reg = self.client().post('/api/v2/auth/signup',
                            content_type="application/json",
                            data=json.dumps({"email": "pass@pass.com",
                                             "password": "pass",
                                             "username": "user",
                                             "role": "admin"}))
        self.assertEqual(user_reg.status_code, 201)

        user_login = self.client().post('/api/v2/auth/login',
                     content_type="application/json",
                     data=json.dumps({"email": "pass@pass.com",
                                      "password": "password"}))
        self.assertEqual(user_login.status_code, 200)

    


