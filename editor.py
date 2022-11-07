# write your code here
# write your code here
# import markdown
a = """# John Lennon
or ***John Winston Ono Lennon*** was one of *The Beatles*.
Here are the songs he wrote I like the most:

- Imagine
- Norwegian Wood
- Come Together
- In My Life
- ~~Hey Jude~~ (that was *McCartney*)"""
# print(a)

formatters_text = "plain bold italic header link inline-code ordered-list unordered-list new-line"
# formatters_text = "plain bold italic header link inline-code new-line"

formatters = formatters_text.split()

spec_com_text = "!help !done"
spec_com = spec_com_text.split()

help_msg = f"""Available formatters: {formatters_text}
Special commands: {spec_com_text}"""

def format_input():
    out = ""
    arg = input("Choose a formatter: ")
    if arg in formatters:
        out = arg
    elif arg not in spec_com:
            print("Unknown formatting type or command")
            out = format_input()
    else:
        out = arg

    if arg == spec_com[0]:
        print(help_msg)
        out = format_input()
    if arg == spec_com[1]: # !done
        file = open("output.md", "w")
        file.write(txt)
        file.close()

        quit()
    return out

def get_level():
    level = input("Level: ")
    try:
        level = int(level)
    except:
        print("The level should be within the range of 1 to 6")
        level = get_level()
    if not 1 <= level <= 6:
        print("The level should be within the range of 1 to 6")
        level = get_level()
    return level

def header_sub():
    level = get_level()
    text_loc = input("Text:")
    out = "#" * level + " " + text_loc + "\n"
    return out

def plain_sub():
    text_loc = input("Text:")
    out = text_loc
    return out

def bold_sub():
    text_loc = input("Text:")
    out = "**" + text_loc + "**"
    return out

def italic_sub():
    text_loc = input("Text:")
    out = "*" + text_loc + "*"
    return out

def link_sub():
    text_loc = input("Label:")
    out = "[" + text_loc + "]"
    text_loc = input("URL:")
    out = out + "(" + text_loc + ")"
    return out

def inline_code_sub():
    text_loc = input("Text:")
    out = "`" + text_loc + "`"
    return out

def new_line_sub():
    out = "\n"
    return out


def row_lines_num():
    read = input("Number of rows:")
    try:
        out = int(read)
    except:
        print("failed to convert to integer")
        out = row_lines_num()

    if out < 1:
        print("The number of rows should be greater than zero")
        out = row_lines_num()
    return out

def list_sub():
    lines_num = row_lines_num()
    lines = []

    for i in range (1,lines_num + 1):
        lines.append(input(f"Row #{i}"))

    out = ""
    pre = ""
    # ordered-list unordered-list
    for i, line in enumerate(lines):
        if f.upper() == "ordered-list".upper():
            pre = f"{i+1}. "
        if f.upper() == "unordered-list".upper():
            pre = f"* "
        out = out + pre + line + "\n"
    # out = out + "\n"
    return out


# pipeline
txt = ""
while True:
    f = format_input()
    if f.upper() == 'header'.upper():
        piece = header_sub()
        if txt != "":
            piece = "\n" + piece

    if f.upper() == 'plain'.upper():
        piece = plain_sub()

    if f.upper() == 'bold'.upper():
        piece = bold_sub()

    if f.upper() == 'italic'.upper():
        piece = italic_sub()

    if f.upper() == 'link'.upper():
        piece = link_sub()

    if f.upper() == 'inline-code'.upper():
        piece = inline_code_sub()

    if f.upper() == 'new-line'.upper():
        piece = new_line_sub()

        # ordered-list unordered-list

    if f.upper() == 'ordered-list'.upper() or f.upper() == 'unordered-list'.upper():
        piece = list_sub()


    txt = txt + piece

    print(txt)
