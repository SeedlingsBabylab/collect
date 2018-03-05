import sys
import os
import shutil

selected = ["_11", "_12", "_13", "_14", "_15", "_16", "_17"]
# selected = "all"


def crawl(start, out):
    for root, dirs, files in os.walk(start):
        # print root
        if "Processing" in root and "Audio_Files" in root:
            for file in files:
                if file.endswith("lena.cha") and (selected == "all" or any(x in file for x in selected)):
                    print file
                    shutil.copy(os.path.join(root, file),
                                os.path.join(out, file))


if __name__ == "__main__":

    start = sys.argv[1]
    out = sys.argv[2]

    crawl(start, out)
