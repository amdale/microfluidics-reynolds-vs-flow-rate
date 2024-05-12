# -*- coding: utf-8 -*-
"""
Calculates Reynold's number for a series of flow rates 
Outputs flow rate vs Re as dataframe and saves as .csv
Outputs line graph of flow rate vs Re and saves as .png

Created on Wed May  8 20:53:49 2024

@author: pyatr
"""

# Imports # 
import pandas as pd 
import matplotlib.pyplot as plt

df_output = pd.DataFrame(columns=["Q ul/ml","Re"]) #Empty dataframe for .csv output

# Adjust printing and saving options # 
out_format = 1 # 0 = lists of Re and Q, 1 = data frame #
save_csv = 1 # saves output as .csv 0 = no, 1 = yes #
save_png = 1 # saves plot as .png 0 = no, 1 = yes #
name = 'testoid' # define name for .csv and .png

# What flow rates to display Re for #
rates = range(0, 650, 50) # range(min flow rate, max flow rate+1 interval, intervals)

# Input #

viscosity_cP = 1
viscosity_Pa_s = viscosity_cP/1000 # converts viscosity to Pa/s 

channel_height_um = 25
channel_width_um = 35
Dh_m = ((2*channel_height_um*channel_width_um)/(channel_height_um+channel_width_um))/1000000 # calculates hydraulic diamter in um

density_kg_m3 = 1000

# Velocity + Re calculations # 

for i in rates: 
    
    flow_rate_ul_min = i
    
    # Calculate velocity #
    
    velocity_m_s = (((flow_rate_ul_min*1000000000)/60)/(channel_height_um*channel_width_um))/1000000 # calculates velocity in m/s
    
    # Calculates Reynold's number #
    Re = (2*velocity_m_s*Dh_m*density_kg_m3)/(3*viscosity_Pa_s)
    df_output.loc[len(df_output)] = [i, Re] # Adds iteration to data frame # 
    
    if out_format == 0: # Prints list of Re, good for copying over quickly # 
        print(Re)
        
if out_format == 0: # Prints list of Q, good for copying over quickly # 
    print('\nFlow rates\n')
    for a in rates:
        print(a)

if out_format == 1: # Prints data frame of Q and Re, clear but harder to copy. Not an issue if saving csv anyway # 
    print(df_output.to_string(index=False))
    
if save_csv == 1: # outputs csv of defined name to script folder # 
    df_output.to_csv(name + '.csv', index=False) 
    
######################################## GRAPH ######################################################

graph_data = pd.read_csv(name + '.csv', index_col=0) # loads the csv #
graph_data.plot() # makes plot of Q vs Re # 
plt.ylabel("Re") # adds y axis title to plot #
plt.title("Flow rate vs Reynold's number") # adds title to plot #
if save_png == 1: # saves plot as png #
    plt.savefig(name + '.png') 
