import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "https://jeremywood.tech")
        node2 = TextNode("This is a text node", "bold", "https://jeremywood.tech")
        self.assertEqual(node, node2)

    def test_non_eq(self):
        node = TextNode("This is a text node", "bold", "https://jeremywood.tech")
        node2 = TextNode("This is another text node", "italic", "https://jeremywood.tech")
        self.assertNotEqual(node, node2)

    def test_no_url(self):
        node = TextNode("This is a text node", "bold")
        assert node.url == "https://jeremywood.tech", f"Node {node} url has no default"

    def test_url_is_none(self):
        node = TextNode("This is a text node", "bold", None)
        self.assertTrue(node.url == None)

if __name__ == "__main__":
    unittest.main()