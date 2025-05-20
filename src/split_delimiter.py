from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):

    italic = "_"
    bold = "**"
    code = "`"

    if not (delimiter == italic or delimiter == bold or delimiter == code):
        raise Exception("not valid Markdown!")

    result = []

    for node in old_nodes:

        new = []

        if node.text_type != TextType.TEXT:
            result.append(node)
            continue

        if node.text.count(delimiter) % 2 != 0:
            raise Exception("Issue with delimiters!")
        if node.text.count(delimiter) == 0:
            new.append(node)
            result.extend(new)
            continue

        content = node.text.split(delimiter)

        for num, item in enumerate(content):
            if item == "":
                continue
            if num % 2 == 0:
                new.append(TextNode(item, TextType.TEXT))
            else:
                new.append(TextNode(item, text_type))

        result.extend(new)

    return result
