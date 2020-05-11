# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Progetto di Linguistica  Computazionale - A.A. 2018/2019
#   Programma 2
#   Laura Rossi - 559715

import sys
import codecs  # classe che contiene il metodo open()
import nltk  # per metodo tokenize
import collections  # per collections.Counter()
import math  # per log() di LMI
from nltk import bigrams


# tokenizza frasi e fa analisi morfosintattica(POS tagging)
def tokenizePOS(frasi):
    tokensList = []
    tokenPOS = []
    tokensPOS = []
    for frase in frasi:
        frase = frase.encode('utf-8')
        # metodo nltk per dividere in parole(token) il testo del file frase per frase
        tokens = nltk.word_tokenize(frase)
        # costruisco lista token
        tokensList = tokensList + tokens

        # metodo nltk per POS tagging su frasi tokenizzate
        tokenPOS = nltk.pos_tag(tokens)
        # costruisco analisi per token
        tokensPOS = tokensPOS + tokenPOS

    return tokensList, tokensPOS


# crea lista token senza la punteggiatura
def tokNoPunct(tokensList):
    tokListNoPunct = []
    punct = [".", ",", ":", ";", "!", "?", "/", "..", "-", "(", ")", "'"]
    for token in tokensList:
        if token not in punct:
            tokListNoPunct.append(token)

    return tokListNoPunct


# calcola i 20 elementi più frequenti e li ordina in maniera descrescente rispetto alla frequenza
def elem20PiuFreqDecresc(elemList):
    # calcolo frequenza di ogni elemento nella lista
    freq = collections.Counter(elemList)
    # restituisco primi 20 elem in ordine decrescente
    most20Freq = freq.most_common(20)

    return most20Freq


# compone liste di sostantivi e aggettivi più frequenti
def mostFreqNomiAgg(tokensPOS):
    # liste vuote
    mostFreqNomi = []
    mostFreqAgg = []
    # liste POS tags, tratte da https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
    tagNomi = ["NN", "NNS", "NNP", "NNPS"]
    tagAggettivi = ["JJ", "JJR", "JJS"]
    # per ogni elemento, formato dai due componenti token-tag, guardo se il secondo(il tag) è uguale a uno di quelli delle liste che mi interessano
    for elem in tokensPOS:
        if elem[1] in tagNomi:
            # creo lista nomi osservati
            mostFreqNomi.append(elem[0])
        if elem[1] in tagAggettivi:
            # creo lista aggettivi osservati
            mostFreqAgg.append(elem[0])

    return mostFreqNomi, mostFreqAgg


# toglie dalla lista dei POS punteggiatura, congiunzioni e articoli e restituisce sifatta lista bigrammi
def noPuntArtCong(tokensPOS):
    # creo lista bigrammi di POS
    listaBigrammi = nltk.bigrams(tokensPOS)
    # prendo tag punteggiatura, congiunzioni e articoli da https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
    listaTagDaEscludere = ["DT", "CC", "IN", "SYM", ".", "!", "?", ",", "(", ")", ":", ";", "-", "_", "'"]
    # creo nuova lista bigrammi i cui tag non sono tra quelli da escludere
    listaBigrNew = []
    for ((tok1, tag1), (tok2, tag2)) in listaBigrammi:
        if tag1 not in listaTagDaEscludere:
            if tag2 not in listaTagDaEscludere:
                bigramma = (tok1, tok2)
                listaBigrNew.append(bigramma)

    return listaBigrNew


# costruisco lista solo di tag POS
def listaTagPOS(tokensPOS):
    listaTag = []

    for (tok, tag) in tokensPOS:
        listaTag.append(tag)

    return listaTag


# calcola i 10 elementi più frequenti e li ordina in maniera descrescente rispetto alla frequenza
def elem10PiuFreqDecresc(elemList):
    # calcolo frequenza di ogni elemento nella lista
    freq = collections.Counter(elemList)
    # restituisco primi 10 elem in ordine decrescente
    most10Freq = freq.most_common(10)

    return most10Freq


# costruisco lista bigrammi (di tag) POS
def bigrPOS(tokensPOS):
    # creo lista bigrammi di POS
    listaBigrammi = nltk.bigrams(tokensPOS)
    # creo nuova lista bigrammi con i tag POS
    listaBigrNew = []
    for ((tok1, tag1), (tok2, tag2)) in listaBigrammi:
        bigramma = (tag1, tag2)
        listaBigrNew.append(bigramma)

    return listaBigrNew


