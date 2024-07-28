def generate_chinese_characters_file(filename):
    with open(filename, 'w', encoding='utf-8') as file:
        # 常用中文字符范围
        for codepoint in range(0x4E00, 0x9FFF + 1):
            file.write(chr(codepoint))
        # 常用中文标点符号范围
        for codepoint in range(0x3000, 0x303F + 1):
            file.write(chr(codepoint))
        # 全角字符和半角字符范围
        for codepoint in range(0xFF00, 0xFFEF + 1):
            file.write(chr(codepoint))


filename = 'chinese_characters.txt'
generate_chinese_characters_file(filename)
print(f'Chinese characters file "{filename}" has been created.')
