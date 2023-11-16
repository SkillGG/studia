Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import nltk
nltk.download()

nltk.download()
showing info https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml
True
nltk.book
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    nltk.book
AttributeError: module 'nltk' has no attribute 'book'
from nltk.book import *
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
text2.concordance("of")
Displaying 25 of 3572 matches:
ne Austen 1811 ] CHAPTER 1 The family of Dashwood had long been settled in Sus
e was at Norland Park , in the centre of their property , where , for many gen
as to engage the general good opinion of their surrounding acquaintance . The 
ounding acquaintance . The late owner of this estate was a single man , who li
advanced age , and who for many years of his life , had a constant companion a
nd received into his house the family of his nephew Mr . Henry Dashwood , the 
 Henry Dashwood , the legal inheritor of the Norland estate , and the person t
ended to bequeath it . In the society of his nephew and niece , and their chil
ll increased . The constant attention of Mr . and Mrs . Henry Dashwood to his 
ely from interest , but from goodness of heart , gave him every degree of soli
ness of heart , gave him every degree of solid comfort which his age could rec
 could receive ; and the cheerfulness of the children added a relish to his ex
was amply provided for by the fortune of his mother , which had been large , a
her , which had been large , and half of which devolved on him on his coming o
f which devolved on him on his coming of age . By his own marriage , likewise 
ers ; for their fortune , independent of what might arise to them from their f
n disposal ; for the remaining moiety of his first wife ' s fortune was also s
uch terms as destroyed half the value of the bequest . Mr . Dashwood had wishe
d had wished for it more for the sake of his wife and daughters than for himse
s son , and his son ' s son , a child of four years old , it was secured , in 
way , as to leave to himself no power of providing for those who were most dea
charge on the estate , or by any sale of its valuable woods . The whole was ti
The whole was tied up for the benefit of this child , who , in occasional visi
, had so far gained on the affections of his uncle , by such attractions as ar
s are by no means unusual in children of two or three years old ; an imperfect
text1.similar("a")
the his that this one their some my any its in so no your those
another these her our not
text1.common_contexts(["a","the"])
for_moment of_whale by_whale of_man for_time of_whaling of_large
for_long to_whale in_whale was_very with_long of_sperm in_most in_bed
of_ship in_ship for_sea of_great at_distance
text4.dispersion_plot(["Europe", "America", "Britain"])
text4.dispersion_plot(["Europe", "America", "Britain"])
import numpy
impott matplotlib
SyntaxError: invalid syntax
import matplotlib
text4.dispersion_plot(["Europe", "America", "Britain"])
import matplot.pyplot as plt
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    import matplot.pyplot as plt
ModuleNotFoundError: No module named 'matplot.pyplot'
import matplotlib.pyplot as plt
plt.show()
text2.generate()
Building ngram index...
knew , had by this remembrance , and if , by rapid degrees , so long .
, she could live without one another , and in her rambles . at least
the last evening of a brother , could you know , from the first .
Dashwood ? this gentleman himself , and must put up with a kindness
which they are very much vexed at , for it -- and I shall keep it
entirely . admire it ; and it is , explain the grounds , or if any
place could give her ease , was a
'knew , had by this remembrance , and if , by rapid degrees , so long .\n, she could live without one another , and in her rambles . at least\nthe last evening of a brother , could you know , from the first .\nDashwood ? this gentleman himself , and must put up with a kindness\nwhich they are very much vexed at , for it -- and I shall keep it\nentirely . admire it ; and it is , explain the grounds , or if any\nplace could give her ease , was a'


lolC = text5.count("lol")
lolC
704
lolC / len(text5) * 100
1.5640968673628082
lolC / len(text5) * 100
1.5640968673628082

d
e
def lD(t):
    return len(set(tekst))/len(tekst)

def per(c,t):
    return c/t * 100

lD(text4)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    lD(text4)
  File "<pyshell#28>", line 2, in lD
    return len(set(tekst))/len(tekst)
NameError: name 'tekst' is not defined
def lD(t):
    return len(set(t))/len(t)

lD(text4)
0.06556530042314962
lD(text1)
0.07406285585022564
per(text3.count("a"), len(text4))
0.22367414209194184
def poW(l,t):
    return per(t.count(l), len(t))

