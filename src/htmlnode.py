class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag 
        self.value = value
        self.children = children 
        self.props = props 
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        props_html = ""
        if self.props:
            for key,value in self.props.items():
                props_html+=f' {key}="{value}"'
        return props_html
     
    def __repr__(self):
        return (
            f'HTMLNode:{"{"}\n'
            f'  tag: {self.tag}\n'
            f'  value: {self.value}\n'
            f'  children: {self.children}\n'
            f'  props: {self.props_to_html()}\n'
            f'{"}"}'
        )
    
    