# costruisco lista trigrammi (di tag) POS
def trigrPOS(tokensPOS):
    # creo lista trigrammi di POS
    listaTrigrammi = nltk.trigrams(tokensPOS)
    # creo nuova lista bigrammi con i tag POS
    listaTrigrNew = []
    for ((tok1, tag1), (tok2, tag2), (tok3, tag3)) in listaTrigrammi:
        trigramma = (tag1, tag2, tag3)
        listaTrigrNew.append(trigramma)

    return listaTrigrNew


# costruisce lista formata solo da aggettivi e sostantivi con frequenza maggiore di 2
def aggSost(tokensPOS):
    # lista vuota
    listaNomiAgg = []
    # liste POS tags, tratte da https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
    tagNomi = ["NN", "NNS", "NNP", "NNPS"]
    tagAggettivi = ["JJ", "JJR", "JJS"]
    # per ogni elemento, formato dai due componenti token-tag, guardo se il secondo(il tag) è uguale a uno di quelli delle liste che mi interessano
    for elem in tokensPOS:
        # calcolo frequenza ogni token
        freq = tokensPOS.count(elem)
        if freq > 2:
            if elem[1] in tagNomi:
                # se sì lo metto nella lista
                listaNomiAgg.append(elem)
            if elem[1] in tagAggettivi:
                # se sì lo metto nella lista
                listaNomiAgg.append(elem)

    return listaNomiAgg


# crea lista di bigrammi aggettivo-sostantivo partendo da lista di nomi e aggettivi
def creaBigrAggSost(listaSostAgg):
    # liste POS tags, tratte da https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
    tagNomi = ["NN", "NNS", "NNP", "NNPS"]
    tagAggettivi = ["JJ", "JJR", "JJS"]
    # creo lista bigrammi
    listaBigrammi = nltk.bigrams(listaSostAgg)
    # creo nuova lista bigrammi con i tag POS
    listaBigrNew = []
    for ((tok1, tag1), (tok2, tag2)) in listaBigrammi:
        if tag1 in tagAggettivi:
            if tag2 in tagNomi:
                bigramma = (tok1, tok2)
                listaBigrNew.append(bigramma)

    return listaBigrNew


# calcola probabilità condizionata di ogni bigramma sost-agg della lista, e lo uso per calcolare la prob congiunta
def probCongiunta(listaAggSost, tokensList):
    probCongiunta = []
    for ((agg, nome), freq) in listaAggSost:
        # calcolo probabilità condizionata
        probCondiz = freq * 1.0 / tokensList.count(agg) * 1.0
        # calcolo probabilità aggettivo(prima parola del bigramma)
        probAgg = tokensList.count(agg) * 1.0 / len(tokensList) * 1.0
        # calcolo probabilità congiunta
        probCong = probAgg * probCondiz
        # aggingo nuovo elemento nella lista, con bigramma e probabilità congiunta
        bigramma = ((agg, nome), probCong)
        probCongiunta.append(bigramma)

    return probCongiunta


# Calcola forza associativa max (LMI) per ogni bigramma
# formula LMI = log2( f(a,b) * C / f(a) * f(b) )
def forzaAssociativaMax(listaAggSost, tokensList):
    # crea nuova lista
    listaBigrLMI = []
    for ((agg, nome), freq) in listaAggSost:
        # primo elemento della formula
        # prodotto tra la frequenza del bigramma e il totale di elementi nel corpus
        part1 = freq * len(tokensList)
        # frequenza della prima parola del bigramma (aggettivo)
        fAgg = tokensList.count(agg)
        # frequenza seconda parola bigramma (sostantivo)
        fSost = tokensList.count(nome)
        # secondo elemento della formula
        # prodotto tra le frequenze delle singole parole
        part2 = fAgg * fSost
        # Local Mutual Information
        LMI = (freq) * (math.log((part1 * 1.0 / part2 * 1.0), 2))
        # aggiungo nuovo elemento nella lista, con bigramma e LMI
        bigramma = ((agg, nome), LMI)
        listaBigrLMI.append(bigramma)
    # ordino la lista per LMI decrescenti
    listaOrdLMI = sorted(listaBigrLMI, key=lambda a: -a[1], reverse=False)

    return listaOrdLMI


# markov ordine 0
def markov0(lungCorpus, freqTok, frase):
    probabilita = 1.0
    probTokTot = {}

    for token in frase:
        # probabilità singoli token
        probTok = (freqTok[token] * 1.0 / lungCorpus * 1.0)

        # prodotto delle probabilità tra loro
        probabilita = probabilita * probTok
        probTokTot[token] = probTok

    return probabilita, probTokTot


