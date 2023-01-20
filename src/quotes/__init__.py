import importlib.resources, random


def quote():
    quotes = importlib.resources.files('quotes').joinpath('quotes.txt').read_text().strip().split("\n")
    return random.choice(quotes)


def main():
    print(quote())


if __name__ == '__main__': main()
