import unittest

from textnode import TextNode
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes


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

    def test_split_images(self):
        node = TextNode("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)","text",)
        
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [
                                    TextNode("This is text with an ", "text"),
                                    TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                                    TextNode(" and another ", "text"),
                                    TextNode("second image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"),
                                    ]
                        )

    def test_split_links(self):
        node = TextNode("Check this [first link](https://example1.com) and this [second link](https://example2.com).", "text")
        
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [
                                    TextNode("Check this ", "text"),
                                    TextNode("first link", "link", "https://example1.com"),
                                    TextNode(" and this ", "text"),
                                    TextNode("second link", "link", "https://example2.com"),
                                    TextNode(".", "text")
                                    ]
                        )
    def test_text_to_text_nodes(self):
        text = "This is **bold** and *italic* and a `code block`."
        new_nodes = text_to_textnodes(text)
        test_nodes = [
            TextNode("This is ", "text"),
            TextNode("bold", "bold"),
            TextNode(" and ", "text"),
            TextNode("italic", "italic"),
            TextNode(" and a ", "text"),
            TextNode("code block", "code"),
            TextNode(".", "text")
        ]
        self.assertEqual(new_nodes, test_nodes)
        
if __name__ == "__main__":
    unittest.main()