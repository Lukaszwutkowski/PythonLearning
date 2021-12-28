from prisindeks import produsentprisindeksen

prod_index = produsentprisindeksen

print(prod_index.read_all_data())

print("Maks:", prod_index.hent_maks_indeks())

print("Gjennomsnitt:", prod_index.beregn_gjennomsnitt_indeks())

#prod_index.line_plot_index()
#prod_index.pris_indeks_av_tid()
prod_index.maanedsendring_for_indeksen()

