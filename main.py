
from seminar7_1 import renaming_files
from seminar7_2 import sort_files

if __name__ == '__main__':
    renaming_files(source_file_extension='txt',
                   end_file_extension='doc',
                   new_file_name='new_name',
                   path='files_from_rename')

    sort_files('file_from_sort')
