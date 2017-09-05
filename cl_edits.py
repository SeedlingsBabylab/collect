import sys
import os
import shutil

months = ["10", "11"]


def correct_folder(root):
    split_root_begin = root.split("Home_Visit")[0][:-1]

    root_base = os.path.basename(split_root_begin)

    if root_base[3:5] in months:
        if "Video_Annotation" in root and\
            "old_opfs" in root:
            return True
    return False

def walk(start):

    for root, dirs, files in os.walk(start):
        if correct_folder(root):
            for file in files:
                if "CLedit" in file:
                    shutil.copy(os.path.join(root, file),
                                os.path.join(output, file))
                    print file

if __name__ == "__main__":

    start_dir = sys.argv[1]
    output = sys.argv[2]

    walk(start_dir)
