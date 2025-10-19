s = input()
letters = 0
digits = 0
spaces = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isdigit():
        digits += 1
    elif c == ' ':
        spaces += 1
    elif '\u4e00' <= c <= '\u9fa5':
        continue
    else:
        others += 1
print(f"英文字符: {letters}")
print(f"数字: {digits}")
print(f"空格: {spaces}")
print(f"其他字符: {others}")
