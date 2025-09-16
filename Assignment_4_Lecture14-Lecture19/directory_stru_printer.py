'''
4. Directory Structure Printer (Recursion on Non-numerics)
Task: Recursively print a nested folder structure.
Input:
files = {"root": {"docs": {"resume.pdf": {}, "cover_letter.docx": {}}, "photos": {"vacation": {"img1.jpg": {},
"img2.png": {}}}}}
print_structure(files)
Expected Output:
root/
docs/
resume.pdf
cover_letter.docx
photos/
vacation/
img1.jpg
img2.png
'''
    
def print_files_and_folder(files):
    for parent, children in files.items():
        if len(children) == 0:
            print(parent)
        else:
            print(f"{parent}/")
        print_files_and_folder(children)

files = {
    "root": {
        "docs": {
            "resume.pdf": {},
            "cover_letter.docx": {}
        },
        "photos": {
              "vacation": {
                  "img1.jpg": {},
                  "img2.png": {}
                  }
        }
    }
}

def main():
    print_files_and_folder(files)

if __name__ == '__main__':
    main()