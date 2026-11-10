import argparse


# Create a function called sayHello() that will display hello along with a
# string parameter name.
def sayHello(name: str) -> None:
    print('Hello', name)


def sayGoodbye(name: str) -> None:
    print('Goodbye', name)


def greetUser(name: str) -> str:
    message = f'Hello {name}!'
    print(message)
    return message


def main() -> None:
    parser = argparse.ArgumentParser(description='Print personalized greetings.')
    parser.add_argument(
        'names',
        nargs='*',
        metavar='NAME',
        help='name to greet (provide multiple names for multiple greetings)',
    )
    args = parser.parse_args()

    if args.names:
        for name in args.names:
            greetUser(name)
        return

    sayHello('Samantha')
    sayGoodbye('Alan')
    greetUser('Class')


if __name__ == '__main__':
    main()