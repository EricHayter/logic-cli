# logic-cli

Logic-CLI is a python tool meant to speed up the process of finding simplified expressions and truth tables for logical
expressions. The tool requires 0 external dependencies and is created %100 within python's standard library.

## Using Logic-CLI

getting started with Logic-CLI is very simple. Simply start with a file with a `.func` or `.table` file extension for
logical expressions and truth tables respectively. Information for either the truth table of function can be found using
the optional flags for the tool such as `--table`, `-sop`, or `-pos`.

Here's two example calls to the tool:

```python main.py function.func --table -sop```

```python main.py table.table -pos```

The first call to the tool will read the given logical expression from `function_name.func` and then proceed to print out the
truth table of the expression and the sum of products simplification of the function. The second call will read a truth
table from `table_name.table` and then print the product of sums simplification of the function in the truth table.

## File formats

