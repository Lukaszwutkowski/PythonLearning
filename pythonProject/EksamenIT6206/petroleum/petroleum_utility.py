import pandas
import numpy as np
from numpy import trapz
import matplotlib.pyplot as plt


data = pandas.read_csv("../data/NorskPetroleum_aarlig_produksjon.csv", delimiter=";")
data = data.replace(",", ".", regex=True)
columns_list = data.columns.to_list()
produkt_list = columns_list[1:]
aar = data["Aar"].to_list()


#1a)

def les_prod_data(i):
    """Take an integer as a column number and return the new list with data from that column"""
    try:
        i = columns_list[i]
        new_list = data[i].to_list()
        return new_list
    except IndexError:
        print(f"Value is to big, please enter the value between 0 and {len(columns_list) - 1}")

#1b)

def stack_plot():
    """Function returns a graph, and use the capabilities of the les_prod_data function"""
    labels = ["Olje", "Kondensat", "NGL", "Gass", "Sum oljeekvivalenter"]
    olje = list(map(float, les_prod_data(1)))
    kondensat = list(map(float, les_prod_data(2)))
    ngl = list(map(float, les_prod_data(3)))
    gass = list(map(float, les_prod_data(4)))
    sum_oljeekvivalenter = list(map(float, les_prod_data(5)))
    data_list = [olje, kondensat, ngl, gass, sum_oljeekvivalenter]
    plt.stackplot(aar, data_list, labels=labels)
    plt.xticks(rotation=45)
    plt.legend(loc='upper left')
    plt.title('Årlig produksjon')
    plt.xlabel('År')
    plt.ylabel('Millioner Sm3 Oljeekvivalenter')
    return plt.show()

#2a)

def beregn_gjennomsnitt(produkt, fra_aar, til_aar):
    """Function returns the average production of chosen product for a specific period.
    It takes a String, which is the name of Product from the list and Integers as a years period"""
    try:
        if produkt == "NGL" or "Ngl" or "ngl":
            produkt_index = produkt_list.index("NGL")
        else:
            produkt_index = produkt_list.index(produkt.title())
    except ValueError:
        print(f"There is no {produkt} product in the list. Please chose product from the list: {produkt_list}")
    try:
        fra_indeks = aar.index(fra_aar)
        til_indeks = aar.index(til_aar)
    except ValueError:
        print(f"Please chose the year between {aar[0]} and {aar[-1]}")
    try:
        new_list = les_prod_data(produkt_index + 1)
    except UnboundLocalError as message_error:
        print(f"The value {message_error} got an error. Please chose product from the list: {produkt_list}")
    try:
        data_float = [float(i) for i in new_list[fra_indeks:til_indeks]]
        avr_result = np.mean(data_float)
        return f"{produkt}-> {np.round(avr_result, decimals=2)}"
    except UnboundLocalError as error:
        print(f"The value {error} got an error. Please chose the year between {aar[0]} and {aar[-1]}")

#2b) og 2c)

def finn_maks(product):
    """Function returns the maximum value for chosen product and shows the year when it happened.
    It takes a String with name of the product in produkt_list"""
    try:
        if product == "NGL" or "Ngl" or "ngl":
            produkt_index = produkt_list.index("NGL")
        else:
            produkt_index = produkt_list.index(product.title())
    except ValueError:
        print(f"There is no {product} product in the list. Please chose product from the list: {produkt_list}")
    try:
        new_list = les_prod_data(produkt_index + 1)
        data_float = [float(i) for i in new_list]
        maks_verdi = np.amax(data_float)
        indeks_av_maks_verdi = data_float.index(maks_verdi)
        aar_med_maks_verdi = aar[indeks_av_maks_verdi]
        return f"The maximum value for product: {product} was: {maks_verdi}, and it happened in year: {aar_med_maks_verdi}"
    except UnboundLocalError as message_error:
        print(f"The value {message_error} got an error. Please chose product from the list: {produkt_list}")

#Oppgave 3:

def beregn_areal_trapz(produkt, fra_aar, til_aar):
    """Function returns the calculated area production of chosen product for a specific period.
    It takes a String, which is the name of Product from the list and Integers as a years period"""
    try:
        if produkt == "NGL" or "Ngl" or "ngl":
            produkt_index = produkt_list.index("NGL")
        else:
            produkt_index = produkt_list.index(produkt.title())
    except ValueError:
        print(f"There is no {produkt} product in the list. Please chose product from the list: {produkt_list}")
    try:
        fra_indeks = aar.index(fra_aar)
        til_indeks = aar.index(til_aar)
    except ValueError:
        print(f"Please chose the year between {aar[0]} and {aar[-1]}")
    new_list = les_prod_data(produkt_index + 1)
    data_float = [float(i) for i in new_list[fra_indeks:til_indeks]]
    areal = trapz(data_float, dx=1)
    return areal


#Oppgave 4

def prosentandel_av_alle_produktene(fra_aar, til_aar):
    """Function calculate the percentage of all products in relation to total oil equivalents for a given period.
    It takes a Integers as a years period"""
    try:
        olje = beregn_areal_trapz("Olje", fra_aar, til_aar)
        gass = beregn_areal_trapz("Gass", fra_aar, til_aar)
        kondensat = beregn_areal_trapz("Kondensat", fra_aar, til_aar)
        ngl = beregn_areal_trapz("NGL", fra_aar, til_aar)
        sum_oljeekvivalenter = beregn_areal_trapz("Sum oljeekvivalenter", fra_aar, til_aar)
    except ValueError:
        print(f"Please chose the year between {aar[0]} and {aar[-1]}")
    prosentandel_olje = olje / sum_oljeekvivalenter * 100
    prosentandel_gass = gass / sum_oljeekvivalenter * 100
    prosentandel_kondensat = kondensat / sum_oljeekvivalenter * 100
    prosentandel_ngl = ngl / sum_oljeekvivalenter * 100
    return f"The percentage share of all products in years {fra_aar} - {til_aar}:\n" \
           f"Olje: {np.round(prosentandel_olje, decimals=2)}%\n" \
           f"Gass: {np.round(prosentandel_gass, decimals=2)}%\n" \
           f"Kondensat: {np.round(prosentandel_kondensat, decimals=2)}%\n" \
           f"NGL: {np.round(prosentandel_ngl, decimals=2)}%"
