import os
import shutil
import zipfile

desktop_dir = os.path.expanduser("~/Desktop")

# Create a dictionary of file types and their corresponding folders
file_types = {
    "App": [".exe", ".EXE", ".lnx", ".url", ".cda"],
    "Image": [".jpg", ".jpeg", ".png", ".gif", ".tiff", ".bmp", ".eps"],
    "Code": [".ipynb",".py", ".js", ".html", ".css", ".php", ".cpp", ".h", ".java", ".ms14", ".m"],
    "Document": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".ogg", ".aup3"],
    "Video": [".mp4", ".avi", ".mov", ".flv", ".wmv", ".mpeg"],
    "Photoshop": [".psd"],
    "Zipped Folders": [".zip"],
}

# Create the folders for each file type
for folder_name in file_types.keys():
    folder_path = os.path.join(desktop_dir, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Iterate over the files in the Downloads folder
for filename in os.listdir(desktop_dir):
    filepath = os.path.join(desktop_dir, filename)

    # Move the file to the appropriate folder based on its extension
    for folder_name, extensions in file_types.items():
        if any(filename.endswith(ext) for ext in extensions):
            dest_folder = os.path.join(desktop_dir, folder_name)
            shutil.move(filepath, os.path.join(dest_folder, filename))
            print(f"Moved {filename} to {dest_folder}")
            break