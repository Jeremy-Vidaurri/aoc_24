# Advent of Code 2024 - Day 23
def make_graph(connections):
    adj = {}
    for comp1, comp2 in connections:
        if comp1 not in adj:
            adj[comp1] = set()
        if comp2 not in adj:
            adj[comp2] = set()

        adj[comp1].add(comp2)
        adj[comp2].add(comp1)
    return adj

def solve_part_one(input):
    connections = [line.strip().split('-') for line in input if line != ""]
    graph_adj = make_graph(connections)
    result = 0
    t_conns = set(['ta','tb','tc','td','te','tf','tg','th','ti','tj','tk','tl','tm','tn','to','tp','tq','tr','ts','tt','tu','tv','tw','tx','ty','tz',])
    seen = set()
    
    for c, conns in graph_adj.items():
        if len(conns) < 2 or c not in t_conns:
            continue
        for c2 in conns:
            for c3 in conns:
                if c2 == c3 or c2 not in graph_adj[c3] or (c, c2, c3) in seen:
                    continue
                result += 1
                seen.add((c, c2, c3))
                seen.add((c, c3, c2))
                seen.add((c2, c, c3))
                seen.add((c2, c3, c))
                seen.add((c3, c, c2))
                seen.add((c3, c2, c))
    return result

def bron_kerbosch(R, P, X, graph):
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from bron_kerbosch(
            R.union({v}),
            P.intersection(graph[v]),
            X.intersection(graph[v]),
            graph
        )
        X.add(v)

def solve_part_two(input):
    connections = [line.strip().split('-') for line in input if line != ""]
    graph_adj = make_graph(connections)
    all_cliques = list(bron_kerbosch(set(), set(graph_adj.keys()), set(), graph_adj))
    max_clique_size = max(len(clique) for clique in all_cliques)
    result = ''.join([','.join(sorted(clique)) for clique in all_cliques if len(clique) == max_clique_size])

    return result
