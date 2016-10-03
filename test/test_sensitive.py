import unittest

from sensitive import do_encryption
from sensitive import get_password

class TestSensitive(unittest.TestCase):
    def test_encryption(self):
        do_encryption()

    def test_password(self):
        get_password()
