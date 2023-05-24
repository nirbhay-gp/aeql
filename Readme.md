### What is werlang?

werlang is a sql inspired expression language, with the goal to build a complete programming feature set for business users to write rules and procedures.


### An example rule
```
with
    describe priority       1
    describe name           "debit_txn_cashback"
    describe description    "This is a test rule"
    store    seed_value     1.4
where
    event_name eq 'm2p_debit_txn'
when
    store consider_txn_from   yield get_txn_date_start [entity_id]
    store person.txn.is_first yield persons_first_txn  [entity_id, use consider_txn_from]
    all 
        txn_amount      gt 100
        txn_type        eq "ECOM"
        any     
            merchant_name                eq "dominos"
            not use is_persons_first_txn eq true
what    
    store  reward_percentage yield dominoes_random_5percent_cashback [entity_id]
    result key               "DEBIT_TXN:"+txn_id
    result amount            txn_amount * use reward_percentage
    result due_date          time 'in 10 days'
```

### Things to be build
- Lexer in python
- Parser in python
- AST generation
- Python executable code generation