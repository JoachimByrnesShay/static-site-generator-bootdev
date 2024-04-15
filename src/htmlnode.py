class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag 
        self.value = value
        self.children = children 
        self.props = props 

    def __eq__(self,other):
        if self.children and other.children:
            if not len(self.children) == len(other.children):
                return False 
            for i in range(len(self.children)):
                if self.children[i] != other.children[i]:
                    return False 
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        props_html = ""
        if self.props:
            for key,value in self.props.items():
                props_html+=f' {key}="{value}"'
        return props_html
     
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
        # return (
        #     f'HTMLNode:{"{"}\n'
        #     f'  tag: {self.tag}\n'
        #     f'  value: {self.value}\n'
        #     f'  children: {self.children}\n'
        #     f'  props: {self.props_to_html()}\n'
        #     f'{"}"}'
        # )
    
    