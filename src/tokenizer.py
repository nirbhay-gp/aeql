import src.rules as rules
import src.tokens as kw_tokens

def generate_token_list(code_str):
    char_index = 0
    tokens = []
    token = ""
    while char_index < len(code_str):
        char = code_str[char_index]
        char_index += 1
        
        is_string_quote = rules.is_string_quote_char(char)
        if is_string_quote:
            token += char
            next_string_quote = False
            while next_string_quote == False or char_index < len(code_str):
                next_char = code_str[char_index]
                char_index += 1
                token += next_char
                is_next_string_quote = rules.is_string_quote_char(next_char)
                if is_next_string_quote:
                    next_string_quote = True
                    break
            tokens.append(token)
            token = ""
            continue
        
        is_math_operator = rules.is_math_operator_char(char)
        if is_math_operator:
            if len(token) > 0:
                tokens.append(token)
            tokens.append(char)
            token = ""
            continue
        
        is_group_operator = rules.is_group_operator_char(char)
        if is_group_operator:
            if len(token) > 0:
                tokens.append(token)
            tokens.append(char)
            token = ""
            continue
        
        is_seperator = rules.is_separator(char)
        if is_seperator:
            if len(token) > 0:
                tokens.append(token)
            tokens.append(char)
            token = ""
            continue
        
        is_whitespace = rules.is_whitespace_char(char)
        if is_whitespace == False:
            token += char
        
        if (is_whitespace == True and len(token) > 0) or \
           (char_index == len(code_str) and len(token) > 0):    
            tokens.append(token)
            token = ""
            
    return tokens

def generate_first_level_labels(tokens):
    tokens_with_labels = []
    for token in tokens:
        if rules.string_literal.fullmatch(token):
            tokens_with_labels.append([token, "string_literal"])
        elif rules.int_literal.fullmatch(token):
            tokens_with_labels.append([token, "int_literal"])
        elif rules.float_literal.fullmatch(token):
            tokens_with_labels.append([token, "float_literal"])
        elif rules.boolean_literal.fullmatch(token):
            tokens_with_labels.append([token, "boolean_literal"])
        elif rules.reserved_keywords.fullmatch(token):
            tokens_with_labels.append([token, "reserved_keyword"])
        elif rules.boolean_keywords.fullmatch(token):
            tokens_with_labels.append([token, "boolean_keyword"])
        elif rules.is_math_operator_char(token):
            tokens_with_labels.append([token, "math_operator"])
        elif rules.is_group_operator_char(token):
            tokens_with_labels.append([token, "group_operator"])
        elif rules.is_separator(token):
            tokens_with_labels.append([token, "separation_operator"])
        else:
            tokens_with_labels.append([token, "unknown"])
    return tokens_with_labels

def generate_second_level_labels(tokens):
    tokens_with_labels = []
    for token in tokens:
        if token[1] == "reserved_keyword":
            if(token[0] == kw_tokens.kw_cache_store):
                token.append("kw_cache_store")
            if(token[0] == kw_tokens.kw_cache_use):
                token.append("kw_cache_use")
                
        if rules.string_literal.fullmatch(token):
            tokens_with_labels.append([token, "string_literal"])
        elif rules.int_literal.fullmatch(token):
            tokens_with_labels.append([token, "int_literal"])
        elif rules.float_literal.fullmatch(token):
            tokens_with_labels.append([token, "float_literal"])
        elif rules.boolean_literal.fullmatch(token):
            tokens_with_labels.append([token, "boolean_literal"])
        elif rules.reserved_keywords.fullmatch(token):
            tokens_with_labels.append([token, "reserved_keyword"])
        elif rules.boolean_keywords.fullmatch(token):
            tokens_with_labels.append([token, "boolean_keyword"])
        elif rules.is_math_operator_char(token):
            tokens_with_labels.append([token, "math_operator"])
        elif rules.is_group_operator_char(token):
            tokens_with_labels.append([token, "group_operator"])
        elif rules.is_separator(token):
            tokens_with_labels.append([token, "separation_operator"])
        else:
            tokens_with_labels.append([token, "unknown"])
    return tokens_with_labels

def generate_labels(tokens):
    tokens_with_labels = []
    tokens_with_labels = generate_first_level_labels(tokens)
    return tokens_with_labels
        

def tokenizer(code_str: "str"):
    tokens = generate_token_list(code_str)
        
        
        