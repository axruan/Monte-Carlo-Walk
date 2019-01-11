# Alex Ruan
# What is the longest walk you can take where you'll be within walking distance of home at least 50% of the time?
# The longest walk is 20 steps.
#
# What is a Monte Carlo simulation? What are they used for? How do they work?
# A Monte Carlo simulation is a technique used to measure the probability and risk of something.
# It is used to forecast models in things like stocks.
# According to palisade.com, "[A] Monte Carlo simulation performs risk analysis by building
# models of possible results by "substituting a range of values—a probability distribution—for
# any factor that has inherent uncertainty"
import random as r

l = [-2, -1, 0, 1, 2]
dart = 0
amt = 100


def throwdart(times):
    global dart
    for i in range(0, times):
        x = r.choice(l)
        y = r.choice(l)

        if abs(0 - x) + abs(0 - y) <= 2:
            dart += 1


def calculate(thrown):
    global dart
    dart = (dart * 4)/thrown
    print(dart)


throwdart(amt)
calculate(amt)
throwdart(amt*10)
calculate(amt*10)
throwdart(amt*100)
calculate(amt*100)
throwdart(amt*1000)
calculate(amt*1000)

# The outputs are all around 2.0

