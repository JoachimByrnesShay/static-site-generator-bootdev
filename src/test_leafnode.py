import unittest
from leafnode import LeafNode 

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode('a', "Click here!", {"href": "https://www.yahoo.com", "target": "_blank"})
        expected = '<a href="https://www.yahoo.com" target="_blank">Click here!</a>'
        return self.assertEqual(node.to_html(), expected)

if __name__ == "__main__":
    unittest.main()