poW("x", text3)
0.0
poW("xero", text3)
0.0
poW("xero", text4)
0.0
poW("xero", text5)
0.0
poW("xerox", text5)
0.0
poW("xerox", text4)
0.0
poW("skill and hibbies", text4)
0.0
poW("skill and hobbies", text4)
0.0
poW("skill", text4)
0.004578125715332143
sen6
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    sen6
NameError: name 'sen6' is not defined. Did you mean: 'sent6'?
sent6
['SCENE', '1', ':', '[', 'wind', ']', '[', 'clop', 'clop', 'clop', ']', 'KING', 'ARTHUR', ':', 'Whoa', 'there', '!']
words
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    words
NameError: name 'words' is not defined
sent6[-2:]
['there', '!']
fdist1 = FreqDist(text1)
print(fdist1)
<FreqDist with 19317 samples and 260819 outcomes>
fdist1["the"]
13721
fdist1.most_common(50)
[(',', 18713), ('the', 13721), ('.', 6862), ('of', 6536), ('and', 6024), ('a', 4569), ('to', 4542), (';', 4072), ('in', 3916), ('that', 2982), ("'", 2684), ('-', 2552), ('his', 2459), ('it', 2209), ('I', 2124), ('s', 1739), ('is', 1695), ('he', 1661), ('with', 1659), ('was', 1632), ('as', 1620), ('"', 1478), ('all', 1462), ('for', 1414), ('this', 1280), ('!', 1269), ('at', 1231), ('by', 1137), ('but', 1113), ('not', 1103), ('--', 1070), ('him', 1058), ('from', 1052), ('be', 1030), ('on', 1005), ('so', 918), ('whale', 906), ('one', 889), ('you', 841), ('had', 767), ('have', 760), ('there', 715), ('But', 705), ('or', 697), ('were', 680), ('now', 646), ('which', 640), ('?', 637), ('me', 627), ('like', 624)]
fdist1.most_common(20)
[(',', 18713), ('the', 13721), ('.', 6862), ('of', 6536), ('and', 6024), ('a', 4569), ('to', 4542), (';', 4072), ('in', 3916), ('that', 2982), ("'", 2684), ('-', 2552), ('his', 2459), ('it', 2209), ('I', 2124), ('s', 1739), ('is', 1695), ('he', 1661), ('with', 1659), ('was', 1632)]
fdist1.hapaxes()

ptl.show()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    ptl.show()
NameError: name 'ptl' is not defined
plt.show()
fdist.plot(50)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    fdist.plot(50)
NameError: name 'fdist' is not defined. Did you mean: 'fdist1'?
fdist1.plot(50)
<Axes: xlabel='Samples', ylabel='Counts'>
V = set(text1)
long = [w for w in V if len(w) > 14]
sorted(set(long))
['Bibliographical', 'CIRCUMNAVIGATION', 'Ehrenbreitstein', 'Mephistophelean', 'Physiognomically', 'amphitheatrical', 'apprehensiveness', 'archiepiscopacy', 'authoritatively', 'cannibalistically', 'characteristically', 'characteristics', 'circumnavigated', 'circumnavigating', 'circumnavigation', 'circumnavigations', 'comfortableness', 'comprehensively', 'comprehensiveness', 'conscientiously', 'disembowelments', 'dissatisfaction', 'hermaphroditical', 'heterogeneously', 'indiscriminately', 'indispensableness', 'individualities', 'individualizing', 'indomitableness', 'inoffensiveness', 'instantaneously', 'interchangeably', 'internationally', 'interrogatively', 'intolerableness', 'irresistibleness', 'miscellaneously', 'multitudinously', 'notwithstanding', 'passionlessness', 'perpendicularly', 'philanthropists', 'philosophically', 'phosphorescence', 'phrenologically', 'physiognomically', 'picturesqueness', 'preternaturalness', 'responsibilities', 'simultaneousness', 'skrimshandering', 'subterraneousness', 'superfluousness', 'supernaturalism', 'supernaturalness', 'superstitiously', 'superstitiousness', 'sympathetically', 'systematization', 'thoughtlessness', 'uncatastrophied', 'unceremoniously', 'uncomfortableness', 'uncompromisedness', 'unconditionally', 'unconsciousness', 'undiscriminating', 'uninterpenetratingly', 'unprecedentedly', 'unsophisticated', 'unsurrenderable', 'untraditionally']
long = [w for w in V if len(w) > 16]
sorted(set(long))
['cannibalistically', 'characteristically', 'circumnavigations', 'comprehensiveness', 'indispensableness', 'preternaturalness', 'subterraneousness', 'superstitiousness', 'uncomfortableness', 'uncompromisedness', 'uninterpenetratingly']
sorted(w for w in set(text3) if len(w) > 7 and FreqDist(text3)[w] > 50)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    sorted(w for w in set(text3) if len(w) > 7 and FreqDist(text3)[w] > 50)
  File "<pyshell#69>", line 1, in <genexpr>
    sorted(w for w in set(text3) if len(w) > 7 and FreqDist(text3)[w] > 50)
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\probability.py", line 102, in __init__
    Counter.__init__(self, samples)
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\collections\__init__.py", line 577, in __init__
    self.update(iterable, **kwds)
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\probability.py", line 140, in update
    super().update(*args, **kwargs)
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\collections\__init__.py", line 670, in update
    _count_elements(self, iterable)
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\probability.py", line 126, in __setitem__
    super().__setitem__(key, val)
