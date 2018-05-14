# Evaluate sum of a Series (Sn) and each of the terms (an)
# until an appears to go to zero (which could be a sign of convergence)
# or until n reaches the specified endpoint
import math


Sn = 0
zeroCounter = 0  # zeroCounter will +1 whenever an < epsylon
epsylon = 0.0001

# Common series: Σ x^n / n!  range(0,infty)  = e^x
# Σ (-1)^n * x^(2n+1)/(2n+1)! range(0,infty) = sin x

for n in range(1, 100000):

    an = 1/(2**n - 3*n**2)
    Sn += an

    print("at n = {:3},\tan = {:15.12f},\tSn = {:15.12f}"
          .format(n, an, Sn), end="  ")

    if abs(an) < epsylon:
        zeroCounter += 1
        print("an < ε")
        if zeroCounter == 30:
            print("\nan appears to -> 0, stopping eval-loop." +
                  "Series *may* be converging!")
            break
    else:
        print("")

if an > epsylon:
    print("an is still > ε, this may indicate that the series diverges")

print("\n*** evaluating series completed ***")
