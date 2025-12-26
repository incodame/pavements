import unittest
from pavements import Pavement
from Tag import Tag
from Application import Application
from Parameter import Parameter

class TestPavementGenerators(unittest.TestCase):
    def setUp(self):
        # Tag objects
        self.tag1 = Tag(name="tag1", genre="genre1", version="1.0")
        self.tag2 = Tag(name="tag2", genre="genre2", version="2.0")

        # Application objects
        self.app1 = Application(name="App1", repositories=[], modules=[], deployments=[], tags=[self.tag1])
        self.app2 = Application(name="App2", repositories=[], modules=[], deployments=[], tags=[self.tag2])
        self.app3 = Application(name="App3", repositories=[], modules=[], deployments=[], tags=[self.tag1, self.tag2])

        # Parameter objects
        self.param1 = Parameter(name="Param1", type="string", isa="", loc="xpath(//'context-root'(text))", doc="", params=[])
        self.param2 = Parameter(name="Param2", type="int", isa="", loc="xpath(//'port'(text))", doc="", params=[])

        # Create a Pavement instance
        self.pavement = Pavement(
            name="TestPavement",
            repository="https://example.com/repo",
            apps=[self.app1, self.app2, self.app3],
            containers=[],
            parameters=[self.param1, self.param2],
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

    def test_get_parameters(self):
        # Test get_parameters to ensure it returns an empty list
        result = list(self.pavement.get_parameters())
        self.assertEqual(result, [self.param1, self.param2])

if __name__ == "__main__":
    unittest.main()