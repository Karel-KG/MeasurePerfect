import tkinter as tk
from tkinter import ttk

# Conversion factors for different categories
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
    }# Add more categories as needed
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
        result_label.config(text="Palun sisesat päris number")
    except KeyError:
        result_label.config(text="Kehtetu teisendus")

# Set up the main window
root = tk.Tk()
root.title("Measure Perfect")

# Create notebook for tabs
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Function to create a tab
def create_conversion_tab(category):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=category)

    # Input field
    tk.Label(tab, text="Enter value:").grid(row=0, column=0, padx=10, pady=5)
    entry = tk.Entry(tab)
    entry.grid(row=0, column=1, padx=10, pady=5)

    # From unit dropdown
    tk.Label(tab, text="From:").grid(row=1, column=0, padx=10, pady=5)
    from_var = tk.StringVar(value=list(conversion_factors[category].keys())[0])
    from_menu = ttk.Combobox(tab, textvariable=from_var, values=list(conversion_factors[category].keys()))
    from_menu.grid(row=1, column=1, padx=10, pady=5)

    # To unit dropdown
    tk.Label(tab, text="To:").grid(row=2, column=0, padx=10, pady=5)
    to_var = tk.StringVar(value=list(conversion_factors[category].keys())[0])
    to_menu = ttk.Combobox(tab, textvariable=to_var, values=list(conversion_factors[category].keys()))
    to_menu.grid(row=2, column=1, padx=10, pady=5)

    # Convert button
    result_label = tk.Label(tab, text="Converted: ", font=("Arial", 14))
    result_label.grid(row=4, column=0, columnspan=2, pady=10)

    convert_button = tk.Button(
        tab, text="Convert",
        command=lambda: convert_units(category, entry, from_var, to_var, result_label)
    )
    convert_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create tabs for each category
for category in conversion_factors.keys():
    create_conversion_tab(category)

# Run the Tkinter event loop
root.mainloop()
