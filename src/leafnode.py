from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if hasattr(self, "value") and self.value != None:
            if hasattr(self, "tag") and self.tag != None:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            else:
                return self.value
        else:
            raise ValueError("Node has no value")