import numpy as np


def prod_non_zero_diag(x):
    d = np.diag(x)
    p = d[d != 0]
    return np.prod(p)
    

def are_multisets_equal(x, y):
    if len(x) != len(y):
        return False
    xs = np.sort(x)
    ys = np.sort(y)
    return np.array_equal(xs, ys)
    

def max_after_zero(x):
    x = np.asarray(x)
    s = x[1:][x[:-1] == 0]
    if len(s) == 0:
        return None
    return s.max()

    

def convert_image(img, coefs):
    img = np.asarray(img)
    coefs = np.asarray(coefs)
    x = img.shape[0]
    y = img.shape[1]
    z = img.shape[2]
    a = (img * coefs).sum(axis=2)
    return a

    

def run_length_encoding(x):
    x = np.asarray(x)
    f = np.ones(len(x), dtype=bool)
    f[1:] = x[1:] != x[:-1]
    a = x[f]
    s = np.diff(np.where(np.append(f, True))[0])
    return a, s
    

def pairwise_distance(x, y):
    x = np.asarray(x)
    y = np.asarray(y)
    n = x.shape[0]
    m = y.shape[0]
    p = x.shape[1]
    r = x[:, None, :] - y[None, :, :]
    a = np.sqrt((r ** 2).sum(axis=2))
    return a
    