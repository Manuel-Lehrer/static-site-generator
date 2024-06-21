from textnode import TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes: 
        if node.text_type == "text":
            split_nodes = node.text.split(delimiter)
            if len(split_nodes) % 2 == 0:
                raise ValueError("Invalid markdown, formatted section not closed")
            index=0 
            for node in split_nodes:
                if index % 2 != 0:
                    new_nodes.append(TextNode(node, text_type))
                else:
                    new_nodes.append(TextNode(node, "text"))
                index +=1
        else:
            new_nodes.append(node)
    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches