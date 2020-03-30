import unittest
import global_header_tests

suite = unittest.defaultTestLoader.loadTestsFromModule(global_header_tests)

if __name__ == "__main__":
    unittest.TextTestRunner().run(suite)