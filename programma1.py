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
    tokensList = tokenPOS = []
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


# conta nomi, aggettivi e verbi nel corpus già POS taggato
def contaNomiAggVerbi(tokensPOS):
    # conteggi
    numNomi = 0
    numAggettivi = 0
    numVerbi = 0
    # liste POS tags, tratte da https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
    tagNomi = ["NN", "NNS", "NNP", "NNPS"]
    tagAggettivi = ["JJ", "JJR", "JJS"]
    tagVerbi = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]
    # per ogni elemento, formato dai due componenti token-tag, guardo se il secondo(il tag) è uguale a uno di quelli delle liste che mi interessano
    for elem in tokensPOS:
        if elem[1] in tagNomi:
            numNomi += 1
        if elem[1] in tagAggettivi:
            numAggettivi += 1
        if elem[1] in tagVerbi:
            numVerbi += 1

    return numNomi, numAggettivi, numVerbi


# la funzione calcola la media tra un tot di elementi(nomi/agg/verbi) e il numero di frasi nel corpus
def media(numElem, frasi):
    media = numElem * 1.0 / len(frasi) * 1.0

    return media


# conta occorrenze di avverbi e punteggiatura nel testo
def contaAvverbiPunteggiatura(tokensPOS):
    numAvverbi = 0
    numPunct = 0
    tagAvverbi = ["RB", "RBR", "RBS"]
    tagPunct = [",", "."]
    for row in tokensPOS:
        if row[1] in tagAvverbi:
            numAvverbi += 1
        if row[1] in tagPunct:
            numPunct += 1

    return numAvverbi, numPunct


# calcola densità lessicale con in input le occorrenze di nomi/aggettivi/verbi/avverbi
def densitaLessicale(nomi, aggettivi, verbi, avverbi, punteggiatura, numTokens):
    densLess = 0
    densLess = (nomi + verbi + aggettivi + avverbi) * 1.0 / (numTokens - punteggiatura) * 1.0

    return densLess


