import shutil


def remove_folder(folder_path):
    try:
        shutil.rmtree('results/')
    except Exception as e:
        print('Failed to delete %s. ' % folder_path)