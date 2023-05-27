import uuid
import string

template_path = "/aeql/src/templates/rule_handler.txt"
with open(template_path, "r") as file:
    with_block_string = file.read()

with_block_template = string.Template(with_block_string)

ast = [
    {
        "type": ["describe", "reserved_keyword"],
        "attributes": [["priority", "unknown"], ["1", "int_literal"]],
    },
    {
        "type": ["describe", "reserved_keyword"],
        "attributes": [["name", "unknown"], ['"debit_txn_cashback"', "string_literal"]],
    },
    {
        "type": ["describe", "reserved_keyword"],
        "attributes": [
            ["description", "unknown"],
            ['"This is a test rule"', "string_literal"],
        ],
    },
    {
        "type": ["store", "reserved_keyword"],
        "attributes": [["seed_value", "unknown"], ["1.4", "float_literal"]],
    },
]

class CodeGeneration:
    TYPES_MAP = {
        "float_literal": float,
        "int_literal": int,
        "string_literal": str,
        "boolean_literal": bool,
    }

    def __init__(self, ast: list[dict], template: string.Template) -> None:
        self.ast = ast
        self.template = template
        self.with_block_statements = {
            "describe": [],
            "store": [],
            "slug": uuid.uuid4()
        }

    def substitute_with_block(self) -> "CodeGeneration":
        # TODO - filter out with block
        node_types = {
            "describe": [],
            "store": []
        }
        for node in ast:
            node_type = node["type"][0]
            label_attributes, value_attributes = node["attributes"]

            label = label_attributes[0]
            value_type = value_attributes[1]
            value = self.TYPES_MAP[value_type](value_attributes[0])

            prefix = None
            if node_type == "describe":
                prefix = "self."
            
            if node_type == "store":
                prefix = "self.context."
            
            statement = f'{prefix}{label} = {f"{value}" if type(value) == str else value}'
            node_types[node_type].append(statement)

            self.with_block_statements["describe"] = "\n\t".join(node_types["describe"])
            self.with_block_statements["store"] = "\n\t".join(node_types["store"])
        
        return self
    
    def code(self) -> str:
        subsituitions = {}
        for key, value in self.with_block_statements.items():
            subsituitions[key] = value
        
        return self.template.safe_substitute(**subsituitions)


code_gen = CodeGeneration(ast, with_block_template)
print(code_gen.substitute_with_block().code())
