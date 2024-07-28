import json
import os


def get_word_list_from_file(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        word_list = [item['word'] for item in data['word_list']]
    return word_list


def get_combined_word_list(folder_path):
    combined_word_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            combined_word_list.extend(get_word_list_from_file(file_path))
    combined_word_list = list(set(combined_word_list))  # 去重
    return combined_word_list


# 示例使用
folder_path = '/Users/duyi/UnityProject/WordPuddingResource/程序操作资源/单词json/单词json'  # 请将此路径替换为实际的文件夹路径
combined_words = get_combined_word_list(folder_path)
print(combined_words)
print(len(combined_words))
