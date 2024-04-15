from textnode import TextNode 
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import *

# TextNode:
#     def __init__(self, text, text_type, url=None):
def main():
    
    


    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node.__repr__())
    print(text_node_to_html_node(node))
   
    node_for_img = TextNode("a fat cat on a mat", "image", "https:/fatcatnamedMattonmat.gov")
    print(text_node_to_html_node(node_for_img) == text_node_to_html_node2(node_for_img))

    print(ParentNode("div", "a div container", [LeafNode("a", "linko", {"class": "link-class","href":"https://www.yahoo.com"}),LeafNode("p", "paragraph")])==
          ParentNode("div", "a div container", [LeafNode("a", "linko", {"href":"https://www.yahoo.com", "class": "link-class"}), LeafNode("p", "paragraph")]))
main()


 # node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    # print(node.__eq__(node2))

    # htmlnode = HTMLNode("1", "good going idiot",[],{"href": "https://www.google.com"})
    # print(htmlnode)

    # node3 = ParentNode(
    # "p",
    # [
    #     LeafNode("b", "Bold text"),
    #     LeafNode(None, "Normal text"),
    #     LeafNode("i", "italic text"),
    #     LeafNode(None, "Normal text"),
    # ],)
    # print(node3.to_html())