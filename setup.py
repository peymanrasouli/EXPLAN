import os
import requests
import zipfile
import shutil

# Downloading YaDT C4.5 decision tree library
url = 'http://pages.di.unipi.it/ruggieri/YaDT/YaDT2.2.0.zip'
r = requests.get(url, allow_redirects=True)
open('YaDT2.2.0.zip', 'wb').write(r.content)

# Extracting required files from YaDT library
with zipfile.ZipFile('YaDT2.2.0.zip', 'r') as zip_ref:
    zip_ref.extractall('./')
os.remove('YaDT2.2.0.zip')

# Making YaDT files executable
os.system("chmod 777 ./yadt/dTcmd")
os.system("chmod 777 ./yadt/libtbb.so.2")

# Moving YaDT files to the root folder
shutil.copyfile('./yadt/dTcmd', './dTcmd')
shutil.copyfile('./yadt/libtbb.so.2', './libtbb.so.2')

# Removing .pyc files
os.system("find . -name '*.pyc' -exec rm -f {} \;")

# Creating a directory for the results
os.makedirs("experiments")

print("Setup is complete!")
