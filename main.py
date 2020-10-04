'''
Created on 03.10.2020

@author: Jocker271
'''
from os import path, system, walk

ONEDRIVEPATH = "B:/OneDrive" #slash statt backslash
ICONPATH = "B:/OneDrive/Bilder/Icons/Windows"

def set_folder_icon(folder, icon):
    """
    set icon of folder by changing the path to the icon in the desktop.ini
    @param str folder: path of the folder
    @param str icon:   path of the icon
    """
    config = folder + "/desktop.ini"
    if path.exists(config):
        with open(config, "r+") as f:
            old = f.read()
            f.seek(0)
            lines = old.split("\n")
            new = ""
            for line in lines:
                if "IconResource=" in line:
                    line = "IconResource=" + icon + ",0"
                new += line + "\n"
            f.write(new)
            f.close()
    else:
        f = open(config, "x")
        f.write("[.ShellClassInfo]\nIconResource=" +  icon + ",0\n[ViewState]\nMode=\nVid=\nFolderType=Generic\n")
        f.close()

def set_folder_readonly(folder_path):
    """
    set folder readonly to initialise containing dektop.ini
    """
    attr_command = "attrib +r " + folder_path
    if " " in folder_path:
        attr_command = "attrib +r " + '"' + folder_path + '"'
    system(attr_command)

def get_folder(parent_path):
    """
    return list of folders inside parent folder
    """
    folder_list = []
    for (dirpath, dirnames, filenames) in walk(parent_path):
        folder_list.extend(dirnames)
        break
    return folder_list

def main(parent_folder_path, icon_folder_path):
    path_dict = {}
    for folder in get_folder(parent_folder_path):
        # ADD MATCH AND ICON'
        f_path = parent_folder_path + "/" + folder
        i_path = icon_folder_path + "/" + folder.lower() + ".ico"
        path_dict[f_path] = i_path
        subfolderpath = parent_folder_path + "/" + folder
        for subfolder in get_folder(subfolderpath):
            f2_path = subfolderpath + "/" + subfolder
            i2_path = icon_folder_path + "/" + folder.lower() + "_" + subfolder.lower() + ".ico"
            path_dict[f2_path] = i2_path
    for f in path_dict:
        if path.exists(path_dict[f]):
            set_folder_icon(f, path_dict[f])
            set_folder_readonly(f)
    print("fertig")

main(ONEDRIVEPATH, ICONPATH)
