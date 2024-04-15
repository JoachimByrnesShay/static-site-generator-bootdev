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