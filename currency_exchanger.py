#Importing necessary libraries 
import datetime as dt

#Defining a function that converts currencies to US Dollars
#This is a test
def currency_converter(amount, exchange_rate):
	"""Converts US dollars to other currencies."""
	value = amount * exchange_rate
	return value

#Creating a dictionary with the exchange rates to US Dollars
exchange_rate = {'yen':0.0091, 'pound':1.30, 'yuan':0.25}

#Asking users to input currency and amount to convert
currency = input ("Which currency would you like to exchange? ")
amountToConvert = input ("How much would you like to exchange? ")

#Creating a for loop and calling the function
for key in exchange_rate:
	if key == currency:
		converted_amount = currency_converter(int(amountToConvert), exchange_rate[currency])
		print ("\n************************************************************************************")
		print ("\nAs per today's date " + str(dt.date.today()) + ", exchange rate for 1 US Dollar is equal to " + str(exchange_rate[currency]) 
		+ " " + currency.title() + ".")
		print ("You will be receiving " + str(converted_amount) + " " + currency.title() + ".")
