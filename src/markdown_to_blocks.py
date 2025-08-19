def markdown_to_blocks(markdown: str) -> list:
    blocks_list = str(markdown).split('\n\n')
    blocks = []
    for block in blocks_list:
        block = block.strip()
        if block:
            blocks.append(block)
    return blocks
