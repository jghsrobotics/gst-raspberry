from PythonFileLibrary.src.RecursiveScanner import RecursiveScanner
from os.path import join
import unittest

class RecursiveScannerTest(unittest.TestCase):

    def setUp(self):
        # Init func for every test
        self.directory = "PythonFileLibrary/integration/RecursiveScannerEnvironment/"
        self.scanner = RecursiveScanner(self.directory)

    def test_None(self):
        depth0 = self.scanner.Scan(['.py'], 0)
        self.assertTrue(len(depth0) == 0)
    
    def test_MP3(self):
        depth0 = self.scanner.Scan(['.mp3'], 0)

        self.assertTrue(len(depth0) == 3)
        self.assertTrue("PythonFileLibrary/integration/RecursiveScannerEnvironment/base/base2/base3/test.mp3" in depth0)

        depth1 = self.scanner.Scan(['.mp3'], 1)
        self.assertTrue(len(depth1) == 0)

        depth2 = self.scanner.Scan('.mp3', 2)
        self.assertTrue(len(depth2) == 1)
        self.assertTrue("PythonFileLibrary/integration/RecursiveScannerEnvironment/base/test.mp3" in depth2)

    def test_TXT(self):
        depth0 = self.scanner.Scan(['.txt'], 0)

        self.assertTrue(len(depth0) == 4)
        self.assertTrue("PythonFileLibrary/integration/RecursiveScannerEnvironment/base/base2/base3/test.txt" in depth0)

        depth1 = self.scanner.Scan(['.txt'], 1)
        self.assertTrue(len(depth1) == 1)
        self.assertTrue("PythonFileLibrary/integration/RecursiveScannerEnvironment/test.txt" in depth1)

        depth2 = self.scanner.Scan(['.txt'], 2)
        self.assertTrue(len(depth2) == 2)
        self.assertTrue("PythonFileLibrary/integration/RecursiveScannerEnvironment/test.txt" in depth2)
        self.assertTrue("PythonFileLibrary/integration/RecursiveScannerEnvironment/base/test.txt" in depth2)
    
    def test_ALL(self):
        depth0 = self.scanner.Scan([], 0)

        self.assertTrue(len(depth0) == 7)
        self.assertTrue("PythonFileLibrary/integration/RecursiveScannerEnvironment/base/base2/base3/test.mp3" in depth0)
        self.assertTrue("PythonFileLibrary/integration/RecursiveScannerEnvironment/base/base2/base3/test.txt" in depth0)

        depth1 = self.scanner.Scan([], 1)
        self.assertTrue(len(depth1) == 1)
        self.assertTrue("PythonFileLibrary/integration/RecursiveScannerEnvironment/test.txt" in depth1)

        depth2 = self.scanner.Scan([], 2)
        self.assertTrue(len(depth2) == 3)
        self.assertTrue("PythonFileLibrary/integration/RecursiveScannerEnvironment/test.txt" in depth2)
        self.assertTrue("PythonFileLibrary/integration/RecursiveScannerEnvironment/base/test.txt" in depth2)
        self.assertTrue("PythonFileLibrary/integration/RecursiveScannerEnvironment/base/test.mp3" in depth2)