# markov ordine 1
def markov1(tokensList, freqTok, frase):
    probabilita = 1.0
    rangeFrase = frase[1:len(frase)]

    # estraggo bigrammi della frase e del testo completo per confrontarne le frequenze
    bigrFrase = list(bigrams(rangeFrase))
    bigrTesto = list(bigrams(tokensList))
    token = frase[1]
    probToken = (freqTok[token] * 1.0 / len(tokensList) * 1.0)

    for bigram in bigrFrase:
        # frequenze
        freqBigr = bigrTesto.count(bigram)

        # probabilità condizionata bigramma
        A = bigram[0]
        probCondiz = (freqBigr * 1.0 / tokensList.count(A) * 1.0)
        probabilita = probabilita * probCondiz

    return probabilita * probToken


def estraiFrasi(tokensList, frasi):
    # frequenza dei token nel testo
    freqToken = nltk.FreqDist(tokensList)

    listaFrasiTok = []
    for frase in frasi:
        frase = frase.encode('utf-8')
        # tokenizzo le frasi
        fraseTok = nltk.word_tokenize(frase)
        # ogni token deve avere frequenza > 2
        if all(freqToken[token] > 2 for token in fraseTok):
            listaFrasiTok.append(fraseTok)

    return listaFrasiTok, freqToken

def calcolaMarkov(tokensList, listaFrasiTok, freqToken):
    # lunghezza corpus
    lungCorpus = len(tokensList)

    # probabilità massima per Markov di ordine 0
    probMassima0 = 0.0
    # probabilità massima per Markov di ordine 1
    probMassima1 = 0.0

    for frase in listaFrasiTok:
        # ogni frase lunga da 6 a 8 token
        if ((len(frase) > 5) and (len(frase) < 9)):

            # calcolo catena di Markov di ordine 0
            probab, probabTok = markov0(lungCorpus, freqToken, frase)
            # calcolo catena di Markov di ordine 1
            probDip = markov1(tokensList, freqToken, frase)

            # assegno probabilità massima(ordine 0)
            if (probab > probMassima0):
                probMassima0 = probab
                # la nuova frase con probabilità massima diventa quella che ho appena trovato
                frasePiuFreq0 = frase
                # probabilità token nella frase
                probTokMax = probabTok

            # assegno probabilità massima(ordine 1)
            if (probDip > probMassima1):
                probMassima1 = probDip
                frasePiuFreq1 = frase

    return frasePiuFreq0, probMassima0, probTokMax, frasePiuFreq1, probMassima1


