#!/usr/bin/python3
import os
import subprocess
import shutil
# Directory paths
zw8dir = "/home/viml/mg/zw8"
pffdir = os.path.join(zw8dir, "pff")
sfddir = os.path.join(pffdir, "sfd")
smallsfddir = os.path.join(sfddir, "small")
bigsfddir = os.path.join(sfddir, "big")
fontdir = os.path.join(zw8dir, "font")
thisdir = os.path.join(pffdir, "py")
# Font directories
bigttfdir = os.path.join(fontdir, "bigttf")
bigwoffdir = os.path.join(fontdir, "bigwoff")
smallttfdir = os.path.join(fontdir, "smallttf")
smallwoffdir = os.path.join(fontdir, "smallwoff")
hsciittfdir = os.path.join(fontdir, "hsciittf")
hsciiwoffdir = os.path.join(fontdir, "hsciiwoff")
# Create directories
for directory in [bigttfdir, bigwoffdir, smallttfdir, smallwoffdir, hsciittfdir, hsciiwoffdir]:
    os.makedirs(directory, exist_ok=True)

# Tree command equivalent (using subprocess)
# subprocess.run(["tree", fontdir], check=True)

################## Small font variations bilo
small15arr = ["15ms", "15s", "115s"]
for i in small15arr:
    currsmalldir = f"source{i}"
    print(f"generating ttf/woff2 fonts in {currsmalldir}")    
    # Change to the current small font directory
    os.chdir(os.path.join(smallsfddir, currsmalldir))    
    # Remove lookup lines from SFD files
    for sfd_file in [f for f in os.listdir('.') if f.endswith(f'{i}.sfd')]:
        with open(sfd_file, 'r') as f:
            lines = f.readlines()        
        lines = [line for line in lines if 'lookup' not in line]        
        with open(sfd_file, 'w') as f:
            f.writelines(lines)    
    # Run conversion script
    subprocess.run(["./convert.pe"] + [f for f in os.listdir('.') if f.endswith(f'{i}.sfd')], check=True)    
    # Create directories for current font variation
    os.makedirs(os.path.join(smallttfdir, i), exist_ok=True)
    os.makedirs(os.path.join(smallwoffdir, i), exist_ok=True)    
    # Move generated font files
    for ext in ['.ttf', '.woff2']:
        for font_file in [f for f in os.listdir('.') if f.endswith(f'{i}{ext}')]:
            if ext == '.ttf':
                shutil.move(font_file, os.path.join(smallttfdir, i, font_file))
            else:
                shutil.move(font_file, os.path.join(smallwoffdir, i, font_file))
################## Small font variations up

################## big font variations bilo
big15arr = ["15mb", "15b", "115b"]
for i in big15arr:
    currbigdir = f"source{i}"
    print(f"generating ttf/woff2 fonts in {currbigdir}")    
    # Change to the current big font directory
    os.chdir(os.path.join(bigsfddir, currbigdir))    
    # remove lookup lines from .sfd files
    for sfd_file in [f for f in os.listdir('.') if f.endswith(f'{i}.sfd')]:
        with open(sfd_file, 'r') as f:
            lines = f.readlines()        
        lines = [line for line in lines if 'lookup' not in line]        
        with open(sfd_file, 'w') as f:
            f.writelines(lines)    
    # run conversion script
    subprocess.run(["./convert.pe"] + [f for f in os.listdir('.') if f.endswith(f'{i}.sfd')], check=True)    
    # create directories for current font variation
    os.makedirs(os.path.join(bigttfdir, i), exist_ok=True)
    os.makedirs(os.path.join(bigwoffdir, i), exist_ok=True)    
    # move generated font files
    for ext in ['.ttf', '.woff2']:
        for font_file in [f for f in os.listdir('.') if f.endswith(f'{i}{ext}')]:
            if ext == '.ttf':
                shutil.move(font_file, os.path.join(bigttfdir, i, font_file))
            else:
                shutil.move(font_file, os.path.join(bigwoffdir, i, font_file))
################## big font variations up

# Return to original directory
os.chdir(fontdir)
subprocess.run(["./fonts_linux_install.py"], check=True)
# Tree command equivalent again
# subprocess.run(["tree", fontdir], check=True)
# font install.
os.chdir(thisdir)
