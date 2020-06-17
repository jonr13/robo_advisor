import requests
import json
import pandas as pd
from dotenv import load_dotenv
import os


load_dotenv() #> loads contents of the .env file into the script's environment
key = os.getenv("api_key")


#Function: check if Stock symbol is valid
def valid_symb_number(stk_symb):
    validity = 0
    number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for letter in stk_symb:
        if len(stk_symb) > 4 or len(stk_symb) < 4:
            validity += 1
        elif letter in number_list:
            validity += 1
        else:
            pass
        return validity


#prompt the user to input one stock or cryptocurrency (ex. "MSFT" or "AAPL")
#allow the user to specify multiple sybmbols in the same request
#Peform validations on user inputs - ensure characterlength for stock symbols - ensure characters are not numeric

symb_list = []
print("Hello, to being please follow the instructions below:")
print("                                                    ")

def enter_ticker():
    while True:
        prompt = "Please enter the ticker symbols of the companies you wish to research (ex. 'MSFT')\nWe'll keep adding more symbols until you're finished. When you're finished, type 'Done'.\n Type Here: "
        stk_symb = input(prompt)
        if stk_symb == "Done" or stk_symb =="done" or stk_symb == "DONE":
            print("                   ")
            print("Done adding ticker symbols!")
            print("                   ")
            break
        elif valid_symb_number(stk_symb) >= 1:
            print("                   ")
            print("Stock ticker is invalid, please enter a valid stock ticker with 4 letter to represent a company.")
            print("                   ")
        else:
            symb_list.append(stk_symb)


def enter_risk_tolerance():
    while True:
        prompt2 = "Please enter your risk tolerance (high, medium, low). If you don't have a risk tolerance, enter 'none'.\nEnter Here: "
        risk = input(prompt2)
        risk_answers = ["High", "high", "HIGH", "LOW", "low", "Low", "MEDIUM", "Medium", "medium"]
        if risk in risk_answers:
            print("                   ")
            print(f"Your risk tolerance is {risk}. On to the next step..")
            break
        elif risk == "NONE" or risk =="none" or risk == "None":
            print("                   ")
            print("You don't have a risk tolerance. On to the next steps..")
            break
        else:
            print("                   ")
            print("Please enter a valid risk tolerence (high, medium, low)")
            print("                   ")
    return risk

enter_ticker()

#also prompt the user to specify additional inputs such as 1. Risk Tolerance, among others

enter_risk_tolerance()

print("                   ")
print("-------------------------")
print("Selected Symbols: ")
for symbol in symb_list:
    print(symbol)

url_list = {}
for symbol in symb_list:
    url_list[symbol] = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={key}"


#Process a GET request to AlphaVantage API to gt stock data
#If sotck data for symbol is not found return "not data found"
#If there is an error, return "we ran into an error"

#Once data is received, write historical data into a CSV file into a data/ directory
# for each stock symbol, produce an individual CSV file (do not need to read the CSV, just read JSON file from API)
print("                 ")
for ticker in url_list:
    try:
        response = requests.get(url_list[ticker])
        response_data = response.text
        stock_df = pd.read_json(response_data)
        stock_df.to_csv(f"data/{ticker}_stock_data.csv")
    except ValueError:
        print(f"Ticker symbol for {ticker} does not exist. Please try another symbol.")




print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")


#Produce the following output:
#  * Selected Stock Symbol, Data & Time when program was executed, the date when data was last refreshed
#  * Latest Closing Price, Recent High Price, Recent Low Price
        #Formulas: 
            #Stocks Close Price @ Lastest Available Day of Trading
            #Recent High Price - maximum daily high price over approx. past 100 available days of training data (already given)
            #Recent Low Price - minimum of all daily low prices

#  * Recommendation - should you purchase? If so, how much should you purchase?

#   * Human friendly reason why recommendation was passed

