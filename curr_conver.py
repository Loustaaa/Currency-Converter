import json
from urllib.request import urlopen


def retrieve():
    '''
        Retrieves data from currency exchange API
    '''
    with urlopen("https://api.exchangeratesapi.io/latest") as r:
        source = r.read()

    rawdata = json.loads(source)

    return rawdata


def userprompt(data):
    '''
        Prompts the user for information.
    '''
    #Creates list to store names of available currencies.
    currlist = []
    for val in data["rates"]:
        print(val)
        currlist.append(val)
    print("Which currency would you like to convert to?")

    #Makes sure user inputs a valid currency.
    valid = False
    while valid == False:
        curr = input("EUR to:" ).upper()
        if curr in currlist:
            valid = True
        else:
            print("Not a valid currency. Please select from the list.")
    return curr
    
def convert(curr, data):
    '''
        Converts currency according to recent exchange rates
    '''
    #Finds the exchange rate in API data.
    for r in data["rates"]:
        if r == curr:
            rate = data["rates"][r]
    print("The exchange rate from EUR to %s is %.4f" % (curr, rate))
    amount = input("How much do you wish to convert?:")

    #Checks to see if user input is valid.
    while amount.isdigit() != True:
        amount = input("Please input the amount you wish to convert: ")
    i = float(amount) * rate
    return i, amount




data = retrieve()
currency = userprompt(data)
i, amount = convert(currency, data)
print("%s EUR = %.4f %s" % (amount, i, currency))
