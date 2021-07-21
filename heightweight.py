import pandas as pd
import statistics
import csv

df=pd.read_csv("data.csv")
height_list=df["Height(Inches)"].to_list()
weight_list=df["Weight(Pounds)"].to_list()

height_mean=statistics.mean(height_list)
height_median=statistics.median(height_list)
height_mode=statistics.mode(height_list)

weight_mean=statistics.mean(weight_list)
weight_median=statistics.median(weight_list)
weight_mode=statistics.mode(weight_list)

height_std_deviation=statistics.stdev(height_list)
weight_std_deviation=statistics.stdev(weight_list)

height_first_std_deviation_start,height_first_std_deviation_end=height_mean-height_std_deviation,height_mean+height_std_deviation
height_second_std_deviation_start,height_second_std_deviation_end=height_mean-(2*height_std_deviation),height_mean+(2*height_std_deviation)
height_third_std_deviation_start,height_third_std_deviation_end=height_mean-(3*height_std_deviation),height_mean+(3*height_std_deviation)


#printing and calculating the % of data that lies in 1st stdm 2nd std and 3rd std
list_of_height_within_1_std_deviation = [result for result in height_list if result > height_first_std_deviation_start and result< height_first_std_deviation_end]
list_of_height_within_2_std_deviation = [result for result in height_list if result > height_second_std_deviation_start and result< height_second_std_deviation_end]
list_of_height_within_3_std_deviation = [result for result in height_list if result > height_third_std_deviation_start and result< height_third_std_deviation_end]


#WEIGHT weight
weight_first_std_deviation_start,weight_first_std_deviation_end=weight_mean-weight_std_deviation,weight_mean+weight_std_deviation
weight_second_std_deviation_start,weight_second_std_deviation_end=weight_mean-(2*weight_std_deviation),weight_mean+(2*weight_std_deviation)
weight_third_std_deviation_start,weight_third_std_deviation_end=weight_mean-(3*weight_std_deviation),weight_mean+(3*weight_std_deviation)


#printing and calculating the % of data that lies in 1st stdm 2nd std and 3rd std
list_of_weight_within_1_std_deviation = [result for result in weight_list if result > weight_first_std_deviation_start and result< weight_first_std_deviation_end]
list_of_weight_within_2_std_deviation = [result for result in weight_list if result > weight_second_std_deviation_start and result< weight_second_std_deviation_end]
list_of_weight_within_3_std_deviation = [result for result in weight_list if result > weight_third_std_deviation_start and result< weight_third_std_deviation_end]

print("Mean of height is {}: ".format(height_mean))
print("Median of height is {}: ".format(height_median))
print("Mode of height is {}: ".format(height_mode))
print("standard deviation of height is {}: ".format(height_std_deviation))
print("{}% of height data lies within first std_deviation".format(len(list_of_height_within_1_std_deviation)*100.0/len(height_list)))
print("{}% of height data lies within second std_deviation".format(len(list_of_height_within_2_std_deviation)*100.0/len(height_list)))
print("{}% of height data lies within third std_deviation".format(len(list_of_height_within_3_std_deviation)*100.0/len(height_list)))

print("Mean of weight is {}: ".format(weight_mean))
print("Median of weight is {}: ".format(weight_median))
print("Mode of weight is {}: ".format(weight_mode))
print("standard deviation of weight is {}: ".format(weight_std_deviation))
print("{}% of weight data lies within first std_deviation".format(len(list_of_weight_within_1_std_deviation)*100.0/len(weight_list)))
print("{}% of weight data lies within second std_deviation".format(len(list_of_weight_within_2_std_deviation)*100.0/len(weight_list)))
print("{}% of weight data lies within third std_deviation".format(len(list_of_weight_within_3_std_deviation)*100.0/len(weight_list)))



