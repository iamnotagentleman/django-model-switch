import argparse
import ast
from pathlib import Path

from visitors.django import ModelVisitor
from generators.pony import PonyOrmGenerator
# Create the parser
my_parser = argparse.ArgumentParser(description='Django Model Parser')

# Add the arguments
my_parser.add_argument(
    "--path",
    "-p",
    dest='ModelPath',
    type=str,
    help='the path to django model')
my_parser.add_argument(
    "--output",
    "-o",
    dest='Output',
    type=str,
    help='the path to output')
my_parser.add_argument(
    '--to',
    '-t',
    dest='To',
    type=str,
    help='output type (ex: pony, tortoise, pydantic')
# Execute the parse_args() method
args = my_parser.parse_args()
model_path = args.ModelPath
output = args.Output
to = args.To
if not all([model_path, output, output]):
    raise ValueError("All arguments must be settled.")

model_file = Path(model_path)
if not model_file.is_file():
    raise ValueError(f"{model_path} File Does Not Exist")
pool = []
with open(model_file, "r") as file:
    parse = ast.parse(file.read())
    model_visitor = ModelVisitor()
    model_visitor.visit(parse)
    parser_2_model = PonyOrmGenerator.generate_pony_fields_from_list(model_visitor.models.fields)
    for i in parser_2_model:
        pool.append(i)
import pprint; pprint.pprint(pool)