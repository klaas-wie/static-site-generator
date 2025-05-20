import unittest

from links_and_images import extract_markdown_links, extract_markdown_images


class TestLinksAndImages(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            [("to boot dev", "https://www.boot.dev"),
             ("to youtube", "https://www.youtube.com/@bootdotdev")], matches
        )

    def test_extract_markdown_images_unmatched_open_bracket(self):
        matches = extract_markdown_images(
            "Try this broken image: ![open [ bracket](https://example.com/image.png)"
        )
    # The pattern will not match this malformed markdown, so expect empty result
        self.assertListEqual([], matches)


if __name__ == "__main__":
    unittest.main()
