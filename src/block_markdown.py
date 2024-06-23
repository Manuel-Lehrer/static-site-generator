def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n\n")
    split_markdown = [block.strip() for block in split_markdown if block.strip() != ""]
    i = 0
    for block in split_markdown:
        block = "\n".join([" ".join(line.split()) for line in block.split("\n")])
        split_markdown[i]=block
        i+=1
    return split_markdown