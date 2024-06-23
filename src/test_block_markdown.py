import unittest
from block_markdown import markdown_to_blocks


class TestMarkdownToHTML(unittest.TestCase):
    def test_splitting_blocks(self):
        test_blocks = ['This is **bolded** paragraph', 'This is another paragraph with *italic* text and `code` here', 'This is the same paragraph on a new line', '* This is a list', '* with items']
        markdown = "This is **bolded** paragraph\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n* This is a list\n* with items"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(test_blocks, blocks)

    def test_splitting_blocks_newlines(self):
        test_blocks = ['This is **bolded** paragraph', 'This is another paragraph with *italic* text and `code` here', 'This is the same paragraph on a new line', '* This is a list', '* with items']
        markdown = """
                    This is **bolded** paragraph




                    This is another paragraph with *italic* text and `code` here
                    This is the same paragraph on a new line

                    * This is a list
                    * with items
            """
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, test_blocks)


