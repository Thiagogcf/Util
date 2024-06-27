import pyperclip

# get cliboard content
content = pyperclip.paste()
pathlist = content.split("\n")
print(pathlist)
clipboard = ''
for path in pathlist:
    print(path)
    clipboard += path + ':\n\n'
    # add file content to clipboard
    path = path.rstrip('\r')  # remove carriage return character
    with open(path, 'r') as file:
        clipboard += file.read() + '\n\n\n\n'

# copy clipboard content
pyperclip.copy(clipboard)
