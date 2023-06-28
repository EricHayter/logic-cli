import re

def parse_proposition(proposition: str):
    matches = re.findall(r'~?[A-Z]', proposition)
    if not matches:
        print('not matching anything')
        return

    # find the final opening bracket and then start simplfying
    return matches

    


def main():
    print(parse_proposition('O=A+B.C'))

if __name__ == '__main__':
    main()

'''
should be able to pass in a string
split at every 'symbol' (except not)

'''
