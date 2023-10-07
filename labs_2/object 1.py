def pascal_triangle(n):
    triangle = [[1], [1,1]]
    for i in range(2, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle [i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
rows_number = int(input('Введите число: '))
triangle = pascal_triangle(rows_number)
for row in triangle:
    print(' '.join(map(str, row)).center(rows_number*2 + 1))

