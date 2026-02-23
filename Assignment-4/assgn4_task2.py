text = input("Enter text to write to the file: ")

with open("output.txt", "wt") as file:
    file.write(text+"\n")
    print("Data successfully written to output.txt.\n")

text_appnd = input("Enter additional text to append: ")

with open("output.txt", "at") as file:
    file.write(text_appnd+"\n")
    print("Data successfully appended")
    
with open("output.txt", "rt") as file:
    content = file.read()
    print("\nFinal content of output.txt:")
    print(content)
    