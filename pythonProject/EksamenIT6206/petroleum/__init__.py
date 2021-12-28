import petroleum_utility as pu

# ------------------- Printed all program functions ----------------------- #

# --------------- Innlesing av dataene --------------- #

print(f"\nInnlesing av dataene funksjonen:\n{pu.les_prod_data(0)}")

# ---------- Gjennomsnitts produksjonen av et produkt for en bestemt periode -------- #

gjennomsnitt = pu.beregn_gjennomsnitt("Olje", 2001, 2010)
print(f"\nGjennomsnitts produksjonen av et produkt for en bestemt periode: {gjennomsnitt}")

# ------ Maks verdi for et gitt produkt med retur av hvilket år det var maks produksjon ------- #

maks_olje = pu.finn_maks("Olje")
print(f"\n{maks_olje}")

# -------- Arealet under grafen for et gitt produkt og for en gitt periode --------- #

areal = pu.beregn_areal_trapz("Olje", 2001, 2010)
print(f"\nArealet under grafen for et gitt produkt: {areal}")

# --- Prosentandel av olje, Gass, Kondensat og NGL i forhold til total oljeekvivalenter for en gitt periode --- #

prosent_andel = pu.prosentandel_av_alle_produktene(2001, 2010)
print(f"\n{prosent_andel}")

# ---------  Årlig produksjon (Figur) ------------- #
pu.stack_plot()
