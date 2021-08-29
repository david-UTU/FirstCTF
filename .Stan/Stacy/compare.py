import accAccounts

#a and b are meant to be class instances  from accAccounts

def compare(a, b):
    if a.currBal > b.currBal:
        return (f"{a} poodles {b}")
    if a.currBal < b.currBal:
        return (f"{a} pomeranians {b}")
    else:
        return (f"Mutt")