KeyboardInterrupt
fd5 = FreqDist(text3)
sorted(w for w in set(text3) if len(w) > 7 and fd5[w] > 50)
['brethren', 'children', 'daughters']
sorted(w for w in set(text3) if len(w) > 7 and fd5[w] > 5)
['Abimelech', 'Aholibamah', 'Almighty', 'Arphaxad', 'Bashemath', 'Beersheba', 'Benjamin', 'Canaanites', 'Egyptian', 'Egyptians', 'Gomorrah', 'Machpelah', 'Manasseh', 'Padanaram', 'Peradventure', 'Philistines', 'Therefore', 'Wherefore', 'according', 'answered', 'appeared', 'birthright', 'blessing', 'brethren', 'buryingplace', 'children', 'circumcised', 'commanded', 'conceived', 'concerning', 'covenant', 'creature', 'creepeth', 'creeping', 'daughter', 'daughters', 'departed', 'establish', 'everlasting', 'exceedingly', 'families', 'favoured', 'firmament', 'firstborn', 'fruitful', 'gathered', 'generations', 'grievous', 'handmaid', 'hearkened', 'journeyed', 'mourning', 'multiply', 'multitude', 'offering', 'peradventure', 'possession', 'presence', 'prevailed', 'returned', 'righteous', 'ringstraked', 'servants', 'speckled', 'stranger', 'substance', 'themselves', 'therefore', 'together', 'wherefore', 'wilderness', 'youngest']
text6.collocations()
BLACK KNIGHT; clop clop; HEAD KNIGHT; mumble mumble; Holy Grail;
squeak squeak; FRENCH GUARD; saw saw; Sir Robin; Run away; CARTOON
CHARACTER; King Arthur; Iesu domine; Pie Iesu; DEAD PERSON; Round
Table; clap clap; OLD MAN; dramatic chord; dona eis
fdWL = FreqDist(len(w) for w in text6)
fdWL.plot()
<Axes: xlabel='Samples', ylabel='Counts'>
fdWL.plot(cummulative=True)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    fdWL.plot(cummulative=True)
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\probability.py", line 300, in plot
    ax.plot(freqs, **kwargs)
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\site-packages\matplotlib\axes\_axes.py", line 1688, in plot
    lines = [*self._get_lines(*args, data=data, **kwargs)]
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\site-packages\matplotlib\axes\_base.py", line 311, in __call__
    yield from self._plot_args(
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\site-packages\matplotlib\axes\_base.py", line 544, in _plot_args
    return [l[0] for l in result]
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\site-packages\matplotlib\axes\_base.py", line 544, in <listcomp>
    return [l[0] for l in result]
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\site-packages\matplotlib\axes\_base.py", line 537, in <genexpr>
    result = (make_artist(x[:, j % ncx], y[:, j % ncy], kw,
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\site-packages\matplotlib\axes\_base.py", line 351, in _makeline
    seg = mlines.Line2D(x, y, **kw)
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\site-packages\matplotlib\_api\deprecation.py", line 454, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\site-packages\matplotlib\lines.py", line 393, in __init__
    self._internal_update(kwargs)
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\site-packages\matplotlib\artist.py", line 1223, in _internal_update
    return self._update_props(
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\site-packages\matplotlib\artist.py", line 1197, in _update_props
    raise AttributeError(
AttributeError: Line2D.set() got an unexpected keyword argument 'cummulative'
fdWL.plot(cummulative=False)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    fdWL.plot(cummulative=False)
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\probability.py", line 300, in plot
    ax.plot(freqs, **kwargs)
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\site-packages\matplotlib\axes\_axes.py", line 1688, in plot
    lines = [*self._get_lines(*args, data=data, **kwargs)]
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\site-packages\matplotlib\axes\_base.py", line 311, in __call__
    yield from self._plot_args(
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\site-packages\matplotlib\axes\_base.py", line 544, in _plot_args
    return [l[0] for l in result]
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\site-packages\matplotlib\axes\_base.py", line 544, in <listcomp>
    return [l[0] for l in result]
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\site-packages\matplotlib\axes\_base.py", line 537, in <genexpr>
    result = (make_artist(x[:, j % ncx], y[:, j % ncy], kw,
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\site-packages\matplotlib\axes\_base.py", line 351, in _makeline
    seg = mlines.Line2D(x, y, **kw)
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\site-packages\matplotlib\_api\deprecation.py", line 454, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\site-packages\matplotlib\lines.py", line 393, in __init__
    self._internal_update(kwargs)
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\site-packages\matplotlib\artist.py", line 1223, in _internal_update
    return self._update_props(
  File "C:\Users\Student\AppData\Local\Programs\Python\Python310\lib\site-packages\matplotlib\artist.py", line 1197, in _update_props
    raise AttributeError(
AttributeError: Line2D.set() got an unexpected keyword argument 'cummulative'
fdWL.plot(cumulative=False)
<Axes: xlabel='Samples', ylabel='Counts'>
fdWL.plot(cumulative=True)
<Axes: xlabel='Samples', ylabel='Cumulative Counts'>
fdist.freq(10)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    fdist.freq(10)
NameError: name 'fdist' is not defined. Did you mean: 'fdist1'?
fdWL.freq(10)
0.002887958979194908
fdWL.freq(3)
0.13997760358342665
fdWL.freq(2)
0.12824895385159427
fdWL.freq(1)
0.3525667472151824
fdWL.most_common()
[(1, 5982), (3, 2375), (4, 2298), (2, 2176), (5, 1450), (6, 1207), (7, 713), (8, 395), (9, 254), (10, 49), (11, 31), (12, 31), (13, 6)]
fdist[1]
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    fdist[1]
NameError: name 'fdist' is not defined. Did you mean: 'fdist1'?
fdWL[1]
5982
fdWL.N()
16967
for sample in fdWL:
    print(sample)

1
3
4
2
5
6
7
8
9
10
11
12
13
>>> fdWL.tabulate()
   1    3    4    2    5    6    7    8    9   10   11   12   13 
5982 2375 2298 2176 1450 1207  713  395  254   49   31   31    6 
>>> sorted(w for w in set(text7) if w.endswith("able"))
['Equitable', 'Huxtable', 'Negotiable', 'Sable', 'Unable', 'able', 'adjustable', 'affordable', 'amicable', 'applicable', 'available', 'cable', 'comfortable', 'comparable', 'conceivable', 'considerable', 'deplorable', 'desirable', 'disagreeable', 'distributable', 'durable', 'enable', 'enviable', 'exercisable', 'expendable', 'favorable', 'foldable', 'hospitable', 'improbable', 'incapable', 'inevitable', 'knowledgeable', 'liable', 'negotiable', 'non-biodegradable', 'non-callable', 'nondurable', 'notable', 'objectionable', 'payable', 'predictable', 'profitable', 'punishable', 'questionable', 'rechargeable', 'recyclable', 'regrettable', 'remarkable', 'respectable', 'retractable', 'salable', 'severable', 'sizable', 'stable', 'table', 'taxable', 'unable', 'uncomfortable', 'undesirable', 'unfathomable', 'unreasonable', 'unrecognizable', 'unworkable', 'valuable', 'venerable', 'workable']
>>> sorted(w for w in set(text7) if w.endswith("able") and w.islower())
['able', 'adjustable', 'affordable', 'amicable', 'applicable', 'available', 'cable', 'comfortable', 'comparable', 'conceivable', 'considerable', 'deplorable', 'desirable', 'disagreeable', 'distributable', 'durable', 'enable', 'enviable', 'exercisable', 'expendable', 'favorable', 'foldable', 'hospitable', 'improbable', 'incapable', 'inevitable', 'knowledgeable', 'liable', 'negotiable', 'non-biodegradable', 'non-callable', 'nondurable', 'notable', 'objectionable', 'payable', 'predictable', 'profitable', 'punishable', 'questionable', 'rechargeable', 'recyclable', 'regrettable', 'remarkable', 'respectable', 'retractable', 'salable', 'severable', 'sizable', 'stable', 'table', 'taxable', 'unable', 'uncomfortable', 'undesirable', 'unfathomable', 'unreasonable', 'unrecognizable', 'unworkable', 'valuable', 'venerable', 'workable']
>>> fdAble = FreqDist(w for w in set(text7) if w.endswith("able") and w.islower())
>>> fdAble.plot()
<Axes: xlabel='Samples', ylabel='Counts'>
>>> fdAble = FreqDist(w for w in text7 if w.endswith("able") and w.islower())
>>> fdAble.plot()
<Axes: xlabel='Samples', ylabel='Counts'>
