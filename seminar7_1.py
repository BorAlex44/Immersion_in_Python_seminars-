import os
from pathlib import Path


def renaming_files(
                   source_file_extension: str,
                   end_file_extension: str,
                   digits_serial_num: int = 3,
                   len_original_name: list[int] = [1, 2],
                   new_file_name: str = None,
                   path: str = None
                   ):
    count = 0
    work_path = Path.cwd() if path is None else Path(path)
    for file in os.listdir(work_path):
        if file.endswith(source_file_extension):
            if new_file_name is None:
                new_file_name = ''
            count += 1
            Path(work_path, file).rename(Path(work_path,
                                              f"{file.split('.')[0][len_original_name[0]-1:len_original_name[1]]}_"
                                              f"{new_file_name}_{count:0{digits_serial_num}}.{end_file_extension}"))


if __name__ == '__main__':
    renaming_files(source_file_extension='txt',
                   end_file_extension='xls',
                   new_file_name='rename',
                   path='files_from_rename')
