#importing pandas module to handle the csv file
import pandas as pd
#import numpy
import numpy as np

#Reading data from the csv file
ReadData = pd.read_csv('BatsmanRanking.csv')
# print(ReadData)

#assigning the variable and get the players name 
players_name = ReadData.Player
# print(players_name)

# #assigning the variable and get the run data
Highest_Run = ReadData.HS
# print(Highest_Run)

Not_Out_Index =  np.where(ReadData['HS'].str.endswith('*'),ReadData.HS,None)

# #assigning all the data to a variable
Output_File = pd.DataFrame([players_name,Not_Out_Index])
# #transposing all the row into columns
Output_File = Output_File.transpose()
# #fixing header names
Headers = ['player Name' , 'High Score *']
# #moving all the datas into csv file
Output_File.to_csv('NotOut.csv',index=0,header=Headers)