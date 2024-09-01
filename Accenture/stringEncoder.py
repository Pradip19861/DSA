def stringEncoder(input1, input2):
    result = []
    for word in input1:
        first_char = word[0]
        middle_char = word[len(word) // 2]
        last_char = word[-1]
        temp = first_char + middle_char + last_char
        saver = temp * input2
        result.append(saver)
    return result

input1 = ["AbC"]
input2 = 2
print(stringEncoder(input1, input2)) 

input1 = ["world", "hello", "madam"]
input2 = 3
print(stringEncoder(input1, input2))