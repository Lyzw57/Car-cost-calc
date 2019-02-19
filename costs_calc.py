VAT_RATE = 0.23
NON_COSTS_PROPORTION = 0.25

def get_vat_amount(net_amount, vat_rate):
    return net_amount * vat_rate

def get_half_of_vat(vat_amount):
    return vat_amount / 2

def get_net_amount():
    while True:
        try:
            net_amount = float(input("Podaj kwotę netto: "))
        except ValueError:
            print("Nieprawidłowe dane!")
        else:
            return net_amount

def calc_non_costs(net_amount, vat_amount, deduction_factor):
    non_costs = (net_amount + vat_amount) * deduction_factor
    return non_costs

    
