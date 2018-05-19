# Evaluate sum of a Series (Sn) and each of the terms (an)
# until an appears to go to zero (which could be a sign of convergence)
# or until n reaches the specified endpoint
import math


Sn = 0
epsilon = 0.0001  # How close to zero an needs to get
zeroCounter = 0   # zeroCounter will +1 whenever abs(an) < epsilon
zeroCountTo = 30  # How many consecutive times abs(an) needs to be < epsilon

for n in range(0, 100000):    # Range for Series

    an = 1/math.factorial(n)  # Expression for terms of sequence (to be sum'ed)
    Sn += an

    print("at n = {:3},\tan = {:15.12f},\tSn = {:15.12f}"
          .format(n, an, Sn), end="  ")

    if abs(an) < epsilon:
        zeroCounter += 1
        print("an < ε")
        if zeroCounter == zeroCountTo:
            print("\nan appears to -> 0, stopping eval-loop." +
                  "Series *may* be converging!")
            break
    else:
        zeroCounter = 0
        print("")

if an > epsilon:
    print("an is still > ε, this *may* indicate divergence")

print("\n*** evaluating series completed ***")
