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
prev = ""
curr = ""
modified = ""
for char in text:
    if char == " ": continue
    if prev.isdigit() and not char.isdigit() and char != "," and char.:
        modified+= char + "\n"
        prev = char
    else:
        modified += char
        prev = char

# print(text)
print(modified)