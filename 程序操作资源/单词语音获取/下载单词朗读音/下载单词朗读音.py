import json
import os
import requests
from tqdm import tqdm


def download_audio_from_json(json_file_path, target_directory):
    # 确保目标目录存在
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # 读取json文件
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 下载每个单词的音频
    word_list = data['word_list']
    for word_info in tqdm(word_list, desc="Downloading audio files"):
        word = word_info['word']
        audio_url = f"https://dict.youdao.com/dictvoice?audio={word}&type=2"
        audio_path = os.path.join(target_directory, f"{word}.mp3")

        # 检查文件是否已经存在
        if os.path.exists(audio_path):
            print(f"Already exists: {word} in {target_directory}")
            continue

        response = requests.get(audio_url)
        if response.status_code == 200:
            with open(audio_path, 'wb') as audio_file:
                audio_file.write(response.content)
            print(f"Downloaded: {word} to {target_directory}")
        else:
            print(f"Failed to download: {word}")


def download_audio_from_folder(json_folder_path, output_base_directory):
    # 确保输出基目录存在
    if not os.path.exists(output_base_directory):
        os.makedirs(output_base_directory)

    # 遍历文件夹中的所有json文件
    for json_file_name in os.listdir(json_folder_path):
        if json_file_name.endswith('.json'):
            json_file_path = os.path.join(json_folder_path, json_file_name)
            # json_file_base_name = os.path.splitext(json_file_name)[0]
            # target_directory = os.path.join(output_base_directory, json_file_base_name)

            # 下载音频
            download_audio_from_json(json_file_path, output_base_directory)


# 使用示例
json_folder_path = '/Users/duyi/UnityProject/WordPuddingResource/程序操作资源/单词json/单词json'  # 替换为你的json文件夹路径
output_base_directory = '/Users/duyi/UnityProject/WordPuddingResourceGitee/mainword/all/wordaudios'  # 替换为你的输出基目录路径
download_audio_from_folder(json_folder_path, output_base_directory)
