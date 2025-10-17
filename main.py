input_str = input()

letter_count = 0  # 英文字符计数器
digit_count = 0   # 数字计数器
space_count = 0   # 空格计数器
other_count = 0   # 其他字符计数器（不含中文）

for char in input_str:
    # 检查是否为中文字符，如果是则跳过统计
    if '\u4e00' <= char <= '\u9fff':
        continue
    
    # 严格判断英文字母（a-z 或 A-Z）
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
        letter_count += 1
    # 严格判断数字（0-9）
    elif '0' <= char <= '9':
        digit_count += 1
    # 严格判断空格（仅普通空格）
    elif char == ' ':
        space_count += 1
    # 其他非中文字符
    else:
        other_count += 1

print("英文字符: {}".format(letter_count))
print("数字: {}".format(digit_count))
print("空格: {}".format(space_count))
print("其他字符: {}".format(other_count))
