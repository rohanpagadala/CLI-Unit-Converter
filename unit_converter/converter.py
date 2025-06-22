import argparse

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--temp", type=float, required=True)
    parser.add_argument("--unit", type=str, choices=['c', 'f'], required=True)
    args = parser.parse_args()

    if args.unit == 'c':
        print(args.temp, "°C is", celsius_to_fahrenheit(args.temp), "°F")
    else:
        print(args.temp, "°F is", fahrenheit_to_celsius(args.temp), "°C")

main()
