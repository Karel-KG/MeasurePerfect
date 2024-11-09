from mahud import *
from massid import *

metric_to_metric = {
    'l_to_dl': l_to_dl,
    'l_to_cl': l_to_cl,
    'l_to_ml': l_to_ml,
    'dl_to_l': dl_to_l,
    'dl_to_cl': dl_to_cl,
    'dl_to_ml': dl_to_ml,
    'cl_to_l': cl_to_l,
    'cl_to_dl': cl_to_dl,
    'cl_to_ml': cl_to_ml,
    'ml_to_l': ml_to_l,
    'ml_to_dl': ml_to_dl,
    'ml_to_cl': ml_to_cl,
}

us_to_us = {
    'gallons_to_quarts': us_gallons_to_us_quarts,
    'quarts_to_gallons': us_quarts_to_us_gallons,
    'quarts_to_pints': us_quarts_to_us_pints,
    'pints_to_quarts': us_pints_to_us_quarts,
    'pints_to_cups': us_pints_to_us_cups,
    'cups_to_pints': us_cups_to_us_pints,
    'cups_to_fl_oz': us_cups_to_us_fl_oz,
    'fl_oz_to_cups': us_fl_oz_to_us_cups,
    'fl_oz_to_tablespoons': us_fl_oz_to_us_tablespoons,
    'tablespoons_to_fl_oz': us_tablespoons_to_us_fl_oz,
    'tablespoons_to_teaspoons': us_tablespoons_to_us_teaspoons,
    'teaspoons_to_tablespoons': us_teaspoons_to_us_tablespoons,
}

imperial_to_imperial = {
    'gallons_to_quarts': imperial_gallons_to_imperial_quarts,
    'quarts_to_gallons': imperial_quarts_to_imperial_gallons,
    'quarts_to_pints': imperial_quarts_to_imperial_pints,
    'pints_to_quarts': imperial_pints_to_imperial_quarts,
    'pints_to_cups': imperial_pints_to_imperial_cups,
    'cups_to_pints': imperial_cups_to_imperial_pints,
    'cups_to_fl_oz': imperial_cups_to_imperial_fl_oz,
    'fl_oz_to_cups': imperial_fl_oz_to_imperial_cups,
    'fl_oz_to_tablespoons': imperial_fl_oz_to_imperial_tablespoons,
    'tablespoons_to_fl_oz': imperial_tablespoons_to_imperial_fl_oz,
    'tablespoons_to_teaspoons': imperial_tablespoons_to_imperial_teaspoons,
    'teaspoons_to_tablespoons': imperial_teaspoons_to_imperial_tablespoons,
}

metric_to_us = {
    'l_to_gallons': l_to_us_gallons,
    'l_to_quarts': l_to_us_quarts,
    'l_to_pints': l_to_us_pints,
    'l_to_fl_oz': l_to_us_fl_oz,
    'ml_to_gallons': ml_to_us_gallons,
    'ml_to_quarts': ml_to_us_quarts,
    'ml_to_pints': ml_to_us_pints,
    'ml_to_fl_oz': ml_to_us_fl_oz,
    'l_to_cups': l_to_us_cups,
    'l_to_tablespoons': l_to_us_tablespoons,
    'l_to_teaspoons': l_to_us_teaspoons,
    'ml_to_cups': ml_to_us_cups,
    'ml_to_tablespoons': ml_to_us_tablespoons,
    'ml_to_teaspoons': ml_to_us_teaspoons,
}

us_to_metric = {
    'gallons_to_l': us_gallons_to_l,
    'quarts_to_l': us_quarts_to_l,
    'pints_to_l': us_pints_to_l,
    'fl_oz_to_l': us_fl_oz_to_l,
    'gallons_to_ml': us_gallons_to_ml,
    'quarts_to_ml': us_quarts_to_ml,
    'pints_to_ml': us_pints_to_ml,
    'fl_oz_to_ml': us_fl_oz_to_ml,
    'cups_to_l': us_cups_to_l,
    'tablespoons_to_l': us_tablespoons_to_l,
    'teaspoons_to_l': us_teaspoons_to_l,
    'cups_to_ml': us_cups_to_ml,
    'tablespoons_to_ml': us_tablespoons_to_ml,
    'teaspoons_to_ml': us_teaspoons_to_ml,
}

