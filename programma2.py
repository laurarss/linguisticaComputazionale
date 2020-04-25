#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Progetto di Linguistica  Computazionale - A.A. 2018/2019
#   Programma 2
#   Laura Rossi - 559715

import sys
import codecs  # classe che contiene il metodo open()
import nltk  # per metodo tokenize
import collections


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
    punct = [".", ",", ":", ";", "!", "?", "/", "..", "-", "(", ")"]
    for token in tokensList:
        if token not in punct:
            tokListNoPunct.append(token)

    return tokListNoPunct


# calcola i 20 token più frequenti(punteggiatura esclusa)
def tok20PiuFreq(tokList):
    # calcolo frequenza di ogni token
    tokFreq = collections.Counter(tokList)
    # restituisco primi 20 token in ord decrescente
    tokMostFreq = tokFreq.most_common(20)

    return tokMostFreq


# compone liste di sostantivi e aggettivi più frequenti
def mostFreqNomiAgg(tokensPOS):
    # liste vuote
    mostFreqNomi = []
    mostFreqAgg = []
    # liste POS tags, tratte da https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
    tagNomi = ["NN", "NNS", "NNP", "NNPS"]
    tagAggettivi = ["JJ", "JJS", "JJR"]
    # per ogni elemento, formato dai due componenti token-tag, guardo se il secondo(il tag) è uguale a uno di quelli delle liste che mi interessano
    for elem in tokensPOS:
        if elem[1] in tagNomi:
            # creo lista nomi osservati
            mostFreqNomi.append(elem[0])
        if elem[1] in tagAggettivi:
            # creo lista aggettivi osservati
            mostFreqAgg.append(elem[0])

    return mostFreqNomi, mostFreqAgg


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
    tok20MostFreq1 = tok20PiuFreq(tokNoPunct1)
    tok20MostFreq2 = tok20PiuFreq(tokNoPunct2)
    print "20 token più frequenti in ordine di frequenza decrescente:"
    print "\nRECENSIONI POSITIVE:\n", tok20MostFreq1
    print "\nRECENSIONI NEGATIVE:\n", tok20MostFreq2

    # sostantivi e aggettivi più frequenti
    sostMostFreq1, aggMostFreq1 = mostFreqNomiAgg(tokensPOS1)
    sostMostFreq2, aggMostFreq2 = mostFreqNomiAgg(tokensPOS2)
    # prendo solo i primi 20 sostantivi
    sostMostFreq1 = tok20PiuFreq(sostMostFreq1)
    sostMostFreq2 = tok20PiuFreq(sostMostFreq2)
    print "\n20 sostantivi più frequenti in ordine di frequenza decrescente:"
    print "\nRECENSIONI POSITIVE:", sostMostFreq1, "\n"
    print "RECENSIONI NEGATIVE:", sostMostFreq2, "\n"
    # prendo solo i primi 20 aggettivi
    aggMostFreq1 = tok20PiuFreq(aggMostFreq1)
    aggMostFreq2 = tok20PiuFreq(aggMostFreq2)
    print "\n20 aggettivi più frequenti in ordine di frequenza decrescente:"
    print "\nRECENSIONI POSITIVE:", aggMostFreq1, "\n"
    print "RECENSIONI NEGATIVE:", aggMostFreq2, "\n"

main(sys.argv[1], sys.argv[2])
