"""
main executable function for running the logic-cli program
"""

import argparse

from function_parser import parse_function
from table_parser import parse_table
from karnaugh import get_prime_implicants, get_essential_implicants, get_sop


# custom file extensions?
def main():
    """main function"""
    parser = argparse.ArgumentParser(
        prog="Logic-CLI",
        description="A simple tool for analyzing and simplifying logical functions",
    )
    parser.add_argument("filename")
    parser.add_argument("-t", "--table")
    args = parser.parse_args()
    if args.filename.endswith('.func'):
        func = parse_function(args.filename)
    elif args.filename.endswith('.table'):
        func = parse_table(args.filename)
    else:
        raise ValueError("Invalid file format")

    # printing out POS or SOP
    # printing out a table if they want it

    prime_implicants = get_prime_implicants(func)
    essential_implicants = get_essential_implicants(
        func, prime_implicants)
    print(get_sop(essential_implicants))


if __name__ == "__main__":
    main()
