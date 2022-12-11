#importing pandas module to handle the csv file
import pandas as pd
#Reading data from the csv file
ReadData = pd.read_csv('BatsmanRanking.csv')
#assigning the variable and get the players name 
players_name = ReadData.Player
#assigning the variable and get the run data
Runs = ReadData.Runs
#using series method get the run difference between each players
Run_Diff = pd.Series(Runs)
#to get the absolute data 
Run_Difference = abs(Run_Diff.diff())
#to remove the NaN data
Run_Difference = Run_Difference.dropna()

#assigning a variable and inserting the output data
Run_file = pd.DataFrame([players_name,Run_Difference])
#to store the datas in each row
Run_file = Run_file.transpose()
#applying the header to the file
column_name=['Player','RunDifference']
#apply all the output datas into the csv file
Run_file.to_csv('RunDifference.csv',index = 0,header=column_name)