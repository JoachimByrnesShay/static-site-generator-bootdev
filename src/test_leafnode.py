import unittest
from leafnode import LeafNode 

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode('a', "Click here!", {"href": "https://www.yahoo.com", "target": "_blank"})
        expected = '<a href="https://www.yahoo.com" target="_blank">Click here!</a>'
        return self.assertEqual(node.to_html(), expected)
    
    def test_to_html_no_tag(self):
        node = LeafNode(None, "Click here buddy!")
        return self.assertEqual(node.to_html(), node.value)
    
    def test_to_html_no_value(self):
        node = LeafNode("div", None)
        with self.assertRaises(ValueError):
             node.to_html()

       
if __name__ == "__main__":
    unittest.main()
