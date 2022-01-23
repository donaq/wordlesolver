import random

alphabet = [c for c in "abcdefghijklmnopqrstuvwxyz"]

def round():
    with open("words") as fp:
        words = [l.strip() for l in fp]

    word = words[0]
    while True:
        sol = input(f"{word}: ")
        positions = {s:list() for s in ['g', 'y', '-']}
        exists = {c:0 for c in alphabet}
        for i in range(5):
            c = word[i]
            cres = sol[i]
            positions[cres].append(i)
            if cres in ("g", 'y'):
                exists[c] += 1

        for i in positions['g']:
            c = word[i]
            words = [w for w in words if w[i]==c]
        for i in positions['y']:
            c = word[i]
            words = [w for w in words if c in w and w[i]!=c]
        for i in positions['-']:
            c = word[i]
            maxc = exists[c]
            if maxc==0:
                words = [w for w in words if c not in w]
            else:
                words = [w for w in words if w.count(c)==maxc]

        word = words[0]

        if len(words) == 1:
            print(f"{words[0]} is the solution")
            break

round()
