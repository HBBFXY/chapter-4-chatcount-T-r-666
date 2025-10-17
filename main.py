
input_str = input()
# 初始化计数器
letter_count = 0  
digit_count = 0   
space_count = 0   
other_count = 0 
for char in input_str:
    if '\u4e00' <= char <= '\u9fff':
        continue
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
        letter_count += 1
    elif '0' <= char <= '9':
        digit_count += 1
    elif char == ' ':
        space_count += 1
    else:
        other_count += 1
print("英文字符: {}".format(letter_count))
print("数字: {}".format(digit_count))
print("空格: {}".format(space_count))
print("其他字符: {}".format(other_count))
