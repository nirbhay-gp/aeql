from parsimonious.grammar import Grammar

import tokens






grammar = Grammar(
    r"""
    algb_expr         = 
    asg_expr          = obj_property asg
    obj_property      = obj accessor word
    word              = ~r"[-\w]+"
    obj               = ~"data|func|result|ctx"
    accessor          = "::"
    compa
    lg_in             = ws? "in" ws?
    lg_or             = ws? "or" ws?
    lg_and            = ws? "and" ws?
    asg               = ws? "=" ws?
    ws                = ~"\s*"
    math_ops          = ~"+|-|*|/"
    """
)

print(grammar.parse('data::amount = '))