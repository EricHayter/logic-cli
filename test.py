import function_parser
import karnaugh

#a = function_parser.FunctionParser('A+B')
a = function_parser.FunctionParser('C.A+B+C')
function = a.get_truth_table()
#print(function)
print(karnaugh.simplify_function(function))

# get rid of parse logic but refactor most of the insides into evaluate
# will need to run the function on every call