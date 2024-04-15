import unittest 
from htmlnode import HTMLNode 

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode('a', "great link", None, {'href': 'https://www.google.com', 'target': '_blank'})
        expected_props_string = ' href="https://www.google.com" target="_blank"'
        return self.assertEqual(node.props_to_html(), expected_props_string)

if __name__=="__main__":
    unittest.main()
