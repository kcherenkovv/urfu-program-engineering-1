import shutil
import os


def remove_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
    except Exception as e:
        print('Failed to delete %s. ' % folder_path)


