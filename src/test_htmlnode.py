import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_node_creation(self):
        node = HTMLNode("h1", "heyo", {}, {"href": "https://www.google.com", "target": "_blank"})
        repr_return = node.__repr__()
        assert "Tag: h1" in repr_return
        assert "Value: heyo" in repr_return

    def props_string_creation(self):
        node = HTMLNode("h1", "heyo", {}, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), "href='https://www.google.com' target='_blank'")
    
    def test_raise_Error(self):
        node = HTMLNode("h1", "heyo", {}, {"href": "https://www.google.com", "target": "_blank"})
        self.assertRaises(NotImplementedError, lambda: node.to_html())

