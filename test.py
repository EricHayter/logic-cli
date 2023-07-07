import function_parser
import karnaugh

a = function_parser.FunctionParser('A+B')
#a = function_parser.FunctionParser('A.B+~A')
function = a.get_truth_table()
print(function)
print(karnaugh.simplify_function(function))
