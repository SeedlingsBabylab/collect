import sys
import os
import shutil

selected = ["_06"]

def crawl(start, out):
    for root, dirs, files in os.walk(start):
        print root
        if "Processing" in root and "Audio_Files" in root:
            for file in files:
                if file.endswith("lena.cha") and any(x in file for x in selected):
                    shutil.copy(os.path.join(root, file),
                                os.path.join(out, file))

if __name__ == "__main__":

    start = sys.argv[1]
    out = sys.argv[2]

    crawl(start, out)
