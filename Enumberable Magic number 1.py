def _all(seq, fun): 
    return all(fun(item) for item in seq)
    