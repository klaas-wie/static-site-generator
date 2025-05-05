from split_images_links import split_nodes_image, split_nodes_link
from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

def text_to_textnodes(text):

    if text == "":
        return []

    node = TextNode(text, TextType.TEXT)
    after_image = split_nodes_image([node])
    after_link = split_nodes_link(after_image)

    after_code = split_nodes_delimiter(after_link, '`', TextType.CODE)
    after_bold = split_nodes_delimiter(after_code, '**', TextType.BOLD)
    after_italic = split_nodes_delimiter(after_bold, '_', TextType.ITALIC)

    return after_italic



