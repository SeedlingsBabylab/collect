import os
import sys
import subprocess as sp


def walk(start_dir):

    for root, dirs, files in os.walk(start_dir):
        if "Audio_Files" in root:
            for file in files:
                if file.endswith("_{}.wav".format(month)):
                    sp.call(["cp", os.path.join(root, file), os.path.join(out_dir, file)])
                    # shutil.copy(os.path.join(root, file),
                    #             os.path.join(out_dir, file))


if __name__ == "__main__":

    start_dir = sys.argv[1]
    out_dir = sys.argv[2]

    month = sys.argv[3]

    walk(start_dir)
