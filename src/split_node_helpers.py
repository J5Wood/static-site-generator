from textnode import TextNode
from extract_markdown_helpers import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    def extract_nodes(node):
        image_nodes = extract_markdown_images(node.text)
        
        if len(image_nodes) == 0:
            return [node]
        
        img = image_nodes[0] 
        pre_text, post_text = node.text.split(f"![{img[0]}]({img[1]})", 1)

        pre_nodes = extract_nodes(TextNode(pre_text, "text")) if pre_text != "" else None
        post_nodes = extract_nodes(TextNode(post_text, "text")) if post_text != "" else None
        new_nodes = []

        if pre_nodes:
            new_nodes = new_nodes + pre_nodes
        new_nodes.append(TextNode(img[0], "image", img[1]) )
        if post_nodes:
            new_nodes = new_nodes + post_nodes
        return new_nodes

    new_node_list = []
    for node in old_nodes:
        new_node_list = new_node_list + extract_nodes(node)
    return new_node_list

def split_nodes_link(old_nodes):
    def extract_nodes(node):
        link_nodes = extract_markdown_links(node.text)
        
        if len(link_nodes) == 0:
            return [node]
        
        lnk = link_nodes[0] 
        pre_text, post_text = node.text.split(f"[{lnk[0]}]({lnk[1]})", 1)

        pre_nodes = extract_nodes(TextNode(pre_text, "text")) if pre_text != "" else None
        post_nodes = extract_nodes(TextNode(post_text, "text")) if post_text != "" else None
        new_nodes = []

        if pre_nodes:
            new_nodes = new_nodes + pre_nodes
        new_nodes.append(TextNode(lnk[0], "link", lnk[1]) )
        if post_nodes:
            new_nodes = new_nodes + post_nodes
        return new_nodes

    new_node_list = []
    for node in old_nodes:
        new_node_list = new_node_list + extract_nodes(node)
    return new_node_list
