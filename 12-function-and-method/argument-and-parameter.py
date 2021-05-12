# Keyword argument
def daftar(*dates):
    print(dates)


# daftar(**{"tanggal": 1, "bulan": "Januari", "tahun": 2020})

# Positional argument
daftar(1, 'Januari', 2020)
daftar(*(1, 'Januari', 2020))
# daftar(**{1: 1, 'Januari': 'Januari', 2020: 2020})

# Anonymous function
multiply = lambda first_value, second_value: first_value * second_value

print(multiply(2, 5))
