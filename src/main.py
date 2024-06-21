from textnode import TextNode
from inline_markdown import split_nodes_image, split_nodes_link

def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node)

    node = TextNode("Check this [first link](https://example1.com) and this [second link](https://example2.com).", "text")
        
    new_nodes = split_nodes_link([node])
    print(new_nodes)
        

main()



