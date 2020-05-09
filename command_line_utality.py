#open terminal and write python filename.py --x value --y value --o operation then enter
#example python command_line_utality.py --x 7 --y 6 --o add
#python command_line_utality.py --x 7 --y 6 --o sub
#python command_line_utality.py --x 7 --y 6 --o mul
#python command_line_utality.py --x 7 --y 6 --o div
#you can also use system cmd and use the path of tha project and write above command

#----------------------------------------calculator--------------------------------------------
import argparse #it is a module which help us to make command line utality
import sys
def calc(args):
    if args.o == 'add':
        return args.x + args.y

    elif args.o == 'mul':
        return args.x * args.y

    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'div':
        return args.x / args.y

    else:
        return "Something went wrong"

if __name__ == '__main__':
    parser = argparse.ArgumentParser() #argumentparser is a class
    parser.add_argument('--x', type=float, default=1.0,
                        help="Enter first number. This is a utility for calculation")

    parser.add_argument('--y', type=float, default=3.0,
                        help="Enter second number. This is a utility for calculation")

    parser.add_argument('--o', type=str, default="add",
                        help="This is a utility for calculation.")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))   #sys.stdout gives the standard output to console and,
    # write write the str version of calc(args),calc(args) is a function
