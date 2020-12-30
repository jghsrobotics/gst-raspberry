# PythonFileLibrary
A small cross-platform file library dedicated to reading and searching for specific files in Python. Features two classes:

## FileReader.py

A line-by-line file reader with cursor manipulation. 

Cached text file can be read through cursor manipulation, where the cursor
can be moved up or down to return the current line. If the cursor is out of
bounds, it will return either the first or last line of the file.

`__init__(self, fileName : str, fileList : [str] = [])` - Choose to create a FileReader from a file via import or from a list.

`GetFilename(self) -> str` - Returns the name of the file that is being read.

`GetFileLength(self) -> int` - Returns the amount of lines counted by each newline escape character (`\n`).

`GetCursorPosition(self) -> int` - Gets the current line position being read by the cursor [0 - GetFileLength() - 1].

`GetCurrentLine(self) -> str` - Gets the current line the cursor is on as a string.

`ResetCursor(self)` - Resets the cursor position to be at the top of the file. 

`Read(self) -> str` - Yields the entire file starting from the current cursor position while allowing for cursor manipulation; 
Detailed information is in source code. 

`__iter__(self) -> str` - Shorthand for Read(self).

`MoveCursorTo(self, line: int)` - Moves the cursor to a specific line in the file [clamped between 0 - GetFileLength() - 1], regardless of it
currently being Read(self) or not. 

`MoveCursorUp(self, amount: int = 1)` - Moves the cursor up by a number of lines [clamped to 0], regardless of it
currently being Read(self) or not. 

`MoveCursorDown(self, amount: int = 1)` - Moves the cursor down by a number of lines [clamped to GetFileLength() - 1], regardless of it
currently being Read(self) or not. 

`ReachedEnd(self) -> bool` - Whether or not the cursor is currently at the last line of the file. 

## RecursiveScanner.py

Recursively scans a directory for files of a specific extension.

`__init__(self, directory)` - Create a Recursive Scanner that scans in a certain directory.

`Scan(self, whitelist: [str], maxDepth: int = 0) -> [str]` - Recursively scan for files in the given directory with a specific extension;
Detailed info in source code. 





