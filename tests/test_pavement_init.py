import unittest
from pavements import Pavement

class TestPavementInit(unittest.TestCase):
    def test_pavement_initialization(self):
        pavement = Pavement('test', 'test', [], [], [], [], [], [])
        self.assertIsNotNone(pavement)

    def test_load_method(self):
        pavement = Pavement('test', 'test', [], [], [], [], [], [])
        pavement.load_from("yaml/paragraph.yml")
        pom_xml = pavement.get_container('pom_xml')
        self.assertTrue(pom_xml is not None)
        pom_xml_params = list(pom_xml.params)
        self.assertTrue("version" in pom_xml_params)        

if __name__ == "__main__":
    unittest.main()