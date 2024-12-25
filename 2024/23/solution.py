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
    for c, conns in graph_adj.items():
        
        if len(conns) < 2 or (len(t_conns.union(conns)) == 0 and c not in t_conns):
            continue
        print(c, conns)
        result += 1

    return result

def solve_part_two(input):
    return None
