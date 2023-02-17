import pyperclip

def split_text(text, max_len):
    lines = text.split('\n')
    result = []
    current_line = ''
    for line in lines:
        if len(current_line) + len(line) > max_len:
            result.append(current_line)
            current_line = ''
        if current_line:
            current_line += '\n'
        current_line += line
    if current_line:
        result.append(current_line)
    return result

text = input("Digite o texto a ser dividido: ")
parts = split_text(text, 2000)

print("Para colar as partes, pressione Enter após cada uma:")
for part in parts:
    pyperclip.copy(part)
    input()