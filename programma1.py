#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Progetto di Linguistica  Computazionale - A.A. 2018/2019
#   Programma 1
#   Laura Rossi - 559715

import sys
import codecs  # classe che contiene il metodo open()
import nltk  # per metodo tokenize


# tokenizza frasi e fa analisi morfosintattica(POS tagging)
def tokenizePOS(frasi):
    tokensList = []
    tokensAnalisis = []
    for frase in frasi:
        frase = frase.encode('utf-8')
        # metodo nltk per dividere in parole(token) il testo del file frase per frase
        tokens = nltk.word_tokenize(frase)
        # costruisco lista token
        tokensList = tokensList + tokens

        # metodo nltk per POS tagging su frasi tokenizzate
        tokensPOS = nltk.pos_tag(tokens)
        # costruisco analisi per token
        tokensAnalisis = tokensAnalisis + tokensPOS

    return tokensList, tokensAnalisis


# estraggo bigrammi POS dal testo analizzato
def bigramsPOS(tokenAnalized):
    bigramsPOS = []
    for bigram in tokenAnalized:
        # append alla lista bigrammi POS
        bigramsPOS.append(bigram[1])

    return bigramsPOS


# calcola lunghezza media in token delle frasi (numero tokens/numero frasi)
def lungMediaFrasi(numFrasi, numTokens):
    media = 0.0
    media = numTokens * 1.0 / numFrasi * 1.0  # cast a float moltiplicando per 1.0

    return media


# calcola lunghezza media in caratteri dei token(somma dei caratteri/numero dei token)
def lungMediaToken(tokensList, numTokens):
    numCaratteri = 0.0
    for token in tokensList:
        caratteri = len(token)
        numCaratteri = numCaratteri + caratteri
    carattToken = numCaratteri / numTokens

    return carattToken


# calcola lista vocaboli del testo con funzione set() e li conta
def vocabularyCount(tokensList):
    voc = set(tokensList)
    contVoc = len(voc)

    return contVoc


# calcola TTR type token ratio
def TTR(vocCount, partTokens):
    numTokens = len(partTokens)
    ttr = vocCount * 1.0 / numTokens * 1.0
    return ttr


# calcola classe di frequenza
def classeFreq(tokensList):
    v3 = 0
    v6 = 0
    v9 = 0
    freqToken = nltk.FreqDist(tokensList)  # funzione nltk che calcola frequenza
    vocabulary = set(freqToken)
    for token in vocabulary:
        if freqToken[token] == 3:  # controllo che freq elemento sia uguale a quello della classe considerata
            v3 += 1
        if freqToken[token] == 6:
            v6 += 1
        if freqToken[token] == 9:
            v9 += 1

    return v3, v6, v9


