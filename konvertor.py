from mahud import *
from massid import *

def teisenda_mahud(arv, ühikust, ühikusse, süsteemist, süsteemi):

    teisendus_võti = f"{ühikust}_to_{ühikusse}"

    if süsteemist == "metric" and süsteemi == "metric":
        tuletis_dict = metric_to_metric
    elif süsteemist == "metric" and süsteemi == "imperial":
        tuletis_dict = metric_to_imperial
    elif süsteemist == "metric" and süsteemi == "US":
        tuletis_dict = metric_to_us
    elif süsteemist == "imperial" and süsteemi == "metric":
        tuletis_dict = imperial_to_metric
    elif süsteemist == "US" and süsteemi == "metric":
        tuletis_dict = us_to_metric
    elif süsteemist == "imperial" and süsteemi == "US":
        tuletis_dict = imperial_to_us
    elif süsteemist == "imperial" and süsteemi == "imperial":
        tuletis_dict = imperial_to_imperial
    elif süsteemist == "US" and süsteemi == "imperial":
        tuletis_dict = us_to_imperial
    elif süsteemist == "US" and süsteemi == "US":
        tuletis_dict = us_to_us
    else:
        return None
    
    if teisendus_võti in tuletis_dict:
        return tuletis_dict[teisendus_võti](arv)
    else:
        print("Sellist teisendus tehet ei leitud.")
        return None

def main_volume():
    arv = float(input("Sisesta arv mida tahad teisendada: "))
    ühikust = input("Sisesta ühik milles arv on(e.g., l, gallons, cups): ").strip()
    ühikusse = input("Sisesta milleks tahad arvu teisendada: ").strip()
    süsteemist = input("Millises süsteemis on algne arv(US, imperial, metric): ").strip()
    süsteemi = input("Millisesse süsteemi tahad teisendada: ").strip()

    tulemus = teisenda_mahud(arv, ühikust, ühikusse, süsteemist,süsteemi)
    if tulemus is not None:
        if süsteemist == "metric" and süsteemi == "metric":
            print(f"{arv} {ühikust} = {round(tulemus, 6)} {ühikusse}")
        elif süsteemist != "metric" and süsteemi == "metric":
            print(f"{arv} {süsteemist} {ühikust} = {round(tulemus, 6)} {ühikusse}")
        elif süsteemist == "metric" and süsteemi != "metric":
            print(f"{arv} {ühikust} = {round(tulemus, 6)} {süsteemi} {ühikusse}")
        else:
            print(f"{arv} {süsteemist} {ühikust} = {round(tulemus, 6)} {süsteemi} {ühikusse}")

def main_massid():
    arv = float(input("Sisesta arv mida tahad teisendada: "))
    #siia tuleb massi kalkulaator

def teisendus():
    print("MeasurePerfect")
    tüüp = input("Millist teisendust soovid teha(e.g. massid, mahud): ")
    if tüüp == "mahud":
        main_volume()
    elif tüüp == "massid":
        main_massid()
    else:
        print("Sellist teisendust ei suuda see programm veel teha")

teisendus()