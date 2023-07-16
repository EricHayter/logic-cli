"""
main executable function for running the logic-cli program
"""


import argparse
import logic.function_parser
import logic.karnaugh


def main():
    """main function"""
    parser = argparse.ArgumentParser(
        prog='Logic-CLI',
        description='A simple tool for analyzing and simplifying logical functions'
    )
    parser.add_argument('filename')
    parser.add_argument('-t', '--table')  # option that takes a value
    args = parser.parse_args()
    with open(args.filename, 'r') as file:
        filetype = file.next().strip()
        if filetype == 'FUNCTION':
            func = logic.function_parser.FunctionParser(file.next().strip())
            func = func.get_truth_table()
            func = logic.karnaugh.simplify_function(func)
            print(logic.karnaugh.get_sop(func, ))
            dont_cares = list(dc for dc in file)
            print(dont_cares)
        elif filetype == 'TABLE':
            pass
        else:
            raise ValueError(f'Invalid file format: {filetype}')


if __name__ == '__main__':
    main()
