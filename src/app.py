from models.avatar_generator import AvatarGenerator

def main():
    print("Welcome to Totem AI!")
    theme = input("Enter a theme (e.g., fantasy, cyberpunk): ")
    style = input("Enter a style (e.g., pixel art, watercolor): ")

    generator = AvatarGenerator()
    avatar = generator.generate(theme, style)
    avatar.save("output/generated_avatar.png")
    print("Avatar saved to output/generated_avatar.png")

if __name__ == "__main__":
    main()
