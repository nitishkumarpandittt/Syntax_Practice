from pathlib import Path
import os

def readFileAndFolder():
    path = Path(__file__).parent
    items = path.rglob('*')
    for i, item in enumerate(items):
        print(f"{i+1}: {item.name}")

def createFile():
    try:
        readFileAndFolder()
        name = input("Enter the file name: ")
        folder_path = Path(__file__).parent
        p = folder_path/name
        if not p.exists():
            with open(p, 'w') as fs:
                data = input("Enter data in the file: ")
                fs.write(data)
            print("FILE CREATED SUCCESSFULLY")
        else:
            print("FILE ALREADY EXISTS")
    except Exception as err:
        print(f"Some error occured -> {err}")

def readFile():
    try: 
        readFileAndFolder()
        name = input("Enter the file name: ")
        folder_path = Path(__file__).parent
        p = folder_path/name
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print(data)
            print("FILE READ SUCCESSFULLY")
        else:
            print("FILE DOESN'T EXIST")
    except Exception as err:
        print(f"Some error occured -> {err}")

def updateFile():
    try:
        readFileAndFolder()
        name = input("Enter the file name you want to modify: ")
        folder_path = Path(__file__).parent
        p = folder_path/name
        if p.exists() and p.is_file():
            print("\nOPTIONS: ")
            print("Press 1 to rename file")
            print("Press 2 to overwrite content in the file")
            print("Press 3 to append content in the file")
    
            res = int(input("Select Option: "))
            if res == 1:
                new_name = input("Enter another name: ")
                p2 = folder_path / new_name
                p.rename(p2)
            elif res == 2:
                with open(p, "w") as fs:
                    data = input("Text to be overriden: ")
                    fs.write(data)
            elif res == 3:
                with open(p, 'a') as fs:
                    data = input("Text to be appended: ")
                    fs.write(" " + data)
            print("FILE UPDATED SUCCESSFULLY")
        else:
            print("FILE DOESN'T EXIST")
    except Exception as err:
        print(f"Some error occured -> {err}")


def deleteFile():
    try:
        readFileAndFolder()
        name = input("Which file you want to delete? ")
        folder_path = Path(__file__).parent
        p = folder_path / name
        if p.exists() and p.is_file():
            os.remove(p)
            print("FILE REMOVED SUCCESSFULLY")
        else:
            print("FILE DOESN'T EXIST")
    except Exception as err:
        print(f"Some error occured -> {err}")

print("\nOPTIONS: ")
print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file", end = "\n\n")

userInput = int(input("Select Option: "))

if userInput == 1:
    createFile()
elif userInput == 2:
    readFile()
elif userInput == 3:
    updateFile()
elif userInput == 4:
    deleteFile()
else:
    print("Enter valid input!!!")