import function_parser
import logic_cli 
import table_parser

t = table_parser.parse_table('table.csv')
print(t)
for key, value in t.items():
    print(key, value)