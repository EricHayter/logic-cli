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
    parser.add_argument("-t", "--table")  # option that takes a value
    args = parser.parse_args()
    with open(args.filename, "r") as file:
        if args.filename.endswith('.func'):
            func = parse_function(file.readline().strip())
        elif args.filename.endswith('.table'):
            func = parse_table(file)
        else:
            raise ValueError(f"Invalid file format")

    prime_implicants = get_prime_implicants(func)
    essential_implicants = get_essential_implicants(
        func, prime_implicants)
    print(get_sop(essential_implicants))


if __name__ == "__main__":
    main()
