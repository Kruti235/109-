import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics

dice_result = []


for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)
  
mean  = sum(dice_result)/len(dice_result)
print("mean of this data is {} ".format(mean))

median = statistics.median(dice_result)
print("median of this data is {} ".format(median))

mode= statistics.mode(dice_result)
print("mode of this data is {} ".format(mode))

std_deviation = statistics.stdev(dice_result)
print("stdev : {}".format(std_deviation) )


fig = ff.create_distplot([dice_result],["Result"], show_hist= False)
fig.show()
fig.show()