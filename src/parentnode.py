from htmlnode import HTMLNode 


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("a parentnode instance requires a tag")
        if not self.children:
            raise ValueError("a parentnode instance requires children")
        tree_html = ''
        for child in self.children:
            tree_html += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{tree_html}</{self.tag}>'
        
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"