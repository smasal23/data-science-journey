# File Handling - Read, Write, Append, Delete

# Creating
text = "Shubham is a good guy."
FH = open(r"F:\onedrive\Desktop\python_codes\30th_Dec.txt", "w")
FH.write(text)
FH.close()

# Reading
FH = open(r"F:\onedrive\Desktop\python_codes\30th_Dec.txt", "r")
print(FH.read())
FH.close()

# Appending
FH = open("30th_Dec.txt", "a")
FH.write("\n He likes football.")
FH.close()

FH = open("30th_Dec.txt", "r")
print(FH.read())
FH.close()

# Deleting
import os
os.remove("30th_Dec.txt")

# Asking input from user
path = r"F:\onedrive\Desktop\python_codes\30th_Dec_2.txt"
FH = open(path, "w")
print("Asking Input from User.")
text = input("Enter your data:")
print("User Input Completed")
print("Saving to File")
FH.write(text)
print("File Saved in {}".format(path))
FH.close()