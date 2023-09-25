from forex_python.converter import CurrencyRates

def usd_to_brl(amount):
    c = CurrencyRates()
    exchange_rate = c.get_rate('USD', 'BRL')
    brl_amount = amount * exchange_rate
    return brl_amount

def brl_to_usd(amount):
    c = CurrencyRates()
    exchange_rate = c.get_rate('BRL', 'USD')
    usd_amount = amount * exchange_rate
    return usd_amount

usd_amount = float(input("Diga a quantidade em USD: "))
brl_amount = usd_to_brl(usd_amount)
print(f"{usd_amount} USD é igual a {brl_amount} BRL")

brl_amount = float(input("Diga a quantidade em BRL: "))
usd_amount = (brl_to_usd(brl_amount))
print(f"{brl_amount} BRL é igual a {usd_amount} USD")