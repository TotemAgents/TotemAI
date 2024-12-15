from PIL import Image, ImageDraw

class AgentGenerator:
    def create_agent(self, theme, gender, style):
        # Placeholder logic for generating an avatar
        print(f"Generating avatar with theme: {theme}, gender: {gender}, style: {style}")
        image = Image.new("RGB", (512, 512), color=(255, 255, 255))
        draw = ImageDraw.Draw(image)
        draw.text((150, 250), f"{theme} {gender} {style}", fill=(0, 0, 0))
        return image
