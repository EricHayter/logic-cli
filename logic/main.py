import argparse
import function_parser
import karnaugh


def main():
    parser = argparse.ArgumentParser(
        prog='Logic-CLI',
        description='A simple tool for analyzing and simplifying logical functions'
    )
    parser.add_argument('filename')
    parser.add_argument('-t', '--table')  # option that takes a value
    args = parser.parse_args()
    with open(args.filename) as file:
        filetype = file.__next__().strip()
        if filetype == 'FUNCTION':
            func = function_parser.FunctionParser(file.__next__().strip())
            func = func.get_truth_table()
            func = karnaugh.simplify_function(func)
            print(karnaugh.get_sop(func))
            dont_cares = [dc for dc in file]
            print(dont_cares)
        elif filetype == 'TABLE':
            pass
        else:
            raise Exception(f'Invalid file format: {filetype}')


if __name__ == '__main__':
    main()
