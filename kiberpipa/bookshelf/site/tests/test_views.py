from ...testing import BaseUnitTest


class ViewsTest(BaseUnitTest):
    def test_index(self):
        from ..views import index
        info = index(self.request)
        self.assertEqual(info, {})
