import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(
            props={"href": "https://www.google.com", "target": "_blank", })
        self.assertEqual(node.props_to_html(),
                         ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode("a")
        self.assertEqual("HTMLNode(a, None, None, None)", repr(node))

    def test_to_html(self):
        node = HTMLNode("a")
        with self.assertRaises(NotImplementedError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
