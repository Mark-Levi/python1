import re

text = "подоходный налог,доход"
# match = re.findall(r"прибыль|обретение|доход", text)
match = re.findall(r"\b(прибыль|обретение|доход)\b", text)
print(match)

text = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1251">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Уроки по Python</title>
</head>
<body>
<script type="text/javascript">
let o = document.getElementById('id_div');
console.log(obj);
</script>
</body>
</html>"""

match = re.findall(r"^<script.*?>([\w\W]+)(?=</script>)", text, re.MULTILINE)
print(match)
