import os

class RecursiveScanner:
    """Recursively scans a directory for files of a specific extension."""

    def __init__(self, directory: str):
        """Creates a RecursiveScanner instance from a directory. 

        Args:
            directory: The location of a directory to recursively scan given as
            a string. After this has been set, you cannot modify it. 
        """

        self._directory = directory
    
    def _Scan(self, directory: str, whitelist: [str], maxDepth: int = 0) -> [str]:
        foundFiles = []
        dirObjects = os.listdir(directory)

        # Recursively search files until depth == 1 or there are no more
        # folders. 
        for obj in dirObjects:
            objDir = os.path.join(directory, obj)

            if os.path.isfile(objDir):
                _, extension = os.path.splitext(objDir)
                if extension in whitelist or len(whitelist) == 0:
                    foundFiles.append(objDir)
            
            elif os.path.isdir(objDir) and (maxDepth > 1 or maxDepth <= 0):
                foundFiles.extend(self._Scan(objDir, whitelist, maxDepth - 1))
    
        return foundFiles

    def Scan(self, whitelist: [str], maxDepth: int = 0) -> [str]:
        """Scan for files with a specific extension in this directory. 

        Args:
            whitelist: 
                A list of strings that denote the types of extensions wanted, such
                as ['.txt', '.mp3']. If the list is empty, no filter will be done
                and every single file in the directory will be returned.  

            maxDepth: 
                Optional; Specifies the maximum depth that will be searched. E.x.
                A depth of 1 means that ONLY the current directory will be searched
                for files, while a depth of 2 means that the current directory and 
                the next level below it will be searched for files. If this is 0 
                (default) or below, the entire directory will be searched.
        
        Returns:
            A list of directories (as strings) that share the common directory
            you specificied in __init__.

            E.x. 

            RecursiveScanner("folder/anotherfolder/") would give files like

            ["folder/anotherfolder/text.txt", "folder/anotherfolder/text.mp3"]

            And RecursiveScanner("home/<user>/Desktop/folder/anotherfolder/") 
            would give files like

            ["home/<user>/Desktop/folder/anotherfolder/text.txt", 
            "home/<user>/Desktop/folder/anotherfolder/text.mp3"]
        """


        return self._Scan(self._directory, whitelist, maxDepth)