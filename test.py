import function_parser
import karnaugh

#a = function_parser.FunctionParser('A+B')
a = function_parser.FunctionParser('(A+B)(A+C)')
function = a.get_truth_table()
#print(function)
print(karnaugh.simplify_function(function,  a.get_symbols()))

# get rid of parse logic but refactor most of the insides into evaluate
# will need to run the function on every call