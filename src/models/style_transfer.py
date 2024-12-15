from PIL import Image, ImageFilter

class StyleTransfer:
    def apply_style(self, avatar, style):
        print(f"Applying {style} style to avatar.")
        if style == "blurred":
            return avatar.filter(ImageFilter.GaussianBlur(5))
        elif style == "sharpened":
            return avatar.filter(ImageFilter.SHARPEN)
        else:
            print("Style not recognized. Returning original avatar.")
            return avatar
