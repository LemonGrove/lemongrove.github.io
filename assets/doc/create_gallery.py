"""
python create_gallery.py {image dir} {md filename} {url}
Ex: python create_gallery.py molecules3 molecules3 molecules3
"""
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
    return [
    (c) for c in re.split(r'(\d+)', text) ]


# if len(sys.argv) != 4:
#     print("Args: {image dir} {md filename} {url}")

img_dir = input("Name of the image directory (/assets/img/{name}): ")
filename =  input(f"Markdown file name ({img_dir}): ") or img_dir
url = input(f"URL ({filename}): ") or filename
filename = f"../../_pages/{filename}.md"
images = os.listdir(f"../img/{img_dir}")
print(f"{len(images)} images found in {img_dir}\nMD: {filename} URL: {url}")
rename = input("Rename files? ([y] / n): ") or "y"
if rename == "y":
    for i in images:
        old_file = os.path.join(f"../img/{img_dir}", i)
        # Change file name
        d = i.split()[2]
        t = i.split()[4]
        new_file = os.path.join(f"../img/{img_dir}", f"{d}_{t}.png")
        os.rename(old_file, new_file)
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
