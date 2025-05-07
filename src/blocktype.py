from enum import Enum
import re

class BlockType(Enum):

    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'


def ordered_list_func(markdown_block):
    lines = markdown_block.splitlines()
    
    for i, line in enumerate(lines, start=1):
        match = re.match(r'^(\d+)\. ', line)
        if not match or int(match.group(1)) != i:
            return False
    
    return True


def block_to_block_type(markdown_block):

    if not markdown_block:
        return BlockType.PARAGRAPH

    heading_pattern = r'^#{1,6} '

    lines = markdown_block.splitlines()

    if re.match(heading_pattern, markdown_block):
        return BlockType.HEADING

    elif len(lines) >= 2 and lines[0].startswith("```") and lines[-1] == "```":
        return BlockType.CODE   
    
    elif all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    
    elif all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    
    elif ordered_list_func(markdown_block):
        return BlockType.ORDERED_LIST
    
    else:
        return BlockType.PARAGRAPH





