import unittest

from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitDelimiter(unittest.TestCase):

    def test_snd_with_one_node(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        #print(f"new nodes = {new_nodes}")
        self.assertEqual([

    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word", TextType.TEXT),

], new_nodes)
        
    def test_snd_with_multiple_delimiters(self):
        node = TextNode("Here is `one code` and `another code` block", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual([

    TextNode("Here is ", TextType.TEXT),
    TextNode("one code", TextType.CODE),
    TextNode(" and ", TextType.TEXT),
    TextNode("another code", TextType.CODE),
    TextNode(" block", TextType.TEXT),

        ], new_nodes)

    def test_snd_with_mismatched_delimiters(self):
        node = TextNode("Text with `mismatched delimiters", TextType.TEXT)
        
        with self.assertRaises(Exception):
            new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    
    def test_multiple_nodes_with_different_types(self):
        # Create a list of nodes with different types
        test9a = TextNode("Regular text", TextType.TEXT)
        test9b = TextNode("Bold text", TextType.BOLD)
        test9c = TextNode("Text with `code block`", TextType.TEXT)
        
        # Process the list
        result9 = split_nodes_delimiter([test9a, test9b, test9c], "`", TextType.CODE)
        
        # Assert the expected results
        self.assertEqual(len(result9), 4)
        
        # First node should remain unchanged
        self.assertEqual(result9[0].text, "Regular text")
        self.assertEqual(result9[0].text_type, TextType.TEXT)
        
        # Second node should remain unchanged (it's already BOLD)
        self.assertEqual(result9[1].text, "Bold text")
        self.assertEqual(result9[1].text_type, TextType.BOLD)
        
        # Third node should be split into two nodes
        self.assertEqual(result9[2].text, "Text with ")
        self.assertEqual(result9[2].text_type, TextType.TEXT)
        
        self.assertEqual(result9[3].text, "code block")
        self.assertEqual(result9[3].text_type, TextType.CODE)

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    


if __name__ == "__main__":
    unittest.main()