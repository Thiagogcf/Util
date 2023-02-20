import pyperclip

def split_string(string, max_length):
    parts = [string[i:i + max_length] for i in range(0, len(string), max_length)]
    return parts

def store_parts(parts):
    for i, part in enumerate(parts):
        part_name = "parte {} #código".format(i + 1)
        print(part_name + "\n" + part + "\n")

def copy_to_clipboard(part):
    pyperclip.copy(part)

def main():
    arquivo = open("String.txt", "r", encoding="utf-8")
    string =  arquivo.read()
    max_length = 2000
    parts = split_string(string, max_length)
    store_parts(parts)

    while True:
        if pyperclip.paste() == "Ctrl + V":
            part = parts.pop(0)
            copy_to_clipboard(part)

if __name__ == "__main__":
    main()
