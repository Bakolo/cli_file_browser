import os

def sel_show_file(fList):
    index_len = len(str(len(fList)))
    for idx,f in enumerate(fList):
        print(f"{idx:>{index_len}}. {f}")
    answer = ask_sel_file()
    return answer

def ask_sel_file():
    answer = input("select/index, string, Quit/q: ")
    return answer


def file_browser(dir):
    #select, quit, go up
    index = 0
    default_path = ['../', './']

    print(f"Current path: '{os.path.abspath(dir)}'")
    dir_info = os.walk(dir)
    cur_dir = next(dir_info)
    
    file_list = []
    file_list.append(default_path[0])
    file_list.append(default_path[1])
    if cur_dir[1]:  #folders
        for item in cur_dir[1]:
            file_list.append(item + '/')
    if cur_dir[2]:  #files
        for item in cur_dir[2]:
            file_list.append(item)
    sel_ans = sel_show_file(file_list)
    sel_name = ""
    while True:
        if sel_ans.isnumeric():
            sel_idx = int(sel_ans)
            if sel_idx >= len(file_list) or sel_idx < 0:
                print("[WARNING!] Invalid input, input over range.")
                sel_ans = ask_sel_file()
            else:
                sel_name = file_list[sel_idx]
                break
        else:
            if sel_ans.lower() == 'q':
               sel_name = ""
               break
            elif sel_ans in file_list:
                sel_name = sel_ans
                break
            else:
                print("[WARNING!] Invalid input, '{sel_ans}' not exist.")
                sel_ans = ask_sel_file()
    #import pdb;pdb.set_trace() 
    if sel_name == "":  #q
        file_name = sel_name
    elif sel_name == default_path[1]: #./
        file_name = os.path.abspath(cur_dir[0])
    else:
        if sel_name == default_path[0]:  # ../
            cur_path = os.path.abspath(cur_dir[0])
            go_path = os.path.dirname(cur_path)
        else:
            cur_path = os.path.join(cur_dir[0], sel_name)
            go_path = os.path.abspath(cur_path)
        if os.path.isdir(go_path):
            file_name = file_browser(go_path)
        else:
            file_name = go_path

    print(file_name)
    return file_name

file_browser('.')
