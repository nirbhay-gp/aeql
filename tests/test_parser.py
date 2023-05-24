from src.parser import generate_boolean_expression


def test_boolean_expression_parser():
    token_blocks = [
        ["event_name","unknown"],
        ["eq","boolean_keyword"],
        ['m2p_debit_txn',"string_literal"]
    ]
    result = generate_boolean_expression(token_blocks, 0)
    
    assert isinstance(result[1], dict) 
    
def test_boolean_expression_parser():
    token_blocks = [
        ["all", "boolean_keyword"],
        ["event_name","unknown"],
        ["eq","boolean_keyword"],
        ["\'m2p_debit_txn\'","string_literal"],
        ["event_type","unknown"],
        ["eq","boolean_keyword"],
        ["\'ecom\'","string_literal"]
    ]
    result = generate_boolean_expression(token_blocks, 0)
    
    assert isinstance(result[1], dict) 
    
    
