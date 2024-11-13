# massmetric to massmetric
def kg_g(kg):
    return kg * 1000

def g_kg(g):
    return g / 1000

def kg_mg(kg):
    return kg * 1000000

def mg_kg(mg):
    return mg / 1000000

def mg_g(mg):
    return mg / 1000

def g_mg(g):
    return g * 1000

# UK-US to metric
def lb_g(lb):
    return lb * 453.59237

def oz_g(oz):
    return oz * 28.3495231

def lb_kg(lb):
    return lb * 0.454

def oz_kg(oz):
    return oz * 0.0283495231

def lb_mg(lb):
    return lb * 453592.37

def oz_mg(oz):
    return oz * 28349.5231


# metric to UK-US
def g_lb(g):
    return g * 0.00220462262

def g_oz(g):
    return g * 0.035274

def kg_lb(kg):
    return kg * 2.205

def kg_oz(kg):
    return kg * 35.2739619

def mg_lb(mg):
    return mg * 0.000002205

def mg_oz(mg):
    return mg * 0.000035274

# UK-US to UK-US
def lb_oz(lb):
    return lb * 16

def oz_lb(oz):
    return oz * 0.0625

massmetric_to_massmetric = {
    'kg_g': kg_g,
    'g_kg': g_kg,
    'kg_mg': kg_mg,
    'mg_kg': mg_kg,
    'mg_g': mg_g,
    'g_mg': g_mg
}

UK_US_to_metric = {
    'lb_g': lb_g,
    'oz_g': oz_g,
    'lb_kg': lb_kg,
    'oz_kg': oz_kg,
    'lb_mg': lb_mg,
    'oz_mg': oz_mg
}

metric_to_UK_US = {
    'g_lb': g_lb,
    'g_oz': g_oz,
    'kg_lb': kg_lb,
    'kg_oz': kg_oz,
    'mg_lb': mg_lb,
    'mg_oz': mg_oz
}

UK_US_to_UK_US = {
    'lb_oz': lb_oz,
    'oz_lb': oz_lb
}