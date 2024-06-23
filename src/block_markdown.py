def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n")
    split_markdown = [block.strip() for block in split_markdown if block.strip() != ""]
    return split_markdown