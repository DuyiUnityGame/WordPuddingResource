import os
import json
from gtts import gTTS
from tqdm import tqdm

def text_to_speech(word, example_sentence, output_folder, lang='en'):
    """
    将单词和例句转换为语音并保存为MP3文件。

    参数：
    word (str): 要转换的单词。
    example_sentence (str): 单词的例句。
    output_folder (str): 保存MP3文件的文件夹。
    lang (str): 语言代码，默认为'英语'（'en'）。

    返回：
    None
    """
    # 保存为MP3文件的完整路径
    filename = os.path.join(output_folder, f"{word}_sentence.mp3")

    # 检查文件是否已经存在
    if os.path.exists(filename):
        print(f"文件已存在：{filename}")
        return

    try:
        # 创建 gTTS 对象
        tts = gTTS(text=f"{example_sentence}", lang=lang)

        # 保存为MP3文件
        tts.save(filename)

        print(f"语音文件已保存为 {filename}")

    except Exception as e:
        print(f"转换失败: {e}")

def process_json(json_file, output_folder):
    """
    处理JSON文件，读取单词和例句，并生成语音文件。

    参数：
    json_file (str): JSON文件路径。
    output_folder (str): 保存MP3文件的文件夹。

    返回：
    None
    """
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 读取JSON文件
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 处理每个单词
    for item in tqdm(data['word_list'], desc="Processing words"):
        word = item['word']
        example_sentence = item['example_sentence']
        text_to_speech(word, example_sentence, output_folder)

# 示例调用
json_file = '/Users/duyi/UnityProject/WordPuddingResource/程序操作资源/单词json/单词json/kaoyan.json'  # 请将此路径替换为你的JSON文件路径
output_folder = '/Users/duyi/UnityProject/WordPuddingResourceGitee/mainword/kaoyan/sentenceaudios'  # 保存MP3文件的文件夹
process_json(json_file, output_folder)
