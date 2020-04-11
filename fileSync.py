#! /user/bin/env python3

from dirsync import sync
import argparse


source = './../source'
dest = './../dest'

def main():
    parser = argparse.ArgumentParser(add_help=True, description='Sync to file directories')
    parser.add_argument('--sync', nargs=2,help='--sync source dest')

    args = parser.parse_args()
    
    if args.sync:
        source = args.sync[0]
        dest = args.sync[1]

        sync(source, dest, 'sync')
    else:
        print("Needs source directory and destination directory")

if __name__ == '__main__':
    main()