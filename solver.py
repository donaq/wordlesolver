def round():
    with open("words") as fp:
        words = [l.strip() for l in fp]

    word = "plant"
    while True:
        sol = input(f"{word}: ")
        for i in range(5):
            c = word[i]
            cres = sol[i]
            if cres == "g":
                words = [w for w in words if w[i] == c]
                continue
            if cres == "y":
                words = [w for w in words if c in w]
                continue
            words = [w for w in words if c not in w]
        word = words[0]
        if len(words) == 1:
            print(f"{words[0]} is the solution")
            break

round()
