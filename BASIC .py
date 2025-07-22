
#--IMPORTING ALL THE REQUIRED LIBRARIES------------------------------------------------------------------  

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

#--Load CSV file (replace filename as needed)-------------------------------------------------------------

df = pd.read_csv("option-chain-ED-NIFTY-10-Jul-2025.csv")
print(df.to_string()) 

#--REMOVING ALL COMMAS -----------------------------------------------------------------------------------

df = df.replace(',', '', regex=True)
df = df.apply(pd.to_numeric, errors='coerce')


#--converting all data of column into numeric form ------------------------------------------------------

cols = ['CALL_OI', 'CALL_CHNG IN OI', 'CALL_VOLUME', 'CALL_IV', 'CALL_LTP', 'CALL_CHNG', 'CALL_BID QTY', 'CALL_BID', 'CALL_ASK', 'CALL_ASK QTY', 'STRIKE', 'PUT_BID QTY', 'PUT-BID', 'PUT_ASK', 'PUT_ASK QTY', 'PUT_CHNG', 'PUT_LTP', 'PUT_IV', 'PUT_VOLUME', 'PUT_CHNG IN OI', 'PUT_OI']

for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')


#--DISPLAYING THE STRIKE v/s CALL_OI---------------------------------------------------------------------

A = df['STRIKE']
B = df['CALL_OI']


xpoints = np.array(A)
ypoints = np.array(B)

plt.title("STRIKE V/S CALL_OI")
plt.xlabel("STRIKE")
plt.ylabel("CALL_OI")

plt.bar(xpoints, ypoints)
plt.show()


#--DISPLAYING THE STRIKE v/s PUT_OI-----------------------------------------------------------------------

C = df['PUT_OI']

plt.figure(figsize=(10,6))
plt.bar(A, C, color='red', alpha=0.6)
plt.title("STRIKE V/S PUT_OI")
plt.xlabel("STRIKE")
plt.ylabel("PUT_OI")
plt.grid(True)
plt.show()

#--DISPLAYING THE STRIKE v/s CHANGE IN CALL_OI------------------------------------------------------------

D = df['CALL_CHNG IN OI']

plt.figure(figsize=(10,6))
plt.bar(A, D, color='cyan', alpha=0.6)
plt.title("STRIKE V/S CHANGE IN CALL_OI")
plt.xlabel("STRIKE")
plt.ylabel("CHANGE IN CALL_OI")
plt.grid(True)
plt.show()

#--DISPLAYING THE STRIKE v/s CHANGE IN PUT_OI--------------------------------------------------------------

E = df['PUT_CHNG IN OI']

plt.figure(figsize=(10,6))
plt.bar(A, E, color='magenta', alpha=0.6)
plt.title("STRIKE V/S CHANGE IN PUT_OI")
plt.xlabel("STRIKE")
plt.ylabel("CHANGE IN PUT_OI")
plt.grid(True)
plt.show()

#--CALCULATE AND PLOT PUT-CALL RATIO (PCR) v/s STRIKE-------------------------------------------------------

# Avoid division by zero by replacing zero Call OI with small number

call_oi_nonzero = df['CALL_OI'].replace(0, 0.01)
pcr = df['PUT_OI'] / call_oi_nonzero

plt.figure(figsize=(10,6))
plt.plot(A, pcr, marker='o', linestyle='-', color='purple')
plt.title("STRIKE V/S PUT-CALL RATIO (PCR)")
plt.xlabel("STRIKE")
plt.ylabel("PUT-CALL RATIO (PCR)")
plt.grid(True)
plt.show()

#--DISPLAYING THE STRIKE v/s IMPLIED VOLATILITY (CALL_IV and PUT_IV)------------------------------------------

plt.figure(figsize=(10,6))
plt.bar(A, df['CALL_IV'], label='CALL_IV', color='blue')
plt.bar(A, df['PUT_IV'], label='PUT_IV', color='red')
plt.title("STRIKE V/S IMPLIED VOLATILITY")
plt.xlabel("STRIKE")
plt.ylabel("IMPLIED VOLATILITY")
plt.legend()
plt.grid(True)
plt.show()

#--DISPLAYING THE STRIKE v/s VOLUME (CALL_VOLUME and PUT_VOLUME)------------------------------------------------

# Offset by 5 for better visibility

plt.figure(figsize=(10,6))
plt.bar(A - 5, df['CALL_VOLUME'], width=10, alpha=0.6, label='CALL_VOLUME', color='blue')

 # Offset by 5 for better visibility
 
plt.bar(A + 5, df['PUT_VOLUME'], width=10, alpha=0.6, label='PUT_VOLUME', color='red')  
plt.title("STRIKE V/S VOLUME")
plt.xlabel("STRIKE")
plt.ylabel("VOLUME")
plt.legend()
plt.grid(True)
plt.show()
