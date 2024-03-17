d = dict(none123=None)
print(d)
d = {None: None, **d}
print(d)
d[1] = 1
print(d)
d = d | {2: 2}
print(d)
_ = d.setdefault(3, 3)
print(d)
print(d.get(4))
print(d)
d.pop(1)
print(d)

print(d.items())

print(d.keys())
print(d.values())
