import re


class Atom:
    # where should I keep the list of symbols?
    #

    def __init__(self, proposition: str) -> None:
        self.symbols = dict()
        self.parse_symbols(proposition)

    def sym(self, symbol: str) -> function:
        '''
        returns a wrapper function to retrieve the value of the given symbol
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
            
    def parse_logic(self):
        return


def main():
    a = Atom('O=A.B+C')


if __name__ == '__main__':
    main()

'''
should be able to pass in a string
split at every 'symbol' (except not)

'''
