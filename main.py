input_str = input()

# 初始化计数器
letter_count = 0  # 英文字符
digit_count = 0   # 数字
space_count = 0   # 空格
other_count = 0   # 其他字符

for char in input_str:
    # 跳过中文字符
    if '\u4e00' <= char <= '\u9fff':
        continue
        
    # 统计英文字符（大小写均计为1）
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
        letter_count += 1
    # 统计数字
    elif '0' <= char <= '9':
        digit_count += 1
    # 统计空格
    elif char == ' ':
        space_count += 1
    # 统计其他字符
    else:
        other_count += 1

# 按要求格式输出结果
print("英文字符: {}".format(letter_count))
print("数字: {}".format(digit_count))
print("空格: {}".format(space_count))
print("其他字符: {}".format(other_count))
