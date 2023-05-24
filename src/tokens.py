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
cmp_eq        = "eq"
cmp_gt        = "gt"
cmp_gte       = "gte"
cmp_lt        = "lt"
cmp_lte       = "lte"
cmp_nte       = "ne"
cmp_operator_group = (
    cmp_eq,
    cmp_gt,
    cmp_gte,
    cmp_lt,
    cmp_lte,
)
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
kw_describe = "describe"
kw_yield  = "yield"
kw_result = "result"
kw_time   = "time"
kw_with   = "with"
kw_when   = "when"
kw_where  = "where"
kw_what   = "what"

bool_all = "all"
bool_any = "any"
bool_not = "not"
bool_group = (bool_all, bool_any, bool_not)

desc_lit_boolean = "boolean_literal"
desc_lit_string = "string_literal"
desc_lit_int = "int_literal"
desc_lit_float = "float_literal"
desc_unknown = "unknown"
desc_reserved = "reserved_keyword"
desc_kw_boolean = "boolean_keyword"
desc_group_value_types = (desc_lit_boolean, desc_lit_float, desc_lit_int, desc_lit_string, desc_unknown)