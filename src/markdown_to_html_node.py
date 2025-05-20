import re

from markdown_to_blocks import markdown_to_blocks
from blocktype import block_to_block_type, BlockType
from htmlnode import HTMLNode, LeafNode, ParentNode
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType


def markdown_to_html_node(markdown):

    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:

        block_type = block_to_block_type(block)
        html_node = block_to_html(block, block_type)

        children.append(html_node)
    return ParentNode("div", children, None)


# helpers

def block_to_html(block, block_type):

    if block_type == BlockType.HEADING:
        html_node = heading_to_html_node(block)

    elif block_type == BlockType.CODE:
        html_node = code_to_html_node(block)

    elif block_type == BlockType.QUOTE:
        html_node = quote_to_html_node(block)

    elif block_type == BlockType.UNORDERED_LIST:
        html_node = unordered_block_to_html(block)

    elif block_type == BlockType.ORDERED_LIST:
        html_node = ordered_block_to_html(block)

    elif block_type == BlockType.PARAGRAPH:
        html_node = paragraph_to_html_node(block)

    return html_node


def heading_to_html_node(block):

    heading_pattern = r'^#{1,6}'

    amount_of_hashes = len(re.match(heading_pattern, block).group())

    heading_text = block[amount_of_hashes:].lstrip()

    children = text_to_children(heading_text)
    html_node = ParentNode(f"h{amount_of_hashes}", children)

    return html_node


def code_to_html_node(block):

    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")

    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])

    return ParentNode("pre", [code])


def quote_to_html_node(block):

    lines = block.split("\n")
    new_lines = []

    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)

    return ParentNode("blockquote", children)


def paragraph_to_html_node(block):

    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)

    return ParentNode("p", children)


def unordered_block_to_html(block):

    items = block.split("\n")
    html_items = []

    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))

    return ParentNode("ul", html_items)


def ordered_block_to_html(block):

    items = block.split("\n")
    html_items = []

    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))

    return ParentNode("ol", html_items)


def text_to_children(text):

    text_nodes = text_to_textnodes(text)

    html_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)

    return html_nodes
