import os
import re
import sys
from datetime import datetime


def write_gallery(images):
    s = "gallery:\n"
    for i in images:
        name = os.path.basename(i).split(".")[0]
        s += f"  - url: {i}\n"
        s += f"    image_path: {i}\n"
        s += f"    alt: {name}\n"
        s += f"    title: {name}\n"
    return s


def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]


if len(sys.argv) != 4:
    print("Args: {image dir} {md filename} {url}")

img_dir = sys.argv[1]
filename = f"../../_pages/{sys.argv[2]}.md"
url = sys.argv[3]



images = os.listdir(f"../img/{img_dir}")
images.sort(key=natural_keys)
print(images)
images = [f"/assets/img/{img_dir}/{i}" for i in images]
gallery = write_gallery(images)
date = datetime.now().strftime("%Y-%m-%d")

# Write page
with open(filename, "w") as f:
    f.write(f"---\nlayout: splash\npermalink: /gallery/{url}\n")
    f.write("title:  Molecule Gallery\ndescription: Nanotube intersections molecule gallery\n")
    f.write(f"author:\n  twitter: geoffclark4\ndate:   {date}\n{gallery}\n---\n")
    f.write("\n{% include feature_row id='gallery' %}\n")
