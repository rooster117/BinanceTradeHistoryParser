from csv import reader
# open file in read mode
with open('trade_history.csv', 'r') as read_obj:

    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object

    tickerSymbols = dict()

    amount_key = "amount"
    paid_key = "paid"
    returned_key = "returned"

    for row in csv_reader:
        symbolString = row[1]
        symbolStringLength = len(symbolString)
        symbol = symbolString[:symbolStringLength - 3]

        if row[2] == "BUY":
            if symbol in tickerSymbols.keys():
                thisTicker = tickerSymbols[symbol]
                tickerSymbols[symbol] = { amount_key : float(thisTicker[amount_key]) + float(row[4]), paid_key : thisTicker[paid_key] + float(row[5]), returned_key : thisTicker[returned_key] }
            else:
                tickerSymbols[symbol] = { amount_key : float(row[4]), paid_key : float(row[5]), returned_key : float(0) }
        else:
            if symbol in tickerSymbols.keys():
                thisTicker = tickerSymbols[symbol]
                tickerSymbols[symbol] = { amount_key : thisTicker[amount_key] - float(row[4]), paid_key : thisTicker[paid_key], returned_key : thisTicker[returned_key] + float(row[5]) }

    for key in tickerSymbols:
        if tickerSymbols[key][amount_key] > 0:
            print("{}: {:.2f} : {:.2f}".format(key, (tickerSymbols[key][paid_key] - tickerSymbols[key][returned_key])/tickerSymbols[key][amount_key], tickerSymbols[key][amount_key]))