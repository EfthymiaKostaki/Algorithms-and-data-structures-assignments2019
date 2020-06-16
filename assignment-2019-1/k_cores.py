import sys


def create_pq():
    return []


def add_last(pq, c):
    pq.append(c)


def extract_last_from_pq(pq):
    return pq.pop()


def has_children(pq, p):
    return 2 * p + 1 < len(pq)


def root(pq):
    return 0


def set_root(pq, c):
    if len(pq) != 0:
        pq[0] = c


def get_data(pq, p):
    return pq[p]


def children(pq, p):
    if 2 * p + 2 < len(pq):
        return [2 * p + 1, 2 * p + 2]
    else:
        return [2 * p + 1]


def parent(p):
    return (p - 1) // 2


def exchange(pq, p1, p2):
    pq[p1], pq[p2] = pq[p2], pq[p1]


def insert_in_pq(pq, pn):
    add_last(pq, pn)
    i = len(pq) - 1
    while i != root(pq) and get_data(pq, i) < get_data(pq, parent(i)):
        p = parent(i)
        exchange(pq, i, p)
        i = p


def update_pq(pq, old, new):
    for n in pq:
       if n == old:
         pq.remove(n)
         insert_in_pq(pq, new)

def extract_min_from_pq(pq):
    c = pq[root(pq)]
    set_root(pq, extract_last_from_pq(pq))
    i = root(pq)
    while has_children(pq, i):
        j = min(children(pq, i), key=lambda x: get_data(pq, x))
        if get_data(pq, i) < get_data(pq, j):
            return c
        exchange(pq, i, j)
        i = j
    return c


def adjacency_list(g, node):
    return g.get(node)


def main():
    #Open file from command line input path of file or file (if in the same folder)
    f = open(sys.argv[1], "r")
    g = {}
    with f as graph_input:
        for line in graph_input:
            nodes = [int(x) for x in line.split()]
            if len(nodes) != 2:
                continue
            if nodes[0] not in g:
                g[nodes[0]] = []
            if nodes[1] not in g:
                g[nodes[1]] = []
            g[nodes[0]].append(nodes[1])
            g[nodes[1]].append(nodes[0])
    mh = create_pq()
    d = {}
    p = {}
    core = {}
    f.close()
    for v in range(len(g)):
        d[v] = len(adjacency_list(g, v))
        p[v] = d[v]
        core[v] = 0
        pn = [p[v], v]
        insert_in_pq(mh, pn)
    while len(mh) > 0:
        t = extract_min_from_pq(mh)
        core[t[1]] = t[0]
        if len(mh) != 0:
            for v in adjacency_list(g, t[1]):
                d[v] = d[v] - 1
                opn = [p[v], v]
                p[v] = max(t[0], d[v])
                npn = [p[v], v]
                update_pq(mh, opn, npn)
    return core


if __name__ == "__main__":
    main()
