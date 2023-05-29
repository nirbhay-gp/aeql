import re
import src.tokens


# literal
int_literal = re.compile("^\d+$")
float_literal = re.compile("^\d+.\d*$")
boolean_literal = re.compile("true|false")
string_literal = re.compile("^[\"'].*[\"']$")
whitespace_literal = re.compile("\s+")

# reserved_keyword
reserved_keywords = re.compile("with|where|when|what|store|use|describe|yield|result")
boolean_keywords = re.compile("all|any|not|eq|gt|gte|lt|lte")
# variable
variable = "^[A-Za-z][A-Za-z0-9_]*"  # a variable cannot start with _ and digits

alegrabic_expr = "(?P<variable_1>)"


token = re.compile("")


def is_whitespace_char(char: "str"):
    return whitespace_literal.fullmatch(char) is not None


def is_string_quote_char(char: "str"):
    return char == '"' or char == "'"


def is_math_operator_char(char):
    return char in ["+", "-", "*", "/", "^"]


def is_group_operator_char(char):
    return char in ["(", ")", "[", "]"]


def is_separator(char):
    return char in [","]
