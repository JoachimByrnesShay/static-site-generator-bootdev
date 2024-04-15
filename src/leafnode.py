from htmlnode import HTMLNode 


class LeafNode(HTMLNode):
    def __init__(self,tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes require a value")
        if not self.tag:
            return self.value 
        result = f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
       
        return result
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
        # return (
        #     f'HTMLNode:{"{"}\n'
        #     f'  tag: {self.tag}\n'
        #     f'  value: {self.value}\n'
        #     f'  props: {self.props_to_html()}\n'
        #     f'{"}"}'
        # )
    