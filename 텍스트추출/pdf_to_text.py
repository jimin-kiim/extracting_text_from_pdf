import fitz
import re
path = "태인일식.pdf"
doc = fitz.open(path)
text = ""
temp = ""
for page in doc:
    temp = page.get_text() # 단어가져오기
    temp = temp.replace("\n", " ")  
    # temp = temp.replace("\n", "NNNN") 
    text += temp
print(text)
prev = ""
modified = ""
for char in text:
    if prev.isdecimal() and char == " ":
        modified+= "\t"
        continue
    elif char == " ": 
        continue
    elif prev.isdecimal() and not char.isdecimal() and char != "," :
        modified+="\n" + char
        prev = char
    # elif char == ")":
    #     modified+= char
    #     prev = char
    # elif prev == " " and char.isnumeric():
        # modified+= char+ "\t"
        # prev = char 
    else:
        modified += char
        prev = char

# print(text)
print(modified)
# print("Ⅴ".isnumeric())