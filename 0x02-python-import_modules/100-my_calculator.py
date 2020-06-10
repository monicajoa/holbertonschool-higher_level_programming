#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as av
    from sys import exit
    import calculator_1

    if len(av) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif av[2] != "+" and av[2] != "-" and av[2] != "*" and av[2] != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        op = av[2]
        num_1 = int(av[1])
        num_2 = int(av[3])
        if op == "+":
            result = calculator_1.add(num_1, num_2)
            print("{} + {} = {}".format(num_1, num_2, result))

        elif op == "-":
            result = calculator_1.sub(num_1, num_2)
            print("{} - {} = {}".format(num_1, num_2, result))

        elif op == "*":
            result = calculator_1.mul(num_1, num_2)
            print("{} * {} = {}".format(num_1, num_2, result))

        elif op == "/":
            result = calculator_1.div(num_1, num_2)
            print("{} / {} = {}".format(num_1, num_2, result))
