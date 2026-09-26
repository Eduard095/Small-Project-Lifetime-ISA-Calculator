from backend.calculation import monthly_calculations

def main():
    while True:
        try:
            contribution = float(input("1. How much will you be contributing monthly?: "))
            years = int(input("2. In how many years do you want to buy your first home?: "))
            if 0 < contribution <= 333 and 0 < years < 40:
                break
            print('''
            Invalid

            Rules 
            -------------------------------------------------------
            1. Contributions must be between £1 and £333
            2. Length of time must be within 1 to 40 years
            -------------------------------------------------------
            
            Try Again
            ''')
        except:
            print('''
            Invalid input
                              
            Try Again
            ''')
            return -1
           
    monthly_calculations(contribution, years)
    return contribution, years



if __name__ == "__main__":
    print('''
Welcome to LISA calulator: 
Please provide the following

-------------------------------------------------------
1. How much will you be contributing monthly?
2. In how many years do you want to buy your first home?
-------------------------------------------------------

''')
    main()