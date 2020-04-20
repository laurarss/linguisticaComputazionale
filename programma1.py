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
    media = numTokens / numFrasi

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
def TTR(vocCount, numTokens):
    ttr = vocCount / numTokens

    return ttr


# porz incrementali
def incrTTR(tokensList):
    mill = 1000
    part = []
    for mill in tokensList:
        part = slice(mill)
        print "Vocabolario:", part, vocabularyCount(tokensList[part]), "TTR:", TTR(tokensList[part], len(tokensList))
        mill = mill + 1000


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
        print "Il corpus recensioni positive presenta un numero maggiore di frasi\n"
    if (numFrasi1 < numFrasi2):
        print "Il corpus recensioni negative presenta un numero maggiore di frasi\n"
    if (numFrasi1 == numFrasi2):
        print "I due corpora presentano lo stesso numero di frasi\n"

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
        print "Il corpus recensioni positive presenta un maggior numero medio di token per frase"
    if (lungFrasi1 < lungFrasi2):
        print "Il corpus recensioni negative presenta un maggior numero medio di token per frase"
    if (lungFrasi1 == lungFrasi2):
        print "I corpora presentano lo stesso numero medio di token per frase"
    if (lungToken1 > lungToken2):
        print "Il corpus recensioni positive presenta un maggior numero medio di caratteri per token"
    if (lungToken1 < lungToken2):
        print "Il corpus recensioni negative presenta un maggior numero medio di caratteri per token"
    if (lungToken1 == lungToken2):
        print "I due corpora presentano lo stesso numero medio di caratteri per token"

    # grandezza vocabolario
    vocCount1 = vocabularyCount(tokensList1)
    vocCount2 = vocabularyCount(tokensList2)
    print "Vocabolario file 1:", vocCount1
    print "Vocabolario file 2:", vocCount2
    # Type Token Ratio per porzioni incrementali
    print "\n\tVocabolario e TTR per porzioni incrementali:\nPOSITIVE:\n", incrTTR(tokensList1), "\n"


main(sys.argv[1], sys.argv[2])


