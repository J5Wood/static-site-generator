from leafnode import LeafNode
# from textnode import TextNode


def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case("text"):
            return LeafNode(None, text_node.text, None)
        case("bold"):
            return LeafNode("b", text_node.text, None)
        case("italic"):
            return LeafNode("i", text_node.text, None)
        case("code"):
            return LeafNode("code", text_node.text, None)
        case("link"):
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case("image"):
            return LeafNode("img", text_node.text, {"url": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Incorrect text_node type provided")