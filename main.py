####################################
# 3. Working on a local repository #
####################################

def calculate_dcf(cash_flow, discount_rate):
    """
    Calculates the cumulative discounted cash flow of 
    cash_flow at discount_rate.
    Expects a list of float as cash flows and a 
    percentage discount_rate.
    """
    dcf = 0
    for i in range(len(cash_flow)):
        dcf += cash_flow[i] / (1. + discount_rate)**(i+1)
    return dcf

#Example to check if everything works:
cash_flow = [2000., 2500., 3000., 3000., 3000.]
discount_rate = 0.1
dcf = round(calculate_dcf(cash_flow, discount_rate), 2)
print(f"The DCF of {cash_flow} at a {discount_rate} discount rate is {dcf}")