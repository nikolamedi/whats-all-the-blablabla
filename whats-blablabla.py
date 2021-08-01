import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import seaborn as sns
import json

from collections import Counter
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from youtube_transcript_api import YouTubeTranscriptApi


# Code combines instructions from these following sources:
# Here how to download captions from YouTube: https://www.geeksforgeeks.org/python-downloading-captions-from-youtube/, also available here: https://github.com/jdepoix/youtube-transcript-api/
# Word cloud instructions: https://www.datacamp.com/community/tutorials/wordcloud-python


### Analysis of SLOCAT's COP23 Transport Talk Shows (November 2017)


# COP23 talk shows
# Capturing all transcripts from video(s) 

COP23_1 = YouTubeTranscriptApi.get_transcript("O1mzkgqKCT0")
COP23_2 = YouTubeTranscriptApi.get_transcript("JNJAyXQ-YfI")
COP23_3 = YouTubeTranscriptApi.get_transcript("ND7xToEpzDs")
COP23_4 = YouTubeTranscriptApi.get_transcript("AqUDjYWKc34")
COP23_5 = YouTubeTranscriptApi.get_transcript("Q_q8IbaUB4A")
COP23_6 = YouTubeTranscriptApi.get_transcript("ulPIwhP4QNw")
COP23_7 = YouTubeTranscriptApi.get_transcript("2Wo1CJCeZ7Q")


COP23_transcript = COP23_1 + COP23_2 + COP23_3 + COP23_4 + COP23_5 + COP23_6 + COP23_7


COP23_result = str(COP23_transcript)

COP23_result = COP23_result.replace("'", "")

with open ('COP23.txt', 'w') as file_object:
    file_object.write(COP23_result)


# Create stopword list:
stopwords = set(STOPWORDS)
stopwords.update(["um", "uh", "u", "im", "us", "much", "now", "see", "youre", "example", "session", "maybe", "things", "term", "dont", "do", "weve", "course", "happen", "said", "new", "different",
                 "text", "start", "duration", "lot", "sort", "thats", "mean", "want", "work", "make", "wave", "kind", "minister", "great", "part", "question", "actually", "way", "time", "lets",
                 "really", "theres", "one", "many", "going", "will", "need", "wave", "let", "theyre", "good", "know", "together", "point", "come", "support", "today", "towards", "world", "still",
                 "think", "thing", "say", "take", "well", "thank", "go", "first", "working", "right", "bring", "big", "okay", "look", "key", "important", "use", "two", "system", "help",
                 "yeah", "interesting", "move", "back", "place", "around", "able", "long", "done", "coming", "thanks", "put", "next", "trying", "level", "action", "last", "even", "mentioned", "Music",
                 "give", "called", "quite", "etc", "little bit", "bit", "tonight", "sure", "something", "basically", "gonna", "talk", "little", "hear", "looking", "three", "across", "yes", "first", "second"])

# Generate a word cloud image
wordcloud = WordCloud(width=1000, height=600, stopwords=stopwords, max_font_size=180, max_words=60, background_color="white", colormap="Dark2").generate(COP23_result)

# Display the generated image with matplotlib:
plt.figure(figsize=(12, 12))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Analysis of COP23 Transport Talk Show", fontsize=20)
plt.show()


### Analysis of SLOCAT's En Route to COP26 events (December 2020)


# EnRoutetoCOP26 high-level events
# Capturing all transcripts from video(s) 

ER_COP26_1 = YouTubeTranscriptApi.get_transcript("s9sgxTBimDc")
ER_COP26_2 = YouTubeTranscriptApi.get_transcript("02l-FDi6V28")
ER_COP26_3 = YouTubeTranscriptApi.get_transcript("1RleHuUQubc")
ER_COP26_4 = YouTubeTranscriptApi.get_transcript("br-2FWUnucg")
ER_COP26_5 = YouTubeTranscriptApi.get_transcript("sAPYq6m-DP8")
ER_COP26_6 = YouTubeTranscriptApi.get_transcript("E9SLzshwuF8")
ER_COP26_7 = YouTubeTranscriptApi.get_transcript("SOI9ZQHZBZw")
ER_COP26_8 = YouTubeTranscriptApi.get_transcript("JZv_leeigjI")
ER_COP26_9 = YouTubeTranscriptApi.get_transcript("w99hPyKGInM")
ER_COP26_10 = YouTubeTranscriptApi.get_transcript("9UZ8CS8_1HM")
ER_COP26_11 = YouTubeTranscriptApi.get_transcript("PbUNo8Taf-o")
ER_COP26_12 = YouTubeTranscriptApi.get_transcript("CecyH9F1aUc")


COP25_transcript = ER_COP26_1 + ER_COP26_2 + ER_COP26_3 + ER_COP26_4 + ER_COP26_5 + ER_COP26_6 + ER_COP26_7 + ER_COP26_8 + ER_COP26_9 + ER_COP26_10 + ER_COP26_11 + ER_COP26_12

COP25_result = str(COP25_transcript)

COP25_result = COP25_result.replace("'", "")

with open ('ER-COP26.txt', 'w') as file_object:
    file_object.write(COP25_result)


