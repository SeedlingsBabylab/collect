import os, sys
from shutil import copy

def copy_files(media_list, output_directory):
    for dir in media_list:
        dir = dir.strip()
        for file in os.listdir(dir):
            if file.endswith("sparse_code.csv"):
                copy(os.path.join(dir, file), output_dir)

if __name__ == "__main__":
    audio_list_file = sys.argv[1]
    video_list_file = sys.argv[2]
    output_dir = sys.argv[3]

    with open(audio_list_file, 'r') as f:
        audio_list = f.readlines()
        copy_files(audio_list, output_dir)
    with open(video_list_file, 'r') as g:
        video_list = g.readlines()
        copy_files(video_list, output_dir)
