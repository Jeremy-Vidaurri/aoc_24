# Advent of Code 2024 - Day 19

class TrieNode():
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert_pattern(self, pattern):
        cur = self.root
        for char in pattern:
            i = ord(char) - ord('a')
            if not cur.children[i]:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.isEnd = True

    def find_pattern(self, pattern):
        cur = self.root

        for char in pattern:
            i = ord(char) - ord('a')
            if not cur.children[i]:
                return False
            cur = cur.children[i]
        return cur.isEnd

def parse_input(input):
    patterns = []
    designs = []
    for line in input:
        line = line.strip()
        if line == '':
            continue
        if ',' in line:
            patterns = line.split(', ')
        else:
            designs.append(line)

    return patterns, designs

def make_trie(patterns):
    trie = Trie()
    for pattern in patterns:
        trie.insert_pattern(pattern)
    return trie

def recursive_solve(design, pattern_trie:Trie):
    if len(design) == 0:
        return True
   #print(design)
    start_idx = 0
    end_idx = start_idx + 1
    while end_idx <= len(design):
        if pattern_trie.find_pattern(design[start_idx:end_idx]) and recursive_solve(design[end_idx:], pattern_trie):
                return True
        end_idx += 1
    #print(design)
    return False

def solve_part_one(input):
    patterns, designs = parse_input(input)
    pattern_trie = make_trie(patterns)
    result = 0
    for design in designs:
        if recursive_solve(design, pattern_trie):
            #print(design)
            result += 1

    print(result)

    return None

def solve_part_two(input):
    return None
