class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self. props = props

    def to_html(self):
        raise NotImplementedError("not yet implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop, value in self.props.items():
            props_html += f' {prop}="{value}"'
        return props_html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children} ,{self. props})"