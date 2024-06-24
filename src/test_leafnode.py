import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_node_creation(self):
        node = LeafNode("h1", "heyo", {"href": "https://www.google.com", "target": "_blank"})
        assert hasattr(node, "tag")
        assert hasattr(node, "value")
        assert hasattr(node, "props")

    def test_returns_html_with_just_tag(self):
        node = LeafNode("div", "heyo")
        assert node.to_html() == "<div>heyo</div>"
    
    def test_raise_no_value_error(self):
        node = LeafNode("h1", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertRaises(ValueError,lambda: node.to_html())

    def test_returns_value_with_no_tag(self):
        node = LeafNode(None, "heyo", {"href": "https://www.google.com", "target": "_blank"})
        assert node.to_html() == "heyo"

    def test_displays_tag_with_proper_attributes(self):
        node = LeafNode("div", "heyo", {"href": "https://www.google.com", "target": "_blank"})
        assert "<div href='https://www.google.com' target='_blank'>heyo</div>" in node.to_html()