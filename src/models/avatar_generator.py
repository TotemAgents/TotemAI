from PIL import Image, ImageDraw

class AvatarGenerator:
    def generate(self, theme, style):
        print(f"Generating avatar with theme: {theme} and style: {style}")
        image = Image.new("RGB", (512, 512), color=(255, 255, 255))
        draw = ImageDraw.Draw(image)
        draw.text((50, 250), f"{theme}\n{style}", fill=(0, 0, 0))
        return image
