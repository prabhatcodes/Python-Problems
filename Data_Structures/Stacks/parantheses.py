from Data_Structures.Stacks.ArrayStack import ArrayStack


def is_matched(expr):
    """Return true if all delimiters match properly, else false"""
    lefty: str = "({[" # opening delimiters
    righto = ")}]" # respective closing delimiters
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c) # push left delimiter on stack
        elif c in righto:
            if S.is_empty():
                return False # nothing to match with
            if righto.index(c) != lefty.index(S.pop()):
                return False # mismatched
        return S.is_empty() # Were all symbols matched