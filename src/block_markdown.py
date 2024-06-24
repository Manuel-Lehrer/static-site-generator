def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n\n")
    split_markdown = [block.strip() for block in split_markdown if block.strip() != ""]
    i = 0
    for block in split_markdown:
        block = "\n".join([" ".join(line.split()) for line in block.split("\n")])
        split_markdown[i]=block
        i+=1
    return split_markdown

def block_to_block_type(markdown):
    if markdown[0] == "#":
        return "heading"
    elif markdown[0] == "```":
        return "code"
    elif markdown[0] == ">":
        return "quote"
    elif markdown[0] == "-" or markdown[0]== "*":
        return "unordered_list"
    elif markdown[0] in "123456789" and markdown[1] == ".":
        return "ordered_list"
    else:
        return "paragraph"
    
    