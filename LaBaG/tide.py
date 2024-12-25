import os

#獲取當前資料夾的東西
dir_file_dict = dict()

def extract_py_to_dict(dir_path:str):
    """提取資料夾中的檔案進字典"""
    dir_items = os.listdir(dir_path)
    dir_file_dict[dir_path] = list()
    for item in dir_items:
        if item == os.path.basename(__file__):
            continue   
        item_path = os.path.join(dir_path, item)
        
        if os.path.isdir(item_path):
            if item == ".git":
                continue 
            extract_py_to_dict(item_path) #如果是資料夾就繼續

        if os.path.isfile(item_path):
                _, extension = os.path.splitext(item_path) # 使用 splitext 分離文件名與副檔名
                if extension == '.cpp' or extension ==".h" :
                    dir_file_dict[dir_path].append(item)
                else: 
                    continue

                
                    


def py_dict_to_txt(files_dict: dict[str, list[str]]):
    with open("cpp.txt", 'w', encoding='utf-8') as txt:
        for dir_path in files_dict:
            for f in files_dict[dir_path]:
                txt.write(f"@{dir_path}\\{f}\n")
                file_path = os.path.join(dir_path, f)
                with open(file_path, "r", encoding='utf-8') as file:
                    txt.write(file.read())
                txt.write("\n\n")


extract_py_to_dict(".")

py_dict_to_txt(dir_file_dict)