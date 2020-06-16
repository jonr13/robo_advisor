print("-------------------------")
print("SELECTED SYMBOL: XYZ")
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


#prompt the user to input one stock or cryptocurrency (ex. "MSFT" or "AAPL")
#allow the user to speciy multiple sybmbols in the same request
#also prompt the user to specify additional inputs such as 1. Risk Tolerance, among others

#Peform validations on user inputs - ensure characterlength for stock symbols - ensure characters are not numeric

#Process a GET request to AlphaVantage API to gt stock data
#If sotck data for symbol is not found return "not data found"
#If there is an error, return "we ran into an error"

#Once data is received, write historical data into a CSV file into a data/ directory
# for each stock symbol, produce an individual CSV file (do not need to read the CSV, just read JSON file from API)
#Produce the following output:
#  * Selected Stock Symbol, Data & Time when program was executed, the date when data was last refreshed
#  * Latest Closing Price, Recent High Price, Recent Low Price
        #Formulas: 
            #Stocks Close Price @ Lastest Available Day of Trading
            #Recent High Price - maximum daily high price over approx. past 100 available days of training data (already given)
            #Recent Low Price - minimum of all daily low prices
#  * Recommendation - should you purchase? If so, how much should you purchase?

#   * Human friendly reason why recommendation was passed

