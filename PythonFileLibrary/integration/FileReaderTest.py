from PythonFileLibrary.src.FileReader import FileReader
from os.path import join
import unittest

class FileReaderTest(unittest.TestCase):
    def setUp(self):
        # Init func for every test
        self.directory = "PythonFileLibrary/integration/FileReaderEnvironment/"
        self.defaultTestFile = join(self.directory, "RegularFile.txt")
        self.fileReader = FileReader(self.defaultTestFile)

    def test_FileException(self):
        # Check if an exception is thrown if given a file that doesn't exist
        with self.assertRaises(FileNotFoundError):
            self.fileReader = FileReader(fileName="nonexistent.txt")
        
    def test_PreserveCache(self):
        # Test if the class accurately preserves cached lists.
        fileCache = [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            " \n"
        ]

        self.fileReader = FileReader("test", fileCache)
        self.fileReader.ResetCursor()

        for index, line in enumerate(self.fileReader.Read()):
            self.assertTrue(fileCache[index] == line)

    
    def test_DoubleConstructor(self):
        # Test if the class correctly places predidence over contructor
        # parameters

        fileCache = [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            " \n"
        ]

        # Check if the cache, not file, was loaded in first. 
        self.fileReader = FileReader(self.defaultTestFile, fileCache)
        self.assertTrue(self.fileReader.GetFileLength() == 5)
    
    def test_Reset(self):
        self.fileReader.MoveCursorDown(10000)
        self.fileReader.ResetCursor()
        self.assertTrue(self.fileReader.GetCursorPosition() == 0)

    def test_UpperBound(self):
        self.fileReader.MoveCursorUp(100000)
        self.assertTrue(self.fileReader.GetCursorPosition() == 0)
    
    def test_LowerBound(self):
        self.fileReader.MoveCursorDown(100000)
        self.assertTrue(self.fileReader.GetCursorPosition() == self.fileReader.GetFileLength() - 1)
    
    def test_Filename(self):
        # Check if the class can correctly recognize filenames
        self.assertTrue(self.fileReader.GetFilename() == "RegularFile.txt")

        fileCache = [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            " \n"
        ]
        self.fileReader = FileReader("test4562", fileCache)
        self.assertTrue(self.fileReader.GetFilename() == "test4562")
    
    def test_Length(self):
        self.assertTrue(self.fileReader.GetFileLength() == 25)

    
    def test_CursorManipulation(self):
        # Test the accuracy of cursor manipulation
        self.fileReader.ResetCursor()

        flag = False
        for line in self.fileReader.Read():
            if not flag:
                self.fileReader.MoveCursorTo(23)
                flag=True

            else:
                self.assertEqual(line, "this is not the end.\n")
                break
        
        flag = False
        for line in self.fileReader.Read():
            if not flag:
                self.fileReader.MoveCursorUp(100000)
                flag=True

            else:
                self.assertEqual(line, "This is the start.\n")
                break


