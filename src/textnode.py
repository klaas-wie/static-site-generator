from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):

    TEXT = 'text'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, other):
        if (self.text == other.text 
            and self.text_type == other.text_type
            and self.url == other.url):
            return True
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):

    #print(f"text_node.text_type = {text_node.text_type}")

    if text_node.text_type == TextType.TEXT:
        text_node = LeafNode(None, text_node.text)
    
    elif text_node.text_type == TextType.BOLD:
        text_node = LeafNode('b', text_node.text)

    elif text_node.text_type == TextType.ITALIC:
        text_node = LeafNode('i', text_node.text)

    elif text_node.text_type == TextType.CODE:
        text_node = LeafNode('code', text_node.text)

    elif text_node.text_type == TextType.LINK:
        text_node = LeafNode('a', text_node.text, {"href": text_node.url})

    elif text_node.text_type == TextType.IMAGE:
        text_node = LeafNode('img', "", {"src": text_node.url, "alt": text_node.text})

    raise ValueError(f"invalid text type: {text_node.text_type}")

    return text_node

    
    


