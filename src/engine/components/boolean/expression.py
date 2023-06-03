from src.engine.protocols import BooleanExpression


class eq_(BooleanExpression):
    def __init__(self, *args):
        super().__init__("eq", *args)

    @property
    def value(self):
        return self.left_operand == self.right_operand


class gt_(BooleanExpression):
    def __init__(self, *args):
        super().__init__("gt", *args)

    @property
    def value(self):
        return self.left_operand > self.right_operand


class lt_(BooleanExpression):
    def __init__(self, *args):
        super().__init__("lt", *args)

    @property
    def value(self):
        return self.left_operand < self.right_operand


class gte_(BooleanExpression):
    def __init__(self, *args):
        super().__init__("gte", *args)

    @property
    def value(self):
        return self.left_operand >= self.right_operand


class lte_(BooleanExpression):
    def __init__(self, *args):
        super().__init__("lte", *args)

    @property
    def value(self):
        return self.left_operand <= self.right_operand


class not_(BooleanExpression):
    def __init__(self, *args):
        super().__init__("not", *args)

    @property
    def value(self):
        return not self.left_operand


__all__ = ("eq_", "gt_", "gte_", "lt_", "lte_", "not_")
