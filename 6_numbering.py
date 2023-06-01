with open('uploads.txt', 'r') as file:
    lines = file.readlines()

with open('uploads_num.txt', 'w') as newfile:
    for i, line in enumerate(lines):
        if i % 10 == 0 and i != 0:  # add a blank line after every 10 lines
            newfile.write('\n')
        newfile.write(f"{i+1}. {line}")
