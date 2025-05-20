import unittest
from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):

    def test_extract_title_basic(self):
        md = "# Welcome"
        self.assertEqual(extract_title(md), "Welcome")

    def test_extract_title_leading_space(self):
        md = " # Greetings"
        self.assertEqual(extract_title(md), "Greetings")

    def test_extract_title_error(self):
        with self.assertRaises(Exception) as context:
            extract_title("## Not a main header")
        self.assertEqual(str(context.exception), "No H1 header found.")

    def test_extract_title_nospace(self):
        with self.assertRaises(Exception) as context:
            extract_title("#NoSpace")
        self.assertEqual(str(context.exception), "No H1 header found.")

    def test_extract_title_tabs_and_spaces(self):
        md = " \t # Tabby Title"
        self.assertEqual(extract_title(md), "Tabby Title")

    def test_extract_title_with_prior_content(self):
        md = "some text before\n# Real Title"
        self.assertEqual(extract_title(md), "Real Title")

    def test_extract_title_missing_header(self):
        md = "Just some random\ntext with no header."
        with self.assertRaises(Exception) as context:
            extract_title(md)
        self.assertEqual(str(context.exception), "No H1 header found.")


if __name__ == "__main__":
    unittest.main()
