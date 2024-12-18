import tkinter as tk
from tkinter import ttk

################################################
# Programmeerimine I
# 2024/2025 sügissemester
#
# MeasurePerfect
# Teema: möötühikute teisendus kalkulaator
#
#
# Autorid: Karel Konga, Triin-Elis Kuum
#
# eeskuju: google'i standartne teisendus tööriist ja teisendus kalkulaatori veebilehed (nt. unitconverters.net)
#
##################################################

# Konverteerimis tabelid
conversion_factors = {
    "Length": {
        "Kilometre": {"Kilometre": 1, "Metre": 1000, "Centimetre": 100000, "Millimetre": 1e6, "Micrometre": 1e9, "Nanometre": 1e12, "Mile": 0.621371, "Yard": 1093.61, "Foot": 3280.84, "Inch": 39370.1, "Nautical mile": 0.539957},
        "Metre": {"Kilometre": 0.001, "Metre": 1, "Centimetre": 100, "Millimetre": 1000, "Micrometre": 1e6, "Nanometre": 1e9, "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701, "Nautical mile": 0.000539957},
        "Centimetre": {"Kilometre": 1e-5, "Metre": 0.01, "Centimetre": 1, "Millimetre": 10, "Micrometre": 10000, "Nanometre": 1e7, "Mile": 6.2137e-6, "Yard": 0.0109361, "Foot": 0.0328084, "Inch": 0.393701, "Nautical mile": 5.39957e-6},
        "Millimetre": {"Kilometre": 1e-6, "Metre": 0.001, "Centimetre": 0.1, "Millimetre": 1, "Micrometre": 1000, "Nanometre": 1e6, "Mile": 6.2137e-7, "Yard": 0.00109361, "Foot": 0.00328084, "Inch": 0.0393701, "Nautical mile": 5.39957e-7},
        "Micrometre": {"Kilometre": 1e-9, "Metre": 1e-6, "Centimetre": 1e-4, "Millimetre": 0.001, "Micrometre": 1, "Nanometre": 1000, "Mile": 6.2137e-10, "Yard": 1.0936e-6, "Foot": 3.2808e-6, "Inch": 3.937e-5, "Nautical mile": 5.3996e-10},
        "Nanometre": {"Kilometre": 1e-12, "Metre": 1e-9, "Centimetre": 1e-7, "Millimetre": 1e-6, "Micrometre": 0.001, "Nanometre": 1, "Mile": 6.2137e-13, "Yard": 1.0936e-9, "Foot": 3.2808e-9, "Inch": 3.937e-8, "Nautical mile": 5.3996e-13},
        "Mile": {"Kilometre": 1.60934, "Metre": 1609.34, "Centimetre": 160934, "Millimetre": 1.609e6, "Micrometre": 1.609e9, "Nanometre": 1.609e12, "Mile": 1, "Yard": 1760, "Foot": 5280, "Inch": 63360, "Nautical mile": 0.868976},
        "Yard": {"Kilometre": 0.0009144, "Metre": 0.9144, "Centimetre": 91.44, "Millimetre": 914.4, "Micrometre": 914400, "Nanometre": 9.144e8, "Mile": 0.000568182, "Yard": 1, "Foot": 3, "Inch": 36, "Nautical mile": 0.000493737},
        "Foot": {"Kilometre": 0.0003048, "Metre": 0.3048, "Centimetre": 30.48, "Millimetre": 304.8, "Micrometre": 304800, "Nanometre": 3.048e8, "Mile": 0.000189394, "Yard": 0.333333, "Foot": 1, "Inch": 12, "Nautical mile": 0.000164579},
        "Inch": {"Kilometre": 2.54e-5, "Metre": 0.0254, "Centimetre": 2.54, "Millimetre": 25.4, "Micrometre": 25400, "Nanometre": 2.54e7, "Mile": 1.5783e-5, "Yard": 0.0277778, "Foot": 0.0833333, "Inch": 1, "Nautical mile": 1.37149e-5},
        "Nautical mile": {"Kilometre": 1.852, "Metre": 1852, "Centimetre": 185200, "Millimetre": 1.852e6, "Micrometre": 1.852e9, "Nanometre": 1.852e12, "Mile": 1.15078, "Yard": 2025.37, "Foot": 6076.12, "Inch": 72913.4, "Nautical mile": 1}
    },
    "Mass": {
        "Kilograms": {"Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274, "Tonne": 0.001, "Milligram": 1e6, "Microgram": 1e9, "Imperial ton": 0.000984207, "US ton": 0.00110231, "Stone": 0.157473},
        "Grams": {"Kilograms": 0.001, "Grams": 1, "Pounds": 0.00220462, "Ounces": 0.035274, "Tonne": 1e-6, "Milligram": 1000, "Microgram": 1e6, "Imperial ton": 9.84207e-7, "US ton": 1.10231e-6, "Stone": 0.000157473},
        "Pounds": {"Kilograms": 0.453592, "Grams": 453.592, "Pounds": 1, "Ounces": 16, "Tonne": 0.000453592, "Milligram": 453592, "Microgram": 4.53592e8, "Imperial ton": 0.000446429, "US ton": 0.0005, "Stone": 0.0714286},
        "Ounces": {"Kilograms": 0.0283495, "Grams": 28.3495, "Pounds": 0.0625, "Ounces": 1, "Tonne": 2.83495e-5, "Milligram": 28349.5, "Microgram": 2.83495e7, "Imperial ton": 2.79018e-5, "US ton": 3.125e-5, "Stone": 0.00446429},
        "Tonne": {"Kilograms": 1000, "Grams": 1e6, "Pounds": 2204.62, "Ounces": 35274, "Tonne": 1, "Milligram": 1e9, "Microgram": 1e12, "Imperial ton": 0.984207, "US ton": 1.10231, "Stone": 157.473},
        "Milligram": {"Kilograms": 1e-6, "Grams": 0.001, "Pounds": 2.20462e-6, "Ounces": 3.5274e-5, "Tonne": 1e-9, "Milligram": 1, "Microgram": 1000, "Imperial ton": 9.84207e-10, "US ton": 1.10231e-9, "Stone": 1.57473e-7},
        "Microgram": {"Kilograms": 1e-9, "Grams": 1e-6, "Pounds": 2.20462e-9, "Ounces": 3.5274e-8, "Tonne": 1e-12, "Milligram": 0.001, "Microgram": 1, "Imperial ton": 9.84207e-13, "US ton": 1.10231e-12, "Stone": 1.57473e-10},
        "Imperial ton": {"Kilograms": 1016.05, "Grams": 1.01605e6, "Pounds": 2240, "Ounces": 35840, "Tonne": 1.01605, "Milligram": 1.01605e9, "Microgram": 1.01605e12, "Imperial ton": 1, "US ton": 1.12, "Stone": 160},
        "US ton": {"Kilograms": 907.184, "Grams": 9.07184e5, "Pounds": 2000, "Ounces": 32000, "Tonne": 0.907184, "Milligram": 9.07184e8, "Microgram": 9.07184e11, "Imperial ton": 0.892857, "US ton": 1, "Stone": 142.857},
        "Stone": {"Kilograms": 6.35029, "Grams": 6350.29, "Pounds": 14, "Ounces": 224, "Tonne": 0.00635029, "Milligram": 6.35029e6, "Microgram": 6.35029e9, "Imperial ton": 0.00625, "US ton": 0.007, "Stone": 1}
    },
    "Volume": {
        "US liquid gallon": {"US liquid gallon": 1, "US liquid quart": 4, "US liquid pint": 8, "US legal cup": 16, "US fluid ounce": 128, "US tablespoon": 256, "US teaspoon": 768, "Cubic meter": 0.00378541, "Liter": 3.78541, "Milliliter": 3785.41, "Imperial gallon": 0.832674, "Imperial quart": 3.3307, "Imperial pint": 6.66139, "Imperial cup": 13.3228, "Imperial fluid ounce": 133.228, "Imperial tablespoon": 213.165, "Imperial teaspoon": 639.494, "Cubic foot": 0.133681, "Cubic inch": 231},
        "US liquid quart": {"US liquid gallon": 0.25, "US liquid quart": 1, "US liquid pint": 2, "US legal cup": 4, "US fluid ounce": 32, "US tablespoon": 64, "US teaspoon": 192, "Cubic meter": 0.000946353, "Liter": 0.946353, "Milliliter": 946.353, "Imperial gallon": 0.208168, "Imperial quart": 0.832674, "Imperial pint": 1.66535, "Imperial cup": 3.3307, "Imperial fluid ounce": 33.307, "Imperial tablespoon": 53.2911, "Imperial teaspoon": 159.873, "Cubic foot": 0.0334201, "Cubic inch": 57.75},
        "US liquid pint": {"US liquid gallon": 0.125, "US liquid quart": 0.5, "US liquid pint": 1, "US legal cup": 2, "US fluid ounce": 16, "US tablespoon": 32, "US teaspoon": 96, "Cubic meter": 0.000473176, "Liter": 0.473176, "Milliliter": 473.176, "Imperial gallon": 0.104084, "Imperial quart": 0.416337, "Imperial pint": 0.832674, "Imperial cup": 1.66535, "Imperial fluid ounce": 16.6535, "Imperial tablespoon": 26.6456, "Imperial teaspoon": 79.9366, "Cubic foot": 0.0167101, "Cubic inch": 28.875},
        "US legal cup": {"US liquid gallon": 0.0625, "US liquid quart": 0.25, "US liquid pint": 0.5, "US legal cup": 1, "US fluid ounce": 8, "US tablespoon": 16, "US teaspoon": 48, "Cubic meter": 0.000236588, "Liter": 0.236588, "Milliliter": 236.588, "Imperial gallon": 0.0520421, "Imperial quart": 0.208168, "Imperial pint": 0.416337, "Imperial cup": 0.832674, "Imperial fluid ounce": 8.32674, "Imperial tablespoon": 13.3228, "Imperial teaspoon": 39.9683, "Cubic foot": 0.00835503, "Cubic inch": 14.4375},
        "US fluid ounce": {"US liquid gallon": 0.0078125, "US liquid quart": 0.03125, "US liquid pint": 0.0625, "US legal cup": 0.125, "US fluid ounce": 1, "US tablespoon": 2, "US teaspoon": 6, "Cubic meter": 2.95735e-05, "Liter": 0.0295735, "Milliliter": 29.5735, "Imperial gallon": 0.00650527, "Imperial quart": 0.0260211, "Imperial pint": 0.0520421, "Imperial cup": 0.104084, "Imperial fluid ounce": 1.04084, "Imperial tablespoon": 1.66535, "Imperial teaspoon": 4.99604, "Cubic foot": 0.00104438, "Cubic inch": 1.80469},
        "US tablespoon": {"US liquid gallon": 0.00390625, "US liquid quart": 0.015625, "US liquid pint": 0.03125, "US legal cup": 0.0625, "US fluid ounce": 0.5, "US tablespoon": 1, "US teaspoon": 3, "Cubic meter": 1.47868e-05, "Liter": 0.0147868, "Milliliter": 14.7868, "Imperial gallon": 0.00325263, "Imperial quart": 0.0130105, "Imperial pint": 0.0260211, "Imperial cup": 0.0520421, "Imperial fluid ounce": 0.520421, "Imperial tablespoon": 0.832674, "Imperial teaspoon": 2.49802, "Cubic foot": 0.00052219, "Cubic inch": 0.902344},
        "US teaspoon": {"US liquid gallon": 0.00130208, "US liquid quart": 0.00520833, "US liquid pint": 0.0104167, "US legal cup": 0.0208333, "US fluid ounce": 0.166667, "US tablespoon": 0.333333, "US teaspoon": 1, "Cubic meter": 4.92892e-06, "Liter": 0.00492892, "Milliliter": 4.92892, "Imperial gallon": 0.00108421, "Imperial quart": 0.00433684, "Imperial pint": 0.00867369, "Imperial cup": 0.0173474, "Imperial fluid ounce": 0.173474, "Imperial tablespoon": 0.277558, "Imperial teaspoon": 0.832674, "Cubic foot": 0.000174063, "Cubic inch": 0.300781},
        "Cubic meter": {"US liquid gallon": 264.172, "US liquid quart": 1056.69, "US liquid pint": 2113.38, "US legal cup": 4226.75, "US fluid ounce": 33814, "US tablespoon": 67628, "US teaspoon": 202884, "Cubic meter": 1, "Liter": 1000, "Milliliter": 1e+06, "Imperial gallon": 219.969, "Imperial quart": 879.877, "Imperial pint": 1759.75, "Imperial cup": 3519.51, "Imperial fluid ounce": 35195.1, "Imperial tablespoon": 56312.1, "Imperial teaspoon": 168936, "Cubic foot": 35.3147, "Cubic inch": 61023.7},
        "Liter": {"US liquid gallon": 0.264172, "US liquid quart": 1.05669, "US liquid pint": 2.11338, "US legal cup": 4.22675, "US fluid ounce": 33.814, "US tablespoon": 67.628, "US teaspoon": 202.884, "Cubic meter": 0.001, "Liter": 1, "Milliliter": 1000, "Imperial gallon": 0.219969, "Imperial quart": 0.879877, "Imperial pint": 1.75975, "Imperial cup": 3.51951, "Imperial fluid ounce": 35.1951, "Imperial tablespoon": 56.3121, "Imperial teaspoon": 168.936, "Cubic foot": 0.0353147, "Cubic inch": 61.0237},
        "Milliliter": {"US liquid gallon": 0.000264172, "US liquid quart": 0.00105669, "US liquid pint": 0.00211338, "US legal cup": 0.00422675, "US fluid ounce": 0.033814, "US tablespoon": 0.067628, "US teaspoon": 0.202884, "Cubic meter": 1e-06, "Liter": 0.001, "Milliliter": 1, "Imperial gallon": 0.000219969, "Imperial quart": 0.000879877, "Imperial pint": 0.00175975, "Imperial cup": 0.00351951, "Imperial fluid ounce": 0.0351951, "Imperial tablespoon": 0.0563121, "Imperial teaspoon": 0.168936, "Cubic foot": 3.53147e-05, "Cubic inch": 0.0610237},
        "Imperial gallon": {"US liquid gallon": 1.20095, "US liquid quart": 4.8038, "US liquid pint": 9.6076, "US legal cup": 19.2152, "US fluid ounce": 153.722, "US tablespoon": 307.443, "US teaspoon": 922.33, "Cubic meter": 0.00454609, "Liter": 4.54609, "Milliliter": 4546.09, "Imperial gallon": 1, "Imperial quart": 4, "Imperial pint": 8, "Imperial cup": 16, "Imperial fluid ounce": 160, "Imperial tablespoon": 256, "Imperial teaspoon": 768, "Cubic foot": 0.160544, "Cubic inch": 277.419},
        "Imperial quart": {"US liquid gallon": 0.300237, "US liquid quart": 1.20095, "US liquid pint": 2.4019, "US legal cup": 4.8038, "US fluid ounce": 38.4304, "US tablespoon": 76.8608, "US teaspoon": 230.582, "Cubic meter": 0.00113652, "Liter": 1.13652, "Milliliter": 1136.52, "Imperial gallon": 0.25, "Imperial quart": 1, "Imperial pint": 2, "Imperial cup": 4, "Imperial fluid ounce": 40, "Imperial tablespoon": 64, "Imperial teaspoon": 192, "Cubic foot": 0.0401359, "Cubic inch": 69.3549},
        "Imperial pint": {"US liquid gallon": 0.150119, "US liquid quart": 0.600475, "US liquid pint": 1.20095, "US legal cup": 2.4019, "US fluid ounce": 19.2152, "US tablespoon": 38.4304, "US teaspoon": 115.291, "Cubic meter": 0.000568261, "Liter": 0.568261, "Milliliter": 568.261, "Imperial gallon": 0.125, "Imperial quart": 0.5, "Imperial pint": 1, "Imperial cup": 2, "Imperial fluid ounce": 20, "Imperial tablespoon": 32, "Imperial teaspoon": 96, "Cubic foot": 0.0200679, "Cubic inch": 34.6774},
        "Imperial cup": {"US liquid gallon": 0.0750594, "US liquid quart": 0.300237, "US liquid pint": 0.600475, "US legal cup": 1.20095, "US fluid ounce": 9.6076, "US tablespoon": 19.2152, "US teaspoon": 57.6456, "Cubic meter": 0.000284131, "Liter": 0.284131, "Milliliter": 284.131, "Imperial gallon": 0.0625, "Imperial quart": 0.25, "Imperial pint": 0.5, "Imperial cup": 1, "Imperial fluid ounce": 10, "Imperial tablespoon": 16, "Imperial teaspoon": 48, "Cubic foot": 0.0100339, "Cubic inch": 17.3387},
        "Imperial fluid ounce": {"US liquid gallon": 0.00750594, "US liquid quart": 0.0300237, "US liquid pint": 0.0600475, "US legal cup": 0.120095, "US fluid ounce": 0.96076, "US tablespoon": 1.92152, "US teaspoon": 5.76456, "Cubic meter": 2.84131e-05, "Liter": 0.0284131, "Milliliter": 28.4131, "Imperial gallon": 0.00625, "Imperial quart": 0.025, "Imperial pint": 0.05, "Imperial cup": 0.1, "Imperial fluid ounce": 1, "Imperial tablespoon": 1.6, "Imperial teaspoon": 4.8, "Cubic foot": 0.00100339, "Cubic inch": 1.73387},
        "Imperial tablespoon": {"US liquid gallon": 0.00469121, "US liquid quart": 0.0187648, "US liquid pint": 0.0375296, "US legal cup": 0.0750594, "US fluid ounce": 0.600475, "US tablespoon": 1.20095, "US teaspoon": 3.60285, "Cubic meter": 1.77582e-05, "Liter": 0.0177582, "Milliliter": 17.7582, "Imperial gallon": 0.00390625, "Imperial quart": 0.015625, "Imperial pint": 0.03125, "Imperial cup": 0.0625, "Imperial fluid ounce": 0.625, "Imperial tablespoon": 1, "Imperial teaspoon": 3, "Cubic foot": 0.000627116, "Cubic inch": 1.08367},
        "Imperial teaspoon": {"US liquid gallon": 0.00156374, "US liquid quart": 0.00625497, "US liquid pint": 0.0125099, "US legal cup": 0.0250197, "US fluid ounce": 0.200158, "US tablespoon": 0.400317, "US teaspoon": 1.20095, "Cubic meter": 5.91939e-06, "Liter": 0.00591939, "Milliliter": 5.91939, "Imperial gallon": 0.00130208, "Imperial quart": 0.00520833, "Imperial pint": 0.0104167, "Imperial cup": 0.0208333, "Imperial fluid ounce": 0.208333, "Imperial tablespoon": 0.333333, "Imperial teaspoon": 1, "Cubic foot": 0.000209039, "Cubic inch": 0.361224},
        "Cubic foot": {"US liquid gallon": 7.48052, "US liquid quart": 29.9221, "US liquid pint": 59.8442, "US legal cup": 119.688, "US fluid ounce": 957.506, "US tablespoon": 1915.01, "US teaspoon": 5745.04, "Cubic meter": 0.0283168, "Liter": 28.3168, "Milliliter": 28316.8, "Imperial gallon": 6.22884, "Imperial quart": 24.9153, "Imperial pint": 49.8307, "Imperial cup": 99.6614, "Imperial fluid ounce": 996.614, "Imperial tablespoon": 1594.58, "Imperial teaspoon": 4783.75, "Cubic foot": 1, "Cubic inch": 1728},
        "Cubic inch": {"US liquid gallon": 0.004329, "US liquid quart": 0.017316, "US liquid pint": 0.034632, "US legal cup": 0.0682794, "US fluid ounce": 0.554113, "US tablespoon": 1.10823, "US teaspoon": 3.32468, "Cubic meter": 1.6387e-5, "Liter": 0.0163871, "Milliliter": 16.3871, "Imperial gallon": 0.00360465, "Imperial quart": 0.0144186, "Imperial pint": 0.0288372, "Imperial cup": 0.0576744, "Imperial fluid ounce": 0.576744, "Imperial tablespoon": 0.92279, "Imperial teaspoon": 2.76837, "Cubic foot": 0.000578704, "Cubic inch": 1},
    },
    "Temperature": {
        "Celsius": {"Celsius": 1, "Kelvin": 273.15, "Fahrenheit": 1.8},
        "Kelvin": {"Celsius": -273.15, "Kelvin": 1, "Fahrenheit": 1.8},
        "Fahrenheit": {"Celsius": 5/9, "Kelvin": 5/9, "Fahrenheit": 1}
    },
    "Area": {
        "Square Meter": {"Square Meter": 1, "Square Kilometer": 1e-6, "Square Centimeter": 1e4, "Square Millimeter": 1e6, "Square Micrometer": 1e12, "Hectare": 1e-4, "Square Mile": 3.861e-7, "Square Yard": 1.196, "Square Foot": 10.764, "Square Inch": 1550, "Acre": 0.000247105},
        "Square Kilometer": {"Square Meter": 1e6, "Square Kilometer": 1, "Square Centimeter": 1e8, "Square Millimeter": 1e12, "Square Micrometer": 1e18, "Hectare": 100, "Square Mile": 0.386102, "Square Yard": 1.196e6, "Square Foot": 1.076e7, "Square Inch": 1.55e9, "Acre": 247.105},
        "Square Centimeter": {"Square Meter": 1e-4, "Square Kilometer": 1e-8, "Square Centimeter": 1, "Square Millimeter": 100, "Square Micrometer": 1e8, "Hectare": 1e-6, "Square Mile": 3.861e-10, "Square Yard": 1.196e-2, "Square Foot": 1.076e-1, "Square Inch": 1.55e1, "Acre": 2.471e-5},
        "Square Millimeter": {"Square Meter": 1e-6, "Square Kilometer": 1e-12, "Square Centimeter": 1e-2, "Square Millimeter": 1, "Square Micrometer": 1e4, "Hectare": 1e-8, "Square Mile": 3.861e-13, "Square Yard": 1.196e-6, "Square Foot": 1.076e-5, "Square Inch": 1.55e-3, "Acre": 2.471e-9},
        "Square Micrometer": {"Square Meter": 1e-12, "Square Kilometer": 1e-18, "Square Centimeter": 1e-8, "Square Millimeter": 1e-4, "Square Micrometer": 1, "Hectare": 1e-16, "Square Mile": 3.861e-19, "Square Yard": 1.196e-12, "Square Foot": 1.076e-11, "Square Inch": 1.55e-9, "Acre": 2.471e-15},
        "Hectare": {"Square Meter": 1e4, "Square Kilometer": 1e-2, "Square Centimeter": 1e6, "Square Millimeter": 1e10, "Square Micrometer": 1e16, "Hectare": 1, "Square Mile": 3.861e-5, "Square Yard": 1.196e4, "Square Foot": 1.076e5, "Square Inch": 1.55e7, "Acre": 2.471},
        "Square Mile": {"Square Meter": 2.59e6, "Square Kilometer": 2.59, "Square Centimeter": 2.59e8, "Square Millimeter": 2.59e12, "Square Micrometer": 2.59e18, "Hectare": 2.59e4, "Square Mile": 1, "Square Yard": 3.098e6, "Square Foot": 2.788e7, "Square Inch": 4.014e9, "Acre": 640},
        "Square Yard": {"Square Meter": 0.8361, "Square Kilometer": 8.361e-7, "Square Centimeter": 8361, "Square Millimeter": 8.361e6, "Square Micrometer": 8.361e12, "Hectare": 8.361e-5, "Square Mile": 3.861e-7, "Square Yard": 1, "Square Foot": 9, "Square Inch": 1296, "Acre": 0.000206612},
        "Square Foot": {"Square Meter": 0.0929, "Square Kilometer": 9.29e-8, "Square Centimeter": 929, "Square Millimeter": 9.29e5, "Square Micrometer": 9.29e11, "Hectare": 9.29e-6, "Square Mile": 3.861e-8, "Square Yard": 0.1111, "Square Foot": 1, "Square Inch": 144, "Acre": 2.295e-5},
        "Square Inch": { "Square Meter": 0.00064516, "Square Kilometer": 6.4516e-10, "Square Centimeter": 6.4516, "Square Millimeter": 645.16, "Square Micrometer": 6.4516e6, "Hectare": 6.4516e-8, "Square Mile": 2.491e-10, "Square Yard": 0.000771, "Square Foot": 0.00694444, "Square Inch": 1, "Acre": 1.595e-7},
        "Acre": { "Square Meter": 4046.86, "Square Kilometer": 4.047e-3, "Square Centimeter": 4.047e4, "Square Millimeter": 4.047e8, "Square Micrometer": 4.047e14, "Hectare": 0.4047, "Square Mile": 1.5625e-3, "Square Yard": 4840, "Square Foot": 43560, "Square Inch": 6272640, "Acre": 1}
    },
    "Speed": {
        "Meters per second": {"Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.23694, "Feet per second": 3.28084, "Knots": 1.94384},
        "Kilometers per hour": {"Meters per second": 0.277778, "Kilometers per hour": 1, "Miles per hour": 0.621371, "Feet per second": 0.911344, "Knots": 0.53996},
        "Miles per hour": {"Meters per second": 0.44704, "Kilometers per hour": 1.60934, "Miles per hour": 1, "Feet per second": 1.46667, "Knots": 0.869},
        "Feet per second": {"Meters per second": 0.3048, "Kilometers per hour": 1.09728, "Miles per hour": 0.681818, "Feet per second": 1, "Knots": 0.592484},
        "Knots": {"Meters per second": 0.514444, "Kilometers per hour": 1.852, "Miles per hour": 1.15078, "Feet per second": 1.68781, "Knots": 1}
    },
    "Time": {
        "Nanosecond": {"Nanosecond": 1, "Microsecond": 1e-3, "Millisecond": 1e-6, "Second": 1e-9, "Minute": 1e-9/60, "Hour": 1e-9/3600, "Day": 1e-9/86400, "Week": 1e-9/604800, "Month": 1e-9/2592000, "Year": 1e-9/31536000, "Decade": 1e-9/315360000, "Century": 1e-9/3153600000},
        "Microsecond": {"Nanosecond": 1e3, "Microsecond": 1, "Millisecond": 1e-3, "Second": 1e-6, "Minute": 1e-6/60, "Hour": 1e-6/3600, "Day": 1e-6/86400, "Week": 1e-6/604800, "Month": 1e-6/2592000, "Year": 1e-6/31536000, "Decade": 1e-6/315360000, "Century": 1e-6/3153600000},
        "Millisecond": {"Nanosecond": 1e6, "Microsecond": 1e3, "Millisecond": 1, "Second": 1e-3, "Minute": 1e-3/60, "Hour": 1e-3/3600, "Day": 1e-3/86400, "Week": 1e-3/604800, "Month": 1e-3/2592000, "Year": 1e-3/31536000, "Decade": 1e-3/315360000, "Century": 1e-3/3153600000},
        "Second": {"Nanosecond": 1e9, "Microsecond": 1e6, "Millisecond": 1e3, "Second": 1, "Minute": 1/60, "Hour": 1/3600, "Day": 1/86400, "Week": 1/604800, "Month": 1/2592000, "Year": 1/31536000, "Decade": 1/315360000, "Century": 1/3153600000},
        "Minute": {"Nanosecond": 1e9/60, "Microsecond": 1e6/60, "Millisecond": 1e3/60, "Second": 60, "Minute": 1, "Hour": 1/60, "Day": 1/1440, "Week": 1/10080, "Month": 1/43200, "Year": 1/525600, "Decade": 1/5256000, "Century": 1/52560000},
        "Hour": {"Nanosecond": 1e9/3600, "Microsecond": 1e6/3600, "Millisecond": 1e3/3600, "Second": 3600, "Minute": 60, "Hour": 1, "Day": 1/24, "Week": 1/168, "Month": 1/730.484, "Year": 1/8760, "Decade": 1/87600, "Century": 1/876000},
        "Day": {"Nanosecond": 1e9/86400, "Microsecond": 1e6/86400, "Millisecond": 1e3/86400, "Second": 86400, "Minute": 1440, "Hour": 24, "Day": 1, "Week": 1/7, "Month": 1/30.44, "Year": 1/365, "Decade": 1/3650, "Century": 1/36500},
        "Week": {"Nanosecond": 1e9/604800, "Microsecond": 1e6/604800, "Millisecond": 1e3/604800, "Second": 604800, "Minute": 10080, "Hour": 168, "Day": 7, "Week": 1, "Month": 1/4.34524, "Year": 1/52.1775, "Decade": 1/521.775, "Century": 1/5217.75},
        "Month": {"Nanosecond": 1e9/2592000, "Microsecond": 1e6/2592000, "Millisecond": 1e3/2592000, "Second": 2592000, "Minute": 43200, "Hour": 730.484, "Day": 30.44, "Week": 4.34524, "Month": 1, "Year": 1/12, "Decade": 1/120, "Century": 1/1200},
        "Year": {"Nanosecond": 1e9/31536000, "Microsecond": 1e6/31536000, "Millisecond": 1e3/31536000, "Second": 31536000, "Minute": 525600, "Hour": 8760, "Day": 365, "Week": 52.1775, "Month": 12, "Year": 1, "Decade": 1/10, "Century": 1/100},
        "Decade": {"Nanosecond": 1e9/315360000, "Microsecond": 1e6/315360000, "Millisecond": 1e3/315360000, "Second": 315360000, "Minute": 5256000, "Hour": 87600, "Day": 3650, "Week": 521.775, "Month": 120, "Year": 10, "Decade": 1, "Century": 1/10},
        "Century": {"Nanosecond": 1e9/3153600000, "Microsecond": 1e6/3153600000, "Millisecond": 1e3/3153600000, "Second": 3153600000, "Minute": 52560000, "Hour": 876000, "Day": 36500, "Week": 5217.75, "Month": 1200, "Year": 100, "Decade": 10, "Century": 1}
    },
    "Angle": {
        "Degrees": {"Degrees": 1, "Gradians": 10/9, "Radians": 3.14159/180, "Arcsecond": 3600, "Milliradian": 0.00174533, "Minute of arc": 60},
        "Gradians": {"Degrees": 9/10, "Gradians": 1, "Radians": 3.14159/200, "Arcsecond": 3240, "Milliradian": 0.0015708, "Minute of arc": 54},
        "Radians": {"Degrees": 180/3.14159, "Gradians": 200/3.14159, "Radians": 1, "Arcsecond": 206265, "Milliradian": 1000, "Minute of arc": 3438},
        "Arcsecond": {"Degrees": 1/3600, "Gradians": 1/3240, "Radians": 1/206265, "Arcsecond": 1, "Milliradian": 0.000004848, "Minute of arc": 1/60},
        "Milliradian": {"Degrees": 1/57.2958, "Gradians": 1/63.662, "Radians": 0.001, "Arcsecond": 206.265, "Milliradian": 1, "Minute of arc": 60},
        "Minute of arc": {"Degrees": 1/60, "Gradians": 1/54, "Radians": 0.0002909, "Arcsecond": 60, "Milliradian": 0.0166667, "Minute of arc": 1}
    },
    "Pressure": {
        "Bar": {"Bar": 1, "Pascal": 1e5, "Pound per square inch": 14.5038, "Standard atmosphere": 0.986923, "Torr": 750.062},
        "Pascal": {"Bar": 1e-5, "Pascal": 1, "Pound per square inch": 0.000145038, "Standard atmosphere": 9.86923e-6, "Torr": 0.00750062},
        "Pound per square inch": {"Bar": 0.0689476, "Pascal": 6894.76, "Pound per square inch": 1, "Standard atmosphere": 0.068046, "Torr": 51.7149},
        "Standard atmosphere": {"Bar": 1.01325, "Pascal": 101325, "Pound per square inch": 14.696, "Standard atmosphere": 1, "Torr": 760},
        "Torr": {"Bar": 1.33322e-3, "Pascal": 133.322, "Pound per square inch": 0.0193368, "Standard atmosphere": 0.00131579, "Torr": 1}
    },
    "Frequency": {
        "Hertz": {"Hertz": 1, "Kilohertz": 1e-3, "Megahertz": 1e-6, "Gigahertz": 1e-9},
        "Kilohertz": {"Hertz": 1e3, "Kilohertz": 1, "Megahertz": 1e-3, "Gigahertz": 1e-6},
        "Megahertz": {"Hertz": 1e6, "Kilohertz": 1e3, "Megahertz": 1, "Gigahertz": 1e-3},
        "Gigahertz": {"Hertz": 1e9, "Kilohertz": 1e6, "Megahertz": 1e3, "Gigahertz": 1}
    },
    "Energy": {
        "Joule": {"Joule": 1, "Kilojoule": 1e-3, "Gram calorie": 0.239006, "Kilocalorie": 0.000239006, "Watt hour": 2.77778e-4, "Kilowatt-hour": 2.77778e-7, "Electronvolt": 6.242e+18, "British thermal unit": 9.478e-2, "US therm": 9.478e-6, "Foot-pound": 0.737562},
        "Kilojoule": {"Joule": 1000, "Kilojoule": 1, "Gram calorie": 239.006, "Kilocalorie": 0.239006, "Watt hour": 0.277778, "Kilowatt-hour": 2.77778e-4, "Electronvolt": 6.242e+21, "British thermal unit": 0.9478, "US therm": 9.478e-4, "Foot-pound": 737.562},
        "Gram calorie": {"Joule": 4.184, "Kilojoule": 4.184e-3, "Gram calorie": 1, "Kilocalorie": 0.001, "Watt hour": 1.1622e-3, "Kilowatt-hour": 1.1622e-6, "Electronvolt": 2.611e+19, "British thermal unit": 3.968e-4, "US therm": 3.968e-8, "Foot-pound": 0.003087},
        "Kilocalorie": {"Joule": 4184, "Kilojoule": 4.184, "Gram calorie": 1000, "Kilocalorie": 1, "Watt hour": 1.1622e-1, "Kilowatt-hour": 1.1622e-4, "Electronvolt": 2.611e+22, "British thermal unit": 3.968e-1, "US therm": 3.968e-5, "Foot-pound": 3.087},
        "Watt hour": {"Joule": 3600, "Kilojoule": 3.6, "Gram calorie": 860.421, "Kilocalorie": 0.860421, "Watt hour": 1, "Kilowatt-hour": 0.001, "Electronvolt": 2.611e+21, "British thermal unit": 3.412e-1, "US therm": 3.412e-4, "Foot-pound": 737.562},
        "Kilowatt-hour": {"Joule": 3.6e6, "Kilojoule": 3600, "Gram calorie": 8.60421e+5, "Kilocalorie": 860.421, "Watt hour": 1000, "Kilowatt-hour": 1, "Electronvolt": 2.611e+24, "British thermal unit": 3412, "US therm": 0.03412, "Foot-pound": 737562},
        "Electronvolt": {"Joule": 1.60218e-19, "Kilojoule": 1.60218e-22, "Gram calorie": 3.8e-20, "Kilocalorie": 3.8e-23, "Watt hour": 4.4505e-23, "Kilowatt-hour": 4.4505e-26, "Electronvolt": 1, "British thermal unit": 3.8e-21, "US therm": 3.8e-25, "Foot-pound": 4.4505e-22},
        "British thermal unit": {"Joule": 1055.06, "Kilojoule": 1.05506, "Gram calorie": 252.164, "Kilocalorie": 0.252164, "Watt hour": 2.9307, "Kilowatt-hour": 2.9307e-3, "Electronvolt": 2.611e+22, "British thermal unit": 1, "US therm": 9.478e-3, "Foot-pound": 778.169},
        "US therm": {"Joule": 1.05506e+7, "Kilojoule": 1.05506e+4, "Gram calorie": 2.52164e+6, "Kilocalorie": 2521.64, "Watt hour": 29307, "Kilowatt-hour": 29.307, "Electronvolt": 2.611e+25, "British thermal unit": 100, "US therm": 1, "Foot-pound": 7.78169e+6},
        "Foot-pound": {"Joule": 1.35582, "Kilojoule": 0.00135582, "Gram calorie": 0.32405, "Kilocalorie": 0.00032405, "Watt hour": 0.00135582, "Kilowatt-hour": 1.35582e-6, "Electronvolt": 3.055e+19, "British thermal unit": 1.35582e-3, "US therm": 1.35582e-9, "Foot-pound": 1}
    },
    "Digital Storage": {
        "bit": {"bit": 1, "kilobit": 1e-3, "kibibit": 0.000976563, "megabit": 1e-6, "mebibit": 9.5367e-7, "gigabit": 1e-9, "gibibit": 9.3132e-10, "terabit": 1e-12, "tebibit": 9.0949e-13, "petabit": 1e-15, "pebibit": 8.8818e-16, "byte": 0.125, "kilobyte": 0.000125, "kibibyte": 0.00012207, "megabyte": 1.25e-7, "mebibyte": 1.1921e-7, "gigabyte": 1.25e-10, "gibibyte": 1.1642e-10, "terabyte": 1.25e-13, "tebibyte": 1.1369e-13, "petabyte": 1.25e-16, "pebibyte": 1.1102e-16},
        "kilobit": {"bit": 1000, "kilobit": 1, "kibibit": 0.976563, "megabit": 1e-3, "mebibit": 0.000953674, "gigabit": 1e-6, "gibibit": 9.3132e-7, "terabit": 1e-9, "tebibit": 9.0949e-10, "petabit": 1e-12, "pebibit": 8.8818e-13, "byte": 1/8000, "kilobyte": 0.125, "kibibyte": 0.12207, "megabyte": 1.25e-6, "mebibyte": 0.000119209, "gigabyte": 1.25e-9, "gibibyte": 1.1642e-7, "terabyte": 1.25e-12, "tebibyte": 1.1369e-10, "petabyte": 1.25e-15, "pebibyte": 1.1102e-13},
        "kibibit": {"bit": 1024, "kilobit": 1.024, "kibibit": 1, "megabit": 0.001024, "mebibit": 0.000976563, "gigabit": 1.024e-6, "gibibit": 9.5367e-7, "terabit": 1.024e-9, "tebibit": 9.3132e-10, "petabit": 1.024e-12, "pebibit": 9.0949e-13, "byte": 128, "kilobyte": 0.128, "kibibyte": 0.125, "megabyte": 0.000128, "mebibyte": 0.00012207, "gigabyte": 1.28e-70, "gibibyte": 1.1921e-7, "terabyte": 1.28e-10, "tebibyte": 1.1642e-10, "petabyte": 1.28e-13, "pebibyte": 1.1369e-13},
        "megabit": {"bit": 1e6, "kilobit": 1000, "kibibit": 976.563, "megabit": 1, "mebibit": 0.953674, "gigabit": 1e-3, "gibibit": 0.000931323, "terabit": 1e-6, "tebibit": 9.0949e-7, "petabit": 1e-9, "pebibit": 8.8818e-10, "byte": 125000, "kilobyte": 125, "kibibyte": 122.07, "megabyte": 0.125, "mebibyte": 0.119209, "gigabyte": 0.000125, "gibibyte": 0.000116415, "terabyte": 1.25e-7, "tebibyte": 1.1369e-7, "petabyte": 1.25e-10, "pebibyte": 1.1102e-10},
        "mebibit": {"bit": 1.049e+6, "kilobit": 1048.58, "kibibit": 1024, "megabit": 1.04858, "mebibit": 1, "gigabit": 0.00104858, "gibibit": 0.000976563, "terabit": 1.0486e-6, "tebibit": 9.5367e-7, "petabit": 1.0486e-9, "pebibit": 9.3132e-10, "byte": 131072, "kilobyte": 131.072, "kibibyte": 128, "megabyte": 0.131072, "mebibyte": 0.125, "gigabyte": 0.000131072, "gibibyte": 0.00012207, "terabyte": 1.3107e-7, "tebibyte": 1.1921e-7, "petabyte": 1.3107e-10, "pebibyte": 1.1642e-10},
        "gigabit": {"bit": 1e9, "kilobit": 1e6, "kibibit": 976563, "megabit": 1000, "mebibit": 953.674, "gigabit": 1, "gibibit": 0.931323, "terabit": 0.001, "tebibit": 0.000909495, "petabit": 1e-6, "pebibit": 8.8818e-7, "byte": 1.25e8, "kilobyte": 125000, "kibibyte": 122070, "megabyte": 125, "mebibyte": 119.209, "gigabyte": 0.125, "gibibyte": 0.116415, "terabyte": 0.000125, "tebibyte": 0.000113687, "petabyte": 1.25e-7, "pebibyte": 1.1102e-7},
        "gibibit": {"bit": 1.074e+9, "kilobit": 1.074e+6, "kibibit": 1.049e+6, "megabit": 1073.74, "mebibit": 1024, "gigabit": 1.07374, "gibibit": 1, "terabit": 0.00107374, "tebibit": 0.000976563, "petabit": 1.0737e-6, "pebibit": 9.5367e-7, "byte": 1.342e+8, "kilobyte": 134218, "kibibyte": 131072, "megabyte": 134.218, "mebibyte": 128, "gigabyte": 0.134218, "gibibyte": 0.125, "terabyte": 0.000134218, "tebibyte": 0.00012207, "petabyte": 1.3422e-7, "pebibyte": 1.1921e-7},
        "terabit": {"bit": 1e12, "kilobit": 1e9, "kibibit": 9.766e+8, "megabit": 1e6, "mebibit": 953674, "gigabit": 1000, "gibibit": 931.323, "terabit": 1, "tebibit": 0.909495, "petabit": 1e-3, "pebibit": 0.000888178, "byte": 1.25e11, "kilobyte": 1.25e8, "kibibyte": 1.221e+8, "megabyte": 125000, "mebibyte": 119209, "gigabyte": 1.25, "gibibyte": 116.415, "terabyte": 0.125, "tebibyte": 0.113687, "petabyte": 0.000125, "pebibyte": 0.000111022},
        "tebibit": {"bit": 1.1e12, "kilobit": 1.1e9, "kibibit": 1.074e9, "megabit": 1.1e+6, "mebibit": 1.049e+6, "gigabit": 1099.51, "gibibit": 1024, "terabit": 1.09951, "tebibit": 1, "petabit": 0.00109951, "pebibit": 0.000976563, "byte": 1.374e11, "kilobyte": 1.374e8, "kibibyte": 1.342e8, "megabyte": 137439, "mebibyte": 131072, "gigabyte": 137.439, "gibibyte": 128, "terabyte": 0.137439, "tebibyte": 0.125, "petabyte": 0.000137439, "pebibyte": 0.00012207},
        "petabit": {"bit": 1e15, "kilobit": 1e12, "kibibit": 9.766e+11, "megabit": 1e9, "mebibit": 9.537e+8, "gigabit": 1e6, "gibibit": 931323, "terabit": 1000, "tebibit": 909.495, "petabit": 1, "pebibit": 0.888178, "byte": 1.25e14, "kilobyte": 1.25e11, "kibibyte": 1.221e11, "megabyte": 1.25e8, "mebibyte": 11.192e8, "gigabyte": 125000, "gibibyte": 116415, "terabyte": 1.25, "tebibyte": 113.687, "petabyte": 0.125, "pebibyte": 0.111022},
        "pebibit": {"bit": 1.126e15, "kilobit": 1.126e12, "kibibit": 1.1e12, "megabit": 1.126e9, "mebibit": 1.074e9, "gigabit": 1.126e6, "gibibit": 1.049e6, "terabit": 1125.9, "tebibit": 1024, "petabit": 1.1259, "pebibit": 1, "byte": 1.407e+4, "kilobyte": 1.407e11, "kibibyte": 1.374e11, "megabyte": 1.407e8, "mebibyte": 1.342e8, "gigabyte": 140737, "gibibyte": 131072, "terabyte": 140.737, "tebibyte": 128, "petabyte": 0.140737, "pebibyte": 0.125},
        "byte": {"bit": 8, "kilobit": 0.008, "kibibit": 0.0078125, "megabit": 8e-6, "mebibit": 7.6294e-6, "gigabit": 8e-9, "gibibit": 7.4506e-9, "terabit": 8e-12, "tebibit": 7.276e-12, "petabit": 8e-15, "pebibit": 7.1054e-15, "byte": 1, "kilobyte": 0.001, "kibibyte": 0.000976563, "megabyte": 1e-6, "mebibyte": 9.5367e-7, "gigabyte": 1e-9, "gibibyte": 9.3132e-10, "terabyte": 1e-12, "tebibyte": 9.0949e-13, "petabyte": 1e-15, "pebibyte": 8.8818e-16},
        "kilobyte": {"bit": 8000, "kilobit": 8, "kibibit": 7.8125, "megabit": 0.008, "mebibit": 0.00762939, "gigabit": 8e-6, "gibibit": 7.4506e-6, "terabit": 8e-9, "tebibit": 7.276e-9, "petabit": 8e-12, "pebibit": 7.1054e-12, "byte": 1000, "kilobyte": 1, "kibibyte": 0.976563, "megabyte": 0.001, "mebibyte": 0.000953674, "gigabyte": 1e-6, "gibibyte": 9.3132e-7, "terabyte": 1e-9, "tebibyte": 9.0949e-10, "petabyte": 1e-12, "pebibyte": 8.8818e-13},
        "kibibyte": {"bit": 8192, "kilobit": 8.192, "kibibit": 8, "megabit": 0.008192, "mebibit": 0.0078125, "gigabit": 8.192e-6, "gibibit": 7.6294e-6, "terabit": 8.192e-9, "tebibit": 7.4506e-9, "petabit": 8.192e-12, "pebibit": 7.276e-12, "byte": 1024, "kilobyte": 1.024, "kibibyte": 1, "megabyte": 0.001024, "mebibyte": 0.000976563, "gigabyte": 1.024e-6, "gibibyte": 9.5367e-7, "terabyte": 1.024e-9, "tebibyte": 9.3132e-10, "petabyte": 1.024e-12, "pebibyte": 9.0949e-13},
        "megabyte": {"bit": 8e6, "kilobit": 8000, "kibibit": 7812.5, "megabit": 8, "mebibit": 7.62939, "gigabit": 0.008, "gibibit": 0.00745058, "terabit": 8e-6, "tebibit": 7.276e-6, "petabit": 8e-9, "pebibit": 7.1054e-9, "byte": 1e6, "kilobyte": 1000, "kibibyte": 976.563, "megabyte": 1, "mebibyte": 0.953674, "gigabyte": 0.001, "gibibyte": 0.000931323, "terabyte": 1e-6, "tebibyte": 9.0949e-7, "petabyte": 1e-9, "pebibyte": 8.8818e-10},
        "mebibyte": {"bit": 8.389e+6, "kilobit": 8388.61, "kibibit": 8192, "megabit": 8.38861, "mebibit": 8, "gigabit": 0.00838861, "gibibit": 0.0078125, "terabit": 8.3886e-6, "tebibit": 7.6294e-6, "petabit": 8.3886e-9, "pebibit": 7.4506e-9, "byte": 1.049e+6, "kilobyte": 1048.58, "kibibyte": 1024, "megabyte": 1.04858, "mebibyte": 1, "gigabyte": 0.00104858, "gibibyte": 0.000976563, "terabyte": 1.0486e-6, "tebibyte": 9.5367e-7, "petabyte": 1.0486e-9, "pebibyte": 9.3132e-10},
        "gigabyte": {"bit": 8e9, "kilobit": 8e6, "kibibit": 7.813e+6, "megabit": 8000, "mebibit": 7629.39, "gigabit": 8, "gibibit": 7.45058, "terabit": 8e-3, "tebibit": 0.00727596, "petabit": 8e-6, "pebibit": 7.1054e-6, "byte": 1e9, "kilobyte": 1e6, "kibibyte": 976563, "megabyte": 1000, "mebibyte": 953.674, "gigabyte": 1, "gibibyte": 0.931323, "terabyte": 1e-3, "tebibyte": 0.000909495, "petabyte": 1e-6, "pebibyte": 8.8818e-7},
        "gibibyte": {"bit": 8.59e9, "kilobit": 8.59e6, "kibibit": 8.389e6, "megabit": 8589.93, "mebibit": 8192, "gigabit": 8.58993, "gibibit": 8, "terabit": 0.00858993, "tebibit": 0.0078125, "petabit": 8.5899e-6, "pebibit": 7.6294e-6, "byte": 1.074e9, "kilobyte": 1.074e6, "kibibyte": 1.049e6, "megabyte": 1073.74, "mebibyte": 1024, "gigabyte": 1.07374, "gibibyte": 1, "terabyte": 0.00107374, "tebibyte": 0.000976563, "petabyte": 1.0737e-6, "pebibyte": 9.5367e-7},
        "terabyte": {"bit": 8e12, "kilobit": 8e9, "kibibit": 7.813e9, "megabit": 8e6, "mebibit": 7.629e+6, "gigabit": 8000, "gibibit": 7450.58, "terabit": 8, "tebibit": 7.27596, "petabit": 0.008, "pebibit": 0.00710543, "byte": 1e12, "kilobyte": 1e9, "kibibyte": 9.766e+8, "megabyte": 1e6, "mebibyte": 953674, "gigabyte": 1000, "gibibyte": 931.323, "terabyte": 1, "tebibyte": 0.909495, "petabyte": 0.001, "pebibyte": 0.000888178},
        "tebibyte": {"bit": 8.796e12, "kilobit": 8.796e9, "kibibit": 8.59e9, "megabit": 8.796e6, "mebibit": 8.389e6, "gigabit": 8796.09, "gibibit": 8192, "terabit": 8.79609, "tebibit": 8, "petabit": 0.00879609, "pebibit": 0.0078125, "byte": 1.1e12, "kilobyte": 1.1e9, "kibibyte": 1.074e9, "megabyte": 1.1e6, "mebibyte": 1.049e6, "gigabyte": 1099.51, "gibibyte": 1024, "terabyte": 1.09951, "tebibyte": 1, "petabyte": 0.00109951, "pebibyte": 0.000976563},
        "petabyte": {"bit": 8e15, "kilobit": 8e12, "kibibit": 7.813e12, "megabit": 8e9, "mebibit": 7.629e9, "gigabit": 8e6, "gibibit": 7.451e6, "terabit": 8000, "tebibit": 7275.96, "petabit": 8, "pebibit": 7.10543, "byte": 1e15, "kilobyte": 1e12, "kibibyte": 9.766e11, "megabyte": 1e9, "mebibyte": 9.537e8, "gigabyte": 1e6, "gibibyte": 931323, "terabyte": 1000, "tebibyte": 909.495, "petabyte": 1, "pebibyte": 0.888178},
        "pebibyte": {"bit": 9.007e15, "kilobit": 9.007e12, "kibibit": 8.796e12, "megabit": 9.007e9, "mebibit": 8.59e9, "gigabit": 9.007e6, "gibibit": 8.389e6, "terabit": 9007.2, "tebibit": 8192, "petabit": 9.0072, "pebibit": 8, "byte": 1.126e15, "kilobyte": 1.126e12, "kibibyte": 1.1e12, "megabyte": 1.126e9, "mebibyte": 1.074e9, "gigabyte": 1.126e6, "gibibyte": 1.049e6, "terabyte": 1125.9, "tebibyte": 1024, "petabyte": 1.1259, "pebibyte": 1}
    },
    "Data Transfer Rate": {
        "Bit per second": {"Bit per second": 1, "Kilobit per second": 1e-3, "Kilobyte per second": 1.25e-4, "Kibibit per second": 1e-3, "Megabit per second": 1e-6, "Megabyte per second": 1.25e-7, "Mebibit per second": 9.5367e-7, "Gigabit per second": 1e-9, "Gigabyte per second": 1.25e-10, "Gibibit per second": 9.3132e-10, "Terabit per second": 1e-12, "Terabyte per second": 1.25e-13, "Tebibit per second": 9.0949e-13},
        "Kilobit per second": {"Bit per second": 1000, "Kilobit per second": 1, "Kilobyte per second": 0.125, "Kibibit per second": 1, "Megabit per second": 1e-3, "Megabyte per second": 1.25e-4, "Mebibit per second": 9.5367e-4, "Gigabit per second": 1e-6, "Gigabyte per second": 1.25e-7, "Gibibit per second": 9.3132e-7, "Terabit per second": 1e-9, "Terabyte per second": 1.25e-10, "Tebibit per second": 9.0949e-10},
        "Kilobyte per second": {"Bit per second": 8000, "Kilobit per second": 8, "Kilobyte per second": 1, "Kibibit per second": 7.8125, "Megabit per second": 8e-3, "Megabyte per second": 1e-3, "Mebibit per second": 7.6294e-4, "Gigabit per second": 8e-6, "Gigabyte per second": 1e-6, "Gibibit per second": 7.4506e-7, "Terabit per second": 8e-9, "Terabyte per second": 1e-9, "Tebibit per second": 7.276e-10},
        "Kibibit per second": {"Bit per second": 1000, "Kilobit per second": 1, "Kilobyte per second": 0.128, "Kibibit per second": 1, "Megabit per second": 1e-3, "Megabyte per second": 1.25e-4, "Mebibit per second": 1, "Gigabit per second": 1e-6, "Gigabyte per second": 1.25e-7, "Gibibit per second": 1e-6, "Terabit per second": 1e-9, "Terabyte per second": 1.25e-10, "Tebibit per second": 9.3132e-10},
        "Megabit per second": {"Bit per second": 1e6, "Kilobit per second": 1000, "Kilobyte per second": 125, "Kibibit per second": 1000, "Megabit per second": 1, "Megabyte per second": 0.125, "Mebibit per second": 0.95367, "Gigabit per second": 1e-3, "Gigabyte per second": 1.25e-4, "Gibibit per second": 9.3132e-5, "Terabit per second": 1e-6, "Terabyte per second": 1.25e-7, "Tebibit per second": 9.0949e-7},
        "Megabyte per second": {"Bit per second": 8e6, "Kilobit per second": 8000, "Kilobyte per second": 1000, "Kibibit per second": 7812.5, "Megabit per second": 8, "Megabyte per second": 1, "Mebibit per second": 7.6294, "Gigabit per second": 8e-3, "Gigabyte per second": 1e-3, "Gibibit per second": 7.4506e-4, "Terabit per second": 8e-6, "Terabyte per second": 1e-6, "Tebibit per second": 7.276e-7},
        "Mebibit per second": {"Bit per second": 1e6, "Kilobit per second": 1000, "Kilobyte per second": 125, "Kibibit per second": 1000, "Megabit per second": 1.0486, "Megabyte per second": 1.3107e-1, "Mebibit per second": 1, "Gigabit per second": 1e-3, "Gigabyte per second": 1.25e-4, "Gibibit per second": 1e-3, "Terabit per second": 1e-6, "Terabyte per second": 1.25e-7, "Tebibit per second": 9.3132e-7},
        "Gigabit per second": {"Bit per second": 1e9, "Kilobit per second": 1e6, "Kilobyte per second": 125000, "Kibibit per second": 1000000, "Megabit per second": 1000, "Megabyte per second": 125, "Mebibit per second": 1024, "Gigabit per second": 1, "Gigabyte per second": 0.125, "Gibibit per second": 0.093132, "Terabit per second": 1e-3, "Terabyte per second": 1.25e-4, "Tebibit per second": 9.3132e-4},
        "Gigabyte per second": {"Bit per second": 8e9, "Kilobit per second": 8e6, "Kilobyte per second": 1000000, "Kibibit per second": 7812500, "Megabit per second": 8000, "Megabyte per second": 1000, "Mebibit per second": 7812.5, "Gigabit per second": 8, "Gigabyte per second": 1, "Gibibit per second": 0.74506, "Terabit per second": 8e-3, "Terabyte per second": 1e-3, "Tebibit per second": 7.276e-4},
        "Gibibit per second": {"Bit per second": 1e9, "Kilobit per second": 1e6, "Kilobyte per second": 125000, "Kibibit per second": 1000000, "Megabit per second": 1000, "Megabyte per second": 125, "Mebibit per second": 1024, "Gigabit per second": 1.0737, "Gigabyte per second": 1.341, "Gibibit per second": 1, "Terabit per second": 1e-3, "Terabyte per second": 1.25e-4, "Tebibit per second": 0.9766},
        "Terabit per second": {"Bit per second": 1e12, "Kilobit per second": 1e9, "Kilobyte per second": 125000000, "Kibibit per second": 1000000000, "Megabit per second": 1e6, "Megabyte per second": 1.25e5, "Mebibit per second": 1.024e6, "Gigabit per second": 1000, "Gigabyte per second": 125, "Gibibit per second": 931.32, "Terabit per second": 1, "Terabyte per second": 0.125, "Tebibit per second": 0.9766},
        "Terabyte per second": {"Bit per second": 8e12, "Kilobit per second": 8e9, "Kilobyte per second": 1000000000, "Kibibit per second": 7812500000, "Megabit per second": 8e6, "Megabyte per second": 1e6, "Mebibit per second": 7812500, "Gigabit per second": 8000, "Gigabyte per second": 1000, "Gibibit per second": 745.06, "Terabit per second": 8, "Terabyte per second": 1, "Tebibit per second": 7.276e-4},
        "Tebibit per second": {"Bit per second": 1.0995e12, "Kilobit per second": 1.0995e9, "Kilobyte per second": 1374375000, "Kibibit per second": 10995000000, "Megabit per second": 1.0995e6, "Megabyte per second": 1374375, "Mebibit per second": 1073742, "Gigabit per second": 1099.5, "Gigabyte per second": 137.44, "Gibibit per second": 1.3422, "Terabit per second": 1.0995, "Terabyte per second": 0.13744, "Tebibit per second": 1}
    }
}

def convert_units(category, entry, from_var, to_var, result_label):
    try:
        value = float(entry.get())
        from_unit = from_var.get()
        to_unit = to_var.get()
        factor = conversion_factors[category][from_unit][to_unit]
        result = value * factor
        result_label.config(text=f"Converted: {result:.4f} {to_unit}")
    except ValueError:
        result_label.config(text="Palun sisesta päris number")
    except KeyError:
        result_label.config(text="Kehtetu teisendus")

# Main ekraani set up
root = tk.Tk()
root.title("Measure Perfect")

# Tab'ide notebook
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Tab'i tegemis funktsioon
def create_conversion_tab(category):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=category)

    # Input sektsioon
    tk.Label(tab, text="Enter value:").grid(row=0, column=0, padx=10, pady=5)
    entry = tk.Entry(tab)
    entry.grid(row=0, column=1, padx=10, pady=5)

    # From ühiku dropdown
    tk.Label(tab, text="From:").grid(row=1, column=0, padx=10, pady=5)
    from_var = tk.StringVar(value=list(conversion_factors[category].keys())[0])
    from_menu = ttk.Combobox(tab, textvariable=from_var, values=list(conversion_factors[category].keys()))
    from_menu.grid(row=1, column=1, padx=10, pady=5)

    # To ühiku dropdown
    tk.Label(tab, text="To:").grid(row=2, column=0, padx=10, pady=5)
    to_var = tk.StringVar(value=list(conversion_factors[category].keys())[0])
    to_menu = ttk.Combobox(tab, textvariable=to_var, values=list(conversion_factors[category].keys()))
    to_menu.grid(row=2, column=1, padx=10, pady=5)

    # Convert nupp
    result_label = tk.Label(tab, text="Converted: ", font=("Arial", 14))
    result_label.grid(row=4, column=0, columnspan=2, pady=10)

    convert_button = tk.Button(
        tab, text="Convert",
        command=lambda: convert_units(category, entry, from_var, to_var, result_label)
    )
    convert_button.grid(row=3, column=0, columnspan=2, pady=10)

# teeb tabid igale conversionile
for category in conversion_factors.keys():
    create_conversion_tab(category)

root.update()
# runnib tkinteri mainloopi
root.mainloop()
