import argparse
from utils import add, subtract, multiply, divide

def main():
    parser = argparse.ArgumentParser(description="Simple CLI Calculator")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"])
    parser.add_argument("a", type=float)
    parser.add_argument("b", type=float)
    args = parser.parse_args()

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }

    result = operations[args.operation](args.a, args.b)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()