#-----------------------------------------------------------------------------------
#   DCS Counter Measures - Python 3  - Author: sthom
#-----------------------------------------------------------------------------------



# Imports ==========================================================================
import os
import shutil



# Classes =========================================================================

class Main:

    # Builder
    def __init__(self):
        "Set the file path"

        # Path of files
        self.pathDefault = "test/test/TestFile.txt"
        self.pathNew = "CustomFiles/TestFile.txt"



    # Tool
    def copyFile(self):
        "Perform the copy of the files"

        # Delete default file
        if os.path.isfile(self.pathDefault):
            os.remove(self.pathDefault)
            print("Default file removed")
        else:
            print("Default file not found!")


        # Copy new file
        if os.path.isfile(self.pathNew):
            shutil.copyfile(self.pathNew, self.pathDefault)
            print("New file copied")
        else:
            print("New file not found!")





# Main =========================================================================
application = Main()
application.copyFile()