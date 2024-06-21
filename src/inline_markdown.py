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

def split_nodes_image(old_nodes):
    new_nodes=[]
    for old_node in old_nodes:
        image_tup = extract_markdown_images(old_node.text)
        
        if image_tup == []:
            if old_node.text !="":
                new_nodes.append(old_node)
        
        else:
            split = old_node.text.split(f"![{image_tup[0][0]}]({image_tup[0][1]})", 1)
            if split[0]!="":
                new_nodes.append(TextNode(split[0], "text"))
            new_nodes.append(TextNode(image_tup[0][0], "image", image_tup[0][1]))
            rest="".join(split[1:])
            new_nodes.extend(split_nodes_image([TextNode(rest, "text")]))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes=[]
    for old_node in old_nodes:
        link_tup = extract_markdown_links(old_node.text)
        
        if link_tup == []:
            if old_node.text !="":
                new_nodes.append(old_node)
        
        else:
            split = old_node.text.split(f"[{link_tup[0][0]}]({link_tup[0][1]})", 1)
            if split[0]!="":
                new_nodes.append(TextNode(split[0], "text"))
            new_nodes.append(TextNode(link_tup[0][0], "link", link_tup[0][1]))
            rest="".join(split[1:])
            new_nodes.extend(split_nodes_link([TextNode(rest, "text")]))

    return new_nodes
