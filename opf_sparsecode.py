import sys
import os
import shutil

ignore = ["old_files", "Old Files", "Old files", "Old_Files", "old_opfs"]
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


def crawl(start, out):
    for root, dirs, files in os.walk(start):
        if correct_month(root):
            if "Coding" in root and "Video_Annotation" in root and not any(x in root for x in ignore):
                for file in files:
                    if file.endswith("sparse_code.opf"):
                        print file
                        shutil.copy(os.path.join(root, file),
                                    os.path.join(out, file))


if __name__ == "__main__":

    # start = sys.argv[1]
    # out = sys.argv[2]
    #
    # crawl(start, out)

    opf_paths = sys.argv[1]
    out = sys.argv[2]
    month = False
    if len(sys.argv)>3:
        month = sys.argv[3]

    with open(opf_paths, 'r') as f:
        lines = f.readlines()

    for line in lines:
        print(line)
        line = line.strip()
        if correct_month(line, month):
            for opf in os.listdir(line):
                if opf.endswith(".opf"):
                    shutil.copy(os.path.join(line, opf), os.path.join(out, opf))
