#!/usr/bin/env python

import pyttsx3
import time

def afficher_nationalites():
    voices = engine.getProperty('voices')
    nationalites = []
    for voice in voices :
        nationalites.append(voice.name)
    print'Nationalities available: \n', nationalites
    return

def gender_selection():
    nation = raw_input('\n Wich Nationality ?: ')
    voices = engine.getProperty('voices')
    voix = ""
    while(voix == ""):
        compteur = 0
        for voice in voices :
            compteur += 1
            if (nation == voice.name):
                voix = voice
                compteur -= 1
        if compteur == 69:
            afficher_nationalites()
            nation = raw_input('\n We couldn\'t find your language, please choose one in the list above: ')
    engine.setProperty('voice', voix.id)
    return

def setSetences(sentences):
    new_sentence = raw_input("\n Give a sentence for the pepper to say or press q to exit: ")
    while(new_sentence !="q" and new_sentence != "Q"):
        sentences.append(new_sentence)
        new_sentence = raw_input("Give a new sentence ou press q to exit:  ")
    return

def dire_phrases(sentences):
    for phrase in sentences:
        engine.say(phrase)
        time.sleep(2)
    return

if __name__ == "__main__":
    engine = pyttsx3.init()
    sentences = ['Hello my name is Pepper']
    gender_selection()
    setSetences(sentences)
    dire_phrases(sentences)
    engine.runAndWait()
    engine.stop()