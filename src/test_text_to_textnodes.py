import unittest

from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):

    def test_all_possible_types(self):
        text = "This is **text** with an _italic_ word and a `code block` and an" \
        " ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        new_nodes = text_to_textnodes(text)

        self.assertEqual(

    [
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),
    ]

, new_nodes)
        
    def test_text_to_textnodes_basic(self):
        # Test with plain text
        text = "Just plain text here"
        nodes = text_to_textnodes(text)
        assert len(nodes) == 1
        assert nodes[0].text == "Just plain text here"
        assert nodes[0].text_type == TextType.TEXT
        assert nodes[0].url is None

    def test_text_to_textnodes_empty(self):
        text = ""
        nodes = text_to_textnodes(text)
        assert nodes == []  # Empty input should return an empty list

    def test_text_to_textnodes_bold(self):
        text = "This is **bold** text"
        nodes = text_to_textnodes(text)
        assert len(nodes) == 3
        assert nodes[1].text_type == TextType.BOLD

if __name__ == "__main__":
    unittest.main()

