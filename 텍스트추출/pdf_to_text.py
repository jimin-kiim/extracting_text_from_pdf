import fitz
import re
path = "태인일식.pdf"
doc = fitz.open(path)
text = ""
temp = ""
for page in doc:
    temp = page.get_text() 
    temp = temp.replace("\n", " ")  
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
    elif prev.isdecimal() and not char.isdecimal() and char != "," and char != ")":
        modified+="\n" + char
        prev = char
    else:
        modified += char
        prev = char

print(modified)