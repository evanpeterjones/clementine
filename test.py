def inc(n):
    return (n + 1)

def our_map(fn, coll):
    def inner(c, v):
        c.append(fn(v))
        return c

    reduce(inner, coll)

our_list = [1, 2, 3]
s = map(inc, our_list)
list(s)
