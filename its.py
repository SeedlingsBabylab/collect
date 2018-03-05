import sys
import os
import shutil

selected = ["_08", "_09", "_10"]
# selected = "all"


def crawl(start, out):
    for root, dirs, files in os.walk(start):
        if "Processing" in root and "Audio_Files" in root:
            for file in files:
                if file == "{}.its".format(file[:5]) and (selected == "all" or any(x in file for x in selected)):
                    print file
                    shutil.copy(os.path.join(root, file),
                                os.path.join(out, file))


if __name__ == "__main__":

    start = sys.argv[1]
    out = sys.argv[2]

    crawl(start, out)
