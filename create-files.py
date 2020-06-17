#!/usr/bin/python3

import os

filenames = ['file1.html', 'file2.css', 'file3.js', 'file4.sass']

for filename in filenames:
    print(os.path.join(os.getcwd(), filename))
