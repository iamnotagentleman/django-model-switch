import ast

from visitors.django import ModelVisitor


def loads(script):
    node = ast.parse(script)
    visitor = ModelVisitor()
    visitor.visit(node)
    return visitor.models
