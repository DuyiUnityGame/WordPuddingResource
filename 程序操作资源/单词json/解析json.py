import json

def process_json_file(input_file, output_file):
    word_list = []

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            word_info = {
                "word": data["headWord"],
                "meaning": "",
                "part_of_speech": "",
                "pronunciation": "",
                "example_sentence": "",
                "example_translation": ""
            }

            content = data["content"]["word"]["content"]

            # 提取单词含义、词性和发音
            if "trans" in content:
                meanings = []
                parts_of_speech = []
                for trans in content["trans"]:
                    meanings.append(trans["tranCn"].split('；')[0])  # 只取第一个分号之前的内容
                    parts_of_speech.append(trans["pos"])
                word_info["meaning"] = '/'.join(meanings)
                word_info["part_of_speech"] = '/'.join(parts_of_speech)

            # 提取发音，优先取usphone，如果为空则取ukphone
            usphone = content.get("usphone", "").strip()
            ukphone = content.get("ukphone", "").strip()
            word_info["pronunciation"] = usphone if usphone else ukphone

            # 提取例句和翻译
            if "sentence" in content and "sentences" in content["sentence"]:
                sentences = content["sentence"]["sentences"]
                if sentences:
                    word_info["example_sentence"] = sentences[0]["sContent"]
                    word_info["example_translation"] = sentences[0]["sCn"]

            word_list.append(word_info)

    # 生成最终的字典
    final_data = {"word_list": word_list}

    # 保存为新的JSON文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(final_data, f, ensure_ascii=False, indent=4)

    print(f"数据已成功保存到 {output_file}")

# 调用函数
input_file = 'KaoYan_3.json'
output_file = 'KaoYan_3_out.json'
process_json_file(input_file, output_file)
