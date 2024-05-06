from unittest import TestCase
from utils import short_link

class ShortLinkTest(TestCase):
    def test_random_url(self):
        # Irrelevant: n/a
        # Initial State: Sample URL to pass
        long_link = "example.com"
        # Action: we would like to pass a URL and return back the auto-generated, shortened URL
        short_link = short_link.build_short_link(long_link)
        # Outcome: we expect to get a 5 character A-Z0-9 string
        self.assertTrue(short_link.isalnum())