import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def ln(self, tag):
        return LeafNode(tag, "heyo", {"href": "https://www.google.com", "target": "_blank"})
    
    def pn(self, tag, *args):
        return ParentNode(tag, args, {"href": "https://www.google.com", "target": "_blank"})
    
    def test_simple_leafs(self):
        node = self.pn("body", self.ln("p"), self.ln("p"), self.ln("p"), self.ln("p"))
        self.assertEqual(node.to_html(), "<body href='https://www.google.com' target='_blank'><p href='https://www.google.com' target='_blank'>heyo</p><p href='https://www.google.com' target='_blank'>heyo</p><p href='https://www.google.com' target='_blank'>heyo</p><p href='https://www.google.com' target='_blank'>heyo</p></body>")
    
    def test_nested_node_creation(self):
        node = self.pn("div", self.ln("p"), self.pn("main", self.pn("ul", self.ln("span")), self.pn("nav", self.ln("a"))), self.pn("section", self.ln("img")), self.ln("footer"))
        self.assertEqual(node.to_html(), "<div href='https://www.google.com' target='_blank'><p href='https://www.google.com' target='_blank'>heyo</p><main href='https://www.google.com' target='_blank'><ul href='https://www.google.com' target='_blank'><span href='https://www.google.com' target='_blank'>heyo</span></ul><nav href='https://www.google.com' target='_blank'><a href='https://www.google.com' target='_blank'>heyo</a></nav></main><section href='https://www.google.com' target='_blank'><img href='https://www.google.com' target='_blank'>heyo</img></section><footer href='https://www.google.com' target='_blank'>heyo</footer></div>")