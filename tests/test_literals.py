import re
import src.rules as token_rules

def test_int_literal():
    int_literal_regex = re.compile(token_rules.int_literal)
    match_obj = int_literal_regex.fullmatch("1")
    assert match_obj is not None
    assert isinstance(match_obj, re.Match) == True

def test_float_literal():
    float_literal_regex = re.compile(token_rules.float_literal)
    match_obj = float_literal_regex.fullmatch("1.0")
    assert match_obj is not None
    assert isinstance(match_obj, re.Match) == True
    
def test_boolean_literal():
    boolean_literal_regex = re.compile(token_rules.boolean_literal)
    match_obj = boolean_literal_regex.fullmatch("true")
    assert match_obj is not None
    assert isinstance(match_obj, re.Match) == True

def test_string_literal():
    string_literal_regex = re.compile(token_rules.string_literal)
    match_obj = string_literal_regex.fullmatch("\"true\"")
    assert match_obj is not None
    assert isinstance(match_obj, re.Match) == True