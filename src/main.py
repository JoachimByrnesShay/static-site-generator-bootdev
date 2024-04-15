from textnode import TextNode 
from htmlnode import HTMLNode


def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node.__repr__())
    node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node.__eq__(node2))

    htmlnode = HTMLNode("1", "good going idiot",[],{"href": "https://www.google.com"})
    print(htmlnode)

main()
