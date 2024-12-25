# Advent of Code 2024 - Day 22

def next_secret(secret):
    secret = ((secret*64) ^ secret) % 16777216
    secret = ((secret//32) ^ secret) % 16777216
    secret = ((secret*2048) ^ secret) % 16777216
    return secret

def solve_part_one(input):
    secrets = [int(line.strip()) for line in input if line != '']
    for i in range(len(secrets)):
        for _ in range(2000):
            secrets[i] = next_secret(secrets[i])
    return sum(secrets)

def get_best(deltas, secrets):
    best_map = {}

    for i in range(3,len(deltas)):
        first = deltas[i-3]
        second = deltas[i-2]
        third = deltas[i-1]
        fourth = deltas[i]
        if (first, second, third, fourth) in best_map:
            continue

        best_map[(first, second, third, fourth)] = secrets[i]
    return best_map

def solve_part_two(input):
    secrets = [[int(line.strip())] for line in input if line != '']
    deltas = [[0] for _ in range(len(secrets))]

    for i in range(len(secrets)):
        for j in range(2000):
            secrets[i].append(next_secret(secrets[i][j]))

    trunc_secrets = [[secret % 10 for secret in buyer] for buyer in secrets]
    deltas = [[0] for _ in range(len(secrets))]
    for buyer in range(len(secrets)):
        for i in range(1, len(secrets[buyer])):
            deltas[buyer].append(trunc_secrets[buyer][i] - trunc_secrets[buyer][i-1])
    
    mappings = []
    for i in range(len(deltas)):
        mappings.append(get_best(deltas[i], trunc_secrets[i]))
    keys = set()
    for m in mappings:
        for k in m.keys():
            keys.add(k)
    result = 0
    for key in keys:
        result = max(result, sum([m[key] for m in mappings if key in m]))

    print(result)


    return None
