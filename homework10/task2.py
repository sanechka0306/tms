import os


def print_docs(directory):
    files = os.walk(directory)
    for case in files:
        print(f'Путь {case[0]} :')
        print(f'Папки: {", ".join([folder for folder in case[1]])}')
        print(f'Файлы: {", ".join([file for file in case[2]])}\n')



print_docs('C:/Users/tms/PycharmProjects')
