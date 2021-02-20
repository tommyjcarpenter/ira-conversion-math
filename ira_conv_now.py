def compute(Pr, r, n, year):
    # stolen from https://stackoverflow.com/questions/34952669/how-to-get-python-compound-interest-calculator-to-give-the-correct-answer
    return Pr * (((1 + ((r / 100.0) / n)) ** (n * year)))


# print(f"{r}% growth Trad on {P} AFTER TAX after {y} years is", compute(100000, r, n, y) * (1 - trim))

# it would have cost me 22k to convert to roth
# assuming I dump an additional 22000 in right now

for trim in (0.15, 0.18, 0.19):
    for P in (100000, 200000, 500000):
        for gr in (1, 3, 7, 10, 20):
            y = 25

            # assume we can pay .22*P out of our own pocket now; which we could invest in roth
            TP = P + (0.22 * P)  # ILLEGAL to actually put this in one year though, so this is slightly optimistic
            trad = compute(TP, gr, 1, y) * (1 - trim)
            # original P
            roth = compute(P, gr, 1, y)

            if roth > trad:
                w = roth - trad
                f = int(roth)
                wp = (w / roth) * 100  # win as a percentage of final
                win = "ROTH"
            else:
                w = trad - roth
                f = int(trad)
                wp = (w / trad) * 100
                win = "TRAD"
            print(
                f"{win} WINS by {w} ({wp:0.2}% of {f}) on {P} after {y} years with {gr}% growth, {trim} retirement rate"
            )
