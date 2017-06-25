import argparse
import sys
from . import to_lipsum, from_lipsum

import bz2
import textwrap
import os

def main():

    parser = argparse.ArgumentParser(prog='lipsum', description='Lipsum encode or decode FILE')

    parser.add_argument('file', nargs='?', help="File(s) to encode or decode", type=argparse.FileType('rb'), default='-')

    parser.add_argument('-d', '--decode',help='Decode lipsum string', action='store_true')
    parser.add_argument('-c', '--compressed', help='Compress/Decompress data (uses bz2)', action='store_true')
    parser.add_argument('-w', '--wrap', help="Wrap output lines at the given width (ignored when decoding)", type=int)

    try:
        a = parser.parse_args()

        bytes = a.file.read()

        if type(bytes) == str:
            bytes = bytes.encode()

        if a.decode:
            fr = from_lipsum(bytes.decode('utf-8'))
            sys.stdout.write(bz2.decompress(fr) if a.compressed else fr)
        else:
            lip = to_lipsum(bz2.compress(bytes, 9) if a.compressed else bytes)
            if a.wrap: lip = os.linesep.join(textwrap.wrap(lip, a.wrap))
            print(lip)


    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()