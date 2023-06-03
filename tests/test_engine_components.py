import src.engine.components as components


def test_boolean_literal_true():
    obj = components.bool_("true")

    assert obj.type == "bool"
    assert obj.value == True


def test_boolean_literal_false():
    obj = components.bool_("false")

    assert obj.type == "bool"
    assert obj.value == False


def test_string_literal():
    python_string_literal = "This is a string literal"
    obj = components.str_(python_string_literal)

    assert obj.type == "str"
    assert obj.value == python_string_literal


def test_int_literal():
    python_int_literal = "1"

    obj = components.int_(python_int_literal)

    assert obj.type == "int"
    assert obj.value == 1


def test_float_literal():
    python_float_literal = "1.2"

    obj = components.float_(python_float_literal)

    assert obj.type == "float"
    assert obj.value == 1.2


def test_math_add_int_values():
    # computes a 1+3

    operand_a = components.int_("1")
    operand_b = components.int_("2")

    add_expression = components.add_(operand_a, operand_b)

    assert add_expression.type == "add"
    assert add_expression.value == 3


def test_math_add_float_values():
    operand_a = components.float_("1.2")
    operand_b = components.float_("2.1")

    add_expression = components.add_(operand_a, operand_b)

    assert add_expression.type == "add"
    assert add_expression.value == 3.3


def test_math_add_mixed_values():
    operand_a = components.int_("1")
    operand_b = components.float_("1.2")

    add_expression = components.add_(operand_a, operand_b)

    assert add_expression.type == "add"
    assert add_expression.value == 2.2


def test_math_subtract_int_values():
    operand_a = components.int_("1")
    operand_b = components.int_("2")

    subtract_expression = components.subtract_(operand_a, operand_b)

    assert subtract_expression.type == "subtract"
    assert subtract_expression.value == -1


def test_math_subtract_float_values():
    operand_a = components.float_("2.5")
    operand_b = components.float_("1.4")

    subtract_expression = components.subtract_(operand_a, operand_b)

    assert subtract_expression.type == "subtract"
    assert subtract_expression.value == 1.1


def test_math_subtract_mixed_values():
    operand_a = components.int_("2")
    operand_b = components.float_("1.4")

    subtract_mixed_expression = components.subtract_(operand_a, operand_b)

    assert subtract_mixed_expression.type == "subtract"
    assert subtract_mixed_expression.value == (
        2 - 1.4
    )  # because of floating point digits in python


def test_math_multiply_int_values():
    operand_a = components.int_("2")
    operand_b = components.int_("2")

    subtract_mixed_expression = components.multiply_(operand_a, operand_b)

    assert subtract_mixed_expression.type == "multiply"
    assert subtract_mixed_expression.value == 4


def test_math_multiply_float_values():
    operand_a = components.float_("2.5")
    operand_b = components.float_("2.5")

    subtract_mixed_expression = components.multiply_(operand_a, operand_b)

    assert subtract_mixed_expression.type == "multiply"
    assert subtract_mixed_expression.value == 2.5 * 2.5

def test_math_multiply_mixed_values():
    operand_a = components.int_("2")
    operand_b = components.float_("2.5")

    subtract_mixed_expression = components.multiply_(operand_a, operand_b)

    assert subtract_mixed_expression.type == "multiply"
    assert subtract_mixed_expression.value == 2 * 2.5

def test_math_divide_int_values():
    operand_a = components.int_("2")
    operand_b = components.int_("2")

    subtract_mixed_expression = components.divide_(operand_a, operand_b)

    assert subtract_mixed_expression.type == "divide"
    assert subtract_mixed_expression.value == 1


def test_math_divide_float_values():
    operand_a = components.float_("2.5")
    operand_b = components.float_("2.5")

    subtract_mixed_expression = components.divide_(operand_a, operand_b)

    assert subtract_mixed_expression.type == "divide"
    assert subtract_mixed_expression.value == 1

def test_math_divide_mixed_values():
    operand_a = components.int_("2")
    operand_b = components.float_("2.5")

    subtract_mixed_expression = components.divide_(operand_a, operand_b)

    assert subtract_mixed_expression.type == "divide"
    assert subtract_mixed_expression.value == 0.8