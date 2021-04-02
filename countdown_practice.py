### Countdown practice game

import random
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
    """Target needs to be betweeen 100 and 999, inclusive"""
    return int(random.random()*900 + 100)

def play_numbers_game():
    """Practice your Countdown numbers game skills."""
    n = None
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
            
