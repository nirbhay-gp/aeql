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
    
def test_boolean_numerical_int_eq():
    operand_a = components.int_("2")
    operand_b = components.int_("2")
    
    eq_condition = components.eq_(operand_a, operand_b)
    assert eq_condition.left_operand == operand_a.value
    assert eq_condition.right_operand == operand_b.value
    assert eq_condition.type == "eq"
    assert eq_condition.value == True
    
def test_boolean_numerical_float_eq():
    operand_a = components.float_("2.0")
    operand_b = components.float_("2.0")
    
    equality_condition = components.eq_(operand_a, operand_b)
    
    assert equality_condition.type == "eq"
    assert equality_condition.value == True

def test_boolean_numerical_mixed_eq():
    operand_a = components.float_("2.0")
    operand_b = components.int_("2")
    
    equality_condition = components.eq_(operand_a, operand_b)
    
    assert equality_condition.type == "eq"
    assert equality_condition.value == True
    
def test_boolean_numerical_int_lt():
    operand_a = components.int_("1")
    operand_b = components.int_("2")
    
    lt_condition = components.lt_(operand_a, operand_b)
    assert lt_condition.left_operand == operand_a.value
    assert lt_condition.right_operand == operand_b.value
    assert lt_condition.type == "lt"
    assert lt_condition.value == True

def test_boolean_numerical_int_gt_1():
    operand_a = components.int_("2")
    operand_b = components.int_("1")
    
    gt_condition = components.gt_(operand_a, operand_b)
    assert gt_condition.left_operand == operand_a.value
    assert gt_condition.right_operand == operand_b.value
    assert gt_condition.type == "gt"
    assert gt_condition.value == True

def test_boolean_numerical_int_gt_2():
    operand_a = components.int_("1")
    operand_b = components.int_("2")
    
    gt_condition = components.gt_(operand_a, operand_b)
    assert gt_condition.left_operand == operand_a.value
    assert gt_condition.right_operand == operand_b.value
    assert gt_condition.type == "gt"
    assert gt_condition.value == False

def test_boolean_numerical_int_gte_1():
    operand_a = components.int_("2")
    operand_b = components.int_("1")
    
    gt_condition = components.gte_(operand_a, operand_b)
    assert gt_condition.left_operand == operand_a.value
    assert gt_condition.right_operand == operand_b.value
    assert gt_condition.type == "gte"
    assert gt_condition.value == True

def test_boolean_numerical_int_gte_2():
    operand_a = components.int_("3")
    operand_b = components.int_("3")
    
    gt_condition = components.gte_(operand_a, operand_b)
    assert gt_condition.left_operand == operand_a.value
    assert gt_condition.right_operand == operand_b.value
    assert gt_condition.type == "gte"
    assert gt_condition.value == True

def test_boolean_numerical_int_gte_3():
    operand_a = components.int_("1")
    operand_b = components.int_("3")
    
    gt_condition = components.gte_(operand_a, operand_b)
    assert gt_condition.left_operand == operand_a.value
    assert gt_condition.right_operand == operand_b.value
    assert gt_condition.type == "gte"
    assert gt_condition.value == False

def test_boolean_numerical_int_gte_4():
    operand_a = components.int_("1")
    operand_b = components.int_("4")
    
    gt_condition = components.gte_(operand_a, operand_b)
    assert gt_condition.left_operand == operand_a.value
    assert gt_condition.right_operand == operand_b.value
    assert gt_condition.type == "gte"
    assert gt_condition.value == False
    
def test_boolean_numerical_int_lte_1():
    operand_a = components.int_("1")
    operand_b = components.int_("2")
    
    gt_condition = components.lte_(operand_a, operand_b)
    assert gt_condition.left_operand == operand_a.value
    assert gt_condition.right_operand == operand_b.value
    assert gt_condition.type == "lte"
    assert gt_condition.value == True

def test_boolean_numerical_int_lte_2():
    operand_a = components.int_("3")
    operand_b = components.int_("3")
    
    gt_condition = components.lte_(operand_a, operand_b)
    assert gt_condition.left_operand == operand_a.value
    assert gt_condition.right_operand == operand_b.value
    assert gt_condition.type == "lte"
    assert gt_condition.value == True

def test_boolean_numerical_int_lte_3():
    operand_a = components.int_("3")
    operand_b = components.int_("1")
    
    gt_condition = components.lte_(operand_a, operand_b)
    assert gt_condition.left_operand == operand_a.value
    assert gt_condition.right_operand == operand_b.value
    assert gt_condition.type == "lte"
    assert gt_condition.value == False

def test_boolean_numerical_int_lte_4():
    operand_a = components.int_("4")
    operand_b = components.int_("1")
    
    gt_condition = components.lte_(operand_a, operand_b)
    assert gt_condition.left_operand == operand_a.value
    assert gt_condition.right_operand == operand_b.value
    assert gt_condition.type == "lte"
    assert gt_condition.value == False
    

def test_boolean_combinator_all_1():
    operand_a = components.int_("1")
    operand_b = components.int_("4")
    operand_c = components.int_("3")
    operand_d = components.int_("3")
    operand_e = components.float_("4.5")
    operand_f = components.float_("3.1")
    
    lte_condition_1 = components.lte_(operand_a, operand_b)
    lte_condition_2 = components.lte_(operand_c, operand_d)
    gt_condition_1 = components.gt_(operand_e, operand_f)
    
    assert lte_condition_1.type == "lte"
    assert lte_condition_1.value == True
    
    assert lte_condition_2.type == "lte"
    assert lte_condition_2.value == True
    
    assert gt_condition_1.type == "gt"
    assert gt_condition_1.value == True
    
    combination = components.all_(lte_condition_1, lte_condition_2, gt_condition_1)
    
    assert combination.type == "all"
    assert combination.value == True
    

def test_boolean_combinator_any_1():
    operand_a = components.int_("4")
    operand_b = components.int_("1")
    operand_c = components.int_("3")
    operand_d = components.int_("3")
    operand_e = components.float_("4.5")
    operand_f = components.float_("3.1")
    
    lte_condition_1 = components.lte_(operand_a, operand_b)
    lte_condition_2 = components.lte_(operand_c, operand_d)
    gt_condition_1 = components.gt_(operand_e, operand_f)
    
    assert lte_condition_1.type == "lte"
    assert lte_condition_1.value == False
    
    assert lte_condition_2.type == "lte"
    assert lte_condition_2.value == True
    
    assert gt_condition_1.type == "gt"
    assert gt_condition_1.value == True
    
    combination = components.any_(lte_condition_1, lte_condition_2, gt_condition_1)
    
    assert combination.type == "any"
    assert combination.value == True
    
    