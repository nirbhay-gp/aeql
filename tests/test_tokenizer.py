import src.tokenizer

def test_token_list_generate():
    tokens = src.tokenizer.generate_token_list("a + b")
    assert len(tokens) == 3
    assert tokens[0] == "a"
    assert tokens[1] == "+"
    assert tokens[2] == "b"
    
def test_string_tokenization():
    tokens = src.tokenizer.generate_token_list("\"alpha\"")
    assert len(tokens) == 1
    assert tokens[0] == "\"alpha\""
    
def test_unspaced_math_expression_tokenization_1():
    tokens = src.tokenizer.generate_token_list("a+b")
    assert len(tokens) == 3
    assert tokens[0] == "a"
    assert tokens[1] == "+"
    assert tokens[2] == "b"
    
def test_unspaced_math_expression_tokenization_2():
    tokens = src.tokenizer.generate_token_list("+b")
    assert len(tokens) == 2
    assert tokens[0] == "+"
    assert tokens[1] == "b"

def test_unspaced_math_expression_tokenization_3():
    tokens = src.tokenizer.generate_token_list("a-")
    assert len(tokens) == 2
    assert tokens[0] == "a"
    assert tokens[1] == "-"

def test_unspaced_group_expression_tokenization_3():
    tokens = src.tokenizer.generate_token_list("(a-b)")
    assert len(tokens) == 5
    assert tokens[0] == "("
    assert tokens[1] == "a"
    assert tokens[2] == "-"
    assert tokens[3] == "b"
    assert tokens[4] == ")"