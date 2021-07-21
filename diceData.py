import plotly.figure_factory as ff
import random
import statistics

dice_result = []
for i in range(0, 1000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_result.append(dice1 + dice2)

#calculating the mean and the standard deviation
mean = sum(dice_result)/len(dice_result)
median = statistics.median(dice_result)
mode= statistics.mode(dice_result)
std_deviation = statistics.stdev(dice_result)


#finding the start and end values for first std_deviation ,second std_deviation,third std_deviation
first_std_deviation_start,first_std_deviation_end=mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end=mean-(3*std_deviation),mean+(3*std_deviation)

fig= ff.create_distplot([dice_result],["Result"],show_hist=False)
fig.show()

#printing and calculating the % of data that lies in 1st stdm 2nd std and 3rd std
list_of_data_within_1_std_deviation = [result for result in dice_result if result > first_std_deviation_start and result< first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in dice_result if result > second_std_deviation_start and result< second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in dice_result if result > third_std_deviation_start and result< third_std_deviation_end]


print("Mean of this data is {}: ".format(mean))
print("Median of this data is {}: ".format(median))
print("Mode of this data is {}: ".format(mode))
print("standard deviation of this data is {}: ".format(std_deviation))
print("{}% of data lies within first std_deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(dice_result)))
print("{}% of data lies within second std_deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(dice_result)))
print("{}% of data lies within third std_deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(dice_result)))