# Create stopword list:
stopwords = set(STOPWORDS)
stopwords.update(["um", "uh", "u", "im", "us", "much", "now", "see", "youre", "example", "session", "maybe", "things", "term", "dont", "do", "weve", "course", "happen", "said", "new", "different",
                 "text", "start", "duration", "lot", "sort", "thats", "mean", "want", "work", "make", "wave", "kind", "minister", "great", "part", "question", "actually", "way", "time", "lets",
                 "really", "theres", "one", "many", "going", "will", "need", "wave", "let", "theyre", "good", "know", "together", "point", "come", "support", "today", "towards", "world", "still",
                 "think", "thing", "say", "take", "well", "thank", "go", "first", "working", "right", "bring", "big", "okay", "look", "key", "important", "use", "two", "system", "help",
                 "yeah", "interesting", "move", "back", "place", "around", "able", "long", "done", "coming", "thanks", "put", "next", "trying", "level", "action", "last", "even", "mentioned", "Music"
                 "give", "called", "quite", "etc", "little bit", "bit", "tonight", "sure", "something", "basically", "gonna", "talk", "little", "hear", "looking", "three", "across", "yes", "first", "second"])

# Generate a word cloud image
wordcloud = WordCloud(width=1000, height=600, stopwords=stopwords, max_font_size=180, max_words=60, background_color="white", colormap="Dark2").generate(COP25_result)

# Display the generated image with matplotlib:
plt.figure(figsize=(12, 12))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Analysis of En Route to COP26", fontsize=20)
plt.show()


# ## Analysis of ITF Summit (May 2021)

# ITF Summit
# Capturing all transcripts from video(s) 

ITF_1 = YouTubeTranscriptApi.get_transcript("DusR8TCnW6Y")
ITF_2 = YouTubeTranscriptApi.get_transcript("Wnu8XjjRkZY")
ITF_3 = YouTubeTranscriptApi.get_transcript("R2l20mayw1U")
ITF_4 = YouTubeTranscriptApi.get_transcript("ts_bwBPGxiI")
ITF_5 = YouTubeTranscriptApi.get_transcript("wDxLURRapAM")
ITF_6 = YouTubeTranscriptApi.get_transcript("GKivwKnJBq4")
ITF_7 = YouTubeTranscriptApi.get_transcript("vOgi2ox4Rq0")
ITF_8 = YouTubeTranscriptApi.get_transcript("B8KhjR7cwvI")
ITF_9 = YouTubeTranscriptApi.get_transcript("Z0mFBt4aYTc")
ITF_10 = YouTubeTranscriptApi.get_transcript("3UY0chaj--0")
ITF_11 = YouTubeTranscriptApi.get_transcript("oJXA6bnBEEk")
ITF_12 = YouTubeTranscriptApi.get_transcript("XB7qqgrL58E")
ITF_13 = YouTubeTranscriptApi.get_transcript("fylc74l4C3I")
ITF_14 = YouTubeTranscriptApi.get_transcript("tbN1RhCO5vE")
ITF_15 = YouTubeTranscriptApi.get_transcript("E_GXVFXCT8U")
ITF_16 = YouTubeTranscriptApi.get_transcript("QVkW3lEEZbc")
ITF_17 = YouTubeTranscriptApi.get_transcript("8zVLp_cqdN0")
ITF_18 = YouTubeTranscriptApi.get_transcript("2O38oPHCIq8")
ITF_19 = YouTubeTranscriptApi.get_transcript("ca_W2gMV3EQ")
ITF_20 = YouTubeTranscriptApi.get_transcript("jXyLyAAMESc")
ITF_21 = YouTubeTranscriptApi.get_transcript("jfZ6ttLSkQ4")
ITF_22 = YouTubeTranscriptApi.get_transcript("SmBNHaK-ksU")
ITF_23 = YouTubeTranscriptApi.get_transcript("mf-ZoAOndb4")

ITF_transcript = ITF_1 + ITF_2 + ITF_3 + ITF_4 + ITF_5 + ITF_6 + ITF_7 + ITF_8 + ITF_9 + ITF_10 + ITF_11 + ITF_12 + ITF_13 + ITF_14 + ITF_15 + ITF_16 + ITF_17 + ITF_18 + ITF_19 + ITF_20 + ITF_21 + ITF_22 + ITF_23

ITF_result = str(ITF_transcript)

ITF_result = ITF_result.replace("'", "")

with open ('ITF.txt', 'w') as file_object:
    file_object.write(ITF_result)


# Create stopword list:
stopwords = set(STOPWORDS)
stopwords.update(["um", "uh", "u", "im", "us", "much", "now", "see", "youre", "example", "session", "maybe", "things", "term", "dont", "do", "weve", "course", "happen", "said", "new", "different",
                 "text", "start", "duration", "lot", "sort", "thats", "mean", "want", "work", "make", "wave", "kind", "minister", "great", "part", "question", "actually", "way", "time", "lets",
                 "really", "theres", "one", "many", "going", "will", "need", "wave", "let", "theyre", "good", "know", "together", "point", "come", "support", "today", "towards", "world", "still",
                 "think", "thing", "say", "take", "well", "thank", "go", "first", "working", "right", "bring", "big", "okay", "look", "key", "important", "use", "two", "system", "help",
                 "yeah", "interesting", "move", "back", "place", "around", "able", "long", "done", "coming", "thanks", "put", "next", "trying", "level", "action", "last", "even", "mentioned", "Music",
                 "give", "called", "quite", "etc", "little bit", "bit", "tonight", "sure", "something", "basically", "gonna", "talk", "little", "hear", "looking", "three", "across", "yes", "first", "second"])

