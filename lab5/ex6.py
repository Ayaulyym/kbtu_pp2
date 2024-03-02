import re

pattern = r"[ ,.]"

text = "Text, for example."

result = re.sub(pattern, ":", text)

print(result)