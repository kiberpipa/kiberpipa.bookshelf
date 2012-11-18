import unittest2 as unittest
import mock

from pyramid import testing


class BaseUnitTest(unittest.TestCase):
    mock = mock

    def setUp(self):
        self.request = testing.DummyRequest()
        self.config = testing.setUp(request=self.request)

    def tearDown(self):
        testing.tearDown()
