from context import logic
import logic.function_parser
import logic.karnaugh

#a = function_parser.FunctionParser('A+B')
a = logic.function_parser.FunctionParser('(A+B).(A+C)')
function = a.get_truth_table()
print(function)
#print(function)
print(logic.karnaugh.simplify_function(function,  ('A','B','C')))

# get rid of parse logic but refactor most of the insides into evaluate
# will need to run the function on every call
