from unittest import TestCase
from shortener.utils.short_link import build_short_link

class ShortLinkTest(TestCase):
    def test_random_url(self):
        # Irrelevant: n/a
        # Initial State: Sample URL to pass
        long_link = "example.com"
        # Action: we would like to pass a URL and return back the auto-generated, shortened URL
        short_link = build_short_link(long_link)
        # Outcome: we expect to get a 5 character A-Z0-9 string
        self.assertTrue(short_link.isalnum())

        second_long_link = "another-example.com"
        second_short_link = build_short_link(second_long_link)
        self.assertNotEqual(second_short_link, short_link)