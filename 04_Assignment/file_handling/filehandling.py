# File handling is essential for reading and writing data to files, enabling persistent storage. Python provides buil-in functions and methods to handle files efficiently.
# we use open() function to open the file
# r:Read
# w:Write(Opens the file for writing.Creates the file if it does'nt exist,or overwrites it if it does)
# a: Append (Opens the file for appending. Creates the file if it doesn't exist, or adds to it if it does.)
# x:Exclusive creation (fails if file exists)
# lines = ["Line 1: Kachi\n", "Line 2: Lahore\n", "Line 3: Peshawar\n"]
# file = open("new_file.txt", "r")
# for line in file:
#     print(line.strip())
# file.close()

# print("This is start with keywords")
# # Using with keyword and it is best practise to use with keyword 
# # When we use with keyword then there is not need to close the file it 
# with open("new_file.txt","r") as f:
#     content=f.read()
#     print(content)
    
# Reading in Chunks
# with open("new_file.txt", "r") as file:
#   print(file.tell())     # 0

#   i = 0  # Initialize the variable `i`
#   while True:
#     content = file.read(10)
#     if not content:
#       print("End of file")
#       break
#     print(content)
#     i += 1  # Increment `i`

#            # reads 5 characters
#   print(file.tell())     # now at position 5
#   file.seek(0)
  
# Program for replacing word with another word in the file
with open("new_file.txt", "r") as file:
    content=file.read()
    print(content)
    content=content.replace("javascript","python")
    print(content)
    
# Program for copying data from one file to another file
def copy_file(source_path,destination_path):
    try:
        with open(source_path,"r") as source_file ,open(destination_path,"w") as dest_file:
            for line in source_file:
                dest_file.write(line)
        print(f"File '{source_path}' copied to '{destination_path}' successfully")
    except FileNotFoundError:
        print(f"Error: Source file '{source_path}' not found.")
    except Exception as e:
        print(f"An error occurred:{e}")

copy_file("new_file.txt","Unique_copy.txt")