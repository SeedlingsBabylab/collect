import os, sys
from shutil import copy
import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Collect basic level files from list of input directories (files containing input directories: a path file) to output directory. You may supply as many input files containing basic level directories as you wish.')
    parser.add_argument('dirfile', help='A file (or files) that contains basic level directories, one per line', nargs='+')
    parser.add_argument('outdir', help='The output directory to copy all the basic level files to.')
    return parser.parse_args()


def copy_files(media_list, output_dir):
    for d in media_list:
        d = d.strip()
        for f in os.listdir(d):
            if f.endswith("sparse_code.csv"):
                copy(os.path.join(d, f), output_dir)
                break
        else:
            sys.stderr.write('No file copied from dir {}\n'.format(d))


if __name__ == "__main__":
    args = get_args()

    for inf in args.dirfile:
        with open(inf, 'r') as f:
            bl_list = f.readlines()
            copy_files(bl_list, args.outdir)
