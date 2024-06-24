from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not hasattr(self, "children") or self.children == None:
            raise ValueError("No children provided to parent node")
        if not hasattr(self, "tag") or self.tag == None:
            raise ValueError("No tag provided to parent node")

        def render_children(child_nodes):
            if child_nodes == None or len(child_nodes) == 0:
                return ""
            return_html = ""
            for child in child_nodes:
                return_html += child.to_html()
            return return_html

        return f"<{self.tag}{self.props_to_html()}>{render_children(self.children)}</{self.tag}>"