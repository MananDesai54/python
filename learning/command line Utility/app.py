import argparse;
import sys;
import os;
from datetime import datetime;

fp = open('tasks.txt','a');

def calc(args):
    result = 'You missplaced args or something went wrong';
    if args.op=='add':
        result =  args.num1 + args.num2;
    elif args.op=='sub':
        result = args.num1 - args.num2;
    elif args.op=='mul':
        result = args.num1 * args.num2;
    elif args.op=='div':
        result = args.num1 / args.num2;
    fp.write(f'{datetime.now()} : Task of {args.op} for {args.num1} and {args.num2} is {result}\n');
    return result;

if __name__ == "__main__":
    parser = argparse.ArgumentParser();

    parser.add_argument('--num1',type=float,default=1.0,help='For more stay tuned');

    parser.add_argument('--num2',type=float,default=1.0,help='For more stay tuned');

    parser.add_argument('--op',type=str,default='add',help='For more stay tuned');

    args = parser.parse_args();

    sys.stdout.write(str(calc(args)));