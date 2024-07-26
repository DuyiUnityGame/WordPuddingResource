from PIL import Image

# Load the WebP image
webp_image_path = 'defaultword.webp'  # Change this path to the actual file path
webp_image = Image.open(webp_image_path)

# Convert the WebP image to JPG
jpg_image_path = webp_image_path.replace('.webp', '.jpg')
webp_image.convert('RGB').save(jpg_image_path, 'JPEG')

