import os, fnmatch, re

#### CONFIG

source_directory = "test_case"
to_replace = r"(https://www.ib.redditor.website/)(.*)(\")"
file_type = "*.html"               # "*.ext"

# WARNING: THIS SCRIPT IS DESTRUCTIVE. BACKUP YOUR DIRECTORY FIRST.
# Run this script in the same directory as the top-level-directory
#   you want to recursively replace in.

#### END CONFIG

def find_replace(directory, find, file_pattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, file_pattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            m = re.finditer(find, s, flags=re.IGNORECASE)
            if m is not None:
                for case in m:
                    #print(case.group(0))
                    #print(case.group(1))
                    #print(case.group(2))
                    #print(case.group(3))
                    s = s.replace(case.group(1) + case.group(2), case.group(1) + case.group(2) + "/", 1)
                    s = s.replace(case.group(1), "", 1)
            with open(filepath, "w") as f:
                f.write(s)


find_replace(source_directory, to_replace, file_type)
