import unittest
from models.avatar_generator import AvatarGenerator

class TestAvatarGenerator(unittest.TestCase):
    def test_create_avatar(self):
        generator = AvatarGenerator()
        avatar = generator.create_avatar("fantasy", "neutral", "watercolor")
        self.assertIsNotNone(avatar, "Avatar generation failed")

if __name__ == "__main__":
    unittest.main()
