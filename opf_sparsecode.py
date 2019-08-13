# usage: python3 opf_sparsecode.py [path/to/opf_directories.txt] [path/to/out/folder/] [month]

import sys
import os
import shutil

def correct_month(root, month):
    """
    root should be a filepath.
    month should be a number (from argv[3])
    Returns True if root pertains to month, False otherwise
    """
    split_root_begin = root.split("Home_Visit")[0][:-1]
    root_base = os.path.basename(split_root_begin)

    # if months and root_base[3:5] in months:
    if month and root_base[3:5]==month:
        return True
    elif not month:
        return True
    return False


if __name__ == "__main__":
    """
    For each of the 44 participants, a copy of their .opf video annotation
    file in Subject Files is gatherd into another working folder in Working Files
    """
    
    # checks correct command line usage
    if len(sys.argv) != 4:
        print('usage: python3 opf_sparsecode.py [path/to/opf_directories.txt] [path/to/out/folder/] [month]')
        exit(-1)

    # a .txt containing a list of paths to directories in which .opfs are stored
    # i.e. opf_directories.txt
    opf_directories = sys.argv[1]

    # path to the folder of where you want to copy the .opfs to
    # the folder needs to be created beforehand
    out_folder = sys.argv[2]

    # month that you would like to copy for
    # e.g. 13 if you are trying to do reliability checks for month 13
    month = sys.argv[3]

    # reads the .txt of paths into a list
    with open(opf_directories, 'r') as f:
        lines = f.readlines()

    # copying occurs here
    for line in lines:
        line = line.strip()
        # only copy for the indicated month
        # (e.g. if you are trying to do reliability checks for month 13,
        # then do not copy .opfs from other months)
        if correct_month(line, month):
            for opf in os.listdir(line):
                # only copy the .opfs
                if opf.endswith(".opf"):
                    shutil.copy(os.path.join(line, opf), os.path.join(out_folder, opf))
                    print("copied " + line)
