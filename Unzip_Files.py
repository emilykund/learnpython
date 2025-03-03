#!/usr/bin/env python
# coding: utf-8

# In[2]:


#load packages to unzip files
import zipfile
import os


# In[3]:


#command to extract zipped files. Note: this command works compared to other ones I tried which were returning a 'no file' error.

with zipfile.ZipFile("/users/public/college_data.zip", 'r') as zip_ref:
    zip_ref.extractall("/users/public/college data")


# In[ ]:


#checking to see if it executed correctly
import os
file_path = "/users/public/college data"

if os.path.exists(file_path):
    print("Path exists")
    if os.path.isfile(file_path):
        print("It is a file")
    elif os.path.isdir(file_path):
        print("It is a directory")
else:
    print("Path does not exist")


# In[ ]:




