import os

class FileReader:
    """A line-by-line file reader with cursor manipulation. 

    Cached text file can be read through cursor manipulation, where the cursor
    can be moved up or down to return the current line. If the cursor is out of
    bounds, it will return either the first or last line of the file.

    Attributes:
        None
    """
    
    def __init__(self, fileName : str, fileList : [str] = []):
        """Creates a FileReader instance from either a file or cached list.

        Args:
            fileName: 
                The absolute or relative location of a .txt or similar file to
                import. If fileList is defined as well, this will simply set the
                fileName. 
            fileList: 
                Optional; A list of strings that make up a file. If this is defined,
                it will take precidence over fileName and a deep copy will occur. 
        
        Raises:
            FileNotFoundError if the imported file was not found.
        """

        self._cursorPosition = 0
        self._fileName = os.path.basename(fileName)
        self._applyCursorChange = False

        if len(fileList) > 0:
            self._fileContents = [i for i in fileList]
        else:
            self._fileContents = self._CacheFile(fileName)



    def _CacheFile(self, location: str) -> [str]:
        file = open(location, "r")
        cached = [line for line in file]
        file.close()
        return cached


    def GetFilename(self) -> str:
        """
        Returns:
            The name of the file, which is the basename of the directory
            imported. If the file was imported using a cached list, this will
            still return the basename of the fileName specified in __init__.
        """
        return self._fileName



    def GetFileLength(self) -> int:
        """
        Returns:
            The length of the file (determined by the number of \n) as an
            integer. 
        """
        return len(self._fileContents)



    def GetCursorPosition(self) -> int:
        """
        Returns:
            The current line of the cursor, from 0 to GetFileLength() - 1.
        """
        return self._cursorPosition



    def GetCurrentLine(self) -> str:
        """
        Returns:
            The current line the cursor is on as a str.
        """
        return self._fileContents[self._cursorPosition]



    def ResetCursor(self):
        """Resets the cursor to be at the top of the file."""
        self._cursorPosition = 0
        self._applyCursorChange = True

    

    def Read(self) -> str:
        """Yields the current line and every line after it until it reaches the
        end of the file. 

        During execution, the cursor position can be manipulated by
        MoveCursorUp(), MoveCursorDown(), or MoveCursorTo() in order to move the
        cursor to anywhere. By doing this, the next line yielded will be the
        current line at that position, where it will continue execution
        normally. 

        If more than one command of MoveCursorUp(), MoveCursorDown(), or
        MoveCursorTo() is executed in the loop, the cumulative total of those
        commands is the location of the next line to be yielded. 

        E.x.

            for line in fileReader.Read():
                fileReader.MoveCursorTo(6)
                fileReader.MoveUp(3)
                fileReader.MoveDown(1)

        ... would result in the end cursor position to be set to 4 every loop,
        causing the same line to be returned each loop. 
        """

        self._applyCursorChange = False
        yield self.GetCurrentLine()
        while not self.ReachedEnd():
            if not self._applyCursorChange:
                self.MoveCursorDown()
                
            self._applyCursorChange = False

            yield self.GetCurrentLine()

    def __iter__(self) -> str:
        return self.Read()


    def MoveCursorTo(self, line: int):
        """Moves the cursor to any line in the file. 

        Args:
            line: The # of the line you want to go to starting from 0 and ending at
            GetFileLength() - 1. Any values of out bound of this range will be clamped. 
        """

        self._cursorPosition = min(max(line, 0), self.GetFileLength() - 1)
        self._applyCursorChange = True



    def MoveCursorUp(self, amount: int = 1):
        """Moves the cursor up by a specific amount.

        Args:
            amount: 
                Optional; The number of lines to move up by. If this amount would
                exceed the top of the file, the cursor is moved to the very first
                line. If it's <=0, then nothing will occur. 
        """

        if amount > 0:
            self._cursorPosition = max(self._cursorPosition - amount, 0)
            self._applyCursorChange = True



    def MoveCursorDown(self, amount: int = 1):
        """Moves the cursor down by a specific amount.

        Args:
            amount: 
                Optional; The number of lines to move down by. If this amount would
                exceed the bottom of the file, the cursor is moved to the very last
                line. If it's <=0, then nothing will occur. 
        """

        if amount > 0:
            self._cursorPosition = min(self._cursorPosition + amount, self.GetFileLength() - 1)
            self._applyCursorChange = True

            

    def ReachedEnd(self) -> bool:
        """Whether or not the cursor is at the very last line.

        Returns:
            True if the cursor is at the last line, False otherwise.
        """

        return self._cursorPosition == self.GetFileLength() - 1
