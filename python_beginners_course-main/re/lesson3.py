import re


text = "lat = 5, lon=7"
# match = re.findall(r"\w+\s*=\s*\d+", text)
match = re.findall(r"(?:lat|lon)\s*=\s*\d+", text)

print(match)
match = re.findall(r"(lat|lon)\s*=\s*(\d+)", text)
print(match)
