import unittest
from textnode import TextNode
from split_node_helpers import split_nodes_image, split_nodes_link

class TestSplitNodeHelpers(unittest.TestCase):

    def test_correct_image_node_splitting(self): 
        node_one = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png) inside of it.",
            "text",
        )
        node_list_one = [TextNode("This is text with an ", "text", "https://jeremywood.tech"), TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), TextNode(" and another ", "text", "https://jeremywood.tech"), TextNode("second image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"), TextNode(" inside of it.", "text", "https://jeremywood.tech")]
        node_two = TextNode(
            "![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) This text is surrounded by images! ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            "text",
        )
        node_list_two = [TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), TextNode(" This text is surrounded by images! ", "text", "https://jeremywood.tech"), TextNode("second image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")]
        node_three = TextNode(
            " ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) This text is surrounded by images, but preserves whitespace at the beginning and end of lines... ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png) ",
            "text",
        )
        node_list_three = [TextNode(" ", "text", "https://jeremywood.tech"), TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), TextNode(" This text is surrounded by images, but preserves whitespace at the beginning and end of lines... ", "text", "https://jeremywood.tech"), TextNode("second image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"), TextNode(" ", "text", "https://jeremywood.tech")]

        self.assertEqual(split_nodes_image([node_one]), node_list_one)
        self.assertEqual(split_nodes_image([node_two]), node_list_two)
        self.assertEqual(split_nodes_image([node_three]), node_list_three)
    
    def test_image_split_returns_original_node_when_applicable(self):
        node = TextNode(
            "This is text with no images inside of it?",
            "text",
        )
        node_list = [TextNode("This is text with no images inside of it?", "text", "https://jeremywood.tech")]

        self.assertEqual(split_nodes_image([node]), node_list)

    def test_correct_link_node_splitting(self): 
        node_one = TextNode(
            "This is text with a [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a second, even cooler [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png) inside of it.",
            "text",
        )
        node_list_one = [TextNode("This is text with a ", "text", "https://jeremywood.tech"), TextNode("link", "link", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), TextNode(" and a second, even cooler ", "text", "https://jeremywood.tech"), TextNode("second link", "link", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"), TextNode(" inside of it.", "text", "https://jeremywood.tech")]
        node_two = TextNode(
            "[link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) This text is surrounded by links! [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            "text",
        )
        node_list_two = [TextNode("link", "link", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), TextNode(" This text is surrounded by links! ", "text", "https://jeremywood.tech"), TextNode("second link", "link", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")]
        node_three = TextNode(
            " [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) This text is surrounded by links, but preserves whitespace at the beginning and end of lines... [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png) ",
            "text",
        )
        node_list_three = [TextNode(" ", "text", "https://jeremywood.tech"), TextNode("link", "link", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), TextNode(" This text is surrounded by links, but preserves whitespace at the beginning and end of lines... ", "text", "https://jeremywood.tech"), TextNode("second link", "link", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"), TextNode(" ", "text", "https://jeremywood.tech")]

        self.assertEqual(split_nodes_link([node_one]), node_list_one)
        self.assertEqual(split_nodes_link([node_two]), node_list_two)
        self.assertEqual(split_nodes_link([node_three]), node_list_three)
    
    def test_link_split_returns_original_node_when_applicable(self):
        node = TextNode(
            "This is text with no links inside of it?",
            "text",
        )
        node_list = [TextNode("This is text with no links inside of it?", "text", "https://jeremywood.tech")]

        self.assertEqual(split_nodes_link([node]), node_list)
    