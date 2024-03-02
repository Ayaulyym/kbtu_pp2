import re

pattern = r"ab{2,3}" 
def match(pattern):

    with open("row.txt", "r", encoding="utf-8") as s:
        text = s.read()
        matches = re.findall(pattern, text)
        return matches

print(match(pattern))