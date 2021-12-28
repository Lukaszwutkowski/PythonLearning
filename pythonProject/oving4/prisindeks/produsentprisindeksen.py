from prisindeks import CSV_FILNAVN
import matplotlib.pyplot as plt
import pandas

data = pandas.read_csv(CSV_FILNAVN, sep=';')
data.rename(columns={'Unnamed: 0': 'Måneder'}, inplace=True)
data = data.replace(",", ".", regex=True)
date_list = []

def title_and_names():
    plt.suptitle("Produsentindeksen")
    plt.xlabel("Måneder")
    plt.ylabel("Indeks")
    for date in data["Måneder"]:
        date_list.append(date)
    plt.xticks(rotation='vertical', fontsize='xx-small')
    return date_list

def read_all_data():
    return data


def beregn_gjennomsnitt_indeks():
    data.Indeks = pandas.to_numeric(data["Indeks"], downcast="float")
    return data.Indeks.mean()


def hent_maks_indeks():
    data.Indeks = pandas.to_numeric(data["Indeks"], downcast="float")
    return data.Indeks.max()


def line_plot_index():
    plt.plot(data.Indeks)
    plt.suptitle("Produsentindeksen")
    plt.ylabel("Indeks")
    return plt.show()


def pris_indeks_av_tid():
    title_and_names()
    plt.plot(date_list, data.Indeks)
    return plt.show()

def maanedsendring_for_indeksen():
    title_and_names()
    plt.plot(date_list, data.Indeks, label="Indeks")
    plt.plot(data.Månedsendring, label="Månedsendring")
    #plt.plot(date_list, data.Indeks, data.Månedsendring)
    plt.xticks(rotation='vertical', fontsize='xx-small')
    plt.yticks()
    plt.legend()
    return plt.show()
