import re

text = "Ærede President, Folkets representanter. Jeg hilser Stortinget velkommen til ansvarsfullt arbeid og ønsker at " \
       "det må bli til gagn for fedrelandet. Den 22 januar ble regjeringen utvidet med Kristelig Folkeparti. Til " \
       "grunn for utvidelsen ligger den politiske plattformen partiene ble enige om på Granavolden. Plattformen " \
       "beskriver regjeringens mål om å skape et bærekraftig velferdssamfunn. Skal vi lykkes, må flere komme i " \
       "arbeid. Det skal bo og arbeide folk i hele landet. Da trenger vi flere arbeidsplasser og mer næringsvennlig " \
       "politikk. Regjeringen vil følge opp strategien for små og mellomstore bedrifter. Regjeringen vil redusere " \
       "næringslivets kostnader ved å forenkle rapportering, lover og regler. Målet er 10 milliarder kroner i " \
       "perioden 2017–2021. Regjeringen vil fortsette satsingen på forskning, infrastruktur og et skattesystem som " \
       "fremmer vekst. Norge er en ledende havnasjon. Den oppdaterte havstrategien, «Blå muligheter», ble lagt frem " \
       "før sommeren. Regjeringen vil gjøre Norge til et laboratorium for blå næringer og grønn ferdsel til havs. " \
       "Regjeringen vil legge frem en melding om den maritime politikken. Flere må kvalifiseres til de nye jobbene. " \
       "Flere innvandrere må inkluderes i arbeidsmarkedet gjennom bedre integrering. Vi må også inkludere flere som " \
       "står utenfor arbeidslivet av andre årsaker. Regjeringen vil styrke arbeidet med kompetansereformen «Lære hele " \
       "livet» og følge opp integreringsløftet og inkluderingsdugnaden. Regjeringen vil iverksette en " \
       "likeverdsreform. Målet er å gjøre hverdagen enklere for familier som venter eller har barn med behov for " \
       "sammensatte tjenester. Blant tiltakene er å forenkle krav til dokumentasjon for ulike hjelpemidler for å " \
       "unngå unødig dokumentasjon ved kroniske eller medfødte tilstander. Et viktig mål i Granavolden-plattformen er " \
       "å sikre at kommende generasjoner skal ha like gode muligheter som oss. Nye varmerekorder verden over, " \
       "svekket naturmangfold og et klima i endring også her hjemme understreker alvoret. Norge skal ta sin del av " \
       "ansvaret for å løse klimautfordringene. Utfordringene må løses gjennom globalt samarbeid. Vi skal nå våre " \
       "klimamål i samarbeid med EU. Regjeringen vil legge til rette for fortsatt utskifting av bilparken og følge " \
       "opp handlingsplanen for grønn skipsfart. Forslag om å åpne områder til havs for vindkraft er sendt på høring. " \
       "Regjeringen arbeider videre med fullskala CO2-håndtering. Det tas sikte på å fremme en sak for Stortinget i " \
       "2020 eller 2021. Internasjonalt vil regjeringen trappe opp arbeidet med klimatilpasning og forebygging av " \
       "naturkatastrofer. Sosial bærekraft er et viktig mål i Granavolden-plattformen. Regjeringen vil beholde et " \
       "samfunn med små forskjeller og tillit mellom folk. Fattigdom og utenforskap skal bekjempes. Regjeringens " \
       "viktigste strategi er å få flere i arbeid. Arbeid forebygger fattigdom og utjevner sosiale forskjeller. En " \
       "god skole og kunnskap er det viktigste for å skape muligheter for alle. Skolens innhold fornyes. Høsten 2020 " \
       "tas nye læreplaner i bruk. Politikken som føres må støtte opp om familiene og deres mulighet til å organisere " \
       "sine egne liv. Regjeringen vil øke barnetrygden for de minste barna. For barn mellom seks og 18 år, " \
       "vil regjeringen prøve ut en ordning med fritidskort. Regjeringen vil innføre redusert betaling for SFO for " \
       "elever på 1. og 2. trinn fra familier med lav inntekt. Det vil fremme deltakelse og muligheter for barn som " \
       "vokser opp i familier med lav inntekt. Innvandring er en viktig årsak til økt fattigdom og økte forskjeller i " \
       "det norske samfunnet. Regjeringen vil videreføre en restriktiv, rettssikker og ansvarlig " \
       "innvandringspolitikk. Regjeringen vil bidra til å finne løsninger for flyktninger i deres nærområder og gi " \
       "beskyttelse til mennesker med et reelt behov for dette. Regjeringen vil legge frem flere handlingsplaner for " \
       "å styrke arbeidet mot diskriminering og hatytringer. Trygghet er et viktig mål i regjeringens politiske " \
       "plattform. Trygghet skaper frihet og rom for utfoldelse. Regjeringen vil styrke beredskapen. Arbeidet med å " \
       "etablere en ny redningsbase i Troms skal starte opp. Politiet i Nord-Norge skal få sivil helikopterberedskap. " \
       "Og det skal etableres HF-dekning i nordområdene for nødkommunikasjon. Regjeringen vil prioritere å " \
       "gjennomføre politireformen. Målet om to politifolk per 1 000 innbyggere skal nås i 2020. Målet er en tryggere " \
       "hverdag og et mer effektivt politi ved å ta i bruk ny teknologi og tilpasse innsatsen til et nytt " \
       "kriminalitetsbilde. Regjeringen vil forsterke innsatsen mot kriminalitet i arbeidslivet. Regjeringen vil " \
       "legge frem en ny nasjonal helse- og sykehusplan. Målet er å realisere pasientens helsetjeneste på en " \
       "bærekraftig måte. Regjeringen vil følge opp reformen «Leve hele livet». «Leve hele livet» handler om det " \
       "grunnleggende som oftest svikter: Mat, aktivitet og fellesskap, helsehjelp og sammenheng i tjenestene. " \
       "Regjeringen vil legge til rette for bygging av flere nye plasser i eldreomsorgen. Forpliktende internasjonalt " \
       "samarbeid gjør verden tryggere og mer stabil. Verden står overfor utfordringer som er så store at ingen kan " \
       "løse dem alene. De globale bærekraftsmålene er verdens og Norges veikart. Regjeringen vil støtte opp om det " \
       "internasjonale samarbeidet i en tid der det er under press. Regjeringen vil arbeide for at EØS-avtalen " \
       "forblir en velfungerende ramme for Norges deltakelse i det felles europeiske markedet. Storbritannia vil " \
       "etter alt å dømme forlate EU og EØS, med eller uten avtale. Regjeringen har inngått avtaler som sikrer norske " \
       "borgere og næringsliv så gode og forutsigbare løsninger som mulig dersom Storbritannia forlater EU uten " \
       "avtale. Det arbeides også med langsiktige, permanente avtaler. Tilgang til store markeder er avgjørende for " \
       "norske arbeidsplasser og norsk velferd. Regjeringen vil bevilge 1 prosent av BNI til bistand. Innsatsen for å " \
       "nå bærekraftsmålene om bekjempelse av fattigdom og sult skal styrkes. Et sterkt forsvar i en sterk allianse " \
       "er avgjørende for Norges sikkerhet i en usikker tid. Regjeringen vil fortsette arbeidet med å styrke Norges " \
       "forsvarsevne. Regjeringen tar sikte på å legge frem neste langtidsplan for forsvarssektoren til våren. " \
       "NATO-solidariteten er bærebjelken i norsk sikkerhetspolitikk. Regjeringen vil fortsette å samarbeide nært med " \
       "USA, Storbritannia, Tyskland, Frankrike og våre naboland i Norden og Baltikum. Dette samarbeidet blir stadig " \
       "viktigere for å ivareta Norges sikkerhet. Regjeringen vil invitere Stortinget til et konstruktivt samarbeid " \
       "for å nå disse viktige målene for det norske samfunnet. Jeg ber Gud velsigne Stortingets arbeid, og erklærer " \
       "Norges 164. storting for åpnet. "

def number_of_words_in_text():
       word_list = text.split()
       number_of_words = len(word_list)
       print(f"There is {number_of_words} words in text")

def number_of_sentences():
       sentences_number = len(re.findall(r"[^?!.][?!.]", text))
       print("Number of sentences in text: ", sentences_number )

def avg_words_number_in_sentence():
       num_words_in_sentences = [len(l.split()) for l in re.split(r'[?!.]', text) if l.strip()]
       avg = sum(num_words_in_sentences)/len(num_words_in_sentences)
       print(f"Average number of words in sentence: {avg}")

def letter_frequency():
       letters_list = []
       ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
       for x in range(0, 26):
              letter = ALPHABET[x]
              letters_list += [(ALPHABET[x], text.count(ALPHABET[x]))]
              print(f"The letter {letter} is used: {text.count(ALPHABET[x])} times")
       print(f"The sorted list by highest number: {sorted(letters_list, key=lambda letter: letter[1], reverse=True)}")

number_of_words_in_text()
number_of_sentences()
avg_words_number_in_sentence()
letter_frequency()
