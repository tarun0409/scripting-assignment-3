import os
import re


def ls(ls_pth='.'):
    entries = os.listdir(path=ls_pth)
    for entry in entries:
        print(entry)


def pwd():
    wd = os.getcwd()
    print(wd)


def cd(pth):
    os.chdir(pth)


def touch(file_path):
    f = open(file_path, "wb")
    f.close()


def grep(search_pattern, search_string):
    match_obj = re.match(search_pattern, search_string)
    if match_obj is not None:
        print(search_string)
    else:
        print()


def head(text):
    i = 0
    for line in text.splitlines():
        if i < 10:
            print(line)
        else:
            break
        i += 1


def tail(text):
    lines = text.split("\n")
    print("lines are :")
    no_of_lines = len(lines)
    start_index = no_of_lines - 10
    if start_index < 0:
        start_index = 0
    for i in range(start_index, no_of_lines):
        print(lines[i])


def tr(text, src, dst):
    trans_table = dict()
    for i in range(0, len(src)):
        trans_table[src[i]] = dst[i]
    t_list = list(text)
    ui = list()
    for c in src:
        for i in range(0, len(t_list)):
            if (t_list[i] == c) and (i not in ui):
                t_list[i] = trans_table[c]
                ui.append(i)
    res = "".join(t_list)
    print(res)
    # tb = str.maketrans(src, dst)
    # print(text.translate(tb))


def sed(text, src, dst, is_global):
    t_list = list(text)
    res_list = list()
    i = 0
    first = True
    while i < len(t_list):
        is_match = True
        j = i
        if is_global or ((not is_global) and first):
            for k in range(0, len(src)):
                if j < len(t_list):
                    if src[k] != t_list[j]:
                        is_match = False
                    j += 1
        else:
            is_match = False
        if is_match:
            first = False
            for c in dst:
                res_list.append(c)
            i += len(src)
        else:
            res_list.append(t_list[i])
            i += 1
    res = "".join(res_list)
    print(res)


def diff(s1, s2):
    lines1 = s1.split("\n")
    lines2 = s2.split("\n")
    if len(lines1) >= len(lines2):
        for i in range(0, len(lines1)-1):
            line1 = lines1[i]
            if i < len(lines2):
                line2 = lines2[i]
                if line1 != line2:
                    print("File 1: "+line1)
                    print("File 2: "+line2)
            else:
                print("File 1: "+line1)
                print("File 2: ")
    else:
        for i in range(0, len(lines2)-1):
            line2 = lines2[i]
            if i < len(lines1):
                line1 = lines1[i]
                if line2 != line1:
                    print("File 1: "+line1)
                    print("File 2: "+line2)
            else:
                print("File 1: ")
                print("File 2: "+line2)


cmd = input("$")
while cmd != "exit":
    cmd_split = cmd.split(" ")
    if cmd_split[0] == "cd":
        if len(cmd_split) < 2:
            print("Kindly enter a valid command")
        else:
            path = cmd_split[1]
            if os.path.isdir(path):
                cd(path)
            else:
                print("Enter a valid directory!")
    elif cmd_split[0] == "ls":
        if len(cmd_split) > 1:
            pth = cmd_split[1]
            if os.path.isdir(pth):
                ls(pth)
            else:
                print("Enter a valid directory!")
        else:
            ls()
    elif cmd_split[0] == "pwd":
        pwd()
    elif cmd_split[0] == "touch":
        if len(cmd_split) < 2:
            print("Enter a valid file name!")
        else:
            f_name = cmd_split[1]
            touch(f_name)
    elif cmd_split[0] == "grep":
        if len(cmd_split) < 3:
            print("Enter a valid grep command!")
        else:
            regexp = cmd_split[1]
            f_name = cmd_split[2]
            if os.path.isfile(f_name):
                fl = open(f_name, "r")
                ln = fl.readline()
                while ln:
                    grep(regexp, ln)
                    ln = fl.readline()
                fl.close()
            else:
                print("Enter a valid file name!")
    elif cmd_split[0] == "head":
        if len(cmd_split) < 2:
            print("Enter a valid head command!")
        else:
            f_name = cmd_split[1]
            if os.path.isfile(f_name):
                fl = open(f_name, "r")
                text = fl.read()
                head(text)
            else:
                print("Enter a valid file name!")
    elif cmd_split[0] == "tail":
        if len(cmd_split) < 2:
            print("Enter a valid tail command!")
        else:
            f_name = cmd_split[1]
            if os.path.isfile(f_name):
                fl = open(f_name, "r")
                text = fl.read()
                tail(text)
            else:
                print("Enter a valid file name!")
    elif cmd_split[0] == "tr":
        if len(cmd_split) < 4:
            print("Enter a valid tr command!")
        else:
            src_str = cmd_split[1]
            dst_str = cmd_split[2]
            tr_str = " ".join(cmd_split[3:])
            tr(tr_str, src_str, dst_str)

    elif cmd_split[0] == "sed":
        if len(cmd_split) < 2:
            print("Enter a valid sed command!")
        else:
            tokens = cmd_split[1].split("/")
            if len(tokens) < 3:
                print("Enter a valid sed command!")
            else:
                f_name = cmd_split[2]
                if os.path.isfile(f_name):
                    fl = open(f_name, "r")
                    text = fl.read()
                    if tokens[0] == "s":
                        src = tokens[1]
                        dst = tokens[2]
                        g = tokens[3]
                        if g == "g":
                            is_global = True
                        else:
                            is_global = False
                        sed(text, src, dst, is_global)
                else:
                    print("Enter a valid file name!")
    elif cmd_split[0] == "diff":
        if len(cmd_split) < 3:
            print("Enter a valid diff command")
        else:
            f1_name = cmd_split[1]
            if os.path.isfile(f1_name):
                f2_name = cmd_split[2]
                if os.path.isfile(f2_name):
                    fl1 = open(f1_name, "r")
                    fl2 = open(f2_name, "r")
                    txt1 = fl1.read()
                    txt2 = fl2.read()
                    diff(txt1, txt2)
                else:
                    print("Enter a valid file name!")
            else:
                print("Enter a valid file name!")

    cmd = input("$")
