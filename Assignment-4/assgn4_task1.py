try:
    with open("sample1.txt", "rt") as file:
        content = file.readlines()
except FileNotFoundError as err:
    print(f"Error: The file was not found.")
else:
    print("Reading file content:")
    for index, line in enumerate(content):
        print(f"Line {index + 1}: {line.strip()}")