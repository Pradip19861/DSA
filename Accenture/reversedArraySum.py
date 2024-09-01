def reversedarraysum(input_str: str) -> int:
    input_list = list(map(int, input_str.split(',')))
    res = 0
    for i in range(len(input_list)):
        if i % 2 == 0:
            res += input_list[i]
    return res
print(reversedarraysum("10,20,30,40,50"))