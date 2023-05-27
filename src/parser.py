from itertools import takewhile
import src.tokens as tokens
import src.rules as rules
from dataclasses import dataclass
from typing import List

@dataclass
class Node:
    value: str
    type: str
    attributes: List["Token"]
    
    def str(self, spacer):
        node_string = "Node({}): {}".format(self.type, self.value)
        print(spacer + "  "+ node_string)
        for attribute in self.attributes:
            attribute.str(spacer + "   ")
        # attributes_string_list = list(map(lambda x: x.__repr__(), self.attributes))
        # attributes_string = ""
        # for item in attributes_string_list:
        #     attributes_string += "  |-" + item + "\n  "
        # # attributes_string = "  |-" + "  |-".join()
        # return node_string + "\n  " + attributes_string

def create_blocks(tokens):
    with_tokens = []
    where_tokens = []
    when_tokens = []
    what_tokens = []
    
    index = 1
    token = tokens[0]
    next_block_tokens = ["where", "when", "what"]
    token_block = []
    
    while token != next_block_tokens[0] and index < len(tokens):
        token = tokens[index]
        if token[0] in next_block_tokens:
            if token[0] == "where":
                with_tokens = token_block 
            elif token[0] == "when":
                where_tokens = token_block
            elif token[0] == "what":
                when_tokens = token_block
            token_block = []
        else:
            token_block.append(token)
        if index + 1 == len(tokens):
            what_tokens = token_block
        index += 1
    
    return {
        "with": with_tokens,
        "where": where_tokens,
        "when": when_tokens,
        "what": what_tokens
    }
    
def generate_store_expression(token_blocks, counter):    
    modifier = token_blocks[counter]
    variable = token_blocks[counter+1]
    value = token_blocks[counter+2]
    
    attributes = [variable]
    if value[0] == tokens.kw_yield:
        latest_counter, stack_element = generate_ast(token_blocks, counter+2)
        counter = latest_counter
        attributes += [stack_element]
    elif value[0] == tokens.kw_cache_use:
        counter += 2
    else:
        counter += 3
        attributes += [value]
    
    # add validation rules
            
    return counter, Node(modifier[0], modifier[1], attributes)

def generate_yield_expression(token_blocks, counter):    
    modifier = token_blocks[counter]
    callable = token_blocks[counter+1]
    params_group_left_separator = token_blocks[counter+2]
    params_group_right_separator = None
    
    if rules.is_group_operator_char(params_group_left_separator):
        right_counter = counter+2
        while params_group_right_separator is None and right_counter < len(token_blocks):
            
        
    if len(token_blocks) >= counter+2:
        params_group_separator = token_blocks[counter+2]
    
    attributes = [variable]
    if value[0] == tokens.kw_yield:
        latest_counter, stack_element = generate_ast(token_blocks, counter+2)
        counter = latest_counter
        attributes += [stack_element]
    elif value[0] == tokens.kw_cache_use:
        counter += 2
    else:
        counter += 3
        attributes += [value]
    
    # add validation rules
            
    return counter, Node(modifier[0], modifier[1], attributes)

def generate_describe_expression(token_blocks, counter):    
    modifier = token_blocks[counter]
    variable = token_blocks[counter+1]
    value = token_blocks[counter+2]
    
    # add validation rules
    
    return counter+3, Node(modifier[0], modifier[1], [
        Node(variable[0], variable[1], []),
        Node(value[0], value[1], [])
    ])
    
def generate_boolean_expression(token_blocks, counter):
    operand_token = token_blocks[counter]
    
    if operand_token[1] == tokens.desc_kw_boolean \
       and operand_token[0] in tokens.bool_group:
        stop = False
        counter += 1
        attributes = []
        while stop == False:
            latest_counter, stack_element = generate_boolean_expression(token_blocks, counter)
            counter = latest_counter
            attributes.append(stack_element)
            if counter == len(token_blocks):
                stop = True
        return counter, Node(operand_token[0], operand_token[1], attributes)
            
    comparator_token = token_blocks[counter+1]
    secondary_operand_token = token_blocks[counter+2]
    counter += 2
    if secondary_operand_token[1] == tokens.desc_reserved \
        and secondary_operand_token[0] == tokens.kw_cache_use:
            latest_counter, inner_stack_element = generate_store_expression(token_blocks, counter)
            counter = latest_counter
            secondary_operand_token = inner_stack_element
    else:
        secondary_operand_token = Node(secondary_operand_token[0], secondary_operand_token[1], [])
    if operand_token[1] in tokens.desc_group_value_types \
       and (secondary_operand_token.type in tokens.desc_group_value_types or secondary_operand_token[1] in tokens.desc_group_value_types \
             or isinstance(secondary_operand_token, dict)\
             or isinstance(secondary_operand_token, Node))\
       and comparator_token[1] == tokens.desc_kw_boolean \
       and comparator_token[0] in tokens.cmp_operator_group:
           return counter+1, Node(comparator_token[0], comparator_token[1], [
                Node(operand_token[0], operand_token[1], []),
                secondary_operand_token
            ])
    
    
    # stack = []
    # token = token_blocks[counter]
    # if token[0] in (tokens.bool_all, tokens.bool_any, tokens.bool_not):
    #     stop = False
    #     attributes = []
    #     while stop == False:
    #         latest_counter, stack_element = generate_boolean_expression(token_blocks, counter+1)
    #         counter = latest_counter
    # else:
    #     operator = token_blocks[counter+1]
    #     second_operand = token_blocks[counter+2]
    
    
            
            
def generate_ast(token_blocks, counter):
    stack = []
    while counter < len(token_blocks):
        token = token_blocks[counter]
        if token[1] == tokens.desc_reserved and token[0] == tokens.kw_cache_store:
            latest_counter, stack_element = generate_store_expression(token_blocks, counter)
            stack.append(stack_element)
            counter = latest_counter
        elif token[1] == tokens.desc_reserved and tokens[0] == tokens.kw_cache_store:
            latest_counter, stack_element = generate_yield_expression(token_blocks, counter)
            stack.append(stack_element)
            counter = latest_counter
        elif token[1] == tokens.desc_reserved and token[0] == tokens.kw_describe:
            latest_counter, stack_element = generate_describe_expression(token_blocks, counter)
            stack.append(stack_element)
            counter = latest_counter
        elif token[1] == tokens.desc_kw_boolean and token[0] in (tokens.bool_all, tokens.bool_any):
            latest_counter, stack_element = generate_boolean_expression(token_blocks, counter)
            stack.append(stack_element)
            counter = latest_counter
        else:
            counter += 1
    
    return counter, stack


def parse(tokens):
    token_blocks = create_blocks(tokens)
    with_result = generate_ast(token_blocks["with"], 0)
    where_result = generate_ast(token_blocks["where"], 0)
    when_result = generate_ast(token_blocks["when"], 0)
    return {
        'with': with_result,
        'where': where_result,
        'when': when_result
    }
        