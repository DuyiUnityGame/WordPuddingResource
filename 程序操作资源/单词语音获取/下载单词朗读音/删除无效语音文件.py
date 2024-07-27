import os
import json


def remove_corrupted_mp3_files(directory):
    # 遍历目录及其所有子目录
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.mp3'):
                file_path = os.path.join(root, filename)

                # 尝试以文本文件打开并检查内容
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        if content.strip() == '{"code": 403}':
                            os.remove(file_path)
                            print(f"Removed corrupted file: {file_path}")
                except Exception as e:
                    # 如果无法以文本文件打开，则认为文件是正常的音频文件
                    pass


# 示例调用
directory = '/Users/duyi/UnityProject/WordPuddingResourceGitee/mainword/all/wordaudios'
remove_corrupted_mp3_files(directory)
