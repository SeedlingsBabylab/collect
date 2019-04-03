# -*- coding: utf-8 -*-

import sys
import os
import shutil

# ignore = ["old_files", "Old Files", "Old files", "Old_Files", "old_opfs"]
#
# months = []


def correct_month(root, month):
    split_root_begin = root.split("Home_Visit")[0][:-1]
    root_base = os.path.basename(split_root_begin)

    # if months and root_base[3:5] in months:
    if month and root_base[3:5]==month:
        return True
    elif not month:
        return True
    return False

def checkandcopy(root, file, out, extension):
    if file.endswith(extension):
        shutil.copy(os.path.join(root, file),
                    os.path.join(out, file))

def crawl(start, out, month, extension):
    for root, dirs, files in os.walk(start):
        if correct_month(root, month): ###add error
            for file in files:
                checkandcopy(root, file, out, extension)


if __name__ == "__main__":

    # start = sys.argv[1]
    # out = sys.argv[2]
    #
    # crawl(start, out)

    opf_paths = sys.argv[1]
    out = sys.argv[2]
    month = False
    extension = False
    if len(sys.argv)>3:
        month = sys.argv[3]
        if len(sys.argv) > 4:
            extension = "."+sys.argv[4]

    with open(opf_paths, 'r') as f:
        lines = f.readlines()

    if '.' not in os.path.basename(lines[0]):
        if not extension:
            extension = ".opf"
        for each in lines:
            each = each.strip()
            crawl(each, out, month, extension)
    else:
        if not extension:
            extension = '.'+os.path.basename(lines[0]).split('.')[-1]
        for each in lines:
            each = each.strip()
            if correct_month(each, month):
                checkandcopy(os.path.dirname(each), os.path.basename(each), out, extension)
