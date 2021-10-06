import string

res = []
ltrs = string.ascii_lowercase
# res += ["".join([a]) for a in ltrs]  # a -> z 26
# res += ["".join([a, b]) for a in ltrs for b in ltrs]  # aa -> zz 26^2
# res += ["".join([a, b, c]) for a in ltrs for b in ltrs for c in ltrs]  # aaa -> zzz 26^3
# res += [
#     "".join([a, b, c, d]) for a in ltrs for b in ltrs for c in ltrs for d in ltrs
# ]  # aaaa -> zzzz 26^4
# res += [
#     "".join([a, b, c, d, e])
#     for a in ltrs
#     for b in ltrs
#     for c in ltrs
#     for d in ltrs
#     for e in ltrs
# ]  # aaaaa -> zzzzz 26^5
res += [
    "".join([a, b, c, d, e, f])
    for a in ltrs
    for b in ltrs
    for c in ltrs
    for d in ltrs
    for e in ltrs
    for f in ltrs
]  # aaaaaa -> zzzzzz 26^3
print(len(res))
print(pow(26, 6))