# Generate a word cloud image
wordcloud = WordCloud(width=1000, height=600, stopwords=stopwords, max_font_size=180, max_words=60, background_color="white", colormap="Dark2").generate(ITF_result)

# Display the generated image with matplotlib:
plt.figure(figsize=(12, 12))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Analysis of ITF Summit 2021", fontsize=20)
plt.show()


### Analysis of GIZ Transport and Climate Change Week (June 2021)


# GIZ TCCW 2021
# Based on the TCCW 2021 playlist on Changing Transport's YouTube, including only the longer sessions: https://www.youtube.com/channel/UCuk7BcQRH0XQQP8pZAk5lUw

# TCCW_1 = YouTubeTranscriptApi.get_transcript("zpaKtwGJ1JE") # Transcript doesn't exist.
TCCW_2 = YouTubeTranscriptApi.get_transcript("PDw6ADjDRpY")
TCCW_3 = YouTubeTranscriptApi.get_transcript("oqDQG-iSFZo")
TCCW_4 = YouTubeTranscriptApi.get_transcript("Pf-Ddv5zL4g")
TCCW_5 = YouTubeTranscriptApi.get_transcript("boqS-aOMC7s")
TCCW_6 = YouTubeTranscriptApi.get_transcript("mAtl_mH4u_k")
TCCW_7 = YouTubeTranscriptApi.get_transcript("0oUhRKJW8ro")
# W_8 = YouTubeTranscriptApi.get_transcript("hQsUnjvyJWc") #Transcript doesn't load.
TCCW_9 = YouTubeTranscriptApi.get_transcript("H-j4agzoQVA")
TCCW_10 = YouTubeTranscriptApi.get_transcript("0oUhRKJW8ro")
TCCW_11 = YouTubeTranscriptApi.get_transcript("lVnZ9jiH9iY")
TCCW_12 = YouTubeTranscriptApi.get_transcript("zfHJlmB5V00")
TCCW_13 = YouTubeTranscriptApi.get_transcript("ATMb47_-ZYU")
TCCW_14 = YouTubeTranscriptApi.get_transcript("KmoisSxSSCs")
TCCW_15 = YouTubeTranscriptApi.get_transcript("0NzZNTQOUls")
TCCW_16 = YouTubeTranscriptApi.get_transcript("Gzza6GWBfEk")
TCCW_17 = YouTubeTranscriptApi.get_transcript("5wTx0rhixlU")
TCCW_18 = YouTubeTranscriptApi.get_transcript("nNUML7pG1zw")


TCCW_transcript = TCCW_2 + TCCW_3 + TCCW_4 + TCCW_5 + TCCW_6 + TCCW_7 + TCCW_9 + TCCW_10 + TCCW_11 + TCCW_12 + TCCW_13 + TCCW_14 + TCCW_14 + TCCW_15 + TCCW_16 + TCCW_17 + TCCW_18


TCCW_result = str(TCCW_transcript)

TCCW_result = TCCW_result.replace("'", "")

with open ('TCCW.txt', 'w') as file_object:
    file_object.write(TCCW_result)


# Create stopword list:
stopwords = set(STOPWORDS)
stopwords.update(["um", "uh", "u", "im", "us", "much", "now", "see", "youre", "example", "session", "maybe", "things", "term", "dont", "do", "weve", "course", "happen", "said", "new", "different",
                 "text", "start", "duration", "lot", "sort", "thats", "mean", "want", "work", "make", "wave", "kind", "minister", "great", "part", "question", "actually", "way", "time", "lets",
                 "really", "theres", "one", "many", "going", "will", "need", "wave", "let", "theyre", "good", "know", "together", "point", "come", "support", "today", "towards", "world", "still",
                 "think", "thing", "say", "take", "well", "thank", "go", "first", "working", "right", "bring", "big", "okay", "look", "key", "important", "use", "two", "system", "help",
                 "yeah", "interesting", "move", "back", "place", "around", "able", "long", "done", "coming", "thanks", "put", "next", "trying", "level", "action", "last", "even", "mentioned", "Music",
                 "give", "called", "quite", "etc", "little bit", "bit", "tonight", "sure", "something", "basically", "gonna", "talk", "little", "hear", "looking", "three", "across", "yes", "first", "second"])

# Generate a word cloud image
wordcloud = WordCloud(width=1000, height=600, stopwords=stopwords, max_font_size=180, max_words=60, background_color="white", colormap="Dark2").generate(TCCW_result)

# Display the generated image with matplotlib:
plt.figure(figsize=(12, 12))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Analysis of Transport and Climate Change Week 2021", fontsize=20)
plt.show()