metric_to_imperial = {
    'l_to_gallons': l_to_imperial_gallons,
    'l_to_quarts': l_to_imperial_quarts,
    'l_to_pints': l_to_imperial_pints,
    'l_to_fl_oz': l_to_imperial_fl_oz,
    'ml_to_gallons': ml_to_imperial_gallons,
    'ml_to_quarts': ml_to_imperial_quarts,
    'ml_to_pints': ml_to_imperial_pints,
    'ml_to_fl_oz': ml_to_imperial_fl_oz,
    'l_to_cups': l_to_imperial_cups,
    'l_to_tablespoons': l_to_imperial_tablespoons,
    'l_to_teaspoons': l_to_imperial_teaspoons,
    'ml_to_cups': ml_to_imperial_cups,
    'ml_to_tablespoons': ml_to_imperial_tablespoons,
    'ml_to_teaspoons': ml_to_imperial_teaspoons,
}

imperial_to_metric = {
    'gallons_to_l': imperial_gallons_to_l,
    'quarts_to_l': imperial_quarts_to_l,
    'pints_to_l': imperial_pints_to_l,
    'fl_oz_to_l': imperial_fl_oz_to_l,
    'gallons_to_ml': imperial_gallons_to_ml,
    'quarts_to_ml': imperial_quarts_to_ml,
    'pints_to_ml': imperial_pints_to_ml,
    'fl_oz_to_ml': imperial_fl_oz_to_ml,
    'cups_to_l': imperial_cups_to_l,
    'tablespoons_to_l': imperial_tablespoons_to_l,
    'teaspoons_to_l': imperial_teaspoons_to_l,
    'cups_to_ml': imperial_cups_to_ml,
    'tablespoons_to_ml': imperial_tablespoons_to_ml,
    'teaspoons_to_ml': imperial_teaspoons_to_ml,
}

us_to_imperial = {
    'gallons_to_gallons': us_gallons_to_imperial_gallons,
    'quarts_to_quarts': us_quarts_to_imperial_quarts,
    'pints_to_pints': us_pints_to_imperial_pints,
    'fl_oz_to_fl_oz': us_fl_oz_to_imperial_fl_oz,
    'cups_to_cups': us_cups_to_imperial_cups,
    'tablespoons_to_tablespoons': us_tablespoons_to_imperial_tablespoons,
    'teaspoons_to_teaspoons': us_teaspoons_to_imperial_teaspoons,

}

imperial_to_us = {
    'gallons_to_gallons': imperial_gallons_to_us_gallons,
    'quarts_to_quarts': imperial_quarts_to_us_quarts,
    'pints_to_pints': imperial_pints_to_us_pints,
    'fl_oz_to_fl_oz': imperial_fl_oz_to_us_fl_oz,
    'cups_to_cups': imperial_cups_to_us_cups,
    'tablespoons_to_tablespoons': imperial_tablespoons_to_us_tablespoons,
    'teaspoons_to_teaspoons': imperial_teaspoons_to_us_teaspoons,
}

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

def main():
    print("MeasurePerfect")
    arv = float(input("Sisesta arv mida tahad teisendada: "))
    ühikust = input("Sisesta ühik milles arv on(e.g., l, gallons, cups): ").strip()
    ühikusse = input("Sisesta milleks tahad arvu teisendada: ").strip()
    süsteemist = input("Millises süsteemis on algne arv(US, imperial, metric): ").strip()
    süsteemi = input("Millisesse süsteemi tahad teisendada: ").strip()

    tulemus = teisenda_mahud(arv, ühikust, ühikusse, süsteemist,süsteemi)
    if tulemus is not None:
        if süsteemist == "metric" and süsteemi == "metric":
            print(f"{arv} {ühikust} = {tulemus} {ühikusse}")
        elif süsteemist != "metric" and süsteemi == "metric":
            print(f"{arv} {süsteemist} {ühikust} = {tulemus} {ühikusse}")
        elif süsteemist == "metric" and süsteemi != "metric":
            print(f"{arv} {ühikust} = {tulemus} {süsteemi} {ühikusse}")
        else:
            print(f"{int(arv)} {süsteemist} {ühikust} = {round(tulemus, 6)} {süsteemi} {ühikusse}")

main()