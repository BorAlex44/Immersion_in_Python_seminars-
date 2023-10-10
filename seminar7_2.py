import os
import shutil
from pathlib import Path


def sort_files(path: str = None):
    file_types = {'video': ('mp4', 'mov', 'avi', 'wmv'),
                  'image': ('jpeg', 'png', 'gif', 'tiff', 'jpg', 'bmp'),
                  'text': ('txt', 'doc', 'md', 'rtf', 'pdf'), }
    work_path = Path.cwd() if path is None else Path(path)
    os.chdir(work_path)
    for key in file_types.keys():
        if not os.path.exists(key):
            os.mkdir(key)
    for file in os.listdir(os.getcwd()):
        if os.path.isfile(file):
            for key, value in file_types.items():
                if file.split('.')[-1] in value:
                    shutil.move(os.path.join(os.getcwd(), file), os.path.join(os.getcwd(), key))


if __name__ == '__main__':
    sort_files('file_from_sort')