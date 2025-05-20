from textnode import TextNode, TextType
from links_and_images import extract_markdown_links, extract_markdown_images


def split_nodes_image(old_nodes):

    result = []

    for node in old_nodes:

        new = []

        if node.text_type != TextType.TEXT:
            new.append(node)
            result.extend(new)
            continue

        list_of_image_tuples = extract_markdown_images(node.text)

        # check if there are no images at all:
        if list_of_image_tuples == []:
            result.append(node)
            continue

        sections = []

        text = node.text

        # split text with alt_image_pair as delimiter, add text before and the pair to sections
        # and continue splitting where last pair was found.
        for alt_image_pair in list_of_image_tuples:

            alt, image = alt_image_pair
            after_split = text.split(f"![{alt}]({image})", 1)
            sections.append(after_split[0])
            sections.append(f"![{alt}]({image})")
            text = "".join(after_split[1:])

        # add trailing text:
        sections.append(text)

        # convert sections into nodes by alternating between TEXT and IMAGE.
        for num, item in enumerate(sections):
            if item == "":
                continue
            if num % 2 == 0:
                new.append(TextNode(item, TextType.TEXT))
            else:
                alt, image = list_of_image_tuples.pop(0)
                new.append(TextNode(alt, TextType.IMAGE, image))

        result.extend(new)

    return result


def split_nodes_link(old_nodes):

    result = []

    for node in old_nodes:

        new = []

        if node.text_type != TextType.TEXT:
            new.append(node)
            result.extend(new)
            continue

        list_of_link_tuples = extract_markdown_links(node.text)

        # check if there are no links at all:
        if list_of_link_tuples == []:
            result.append(node)
            continue

        sections = []

        text = node.text

        for alt_link_pair in list_of_link_tuples:

            alt, link = alt_link_pair
            after_split = text.split(f"[{alt}]({link})", 1)
            sections.append(after_split[0])
            sections.append(f"[{alt}]({link})")
            text = "".join(after_split[1:])

        # add trailing text:
        sections.append(text)

        for num, item in enumerate(sections):
            if item == "":
                continue
            if num % 2 == 0:
                new.append(TextNode(item, TextType.TEXT))
            else:
                alt, link = list_of_link_tuples.pop(0)
                new.append(TextNode(alt, TextType.LINK, link))

        result.extend(new)

    return result
