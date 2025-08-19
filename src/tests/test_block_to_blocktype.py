import unittest
from src.block_to_blocktype import block_to_blocktype, BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        self.assertEqual(block_to_blocktype("This is a paragraph."), BlockType.PARAGRAPH)

    def test_heading(self):
        self.assertEqual(block_to_blocktype("# This is a heading"), BlockType.HEADING)

    def test_code_block(self):
        self.assertEqual(block_to_blocktype("```python\nprint('Hello')\n```"), BlockType.CODE)

    def test_quote(self):
        self.assertEqual(block_to_blocktype("> This is a quote"), BlockType.QUOTE)

    def test_unordered_list(self):
        self.assertEqual(block_to_blocktype("- Item 1\n- Item 2"), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        self.assertEqual(block_to_blocktype("1. First item\n2. Second item"), BlockType.ORDERED_LIST)