#stock viewer
import yfinance as yf

def company_selecter(c_name):
    stock = yf.Ticker(c_name)
    return stock.info['currentPrice']

def stock_price_checker():    
    while True:
        c_name = input('Stock name to evaluate: ')

        try:
            price = company_selecter(c_name.upper())
            print(f'${price}')
            x = 1

            while True:
                print('Evalute another? Y/N')
                y_n = input()

                if y_n.upper() == 'Y':
                    break

                elif y_n.upper() == 'N':
                    print('Good trading.')
                    return 0

                else:
                    print('Please enter Y or N.')

        except KeyError:
            print('what are you trolling? lolll???')


stock_price_checker()    























































