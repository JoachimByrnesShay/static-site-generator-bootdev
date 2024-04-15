from leafnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text 
        self.text_type = text_type 
        self.url = url 
    def __eq__(self, other):
        # return (other.text, other.text_type, other.url) == (self.text, self.text_type, self.url)
        text_check = other.text == self.text 
        text_type_check = other.text_type == self.text_type
        url_check = other.url == self.url 
        if not text_check or not text_type_check or not url_check:
            return False
        return True
    
    def __repr__(self):
        return f"{type(self).__name__}({self.text},{self.text_type},{self.url})"
    

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    if text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Invalid text type: {text_node.text_type}")

def text_node_to_html_node2(text_node):
    conversions = {
        "text": LeafNode(None, text_node.text),
        "bold": LeafNode("b", text_node.text),
        "italic": LeafNode("i", text_node.text),
        "code": LeafNode("code", text_node.text),
        "link": LeafNode("a", text_node.text, {"href": text_node.url}),
        "image": LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    }
    if not text_node.text_type in conversions:
        raise ValueError("this text type is not supported")
    return conversions[text_node.text_type]