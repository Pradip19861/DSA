def intToRoman(num: int) -> str:
    symList = [
        ["I", 1],
        ["IV", 4],
        ["V", 5],
        ["IX", 9],
        ["X", 10],
        ["XL", 40],
        ["L", 50],
        ["XC", 90],
        ["C", 100],
        ["CD", 400],
        ["D", 500],
        ["CM", 900],
        ["M", 1000]
    ]
    res = ""
    for sym, val in reversed(symList):
        while num >= val:
            res += sym
            num -= val
    return res
print(intToRoman(140000))
