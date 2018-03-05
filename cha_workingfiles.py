import os
import sys
from shutil import copy

months = ["09"]


def correct_file(file):
    if any("_{}".format(x) in file for x in months) and\
        file.endswith(".cha") and not file.endswith("lena.cha"):
        return True
    return False


def walk(dir):
    for root, dirs, files in os.walk(dir):
        if any("_{}".format(x) in root for x in months):
            for file in files:
                if correct_file(file):
                    print os.path.join(root, file)
                    copy(os.path.join(root, file),
                         os.path.join(out_dir, file))


if __name__ == "__main__":
    wf_dir = sys.argv[1]
    out_dir = sys.argv[2]

    walk(wf_dir)
