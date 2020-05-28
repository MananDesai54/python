import argparse;
import sys;
import webbrowser as wb;

url = 'https://www.google.com/search?q=';

def getData(args):
    wb.open(f'{url}{args.google}');
    return 'Loading...';

if __name__ == "__main__":
    parser = argparse.ArgumentParser();

    parser.add_argument('--google',type=str,default='nodejs',help="Check your connection we can't be wrong");

    args = parser.parse_args();

    sys.stdout.write(str(getData(args)));