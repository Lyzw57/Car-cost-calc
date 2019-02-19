VAT_RATE = 0.23
NON_COSTS_PROPORTION = 0.25

def get_vat(net_amount):
    return net_amount * VAT_RATE

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