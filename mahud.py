# Metric to Metric

def l_to_dl(l):
    return l * 10

def l_to_cl(l):
    return l * 100

def l_to_ml(l):
    return l * 1000

def dl_to_l(dl):
    return dl / 10

def dl_to_cl(dl):
    return dl * 10

def dl_to_ml(dl):
    return dl * 100

def cl_to_l(cl):
    return cl / 100

def cl_to_dl(cl):
    return cl / 10

def cl_to_ml(cl):
    return cl * 10

def ml_to_l(ml):
    return ml / 1000

def ml_to_dl(ml):
    return ml / 100

def ml_to_cl(ml):
    return ml / 10

# Metric to Imperial

def l_to_imperial_gallons(l):
    return l / 4.54609

def l_to_imperial_quarts(l):
    return l / 1.13652

def l_to_imperial_pints(l):
    return l / 0.568261

def l_to_imperial_fl_oz(l):
    return l / 0.0284131

def ml_to_imperial_gallons(ml):
    return ml / (4.54609 * 1000)

def ml_to_imperial_quarts(ml):
    return ml / (1.13652 * 1000)

def ml_to_imperial_pints(ml):
    return ml / (0.568261 * 1000)

def ml_to_imperial_fl_oz(ml):
    return ml / (0.0284131 * 1000)

def l_to_imperial_cups(l):
    return l / 0.284131

def l_to_imperial_tablespoons(l):
    return l / 0.0177582

def l_to_imperial_teaspoons(l):
    return l / 0.00591939

def ml_to_imperial_cups(ml):
    return ml / (0.284131 * 1000)

def ml_to_imperial_tablespoons(ml):
    return ml / (0.0177582 * 1000)

def ml_to_imperial_teaspoons(ml):
    return ml / (0.00591939 * 1000)


# Metric to US

def l_to_us_gallons(l):
    return l / 3.78541

def l_to_us_quarts(l):
    return l / 0.946353

def l_to_us_pints(l):
    return l / 0.473176

def l_to_us_fl_oz(l):
    return l / 0.0295735

def ml_to_us_gallons(ml):
    return ml / (3.78541 * 1000)

def ml_to_us_quarts(ml):
    return ml / (0.946353 * 1000)

def ml_to_us_pints(ml):
    return ml / (0.473176 * 1000)

def ml_to_us_fl_oz(ml):
    return ml / (0.0295735 * 1000)

def l_to_us_cups(l):
    return l / 0.24

def l_to_us_tablespoons(l):
    return l / 0.0147868

def l_to_us_teaspoons(l):
    return l / 0.00492892

def ml_to_us_cups(ml):
    return ml / (0.24 * 1000)

def ml_to_us_tablespoons(ml):
    return ml / (0.0147868 * 1000)

def ml_to_us_teaspoons(ml):
    return ml / (0.00492892 * 1000)


# Imperial to Metric

def imperial_gallons_to_l(imp_gal):
    return imp_gal * 4.54609

def imperial_quarts_to_l(imp_qt):
    return imp_qt * 1.13652

def imperial_pints_to_l(imp_pt):
    return imp_pt * 0.568261

def imperial_fl_oz_to_l(imp_oz):
    return imp_oz * 0.0284131

def imperial_gallons_to_ml(imp_gal):
    return imp_gal * 4.54609 * 1000

def imperial_quarts_to_ml(imp_qt):
    return imp_qt * 1.13652 * 1000

def imperial_pints_to_ml(imp_pt):
    return imp_pt * 0.568261 * 1000

def imperial_fl_oz_to_ml(imp_oz):
    return imp_oz * 0.0284131 * 1000

def imperial_cups_to_l(imp_cups):
    return imp_cups * 0.284131

def imperial_tablespoons_to_l(imp_tbsp):
    return imp_tbsp * 0.0177582

def imperial_teaspoons_to_l(imp_tsp):
    return imp_tsp * 0.00591939

def imperial_cups_to_ml(imp_cups):
    return imp_cups * 0.284131 * 1000

def imperial_tablespoons_to_ml(imp_tbsp):
    return imp_tbsp * 0.0177582 * 1000

def imperial_teaspoons_to_ml(imp_tsp):
    return imp_tsp * 0.00591939 * 1000


# US to Metric 

def us_gallons_to_l(us_gal):
    return us_gal * 3.78541

def us_quarts_to_l(us_qt):
    return us_qt * 0.946353

def us_pints_to_l(us_pt):
    return us_pt * 0.473176

def us_fl_oz_to_l(us_oz):
    return us_oz * 0.0295735

