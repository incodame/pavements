import unittest
from unittest.mock import MagicMock
from pavements import Pavement
from Tag import Tag
from Application import Application

class TestPavementGenerators(unittest.TestCase):
    def setUp(self):
        # Mock Tag objects
        self.tag1 = Tag(name="tag1", genre="genre1", version="1.0")
        self.tag2 = Tag(name="tag2", genre="genre2", version="2.0")

        # Mock Application objects
        self.app1 = MagicMock(spec=Application, tags=[self.tag1])
        self.app2 = MagicMock(spec=Application, tags=[self.tag2])
        self.app3 = MagicMock(spec=Application, tags=[self.tag1, self.tag2])

        # Create a Pavement instance
        self.pavement = Pavement(
            name="TestPavement",
            repository="https://example.com/repo",
            apps=[self.app1, self.app2, self.app3],
            containers=[],
            parameters=[],
            deployments=[],
            connect=[],
            tags=[self.tag1, self.tag2],
        )

    def test_get_apps_with_empty_tag_list(self):
        # Test get_apps with an empty tag list
        result = list(self.pavement.get_apps(tag_list=[]))
        self.assertEqual(result, [self.app1, self.app2, self.app3])

    def test_get_apps_with_specific_tags(self):
        # Test get_apps with a specific tag
        result = list(self.pavement.get_apps(tag_list=[self.tag1]))
        self.assertEqual(result, [self.app1, self.app3])

        result = list(self.pavement.get_apps(tag_list=[self.tag2]))
        self.assertEqual(result, [self.app2, self.app3])

    def test_get_tags(self):
        # Test get_tags to ensure all tags are returned
        result = list(self.pavement.get_tags())
        self.assertEqual(result, [self.tag1, self.tag2])

if __name__ == "__main__":
    unittest.main()