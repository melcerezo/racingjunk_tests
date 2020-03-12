import unittest
import hero_section_tests

suite = unittest.defaultTestLoader.loadTestsFromModule(hero_section_tests)

if __name__ == "__main__":
    unittest.TextTestRunner().run(suite)
