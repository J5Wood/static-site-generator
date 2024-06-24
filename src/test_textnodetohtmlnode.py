import unittest
from textnode import TextNode
from textnodetohtmlnode import text_node_to_html_node

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_correct_node_conversion(self):
        
        node = TextNode("hello", "text", "https://jeremywood.tech")

        text_leaf = text_node_to_html_node(node)
        self.assertEqual(text_leaf.tag, None)
        self.assertEqual(text_leaf.value, "hello")

        node.text_type = "bold"
        bold_leaf = text_node_to_html_node(node)
        self.assertEqual(bold_leaf.tag, "b")
        self.assertEqual(bold_leaf.value, "hello")

        node.text_type = "italic"
        italic_leaf = text_node_to_html_node(node)
        self.assertEqual(italic_leaf.tag, "i")
        self.assertEqual(italic_leaf.value, "hello")

        node.text_type = "code"
        code_leaf = text_node_to_html_node(node)
        self.assertEqual(code_leaf.tag, "code")
        self.assertEqual(code_leaf.value, "hello")

        node.text_type = "link"
        link_leaf = text_node_to_html_node(node)
        self.assertEqual(link_leaf.tag, "a")
        self.assertEqual(link_leaf.value, "hello")
        self.assertEqual(link_leaf.props, {'href': 'https://jeremywood.tech'})

        node.text_type = "image"
        image_leaf = text_node_to_html_node(node)
        self.assertEqual(image_leaf.tag, "img")
        self.assertEqual(image_leaf.value, "hello")
        self.assertEqual(image_leaf.props, {'url': 'https://jeremywood.tech', 'alt': 'hello'})

        node.text_type = "error"
        self.assertRaises(Exception, lambda: text_node_to_html_node(node))