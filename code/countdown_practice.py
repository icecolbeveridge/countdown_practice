### Countdown practice game

import random
import collections
import itertools

def draw_tiles(large = None, small = None):
    """Pull six tiles from the bag"""
    
    if large is None and small is None:
        large = random.choice([0,1,2,3,4])
        small = 6 - large
    elif large is None: 
        large = 6 - small
    elif small is None:
        small = 6 - large
    
    if large < 0 or small < 0 or large+small != 6:
        raise ValueError("Large and small ")
    
    SMALL = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
    LARGE = [25,50,75,100]
    
    random.shuffle(SMALL)
    random.shuffle(LARGE)
    
    tiles = LARGE[:large] + SMALL[:small]
    return tiles

def make_target():
    return int(random.random()*900 + 100)

def _add(a,b):
    return a+b, f"{a} + {b} = {a+b}"

def _mul(a,b):
    return a*b, f"{a} * {b} = {a*b}"
    
def _sub(a,b):
    M = max(a,b); m = min(a,b)
    return M-m, f"{M} - {m} = {M-m}"

def _div(a,b):
    M = max(a,b); m = min(a,b)
    if m>0 and M % m == 0:
        return M // m, f"{M} / {m} = {M//m}"
    else:
        return None, None

def all_possible_binary_sums(tiles):
    """All of the possible ways to combine two tiles. Keep the sums that get there, too."""
    # tiles is a sorted tuple
    
    out = []
    for i, j in itertools.combinations(range(len(tiles)),2): 
        # have to do this index-wise to generate 'rest'
        # this section is smelly.
        rest = [t for k,t in enumerate(tiles) if k not in (i,j)]
        si = tiles[i]
        sj = tiles[j]
        for f in [_add, _mul, _div, _sub]:
            res, cal = f(si,sj)
            if res is not None:
                temp_tiles = [res]+rest
                temp_tiles.sort()
                out.append( (tuple(temp_tiles), cal))
    return out
            
        
def is_anagram(a,b):
    ai = a.split(";")
    bi = b.split(";")
    ai.sort(); bi.sort()
    z = zip(ai,bi)
    return all( [i[0] == i[1] for i in z])
    
def remove_anagrams(solutions):
    out = []
    while solutions:
        x = solutions.pop()
        to_add = True
        for i in out:
            if is_anagram(x,i):
                to_add = False
                continue
        if to_add:
            out.append(x)
    return out
                
def pretty(s):
    return s.replace(";", "\n")


def solve_numbers_game(target, tiles):
    """Recursively work through all possible Countdown sums, keep answers"""
    # workings has as its key a frozenset of tiles, and all of the ways to reach that set as values.
    out = []
    tiles.sort()
    workings = collections.defaultdict(list) 
    workings[tuple(tiles)] = [""]
    
    while workings:
        t, w = workings.popitem()
        if len(t) >= 2:        
            apb = all_possible_binary_sums(t)
            for si, wi in apb:
                if target in si:
                    for wj in w:
                        out.append(f"{wj}; {wi}")
                else:
                    for wj in w:
                        workings[si].append(f"{wj}; {wi}")
                    
    # some of the outputs can be morally the same -- effectively anagrams of each other.
    out = remove_anagrams(out)
    out = [pretty(i) for i in out]  
    return out    

def play_numbers_game(n = None):

    while n is None:

        try: 
            n = input("How many large numbers would you like? [0-4] ")
            tiles = draw_tiles(large = int(n))
        except:
            pass
    target = make_target()
    nice_tiles = ', '.join([str(t) for t in tiles[:-1]]) + f" and {tiles[-1]}"

    print (f"Your numbers are {nice_tiles}")
    print (f"And your target is {target}")
    return target, tiles
    
def play():
    target, tiles = play_numbers_game()
    out = solve_numbers_game(target,tiles)
    input (f"Press return to see {len(out)} solutions.")
    print ("\n***\n".join(out)               )