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

def all_possible_binary_sums(tiles):
    """All of the possible ways to combine two tiles. Keep the sums that get there, too."""
    # tiles is a sorted tuple
    
    out = []
    for i, j in itertools.combinations(range(len(tiles)),2): 
        # have to do this index-wise to generate 'rest'
        rest = [t for k,t in enumerate(tiles) if k not in (i,j)]
        si = tiles[i]
        sj = tiles[j]
        mi = max(si ,sj)
        mj = min(si, sj)
        # add
        a = si + sj
        ta = [a] + rest
        ta.sort()
        out.append(( tuple(ta), f"{si} + {sj} = {a}"))
        # sub
        s = mi - mj
        ts = [s] + rest
        ts.sort()
        out.append(( tuple(ts), f"{mi} - {mj} = {s}"))
        # mul
        m = si * sj
        tm = [m] + rest
        tm.sort()
        out.append(( tuple(tm), f"{si} * {sj} = {m}"))
        # div
        if mj > 0 and mi % mj == 0:
            d = mi // mj
            td = [d] + rest
            td.sort()
            out.append(( tuple(td), f"{mi} / {mj} = {d}"))
    return out
            
        

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
                    out.append(f"{wj}; {wi}")
                else:
                    for wj in w:
                        workings[si].append(f"{wj}; {wi}")
                    
        
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
            