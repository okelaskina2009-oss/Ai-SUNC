import math


def prod_non_zero_diag(x):
    p = 1
    n = min(len(x), len(x[0])) 
    for i in range(n):
        if x[i][i] != 0:
            p = p *  x[i][i]
    return p



def are_multisets_equal(x, y):
    if len(x) != len(y):
        return False
    xs = sorted(x)
    ys = sorted(y)
    for i in range(len(xs)):
        if xs[i] != ys[i]:
            return False
    return True



def max_after_zero(x):
    s = None
    for i in range(1, len(x)):
        if x[i-1] == 0:
            if s is None or x[i] > s:
                s = x[i]
    return s



def convert_image(img, coefs):
    x = len(img)
    y = len(img[0])
    z = len(coefs)
    a = []
    for i in range(x):
        b = []
        for j in range(y):
            s = 0
            for l in range(z):
                s = s + img[i][j][l] * coefs[l]
            b.append(s)
        a.append(b)
    return a



def run_length_encoding(x):
    a = []
    s = []
    f = None
    for i in x:
        if i == f:
            s[-1] = s[-1] + 1
        else:
            a.append(i)
            s.append(1)
            f = i
    return a, s



def pairwise_distance(x, y):
    n = len(x)
    m = len(y)
    p = len(x[0])
    a = []
    for i in range(n):
        b = []
        for j in range(m):
            s = 0
            for l in range(p):
                 s = s + (x[i][l] - y[j][l]) * (x[i][l] - y[j][l])
            b.append(math.sqrt(s))
        a.append(b)
    return a

