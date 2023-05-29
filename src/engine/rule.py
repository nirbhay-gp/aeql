from typing import List, Union
from src.engine.protocols import Rule
from src.parser import Node
import src.engine.components as components


def generate_expression_tree(node: "Union[Node,List[Node]]"):
    if isinstance(node, list):
        return list(map(lambda x: generate_expression_tree(x)))

    operands = []
    if node.is_leaf == False:
        operands = generate_expression_tree(node.attributes)
        
    if node.type == "boolean_keyword":
        if node.value == "all":
            return components.all_(operands)
        if node.value == "any":
            return components.all_(operands)
        if node.value == "not":
            return components.not_(operands)
        if node.value == "eq":
            return components.eq_(operands)
        if node.value == "gte":
            return components.gte_(operands)
        if node.value == "gt":
            return components.gte_(operands)
        if node.value == "lte":
            return components.gte_(operands)
        if node.value == "lt":
            return components.gte_(operands)
    elif node.type == "math_operator":
        if node.value == "+":
            return components.add_(operands)
        if node.value == "-":
            return components.subtract_(operands)
        if node.value == "/":
            return components.divide_(operands)
        if node.value == "*":
            return components.multiply_(operands)
        if node.value == "^":
            return components.exponent_(operands)
    elif node.type == "unknown":
        return components.data_(node.value)
    elif node.type == "cache":
        return components.context_(node.value)
    elif node.type == "string_literal":
        return components.str_(node.value)
    elif node.type == "int_literal":
        return components.int_(node.value)
    elif node.type == "float_literal":
        return components.float_(node.value)
    elif node.type == "boolean_literal":
        return components.bool_(node.value)
        


class rule_(Rule):
    
    def __init__(self, config):
        when_block = config["when"]
        what_block = config["what"]
        self.__qualifier_tree = generate_expression_tree(when_block)
        self.__result_tree = generate_expression_tree(what_block)

    def __call__(self, procedures, result, context, data):
        pass    
    
    @property
    def selector(self):
        # return a json scheme
        pass
    
    @property
    def qualifier(self):
        qualifying_statements = list(map(lambda x: x.value, self.__qualifier_tree))
        return qualifying_statements[-1]

    @property
    def result(self):
        resulting_statements = list(map(lambda x: x.value, self.__result_tree))
        
        