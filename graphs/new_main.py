s = open("code.txt", "r", encoding="utf-8")
st = s.read()
a = []
b = []
for i in range(len(st)):
    if st[i] not in a:
        a.append(st[i])
        b.append(st.count(st[i]))
c = dict(zip(b, a))
b.sort(reverse=True)
code = []
for i in range(10):
    code.append(c[b[i]])
letters = ['о', 'е', 'а', 'и', 'н', 'т', 'с', 'р', 'в', 'л']
key = dict(zip(code, letters))
key['н'] = 'ы'
key['о'] = 'г'
key['й'] = 'д'
key['э'] = 'ь'
key['в'] = 'ч'
key['я'] = 'п'
key['ш'] = 'з'
key['м'] = 'к'
key['г'] = 'я'
key['з'] = 'м'
key['ю'] = 'й'
key['щ'] = 'у'
key['у'] = 'ю'
key['ц'] = 'щ'
key['с'] = 'х'
key['ф'] = 'б'
key['д'] = 'ш'
key['а'] = 'ж'
key['ч'] = 'ф'
key['р'] = 'ц'
key['ы'] = 'э'
for x in key.keys():
    if x not in code:
        code.append(x)
for y in key.values():
    if y not in letters:
        letters.append(y)
de_key = dict(zip(letters, code))
string = 'вовсехтыдушеньканарядаххороша'
for c in string:
    print(de_key[c], end='')
