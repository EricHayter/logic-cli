"""
main executable function for running the logic-cli program
"""

import argparse

from function_parser import parse_function
from table_parser import parse_table
from logic_function import print_truth_table
from karnaugh import print_sop, print_pos


def main():
    """main function"""
    parser = argparse.ArgumentParser(
        prog="Logic-CLI",
        description="A simple tool for analyzing and simplifying logical functions",
    )
    parser.add_argument("filename")
    parser.add_argument("-t", "--table", action="store_true")
    parser.add_argument("-sop", "--sum-of-products", action="store_true")
    parser.add_argument("-pos", "--product-of-sums", action="store_true")
    args = parser.parse_args()
    if args.filename.endswith('.func'):
        func = parse_function(args.filename)
    elif args.filename.endswith('.table'):
        func = parse_table(args.filename)
    else:
        raise ValueError("Invalid file format")

    if args.table:
        print_truth_table(func)
    if args.sum_of_products:
        print_sop(func)
    if args.product_of_sums:
        print_pos(func)


if __name__ == "__main__":
    main()
