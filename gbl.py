import os
import sys
from shutil import copy


start_dir = ""
output_dir = ""

subject= ""
month = ""

def walk_tree():
    for root, dirs, files in os.walk(start_dir):
        if os.path.split(root)[1] == "Audio_Analysis":
            for file in files:
                if month:
                    print "file[3:5] = {}".format(file[3:5])
                    print "file = {}".format(file)
                    if correct_audio_bl_name(file) and int(file[3:5]) == int(month):
                        copy(os.path.join(root, file), output_dir)
                else:
                    if correct_audio_bl_name(file):
                        print os.path.join(root, file)
                        copy(os.path.join(root, file), output_dir)
        if os.path.split(root)[1] == "Video_Analysis":
            for file in files:
                if month:
                    print "file[3:5] = {}".format(file[3:5])
                    print "file = {}".format(file)
                    if correct_video_bl_name(file) and int(file[3:5]) == int(month):
                        copy(os.path.join(root, file), output_dir)
                else:
                    if correct_video_bl_name(file):
                        print os.path.join(root, file)
                        copy(os.path.join(root, file), output_dir)


def correct_audio_bl_name(name):
    if name.endswith(".csv") and ("audio_sparse_code" in name):
            return True
    return False


def correct_video_bl_name(name):
    if name.endswith(".csv") and ("video_sparse_code" in name):
            return True
    return False


if __name__ == "__main__":

    start_dir = sys.argv[1]
    output_dir = sys.argv[2]

    subject = sys.argv[3]
    month = sys.argv[4]

    if subject == "--all":
        subject = ""
    if month == "--all":
        month = ""


    walk_tree()
