import sys
from src.tokenizer import generate_token_list, generate_labels
from src.parser import parse
from colorama import init, Fore, Style
from pprint import pprint
import json

if __name__ == '__main__':
    init(autoreset=True)
    filename = sys.argv[1]
    text = open(filename, 'r').read()
    tokens = generate_token_list(text)
    tokens = generate_labels(tokens)
    for token in tokens:
        value = Style.BRIGHT + Fore.BLUE + token[0].ljust(40, " ")
        label = token[1]
        if label == "unknown":
            label = Style.BRIGHT + Fore.RED + token[1]
        else:
            label = Style.NORMAL + Fore.WHITE + token[1]
        print("{}: {}".format(value, label))
        
    tokens = parse(tokens)
    
    print(json.dumps(tokens['with'][1], indent=2))
    print(json.dumps(tokens['where'][1], indent=2))