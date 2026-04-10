from __future__ import annotations


def find_non_injective_pair(mapping: dict) -> tuple | None:
    """Return (x1, x2) where f(x1)==f(x2) and x1!=x2, or None if injective."""
    # === TODO ===
    # Your code here
    mappingDupe = mapping.copy()
    for comparee in mapping:
        #iterates len(mapping) - 1 times
        #comparee = key
        mappingDupe.pop(comparee)
        for compared in mappingDupe:
            #iterates len(mappingDupe) - 1 times
            #mapping dupe is always 1 shorter each iteration of mapping
            
            
    # === END TODO ===


def find_non_surjective_element(mapping: dict, target: set):
    """Return one target element with no input mapping to it, or None if surjective."""
    # === TODO ===
    # Your code here
    pass
    # === END TODO ===

def my_floor(x: float) -> int:
    """Return floor(x) without using math.floor."""
    # === TODO ===
    # Your code here
    return int(x) if x >= 0 else -my_ceil(-x)
    # === END TODO ===


def my_ceil(x: float) -> int:
    """Return ceil(x) without using math.ceil."""
    # === TODO ===
    # Your code here
    #return int(x) if float(int(x)) == x
    #return int(x) if x % 1 == 0.0 else 
    #if float(int(x)) == x: return int(x)
    #return int(x) + 1 if x >= 0 else int(x)
    #return int(x) if float(int(x)) == x or x >= 0 else int(x)
    return int(x) if float(int(x)) == x or x <= 0 else int(x) + 1
    # === END TODO ===
