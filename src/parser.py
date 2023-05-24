from itertools import takewhile
import src.tokens as tokens

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
            
    return counter, {
        "type": modifier, 
        "attributes": attributes
    } 

def generate_describe_expression(token_blocks, counter):    
    modifier = token_blocks[counter]
    variable = token_blocks[counter+1]
    value = token_blocks[counter+2]
    
    # add validation rules
    
    return counter+3, {
        "type": modifier,
        "attributes": [
            variable,
            value
        ]
    }
    
def generate_boolean_expression(token_blocks, counter):
    print("COUNTER", counter)
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
        return counter, {
            "type": operand_token,
            "attributes": attributes
        }
            
    comparator_token = token_blocks[counter+1]
    secondary_operand_token = token_blocks[counter+2]
    counter += 2
    if secondary_operand_token[1] == tokens.desc_reserved \
        and secondary_operand_token[0] == tokens.kw_cache_use:
            latest_counter, inner_stack_element = generate_store_expression(token_blocks, counter)
            counter = latest_counter
            secondary_operand_token = inner_stack_element
    
    if operand_token[1] in tokens.desc_group_value_types \
       and secondary_operand_token[1] in tokens.desc_group_value_types \
       and comparator_token[1] == tokens.desc_kw_boolean \
       and comparator_token[0] in tokens.cmp_operator_group:
           return counter+1, {
               "type": comparator_token,
               "attributes": [
                   operand_token,
                   secondary_operand_token
               ]
           }
    
    
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
    return {
        'with': with_result,
        'where': where_result
    }
        