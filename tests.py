import unittest
from auth import *
from message import Messages

class MessageTests(unittest.TestCase):
    def setUp(self):  # setUp will allow us to not keep on recreating messages objects, but also renews after each testcase
        self.message = Messages(account_sid, auth_token)

    def test_init(self):  # test init for Messages class to confirm account_sid and auth_token
      """Messages need an auth token and account sid"""
      self.assertEqual(self.message.account_sid, account_sid)  # confirm account_sid
      self.assertEqual(self.message.auth_token, auth_token)  # confirm auth_token

if __name__ == "__main__":  # must call this to run tests
    unittest.main()