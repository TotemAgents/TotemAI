def save_avatar(avatar, file_path):
    try:
        avatar.save(file_path)
        print(f"Avatar saved to {file_path}.")
    except Exception as e:
        print(f"Failed to save avatar: {e}")
