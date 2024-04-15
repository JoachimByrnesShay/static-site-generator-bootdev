import unittest 
from parentnode import ParentNode 
from leafnode import LeafNode 
from htmlnode import HTMLNode 



class TestParentNode(unittest.TestCase):
    
   
    def test_to_html(self):
        parent2 = ParentNode("main",[ParentNode('section', [ParentNode("article", [LeafNode("p", "the great paragraph in the article in the section", {"class": "paragraph-in-article"})], {"class": "article-class"})]), ParentNode("footer", [LeafNode('p', "paragraph in the footer")])])                         
        print(parent2.to_html())
        expected = '<main><section><article class="article-class"><p class="paragraph-in-article">the great paragraph in the article in the section</p></article></section><footer><p>paragraph in the footer</p></footer></main>'
        return self.assertEqual(parent2.to_html(), expected)
         
    def test_to_html2(self):
        parent1 = ParentNode("div",[LeafNode("h1", "the girls are bad"), LeafNode("p", "once upon a time, there were some gangsters...")])

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(), 
            "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>"
        )

if __name__ == "__main__":
    unittest.main()

