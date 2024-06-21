import unittest

from textnode import TextNode
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", "italic", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "italic", "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_split_delimiter(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", "text"),
            TextNode("code block", "code"),
            TextNode(" word", "text"),
                                    ])
    def test_non_matching_delimiters(self):
        node = TextNode("Hello `world", "text")
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node], "`", "code")
        self.assertEqual(str(context.exception), "Invalid markdown, formatted section not closed")

    def test_extracing_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        matches = extract_markdown_images(text)
        self.assertEqual(matches, [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")])

    def test_extracting_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        matches = extract_markdown_links(text)
        self.assertEqual(matches,[("link", "https://www.example.com"), ("another", "https://www.example.com/another")])

         
        
if __name__ == "__main__":
    unittest.main()