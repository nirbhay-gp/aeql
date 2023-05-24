"""
    this document contains all the possible
    token elements in the lang, this tokenset
    will define grammar and syntax of werlang
"""

# whitespace
ws            = "\\s*"

# mathematical operators
mt_add        = "\+"
mt_sub        = "\-"
mt_product    = "\*"
mt_division   = "\/"
mt_exp        = "\^"

# comparison operators
cmp_eq        = "=="
cmp_gt        = ">"
cmp_gte       = ">="
cmp_lt        = "<"
cmp_lte       = "<="
cmp_nte       = "!="

# logical operators
lg_and        = "all"
lg_or         = "any"
lg_not        = "not"

# accessor operator
access        = "::"

# grouping operators
grp_lpar = "\("
grp_rpar = "\)"

# literals
ltr_str       = "\"(\\w*|\\W*)*\""
ltr_num       = "\\d*\\.\\d*"
ltr_bool      = "true|false"
ltr_true      = "true"
ltr_false     = "false"

#keywords
kw_cache_store  = "store"
kw_cache_use    = "use"
kw_yield  = "yield"
kw_result = "result"
kw_time   = "time"
kw_with   = "with"
kw_when   = "when"
kw_where  = "where"
kw_what   = "what"