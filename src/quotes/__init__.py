import importlib.resources, random, sys


class Quotes:
    def __init__(self, filename = None):
        if filename != None:
            file = open(filename, 'r')

            self.quotes = []
            for line in file.readlines(): self.quotes.append(line.strip())

            file.close()

        else: self.quotes = importlib.resources.files('quotes').joinpath('quotes.txt').read_text().strip().split("\n")


    def quote(self):
        return random.choice(self.quotes)


def quote():
    q = Quotes()
    return q.quote()


def main():
    if len(sys.argv) > 1: q = Quotes(sys.argv[1])
    else: q = Quotes()

    print(q.quote())


if __name__ == '__main__': main()
