import unittest
from pavements import Pavement

class TestPavement(unittest.TestCase):
    def test_pavement_initialization(self):
        pavement = Pavement('test', 'test', [], [], [], [], [], [])
        self.assertIsNotNone(pavement)

    def test_some_method(self):
        pavement = Pavement('test', 'test', [], [], [], [], [], [])
        pavement.load_from("yaml/paragraph.yml")

if __name__ == "__main__":
    unittest.main()