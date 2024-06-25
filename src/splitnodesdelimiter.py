from textnode import TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    delimit_type = ""
    formatted_delimiter = ""
    match(delimiter):
        case("`"):
            delimit_type = "code"
            formatted_delimiter = delimiter
        case("*"):
            delimit_type = "bold"
            formatted_delimiter = "\\*"
        case("**"):
            delimit_type = "italics"
            formatted_delimiter = "\\*\\*"
        case _:
            raise Exception("Incorrect delimiting string passed in")

    new_nodes = []

    for node in old_nodes:
        delimit = False
        if node.text.count(delimiter) % 2 != 0:
            raise Exception("Invalid number of delimiters, likely missing a closing tag.")
        split_text = re.split(f"({formatted_delimiter})", node.text)

        for str in split_text:
            # if the current string is a delimiter, turn on or off delimiting
            if str == delimiter:
                delimit = not delimit
            # If delimiting, return delimited type of node
            elif delimit == True:
                new_nodes.extend([TextNode(str, delimit_type, None)])
            # Else, return normal text
            else:
                new_nodes.extend([TextNode(str, text_type, None)]) 
    return new_nodes
