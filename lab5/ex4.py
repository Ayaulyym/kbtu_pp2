import re 

pattern = r"[A-Z][a-z]+"
def match(pattern):

    with open("row.txt", "r", encoding="utf-8") as s:
        text = s.read()
        matches = re.findall(pattern, text)
        return matches

print(match(pattern))