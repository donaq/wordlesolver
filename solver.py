alphabet = [c for c in "abcdefghijklmnopqrstuvwxyz"]

def round():
    with open("words") as fp:
        words = [l.strip() for l in fp]

    word = "plant"
    while True:
        sol = input(f"{word}: ")
        greens, yellows, blanks = list(), list(), list()
        exists = {c:0 for c in alphabet}
        for i in range(5):
            c = word[i]
            cres = sol[i]
            if cres == "g":
                greens.append(i)
                exists[c] += 1
            elif cres == "y":
                yellows.append(i)
                exists[c] += 1
            else:
                blanks.append(i)

        for i in greens:
            c = word[i]
            words = [w for w in words if w[i]==c]
        for i in yellows:
            c = word[i]
            words = [w for w in words if c in w and w[i]!=c]
        for i in blanks:
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
