def array1(a):
    for i in range(0, len(a) // 2, 2):
        for k in range(2):
            for j in range(i, i + 2):
                print(a[j])
            a = a[::-1]

def array2(a):
    return max([a.count(i) for i in a])

def array3(a, b):
    return sorted(a + b)

def array4(a):
    for i in range(1, len(a), 2):
        a[i] *= 3

def matrix1(a, k):
    a[k] = list([0] * len(a[k]))
    a[k + 1:] = a[k:]

def matrix2(a):
    for j in range(len(a)):
        for i in range(j, len(a) - j):
            a[i][j] = 0

def string1(s, s2):
    return s.count(s2)

def string2(s):
    return s.replace(' ', '.')