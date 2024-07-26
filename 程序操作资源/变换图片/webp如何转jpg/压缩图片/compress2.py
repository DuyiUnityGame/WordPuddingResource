import cv2
import os

def compress_image(input_path, output_path, quality=85):
    """
    使用OpenCV压缩单个JPG文件
    :param input_path: 输入文件路径
    :param output_path: 输出文件路径
    :param quality: 压缩质量，默认为85
    """
    img = cv2.imread(input_path)
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    cv2.imwrite(output_path, img, encode_param)

def compress_images_in_directory(input_dir, output_dir, quality=85):
    """
    压缩目录中的所有JPG文件
    :param input_dir: 输入目录路径
    :param output_dir: 输出目录路径
    :param quality: 压缩质量，默认为85
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(input_dir):
        if file_name.lower().endswith(".jpg") or file_name.lower().endswith(".jpeg"):
            input_file = os.path.join(input_dir, file_name)
            output_file = os.path.join(output_dir, file_name)
            compress_image(input_file, output_file, quality)
            print(f"Compressed {file_name} and saved to {output_file}")

# 示例用法
input_directory = "input"
output_directory = "output"
compression_quality = 10  # 你可以调整这个值来改变压缩质量

compress_images_in_directory(input_directory, output_directory, compression_quality)
