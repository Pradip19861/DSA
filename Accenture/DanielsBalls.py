def danielsballs(input1,  input2, input3):
    e = input2 / input3
    Rebound = input1 * pow(e,2)
    return round (Rebound)
input1 = 5
input2 = 10
input3 = 20
print(danielsballs(input1, input2, input3))