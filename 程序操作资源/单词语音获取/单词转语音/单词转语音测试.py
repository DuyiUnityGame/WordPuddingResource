from gtts import gTTS
import os

# 要转换的文本
text = "我爱你中国"

# 设置语言
tts = gTTS(text=text, lang='zh')

# 保存为MP3文件
tts.save("output.mp3")

# 播放MP3文件
# os.system("start output.mp3")  # 对于Windows系统
# os.system("afplay output.mp3")  # 对于macOS系统
# os.system("mpg321 output.mp3")  # 对于Linux系统