def us_gallons_to_ml(us_gal):
    return us_gal * 3.78541 * 1000

def us_quarts_to_ml(us_qt):
    return us_qt * 0.946353 * 1000

def us_pints_to_ml(us_pt):
    return us_pt * 0.473176 * 1000

def us_fl_oz_to_ml(us_oz):
    return us_oz * 0.0295735 * 1000

def us_cups_to_l(us_cups):
    return us_cups * 0.24

def us_tablespoons_to_l(us_tbsp):
    return us_tbsp * 0.0147868

def us_teaspoons_to_l(us_tsp):
    return us_tsp * 0.00492892

def us_cups_to_ml(us_cups):
    return us_cups * 0.24 * 1000

def us_tablespoons_to_ml(us_tbsp):
    return us_tbsp * 0.0147868 * 1000

def us_teaspoons_to_ml(us_tsp):
    return us_tsp * 0.00492892 * 1000

# Imperial to US

def imperial_gallons_to_us_gallons(imp_gal):
    return imp_gal * 1.20095

def imperial_quarts_to_us_quarts(imp_qt):
    return imp_qt * 1.20095

def imperial_pints_to_us_pints(imp_pt):
    return imp_pt * 1.20095

def imperial_fl_oz_to_us_fl_oz(imp_oz):
    return imp_oz * 1.04084

def imperial_cups_to_us_cups(imp_cup):
    return imp_cup * 1.20095

def imperial_tablespoons_to_us_tablespoons(imp_tbsp):
    return imp_tbsp * 1.20095

def imperial_teaspoons_to_us_teaspoons(imp_tsp):
    return imp_tsp * 1.20095


# US to Imperial

def us_gallons_to_imperial_gallons(us_gal):
    return us_gal * 0.832674

def us_quarts_to_imperial_quarts(us_qt):
    return us_qt * 0.832674

def us_pints_to_imperial_pints(us_pt):
    return us_pt * 0.832674

def us_fl_oz_to_imperial_fl_oz(us_oz):
    return us_oz * 0.96076

def us_cups_to_imperial_cups(us_cup):
    return us_cup * 0.832674

def us_tablespoons_to_imperial_tablespoons(us_tbsp):
    return us_tbsp * 0.832674

def us_teaspoons_to_imperial_teaspoons(us_tsp):
    return us_tsp * 0.832674


# US to US

def us_gallons_to_us_quarts(us_gal):
    return us_gal * 4

def us_quarts_to_us_gallons(us_qt):
    return us_qt / 4

def us_quarts_to_us_pints(us_qt):
    return us_qt * 2

def us_pints_to_us_quarts(us_pt):
    return us_pt / 2

def us_pints_to_us_cups(us_pt):
    return us_pt * 2

def us_cups_to_us_pints(us_cup):
    return us_cup / 2

def us_cups_to_us_fl_oz(us_cup):
    return us_cup * 8

def us_fl_oz_to_us_cups(us_oz):
    return us_oz / 8

def us_fl_oz_to_us_tablespoons(us_oz):
    return us_oz * 2

def us_tablespoons_to_us_fl_oz(us_tbsp):
    return us_tbsp / 2

def us_tablespoons_to_us_teaspoons(us_tbsp):
    return us_tbsp * 3

def us_teaspoons_to_us_tablespoons(us_tsp):
    return us_tsp / 3


# Imperial to Imperial

def imperial_gallons_to_imperial_quarts(imp_gal):
    return imp_gal * 4

def imperial_quarts_to_imperial_gallons(imp_qt):
    return imp_qt / 4

def imperial_quarts_to_imperial_pints(imp_qt):
    return imp_qt * 2

def imperial_pints_to_imperial_quarts(imp_pt):
    return imp_pt / 2

def imperial_pints_to_imperial_cups(imp_pt):
    return imp_pt * 2

def imperial_cups_to_imperial_pints(imp_cup):
    return imp_cup / 2

def imperial_cups_to_imperial_fl_oz(imp_cup):
    return imp_cup * 10

def imperial_fl_oz_to_imperial_cups(imp_oz):
    return imp_oz / 10

def imperial_fl_oz_to_imperial_tablespoons(imp_oz):
    return imp_oz * 1.6

def imperial_tablespoons_to_imperial_fl_oz(imp_tbsp):
    return imp_tbsp / 1.6

def imperial_tablespoons_to_imperial_teaspoons(imp_tbsp):
    return imp_tbsp * 3

def imperial_teaspoons_to_imperial_tablespoons(imp_tsp):
    return imp_tsp / 3


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