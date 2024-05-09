import argparse

def cli_command():
    parser = argparse.ArgumentParser(description="A simple CLI using argparse.")
    parser.add_argument('--name', type=str, required=True, help='Your name')
    parser.add_argument('--age', type=int, help='Your age')

    args = parser.parse_args()

    print(f"Hello, {args.name}!")
    if args.age:
        print(f"You are {args.age} years old.")

if __name__ == "__main__":
    cli_command()