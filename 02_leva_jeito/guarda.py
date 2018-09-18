import ast
import hashlib
import os
import sys

dir_base = ".report/"
report_base = "report.json"
diff_base = "diff.json"
dir_track = '.'


def create_dir(dir_local='./'):
    global dir_base
    dir_local += dir_base
    if not os.path.isdir(os.path.abspath(dir_local)):
        os.mkdir(os.path.abspath(dir_local))
    dir_base = dir_local


def delete_dir(dir_local='./'):
    global dir_base
    dir_local += dir_base
    if os.path.isdir(os.path.abspath(dir_local)):

        for raiz, diretorios, arquivos in os.walk(os.path.abspath(dir_local)):
            for arquivo in arquivos:
                os.remove(os.path.join(raiz, arquivo))

        os.removedirs(os.path.abspath(dir_local))


def filehash(filepath, blocksize=4096):
    sha = hashlib.sha256()
    with open(filepath, 'rb') as fp:
        while 1:
            data = fp.read(blocksize)
            if data:
                sha.update(data)
            else:
                break
    return sha.hexdigest()


def save_report(dict_file):
    global dir_track
    global dir_base
    archive = dir_base + report_base
    dict_file = dir_track + '\n' + str(dict_file)
    with open(os.path.abspath(archive), 'w') as report:
        report.write(dict_file)
    report.close()


def load_report(path_name):
    global dir_track
    global dir_base
    archive = path_name + dir_base + report_base
    report = open(os.path.abspath(archive))
    rows = report.read().split('\n')

    dir_track = str(rows[0])
    dict_file = ast.literal_eval(str(rows[1]))

    return dict_file


def scanner_dir(path_name):
    dict_file = {}

    for p, _, files in os.walk(os.path.abspath(path_name)):
        if '.report' in p: del p; continue
        for file in files:
            file_open = os.path.join(p, file)
            dict_file[file_open] = filehash(file_open)
    return dict_file


def dict_report(path_name):
    save_report(scanner_dir(path_name))


def dict_diff(path_name, output_file):
    dict_file = scanner_dir(path_name)
    report = load_report(pasta)

    return calculate_dict_diff(report, dict_file, output_file)


def calculate_dict_diff(dict_base, dict_file, output_file=None):
    data = dict()
    data['created'] = list(set(dict_file) - set(dict_base))
    data['deleted'] = list(set(dict_base) - set(dict_file))
    data['updated'] = []

    for f in set(dict_file).intersection(set(dict_base)):
        if dict_base[f] != dict_file[f]:
            data['updated'].append(f)

    archive = dir_base + diff_base
    if output_file is not None:
        archive = dir_base + output_file

    with open(os.path.abspath(archive), 'w') as diff:
        diff.write(str(data))
        diff.close()

    if output_file is None:
        print(data)


if __name__ == '__main__':

    metodo = sys.argv[1]
    opcao = sys.argv[2]
    pasta = None
    saida = None
    try:
        pasta = sys.argv[3]
        saida = sys.argv[4]
    except:
        pass

    if metodo == "-hash" and opcao == '-i':
        create_dir(pasta)
        dict_report(pasta)

    elif metodo == "-hash" and opcao == '-t':
        dict_diff(pasta, saida)

    elif opcao == '-x':
        delete_dir()

    else:
        print("Comando inválido!")
