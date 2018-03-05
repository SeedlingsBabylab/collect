import sys
import os
import shutil

ignore = ["old_chas", "old_files", "Old Files", "Old files", "Old_Files"]

months = ["17"]

def correct_month(root):
    split_root_begin = root.split("Home_Visit")[0][:-1]
    root_base = os.path.basename(split_root_begin)
    if root_base[3:5] in months:
        return True
    return False

def get_prefix(root):
    split_root_begin = root.split("Home_Visit")[0][:-1]
    root_base = os.path.basename(split_root_begin)
    return root_base[:5]

def crawl(start, out):
    for root, dirs, files in os.walk(start):
        if correct_month(root):
            if "Analysis" in root and "Audio_Analysis" in root and not any(x in root for x in ignore):
                for file in files:
                    if file.endswith("sparse_code.csv"):
                        print file
                        shutil.copy(os.path.join(root, file),
                                    os.path.join(out, file))

def crawl_exact(start, out, exact):
    prefixes = get_file_prefixes(exact)
    print "\nPulling these files: \n\n{}\n\n".format(prefixes)
    print "Total file count: {}\n\n".format(len(prefixes))
    for root, dirs, files in os.walk(start):
        if "Analysis" in root and\
         "Audio_Analysis" in root and\
          not any(x in root for x in ignore) and\
          get_prefix(root) in prefixes:
          for file in files:
                    if file.endswith("sparse_code.csv"):
                        print file
                        shutil.copy(os.path.join(root, file),
                                    os.path.join(out, file))


def get_file_prefixes(dir):
    return [x[:5] for x in os.listdir(dir)]

if __name__ == "__main__":

    start = sys.argv[1]
    out = sys.argv[2]

    if len(sys.argv) == 4:
        exact_f_dir = sys.argv[3]
    else:
        exact_f_dir = None
    
    if exact_f_dir:
        crawl_exact(start, out, exact_f_dir)
    else:
        crawl(start, out)
