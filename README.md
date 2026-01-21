# Numpy-Project
File Organizer with NumPy &amp; Python  This project demonstrates a Python-based file organization system using os, shutil, csv, and NumPy for basic image analysis. It is designed to help automate the process of sorting files in a folder and summarizing their properties.

Project Overview

The project works on a folder named files containing documents, audio files, and images. The goal is to:

Organize files by type into subfolders (docs, audio, images).

Print and save file information (name, type, size) into a recap.csv file.

Update existing folders and CSV without overwriting previous data.

Provide a command-line interface (CLI) to move a single file into its corresponding folder and update the recap.

Analyze images with NumPy and PIL, identifying whether they are grayscale, RGB, or RGBA.

Folder Structure

Before organizing:
files/
├─ 2 text files
├─ 2 audio files
├─ 4 images

After running the scripts:
files/
├─ audio/
│  ├─ song1.mp3
│  └─ song2.mp3
├─ docs/
│  ├─ ciao.txt
│  └─ pippo.odt
├─ images/
│  ├─ bw.png
│  ├─ daffodil.jpg
│  ├─ eclipse.png
│  └─ trump.jpeg

How to Use

Clone the repository.

Add your files to the files folder.

Run the Jupyter Notebook for Step 1 and Step 3.

Use addfile.py to move individual files via CLI.
├─ recap.csv
