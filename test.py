import logic_function
import logic_cli 

v = logic_cli.input_combos(2)
a = logic_function.LogicFunction('A+(A.C)')
print(a.get_symbols())
for i in v:
    print(i, a.evaluate(i))