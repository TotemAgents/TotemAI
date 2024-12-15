import unittest
from models.avatar_generator import AvatarGenerator

class TestAvatarGenerator(unittest.TestCase):
    def test_generate(self):
        generator = AvatarGenerator()
        avatar = generator.generate("fantasy", "pixel art")
        self.assertIsNotNone(avatar, "Avatar generation failed.")

if __name__ == "__main__":
    unittest.main()
