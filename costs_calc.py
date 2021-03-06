VAT_RATE = 0.23
NON_COSTS_PROPORTION = 0.25

def get_vat_amount(net_amount, vat_rate):
    return round((net_amount * vat_rate), 2)

def get_half_of_vat(vat_amount):
    return round((vat_amount / 2), 2)

def get_net_amount():
    while True:
        try:
            net_amount = float(input("Podaj kwotę netto: "))
        except ValueError:
            print("Nieprawidłowe dane!")
        else:
            return round(net_amount, 2)

def calc_non_costs(net_amount, vat_amount, deduction_factor):
    non_costs = (net_amount + vat_amount) * deduction_factor
    return round(non_costs, 2)

def display_results(costs, vat_amount, non_costs):
    print("KUP: {0}\n50% VAT: {1}\nNKUP: {2}".format(costs, vat_amount, non_costs))

def init_calc(vat_rate, deduction_factor):
    user_input = input("Czy chcesz obliczyć NKUP od wydatku? (t/n) : ")

    while user_input.lower() != 'n':
        net_amount = get_net_amount()
        half_of_vat = get_half_of_vat(get_vat_amount(net_amount, vat_rate))
        non_costs = calc_non_costs(net_amount, half_of_vat, deduction_factor)
        costs = (net_amount + half_of_vat) - non_costs
        display_results(costs, half_of_vat, non_costs)

        while True:
            user_input = input("Czy chcesz przeliczyć ponownie? (t/n) : ")
            if user_input.lower() == 't' or user_input.lower() == 'n':
                break
            else:
                print("Nie ma takiej opcji.")


if __name__ == "__main__":
    init_calc(VAT_RATE, NON_COSTS_PROPORTION)