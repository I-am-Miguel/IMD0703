import hashlib
import os
import sys
import yaml

dir_base = ".report/"
report_base = "report.json"
diff_base = "diff.json"

report_file = dir_base + report_base


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
    global report_file
    archive = report_file

    with open(os.path.abspath(archive), 'w') as report:
        report.write(str(dict_file))
    report.close()


def load_report(archive=report_file):
    report = open(os.path.abspath(archive))
    dict_file = yaml.load(str(report.read()))

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



def dict_diff(path_name):
    dict_file = scanner_dir(path_name)
    report = load_report()

    return calculate_dict_diff(report,dict_file)



def calculate_dict_diff(dict_base, dict_file):
    data = {}
    data['deleted'] = list(set(dict_file) - set(dict_base))
    data['created'] = list(set(dict_base) - set(dict_file))
    data['updated'] = []

    for f in set(dict_file).intersection(set(dict_base)):
        if dict_base[f] != dict_file[f]:
            data['updated'].append(f)

    with open(os.path.abspath(dir_base + diff_base), 'w') as diff:
        diff.write(str(data))
        diff.close()


if __name__ == '__main__':
    metodo = sys.argv[1]
    opcao = sys.argv[2]
    if metodo == "-hash" and opcao == '-i':
        dict_report(sys.argv[3])
    elif metodo == "-hash" and opcao == '-t':
        dict_diff(sys.argv[3])

    else:
        print("Comando inválido!")
