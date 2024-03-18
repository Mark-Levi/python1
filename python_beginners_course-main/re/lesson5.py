import re

text = "<font color=#CC0000>"
match = re.search(r"(\w+)=(#[\da-fA-F]{6})\b", text)
print(match.group(0), match.group(1), match.group(2))
print(match)
print(match.group(0))

match = re.search(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text)
print(match.groupdict())
print(match.expand(r"\g<key>:\g<value>"))
