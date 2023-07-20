"""
main executable function for running the logic-cli program
"""


import argparse
from pprint import pprint

from function_parser import parse_function
from karnaugh import get_prime_implicants, get_essential_implicants


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
        filetype = file.readline().strip()
        if filetype == "FUNCTION":
            func = parse_function(file.readline().strip())
            prime_implicants = get_prime_implicants(func)
            pprint(get_essential_implicants(func, prime_implicants))
        elif filetype == "TABLE":
            func = "xd"
            pass
        else:
            raise ValueError(f"Invalid file format: {filetype}")
        print(func)


if __name__ == "__main__":
    main()
