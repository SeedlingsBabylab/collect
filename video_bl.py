import sys
import os
import shutil

ignore = ["old_chas", "old_files", "Old Files", "Old files", "Old_Files"]

months = ["13"]

def correct_month(root):
    split_root_begin = root.split("Home_Visit")[0][:-1]
    root_base = os.path.basename(split_root_begin)
    if root_base[3:5] in months:
        return True
    return False

def crawl(start, out):
    for root, dirs, files in os.walk(start):
        if correct_month(root):
            if "Analysis" in root and "Video_Analysis" in root and not any(x in root for x in ignore):
                for file in files:
                    if file.endswith("sparse_code.csv"):
                        print file
                        shutil.copy(os.path.join(root, file),
                                    os.path.join(out, file))

if __name__ == "__main__":

    start = sys.argv[1] #path/to/Subject_Files
    out = sys.argv[2] #path/to/processed_and_old

    crawl(start, out)
