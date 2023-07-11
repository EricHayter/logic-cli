from context import logic
import logic.function_parser
import logic.karnaugh
from pprint import pprint

a = logic.function_parser.FunctionParser('(A+B).(A+C)') # (A+B).(A+C)
function = a.get_truth_table()

print('This is the function: ')
print(a.get_variables())
pprint(function)


simple_function = logic.karnaugh.simplify_function(function)
print('This prime implicants are: ')
pprint(simple_function)

print(logic.karnaugh.print_sop(simple_function,  a.get_variables()))

# get rid of parse logic but refactor most of the insides into evaluate
# will need to run the function on every call
