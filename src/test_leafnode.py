import unittest

from htmlnode import HTMLNode, LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')




    # def test_repr(self):
    #     node = HTMLNode("a")
    #     self.assertEqual("HTMLNode(a, None, None, None)", repr(node))
        
    # def test_to_html(self):
    #     node = HTMLNode("a")
    #     with self.assertRaises(NotImplementedError):
    #         node.to_html()


if __name__ == "__main__":
    unittest.main()