# In input i due file
def main(file1, file2):
    # metodo open per aprire file di testo
    fileInput1 = codecs.open(file1, "r", "utf-8")
    fileInput2 = codecs.open(file2, "r", "utf-8")
    # metodo read per leggere i file e assegnarli alla var string raw
    raw1 = fileInput1.read()
    raw2 = fileInput2.read()

    # modulo statistico nltk per frasi
    sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    # funzione nltk che divide il testo in frasi
    frasi1 = sent_tokenizer.tokenize(raw1)
    frasi2 = sent_tokenizer.tokenize(raw2)

    # tokenizzo le frasi e POS tagging
    tokensList1, tokensAnalisis1 = tokenizePOS(frasi1)
    tokensList2, tokensAnalisis2 = tokenizePOS(frasi2)
    # creo lista di coppie coppie token-tag
    POS1 = bigramsPOS(tokensAnalisis1)
    POS2 = bigramsPOS(tokensAnalisis2)

    # numero frasi(conta frasi da testo diviso in frasi)
    numFrasi1 = len(frasi1)
    numFrasi2 = len(frasi2)
    # numero token(conta token da testo diviso in frasi)
    numToken1 = len(tokensList1)
    numToken2 = len(tokensList2)
    print "\nPROVA:\n"
    print "\nNUMERO FRASI E TOKEN:\n"
    print "RECENSIONI POSITIVE:\n Numero frasi:\t", numFrasi1, "\tNumero token:\t", numToken1,
    print "\nRECENSIONI NEGATIVE:\n Numero frasi:\t", numFrasi2, "\tNumero token:\t", numToken2, "\n"
    if (numFrasi1 > numFrasi2):
        print " Il corpus recensioni positive presenta un numero maggiore di frasi\n"
    if (numFrasi1 < numFrasi2):
        print " Il corpus recensioni negative presenta un numero maggiore di frasi\n"
    if (numFrasi1 == numFrasi2):
        print " I due corpora presentano lo stesso numero di frasi\n"

    # lunghezza media frasi
    lungFrasi1 = lungMediaFrasi(numFrasi1, numToken1)
    lungFrasi2 = lungMediaFrasi(numFrasi2, numToken2)
    # lunghezza media token
    lungToken1 = lungMediaToken(tokensList1, numToken1)
    lungToken2 = lungMediaToken(tokensList2, numToken2)
    print "\nLUNGHEZZA MEDIA FRASI E TOKEN\n"
    print "RECENSIONI POSITIVE:\n Lunghezza media frasi in token:\t", lungFrasi1, "\tLunghezza media token:", lungToken1
    print "RECENSIONI NEGATIVE:\n Lunghezza media frasi in token:\t", lungFrasi2, "\tLunghezza media token:", lungToken2, "\n"
    if (lungFrasi1 > lungFrasi2):
        print " Il corpus recensioni positive presenta un maggior numero medio di token per frase"
    if (lungFrasi1 < lungFrasi2):
        print " Il corpus recensioni negative presenta un maggior numero medio di token per frase"
    if (lungFrasi1 == lungFrasi2):
        print " I corpora presentano lo stesso numero medio di token per frase"
    if (lungToken1 > lungToken2):
        print " Il corpus recensioni positive presenta un maggior numero medio di caratteri per token"
    if (lungToken1 < lungToken2):
        print " Il corpus recensioni negative presenta un maggior numero medio di caratteri per token"
    if (lungToken1 == lungToken2):
        print " I due corpora presentano lo stesso numero medio di caratteri per token"

    # grandezza vocabolario e TTR per porzioni incrementali di 1000 token
    # parziali RECENSIONI POSITIVE
    parz1 = tokensList1[0:1000]  # funzione che prende elem da 1 a 1000 della lista di token
    parz2 = tokensList1[0:2000]
    parz3 = tokensList1[0:3000]
    parz4 = tokensList1[0:4000]
    parz5 = tokensList1[0:5000]
    # calcolo vocabolario parziali (positive)
    vocCount1 = vocabularyCount(parz1)
    vocCount2 = vocabularyCount(parz2)
    vocCount3 = vocabularyCount(parz3)
    vocCount4 = vocabularyCount(parz4)
    vocCount5 = vocabularyCount(parz5)
    # calcolo TTR parziali (positive)
    TTR1 = TTR(vocCount1, parz1)
    TTR2 = TTR(vocCount2, parz2)
    TTR3 = TTR(vocCount3, parz3)
    TTR4 = TTR(vocCount4, parz4)
    TTR5 = TTR(vocCount5, parz5)

    print "\nVOCABOLARIO E TTR PER PORZIONI INCREMENTALI DI TOKEN\n"
    print " Recensioni positive"
    print " - primi 1000 token \tvocabolario:", vocCount1, "\tTTR:", TTR1
    print " - primi 2000 token \tvocabolario:", vocCount2, "\tTTR:", TTR2
    print " - primi 3000 token \tvocabolario:", vocCount3, "\tTTR:", TTR3
    print " - primi 4000 token \tvocabolario:", vocCount4, "\tTTR:", TTR4
    print " - primi 5000 token \tvocabolario:", vocCount5, "\tTTR:", TTR5

    # grandezza vocabolario e TTR per porzioni incrementali di 1000 token
    # parziali RECENSIONI NEGATIVE
    parz1 = tokensList2[0:1000]  # funzione che prende elem da 1 a 1000 della lista di token
    parz2 = tokensList2[0:2000]
    parz3 = tokensList2[0:3000]
    parz4 = tokensList2[0:4000]
    parz5 = tokensList2[0:5000]
    # calcolo vocabolario parziali (negative)
    vocCount1 = vocabularyCount(parz1)
    vocCount2 = vocabularyCount(parz2)
    vocCount3 = vocabularyCount(parz3)
    vocCount4 = vocabularyCount(parz4)
    vocCount5 = vocabularyCount(parz5)
    # calcolo TTR parziali (negative)
    TTR1 = TTR(vocCount1, parz1)
    TTR2 = TTR(vocCount2, parz2)
    TTR3 = TTR(vocCount3, parz3)
    TTR4 = TTR(vocCount4, parz4)
    TTR5 = TTR(vocCount5, parz5)

    print "\n Recensioni negative"
    print " - primi 1000 token \tvocabolario:", vocCount1, "\tTTR:", TTR1
    print " - primi 2000 token \tvocabolario:", vocCount2, "\tTTR:", TTR2
    print " - primi 3000 token \tvocabolario:", vocCount3, "\tTTR:", TTR3
    print " - primi 4000 token \tvocabolario:", vocCount4, "\tTTR:", TTR4
    print " - primi 5000 token \tvocabolario:", vocCount5, "\tTTR:", TTR5

    # CLASSI DI FRQUENZA V3, V6, V9
    freq1V3, freq1V6, freq1V9 = classeFreq(tokensList1)
    freq2V3, freq2V6, freq2V9 = classeFreq(tokensList2)
    print "\nCLASSI DI FREQUENZA V3, V6 e V9"
    print "\nRecensioni positive:"
    print "\nV3:\t", freq1V3, "\nV6:\t", freq1V6, "\nV9:\t", freq1V9
    print "\nRecensioni negative:"
    print "\nV3:\t", freq2V3, "\nV6:\t", freq2V6, "\nV9:\t", freq2V9


main(sys.argv[1], sys.argv[2])
