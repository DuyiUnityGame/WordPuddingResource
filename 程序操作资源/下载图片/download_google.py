import json
import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import random
from tqdm import tqdm


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


# 创建用于保存图片的目录
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


# 获取搜索结果页面的HTML内容
def get_search_results(query):
    url = f"https://www.bing.com/images/search?q={query}&FORM=HDRSC2"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    return response.text


# 解析HTML获取图片URL
def parse_image_urls(html):
    soup = BeautifulSoup(html, 'html.parser')
    image_elements = soup.find_all('img', class_='mimg')
    image_urls = [img['src'] for img in image_elements if
                  'src' in img.attrs and not img['src'].startswith('data:image')]
    return image_urls[:4]


# 下载图片并保存到本地
def download_image(image_url, directory, word):
    try:
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        image.save(os.path.join(directory, f'{word}.jpg'))
        print(f"{word}.jpg 下载完成")
    except Exception as e:
        print(f"无法下载图片 {image_url}。错误信息：{e}")


# 遍历每一个单词并下载图片
def download_images_for_words(word_list, directory):
    for word in tqdm(word_list, desc="Downloading images"):
        download_random_image_for_word(word, directory)


# 主函数
def download_random_image_for_word(word, directory):
    # 创建用于保存图片的目录
    create_directory(directory)

    if not os.path.exists(os.path.join(directory, f'{word}.jpg')):
        query = f"{word} cartoon"  # 使用单词加上 "cartoon" 作为查询关键字
        html = get_search_results(query)
        image_urls = parse_image_urls(html)

        if image_urls:
            random_image_url = random.choice(image_urls)
            download_image(random_image_url, directory, word)
        else:
            print(f"未找到任何关于 {word} 的图片")
    else:
        print(f"{word}.jpg 已存在，跳过下载")


# 示例使用
folder_path = '/Users/duyi/UnityProject/WordPuddingResource/程序操作资源/单词json/单词json'  # 请将此路径替换为实际的文件夹路径
directory = 'images'  # 保存图片的文件夹
combined_words = get_combined_word_list(folder_path)
combined_words.sort()
combined_words = combined_words[:100]
download_images_for_words(combined_words, directory)

print(combined_words)
print(len(combined_words))
