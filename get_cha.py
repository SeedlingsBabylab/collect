import os
import shutil

# unless you do the "if __name__ == __main__" thing from that other script,
# execution starts from the top of the script and goes to the bottom


# this is an absolute path to
start_dir = "/Volumes/pn-opus/Seedlings/Subject_Files"
# this is a relative path (i.e. relative to wherever you launch the script)
# out_dir = "/Volumes/pn-opus/Seedlings/Code/seedlings/annot_id/data/audio"
out_dir = "all_cha"
# arguments to specify a subset of files to collect
subj = ""
month = ""


# now we define a couple functions and variables:

# we want to know to ignore these folders
ignorable_folders = ["old_files", "old_chas", "Old Files", "Old_Files"]


# define a function called "walk_sf" which takes 1 argument (sf_dir)
# you can then call this function like this: walk_sf("/path/to/somewhere")
def walk_sf(sf_dir):

    # this for loop is kind of weird, but basically, os.walk() is
    # an iterator that on each iteration returns a new position on
    # the directory tree you're walking (it updates root, dirs, and
    # files variables on each iteration). "root" is a string that's
    # the current folder you're in (updated on each iteration),
    # "dirs" is a list (see https://developers.google.com/edu/python/lists)
    # of directories within the current root folder, and "files" is
    # a list of files in that same root folder
    for root, dirs, files in os.walk(sf_dir):
        # if "Audio_Annotation" is in the root, we know that we are at least
        # deep enough in the directory tree to be where the final.cha file is
        # though we could also be deeper (some subfolder inside Audio_Annotation).
        # The any() check just says, make sure nothing that's in ignorable_folders
        # is a substring in root (i.e. we've traveresed too far in Audio_Annotation and we're
        # in a subfolder called x)
        if "Audio_Annotation" in root and not any(x in root for x in ignorable_folders):
            for file in files:
                # we only care about the .cha files in Audio_Annotation
                if file.endswith(".cha"):
                    correct_file = check_if_right_subj_month(file)
                    if correct_file:
                        # copy, from source (first argument) to destination (second argument)
                        # the os.path.join is because we need to pass in absolute paths, and not
                        # just the filename
                        shutil.copy(os.path.join(root, file),
                                    os.path.join(out_dir, file))

                        # print the name of the file just copied to terminal
                        # notice the format() function is being called on the
                        # string itself. it's a super useful function. more
                        # info here: https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3
                        print "copied:  {}".format(file)


def check_if_right_subj_month(filename):
    # if subj and month are empty strings (i.e. we didn't set them at them
    # at the top of the script) we're going to say true for any file that's
    # passed in.
    if subj == "" and month == "":
        return True
    # filename[3:5] is the part of the file name with the month
    elif subj == "" and filename[3:5] == month:
        return True
    # filename[0:2] is the subject number. you can also write this as filename[:2],
    # omitting the 0
    elif subj == filename[0:2] and month == "":
        return True
    # both variables specified, and both match
    elif subj == filename[0:2] and filename[3:5] == month:
        return True
    # otherwise return False
    return False



# here we actually call the function defined above. execution goes from top to bottom,
# so this function call is the last thing executed
walk_sf(start_dir)
