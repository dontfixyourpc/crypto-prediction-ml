# Name: crypto-prediction-ml
# Description: Prediction of a possible rate of exchange of a crypto currency to dollar
# Version: 0.0.1
# Author: Rhein Richard


from autots import AutoTS
import pandas as pd

from os import system,name

def clear():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear')
   
def crypto_prediction(crypto, forecast, cryptoName):
   data = pd.read_csv(crypto)   

   model = AutoTS(
      forecast_length= forecast,
      frequency='infer', 
      ensemble='simple', 
      drop_data_older_than_periods= 200)

   model = model.fit(
      data,                    
      date_col='Date',    
      value_col='Close',  
      id_col=None)             


   prediction = model.predict() 
   forecast = prediction.forecast
   print("\n")
   print("Price Prediction for " + cryptoName)
   print(forecast)
   
   

def menu():
   print("Crypto Price Prediction in USD\n")
   print("_______________________________________")

   print("Choose one following crypto currency:\n")
   print("---------------------------------------")
   print("1. Bitcoin ")
   print("2. Ethereum ")
   print("3. Dogecoin ")
   print("---------------------------------------")

   choice = input("Type in your choice: ")
   forecast_str = input("Type your forecast: ")
   forecast_int = int(forecast_str)

   if(choice == '1'):
      crypto = "CSV/coin_Bitcoin.csv"
      cryptoName = "Bitcoin"
   elif(choice == '2'):
      crypto = "CSV/coin_Ethereum.csv"
      cryptoName = "Ethereum"
   elif(choice == '3'):
      crypto = "CSV/coin_Dogecoin.csv"
      cryptoName = "Dogecoin"
   else:
      print("Invalid input.")
      menu()
   crypto_prediction(crypto, forecast_int, cryptoName)

menu()