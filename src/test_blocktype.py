import unittest

from blocktype import block_to_block_type, BlockType

#standard cases

header_block = "# This is a heading"

paragraph_block = "This is a paragraph of text. It has some **bold** and _italic_ words inside of it."

unordered_list_block = """- This is the first list item in a list block
- This is a list item
- This is another list item"""

ordered_list_block = """1. this is
2. an ordered
3. list block"""

code_block = """```
for item in iterable print(item)
```"""

quote_block = """>this is
>a quote
>block"""

class TestBlockType(unittest.TestCase):

    def test_header_block(self):
        block = header_block
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_paragraph_block(self):
        block = paragraph_block
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_unordered_list_block(self):
        block = unordered_list_block
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_ordered_list_block(self):
        block = ordered_list_block
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_code_block(self):
        block = code_block
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote_block(self):
        block = quote_block
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    #edge cases

    def test_edge_case_heading_without_space(self):
        block = "#NoSpaceHeading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)  # Not a valid heading

    def test_edge_case_heading_too_many_hashes(self):
        block = "####### Too many hashes"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_edge_case_ordered_list_wrong_start(self):
        block = """2. Should start with 1
        3. Then go to 2"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_edge_case_ordered_list_wrong_increment(self):
        block = """1. First
        3. Skipped 2"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_edge_case_unordered_list_no_space(self):
        block = """-No space
-After the dash"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


    def test_edge_case_quote_missing_prefix(self):
        block = """>This line has a prefix
This line doesn't
>This line does again"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)  # Not a valid quote block

    def test_edge_case_code_missing_backticks(self):
        block = """```
Some code here
"""  # Missing closing backticks
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_edge_case_empty_block(self):
        block = ""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_valid_heading_levels(self):
        for i in range(1, 7):
            block = "#" * i + " Heading level " + str(i)
            self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_multi_line_code_block(self):
        block = """```
def hello():
print("Hello world!")
```"""
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_multi_line_quote(self):
        block = """>Line one of quote
>Line two of quote
>Line three of quote"""
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    



if __name__ == "__main__":
    unittest.main()