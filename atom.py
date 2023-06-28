import re


class Atom:
    # where should I keep the list of symbols?
    #

    def __init__(self, proposition: str) -> None:
        self.symbols = dict()
        self.parse_symbols(proposition)
        self.logic_function = self.parse_logic()

    def sym(self, symbol: str) -> function:
        '''
        returns a wrapper function to retrieve the value of the given symbol\
        WORKS PERFECTLY SMARTEST PROGRAMMER THAT EVER LIVED TYPE BEAT
        '''
        if symbol not in self.symbols:
            raise Exception(f'Unkown symbol {symbol}')

        return lambda symbol: self.symbols[symbol]

    def parse_symbols(self, proposition: str) -> None:
        matches = re.findall(r'[~().+A-Z]', proposition)
        if not matches:
            print('not matching anything')
            return

        for symbol in matches:
            if symbol >= 'A' and symbol <= 'Z':
                if symbol not in self.symbols:
                    self.symbols[symbol] = None
            else:
                raise Exception('Symbol must be in range [A-Z]')
            
    def parse_logic(self, expression: list[object]) -> list[function]:
        # could make it a recursive function
        # return lambdas each step of the way
        if '(' in expression:
            start, stop = Atom.find_parenth_pair(expression)
            logic = self.parse_logic(expression[start:stop+1])
            for i in range(stop-start):
                expression.pop(i)
            expression[i] = logic
        elif '+' in expression:
            # or the stuff together
            # find the nearest '+' in the string
            # if str on side then call the sym class method to turn into labmda
            # otherwise just or if it it's already a lambda function
            loc = expression.index('+')
            if loc == 0 or loc == len(expression):
                raise Exception('Incorrect formatting, OR statements must take two expressions to evaluate')
            


        elif '.' in expression:
            pass
            # or the stuff together

        return expression[0]
    
    def find_parenth_pair(characters: list[object]) -> int:
        # maybe remake this into find pair type beat
        # then return tuple for start + stop
        paren_open = False
        count = 0
        for idx, chr in enumerate(characters):
            if chr == '(':
                paren_open = True
                count += 1
            elif chr == ')':
                count -= 1
            if count == 0 and paren_open:
                return characters.index('('), idx
        raise Exception('No closing bracket in the list of characters')

    def set_symbols(self, **kwargs):
        for key, value in kwargs.items():
            if key not in self.symbols:
                raise Exception(f'Uknown symbol {key}')
            if type(value) is not bool:
                raise Exception(f'Value of {key} must be a boolean type')
            self.symbols[key] = value

def main():
    a = Atom('O=A.B+C')


if __name__ == '__main__':
    main()

'''
should be able to pass in a string
split at every 'symbol' (except not)

'''
