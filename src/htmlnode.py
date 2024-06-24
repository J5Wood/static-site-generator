class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        string_list = []
        if self.props == None:
            return ""
        for key in self.props:
            string = f" {key}='{self.props[key]}'"
            string_list.append(string)

        return "".join(string_list)
    
    def __repr__(self):
        return (f"""
    Node:
Tag: {self.tag}
Value: {self.value}
Children: {self.children}
Props: {self.props}\n
""")