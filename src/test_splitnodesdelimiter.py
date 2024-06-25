import unittest
from splitnodesdelimiter import split_nodes_delimiter
from textnode import TextNode
class TestTextNodeToHtmlNode(unittest.TestCase):

    def test_correct_node_conversion(self):       
        node1 = TextNode("This is text with a `code block` word", "text")
        node2 = TextNode("This is text with an **italics** word", "text")
        node3 = TextNode("This is text with a *bold* word", "text")
        
        code_delimiter = split_nodes_delimiter([node1], "`", "text")
        italics_delimiter = split_nodes_delimiter([node2], "**", "text")
        bold_delimiter = split_nodes_delimiter([node3], "*", "text")

        self.assertEqual(code_delimiter, [TextNode("This is text with a " , "text", None), TextNode("code block", "code", None), TextNode( " word", "text", None)])
        self.assertEqual(bold_delimiter, [TextNode("This is text with a " , "text", None), TextNode("bold", "bold", None), TextNode( " word", "text", None)])
        self.assertEqual(italics_delimiter, [TextNode("This is text with an " , "text", None), TextNode("italics", "italics", None), TextNode( " word", "text", None)])

    def test_incorrectly_formatted_string(self):
        node1 = TextNode("This is text with a `single delimiter, word", "text")
        self.assertRaises(Exception, lambda: split_nodes_delimiter([node1], "`", "text"))
        
        
        
        
        
        # node = TextNode("hello", "text", "https://jeremywood.tech")