# In input i due file
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

    # tokenizzo le frasi e POS tagging
    tokensList1, tokensPOS1 = tokenizePOS(frasi1)
    tokensList2, tokensPOS2 = tokenizePOS(frasi2)

    # numero frasi(conta frasi da testo diviso in frasi)
    numFrasi1 = len(frasi1)
    numFrasi2 = len(frasi2)
    # numero token(conta token da testo diviso in frasi)
    numToken1 = len(tokensList1)
    numToken2 = len(tokensList2)

    print "NUMERO FRASI E TOKEN:\n"
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
    print "RECENSIONI POSITIVE:\n Lunghezza media frasi in token:\t", lungFrasi1, "\tLunghezza media token in caratteri:", lungToken1
    print "RECENSIONI NEGATIVE:\n Lunghezza media frasi in token:\t", lungFrasi2, "\tLunghezza media token in caratteri:", lungToken2, "\n"
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
    # lista parziali
    listaPart = [1000, 2000, 3000, 4000, 5000]
    # RECENSIONI POSITIVE
    # calcolo vocabolario e TTR parziali
    print "\nVOCABOLARIO E TTR PER PORZIONI INCREMENTALI DI 1000 TOKEN\n"
    print "RECENSIONI POSITIVE:"
    for part in listaPart:
        # rendo intero valore da listaPart, usato come estremo, usando int()
        vocCount1 = vocabularyCount(tokensList1[:int(part)])
        # TTR parz
        TTR1 = TTR(vocCount1, tokensList1[:int(part)])
        # stampo risultati
        print " - primi", int(part), "token:\tvocabolario:", vocCount1, "\tTTR:", TTR1

    # vocabolario intero corpus
    vocabulary1 = vocabularyCount(tokensList1)
    # TTR intero corpus
    TTRcorpus1 = TTR(vocabulary1, tokensList1)
    print " Intero Corpus: \tvocabolario:", vocabulary1, "\tTTR:", TTRcorpus1

    # RECENSIONI NEGATIVE
    # calcolo vocabolario e TTR parziali
    print "RECENSIONI NEGATIVE:"
    for part in listaPart:
        # rendo intero valore da listaPart, usato come estremo, usando int()
        vocCount2 = vocabularyCount(tokensList2[:int(part)])
        # TTR parz
        TTR2 = TTR(vocCount2, tokensList2[:int(part)])
        # stampo risultati
        print " - primi", int(part), "token:\tvocabolario:", vocCount2, "\tTTR:", TTR2

    # vocabolario intero corpus
    vocabulary2 = vocabularyCount(tokensList2)
    # TTR intero corpus
    TTRcorpus2 = TTR(vocabulary2, tokensList2)
    print " Intero Corpus: \tvocabolario:", vocabulary2, "\tTTR:", TTRcorpus2

    # CLASSI DI FREQUENZA V3, V6, V9 sui primi 5000 token
    freq1V3, freq1V6, freq1V9 = classeFreq(tokensList1[0:5000])
    freq2V3, freq2V6, freq2V9 = classeFreq(tokensList2[0:5000])
    print "\nCLASSI DI FREQUENZA V3, V6 e V9"
    print "\nRECENSIONI POSITIVE:"
    print " |V3|:\t", freq1V3, "\t|V6|:\t", freq1V6, "\t|V9|:\t", freq1V9
    print "RECENSIONI NEGATIVE:"
    print " |V3|:\t", freq2V3, "\t|V6|:\t", freq2V6, "\t|V9|:\t", freq2V9

    # NUMERO MEDIO SOSTANTIVI, AVVERBI E VERBI PER FRASE
    # totale nomi, verbi e aggettivi nel corpus di ogni file
    nomi1, aggettivi1, verbi1 = contaNomiAggVerbi(tokensPOS1)
    nomi2, aggettivi2, verbi2 = contaNomiAggVerbi(tokensPOS2)
    # calcolo media nomi per frase
    # recensioni positive
    mediaNomi1 = media(nomi1, frasi1)
    mediaAggettivi1 = media(aggettivi1, frasi1)
    mediaVerbi1 = media(verbi1, frasi1)
    # recensioni negative
    mediaNomi2 = media(nomi2, frasi2)
    mediaAggettivi2 = media(aggettivi2, frasi2)
    mediaVerbi2 = media(verbi2, frasi2)
    print "\nNUMERO MEDIO SOSTANTIVI, AVVERBI E VERBI PER FRASE"
    print "\nRECENSIONI POSITIVE: Media..\tnomi:", mediaNomi1, "\taggettivi:", mediaAggettivi1, "\tverbi:", mediaVerbi1
    print "\nRECENSIONI NEGATIVE: Media..\tnomi:", mediaNomi2, "\taggettivi:", mediaAggettivi2, "\tverbi:", mediaVerbi2

    # DENSITA' LESSICALE
    # calcolo occorrenze avverbi e punteggiatura nel testo dei ogni file
    avverbi1, punct1 = contaAvverbiPunteggiatura(tokensPOS1)
    avverbi2, punct2 = contaAvverbiPunteggiatura(tokensPOS2)

    # calcolo densità lessicale per ogni file
    densLess1 = densitaLessicale(nomi1, aggettivi1, verbi1, avverbi1, punct1, numToken1)
    densLess2 = densitaLessicale(nomi2, aggettivi2, verbi2, avverbi2, punct2, numToken2)

    print"\nDENSITA' LESSICALE"
    print"\nRECENSIONI POSITIVE:", densLess1
    print"\nRECENSIONI NEGATIVE:", densLess2
    if (densLess1 > densLess2):
        print "\nIl corpus recensioni positive ha una densità lessicale maggiore"
    if (densLess1 < densLess2):
        print "\nIl corpus recensioni negative ha una densità lessicale maggiore"
    if (densLess1 == densLess2):
        print "\nI due corpus hanno la stessa densità lessicale"


main(sys.argv[1], sys.argv[2])