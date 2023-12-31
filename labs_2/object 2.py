def sierpinskiTriangle(n):
    if n == 0:
        return ["*"]
    else:
        previous = sierpinskiTriangle(n - 1) 
        space = " " * (2 ** (n - 1)) 
        result = [] 
        for line in previous:
            result.append(space + line + space)
        for line in previous:
            result.append(line + " " + line)
        return result

depthOfTriangle = int(input("Введите глубину треугольника Серпинского: \n"))
triangle = sierpinskiTriangle(depthOfTriangle)
for line in triangle:
    print(line)