def main(file1, file2):
    # metodo open per aprire file di testo
    fileInput1 = codecs.open(file1, "r", "utf-8")
    fileInput2 = codecs.open(file2, "r", "utf-8")
    # metodo read per leggere i file e assegnarli alla variabile "raw" di tipo string
    raw1 = fileInput1.read()
    raw2 = fileInput2.read()

    # modulo statistico nltk per frasi
    sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    # funzione nltk che divide il testo dei due corpora in frasi
    frasi1 = sent_tokenizer.tokenize(raw1)
    frasi2 = sent_tokenizer.tokenize(raw2)

    # memorizzo i testi tokenizzati e il POS tagging su due variabili
    tokensList1, tokensPOS1 = tokenizePOS(frasi1)
    tokensList2, tokensPOS2 = tokenizePOS(frasi2)

    # 20 token più frequenti escludendo la punteggiatura
    # rimozione punteggiatura
    tokNoPunct1 = tokNoPunct(tokensList1)
    tokNoPunct2 = tokNoPunct(tokensList2)
    # compongo lista solo con primi 20 token più freq
    tok20MostFreq1 = elem20PiuFreqDecresc(tokNoPunct1)
    tok20MostFreq2 = elem20PiuFreqDecresc(tokNoPunct2)

    print "20 token più frequenti in ordine di frequenza decrescente:"
    print "\nRECENSIONI POSITIVE:\nToken:", "\tFrequenza:"
    for token in tok20MostFreq1:
        print token[0], "\t", token[1]

    print "\nRECENSIONI NEGATIVE:\nToken:", "\tFrequenza:"
    for token in tok20MostFreq2:
        print token[0], "\t", token[1]

    # sostantivi e aggettivi più frequenti
    sostMostFreq1, aggMostFreq1 = mostFreqNomiAgg(tokensPOS1)
    sostMostFreq2, aggMostFreq2 = mostFreqNomiAgg(tokensPOS2)
    # prendo solo i primi 20 sostantivi
    sostMostFreq1 = elem20PiuFreqDecresc(sostMostFreq1)
    sostMostFreq2 = elem20PiuFreqDecresc(sostMostFreq2)

    print "\n20 sostantivi più frequenti in ordine di frequenza decrescente:"
    print "\nRECENSIONI POSITIVE:"
    for sostantivo in sostMostFreq1:
        print sostantivo[0], sostantivo[1]

    print "\nRECENSIONI NEGATIVE:"
    for sostantivo in sostMostFreq2:
        print sostantivo[0], sostantivo[1]

    # prendo solo i primi 20 aggettivi
    aggMostFreq1 = elem20PiuFreqDecresc(aggMostFreq1)
    aggMostFreq2 = elem20PiuFreqDecresc(aggMostFreq2)

    print "\n20 aggettivi più frequenti in ordine di frequenza decrescente:"
    print "\nRECENSIONI POSITIVE:"
    for aggettivo in aggMostFreq1:
        print aggettivo[0], aggettivo[1]

    print "\nRECENSIONI NEGATIVE:"
    for aggettivo in aggMostFreq2:
        print aggettivo[0], aggettivo[1]

    # 20 bigrammi di token più frequenti (no punteggiatura, articoli e congiunzioni)
    # prendo lista POS e rimuovo punteggiatura, articoli e congiunzioni formando la lista dei bigrammi
    listaBigr1 = noPuntArtCong(tokensPOS1)
    listaBigr2 = noPuntArtCong(tokensPOS2)
    # prendo solo i primi 20 bigrammi
    lista20Bigr1 = elem20PiuFreqDecresc(listaBigr1)
    lista20Bigr2 = elem20PiuFreqDecresc(listaBigr2)

    print "\n20 bigrammi di token più frequenti in ordine di frequenza decrescente"
    print "\nRECENSIONI POSITIVE:\n",
    for bigramma in lista20Bigr1:
        print bigramma[0], bigramma[1]

    print "\nRECENSIONI NEGATIVE:"
    for bigramma in lista20Bigr2:
        print bigramma[0], bigramma[1]

    # 10 POS più frequenti
    listaTag1 = listaTagPOS(tokensPOS1)
    listaTag2 = listaTagPOS(tokensPOS2)
    POSfreq1 = elem10PiuFreqDecresc(listaTag1)
    POSfreq2 = elem10PiuFreqDecresc(listaTag2)

    print "\n10 PoS più frequenti in ordine di frequenza decrescente"
    print "\nRECENSIONI POSITIVE:\n",
    for elem in POSfreq1:
        print elem[0], "\t", elem[1]

    print "\nRECENSIONI NEGATIVE:"
    for elem in POSfreq2:
        print elem[0], "\t", elem[1]

    # 10 BIGRAMMI di POS più frequenti
    # costruisco lista bigrammi POS
    listaBigrPOS1 = bigrPOS(tokensPOS1)
    listaBigrPOS2 = bigrPOS(tokensPOS2)
    # prendo i primi 10 in ordine decrescente
    decrBigrPOS1 = elem10PiuFreqDecresc(listaBigrPOS1)
    decrBigrPOS2 = elem10PiuFreqDecresc(listaBigrPOS2)
    print "\n10 bigrammi di PoS più frequenti in ordine di frequenza decrescente"
    print "\nRECENSIONI POSITIVE:\n",
    for elem in decrBigrPOS1:
        print elem[0], "\t", elem[1]

    print "\nRECENSIONI NEGATIVE:"
    for elem in decrBigrPOS2:
        print elem[0], "\t", elem[1]

    # 10 TRIGRAMMI di PoS più frequenti
    # costruisco lista trigrammi POS
    listaTrigrPOS1 = trigrPOS(tokensPOS1)
    listaTrigrPOS2 = trigrPOS(tokensPOS2)
    # prendo i primi 10 in ordine decrescente
    decrTrigrPOS1 = elem10PiuFreqDecresc(listaTrigrPOS1)
    decrTrigrPOS2 = elem10PiuFreqDecresc(listaTrigrPOS2)
    print "\n10 trigrammi di PoS più frequenti in ordine di frequenza decrescente"
    print "\nRECENSIONI POSITIVE:\n",
    for elem in decrTrigrPOS1:
        print elem[0], "\t", elem[1]
    print "\nRECENSIONI NEGATIVE:"
    for elem in decrTrigrPOS2:
        print elem[0], "\t", elem[1]

    # 20 bigrammi aggettivo-sostantivo (dove ogni token ha una frequenza > 2)
    # costruisce lista formata solo da aggettivi e sostantivi con frequenza maggiore di 2
    sostAgg1 = aggSost(tokensPOS1)
    sostAgg2 = aggSost(tokensPOS2)
    # costruisco lista bigrammi aggettivo-sostantivo
    bigrSostAgg1 = creaBigrAggSost(sostAgg1)
    bigrSostAgg2 = creaBigrAggSost(sostAgg2)
    # prendo solo i primi 20 in ordine decresc (con frequenza massima)
    bigr20AggSost1 = elem20PiuFreqDecresc(bigrSostAgg1)
    bigr20AggSost2 = elem20PiuFreqDecresc(bigrSostAgg2)
    print "\n\n20 bigrammi aggettivo-sostantivo (dove ogni token ha una frequenza > 2)\n"
    print "- Con Frequenza Massima\n"
    print "RECENSIONI POSITIVE:\n"
    for (tok1, tok2), freq in bigr20AggSost1:
        print(tok1, tok2), "\tFreq bigramma", freq
        print "\tAggettivo:", tok1, "\tFreq assoluta:", tokensList1.count(tok1)
        print "\tNome:", tok2, "\tFreq assoluta:", tokensList1.count(tok2), "\n"

    print "RECENSIONI NEGATIVE:\n"
    for (tok1, tok2), freq in bigr20AggSost2:
        print(tok1, tok2), "\tFreq bigramma", freq
        print "\tAggettivo:", tok1, "\tFreq assoluta:", tokensList2.count(tok1)
        print "\tNome:", tok2, "\tFreq assoluta:", tokensList2.count(tok2), "\n"

    # 20 bigrammi aggettivo-sostantivo con probabilità congiunta
    print "\n- Con Probabilità Congiunta\n"
    print "RECENSIONI POSITIVE:\n"
    listaProbCong1 = probCongiunta(bigr20AggSost1, tokensList1)

    for elem in listaProbCong1:
        print elem[0], "\n\tProbabilità:", elem[1], "\n"

    print "\nRECENSIONI NEGATIVE:\n"
    listaProbCong2 = probCongiunta(bigr20AggSost2, tokensList2)

    for elem in listaProbCong2:
        print elem[0], "\n\tProbabilità:", elem[1], "\n"

    # 20 bigrammi aggettivo-sostantivo con forza associativa max (attraverso la LMI)
    print "\n- Con Forza Associativa Massima (attraverso la Local Mutual Information)\n"
    print "RECENSIONI POSITIVE:\n"

    bigrLMI1 = forzaAssociativaMax(bigr20AggSost1, tokensList1)

    for elem in bigrLMI1:
        print elem[0], "\n\tLocal Mutual Information:", elem[1], "\n"
    print "RECENSIONI NEGATIVE:\n"

    bigrLMI2 = forzaAssociativaMax(bigr20AggSost2, tokensList2)
    for elem in bigrLMI2:
        print elem[0], "\n\tLocal Mutual Information:", elem[1], "\n"

    # Le 2 frasi più probabili con catene di Markov di ordine 0 e 1
    # RECENSIONI POSITIVE
    listaFrasiTok1, freqToken1 = estraiFrasi(tokensList1, frasi1)
    frasePiuFreq0_1, probMassima0_1, probTokMax1, frasePiuFreq1_1, probMassima1_1 = calcolaMarkov(tokensList1, listaFrasiTok1, freqToken1)
    # RECENSIONI NEGATIVE
    listaFrasiTok2, freqToken2 = estraiFrasi(tokensList2, frasi2)
    frasePiuFreq0_2, probMassima0_2, probTokMax2, frasePiuFreq1_2, probMassima1_2 = calcolaMarkov(tokensList2, listaFrasiTok2, freqToken2)

    print "\n\tLe 2 frasi più probabili con catene di Markov di ordine 0 e 1"
    print "\nRECENSIONI POSITIVE:\n"
    print "Frase più frequente con ordine 0:\t", frasePiuFreq0_1, "\nProbabilità:\t", probMassima0_1, "\n"
    for tok in frasePiuFreq0_1:
        print "\t", tok, "\tprobabilità:\t", probTokMax1[tok]
    print "\nFrase più frequente con ordine 1:\t", frasePiuFreq1_1, "\nProbabilità:\t", probMassima1_1, "\n"

    print "\nRECENSIONI NEGATIVE:\n"
    print "Frase più frequente con ordine 0:\t", frasePiuFreq0_2, "\nProbabilità:\t", probMassima0_2, "\n"
    for tok in frasePiuFreq0_2:
        print "\t", tok, "\tprobabilità:\t", probTokMax2[tok]
    print "\nFrase più frequente con ordine 1:\t", frasePiuFreq1_2, "\nProbabilità:\t", probMassima1_2, "\n"


main(sys.argv[1], sys.argv[2])