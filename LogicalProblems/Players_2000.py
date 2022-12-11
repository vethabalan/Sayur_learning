#importing pandas module
import pandas as pd 
#importing numpy module
import numpy as np
# importing csv module
import csv
#to read the data using pandas
ReadData = pd.read_csv("BatsmanRanking.csv")
#assigning the variable and get the players name 
players_name = ReadData.Player

#assigning the variable and get the Span data
Players_Span = ReadData.Span
#getting the players played in the year 2000
Players_Span = np.where(ReadData['Span'].str.contains('2000'),ReadData.Span,None)

# gathering all the data into a variable
Output_File = pd.DataFrame([players_name,Players_Span])
#transposing all the rows into columns
Output_File = Output_File.transpose()
#applying headers
header = ['player Name','Span']
#writing the datas to the new csv file
Output_File.to_csv('Span2000.csv',header=header)

