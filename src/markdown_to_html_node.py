import re

from markdown_to_blocks import markdown_to_blocks
from blocktype import block_to_block_type, BlockType


test_md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

def markdown_to_html_node(markdown):

    md_blocks = markdown_to_blocks(markdown)

    for block in md_blocks:

        block_type = block_to_block_type(block)

        html = block_to_html(block, block_type)


#helpers

def block_to_html(block, block_type):

    if block_type == BlockType.HEADING:
        html = heading_to_html(block)

    if block_type == BlockType.CODE:
        html = f"<pre><code>{block}</code></pre>"

    if block_type == BlockType.QUOTE:
        html = f"<blockquote>{block}</blockquote>"

    if block_type == BlockType.UNORDERED_LIST:
        html = unordered_block_to_html(block)

    if block_type == BlockType.ORDERED_LIST:
        html = ordered_block_to_html(block)

    if block_type == BlockType.PARAGRAPH:
        html = f"<p>{block}</p>"

    return html


def heading_to_html(block):

    heading_pattern = r'^#{1,6}'

    amount_of_hashes = len(re.match(heading_pattern, block).group())

    html = f"<h{amount_of_hashes}>{block}</h{amount_of_hashes}>"

    return html

def unordered_block_to_html(block):

    lines = block.splitlines()

    list_items = "".join([f"<li>{item}</li>" for item in lines])

    html = f"<ul>{list_items}</ul>"

    return html

def ordered_block_to_html(block):

    lines = block.splitlines()

    list_items = "".join([f"<li>{item}</li>" for item in lines])

    html = f"<ol>{list_items}</ol>"

    return html


