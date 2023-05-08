import argparse # https://docs.python.org/3/library/argparse.html

parser = argparse.ArgumentParser()

## add argument definitions
parser.add_argument('numbers', nargs='*')
parser.add_argument('-i','--integer', 
                    help="number to enter", 
                    required=False,
                    nargs=1)

parser.add_argument('-p','--patent', 
                    help="number to enter", 
                    required=False,
                    nargs=1)

parser.add_argument('-m','--mephobic', 
                    help="number to enter", 
                    required=False,
                    action='store_true')

parser.add_argument('-y','--youphobic', 
                    help="number to enter", 
                    required=False,
                    action='store_true')


# parse args and act on them
args = parser.parse_args()

if len(args.numbers) > 0:
    print('numbers: ', args.numbers)
else:
    print('nu numbers were entered')

if args.integer:
    print(f'integer: {args.integer}')

if args.patent:
    print(f'patent: {args.patent}')

if args.mephobic:
    print('m was entered')

if args.youphobic:
    print('y was entered')


