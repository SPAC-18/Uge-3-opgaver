names = ["Bob", "Verylongname", "Nora", "AAAAA"]

def name_to_character_set(name):
    result = set()
    for i in range(len(name)):
        result = result.union({name[i]})
    return result

def name_list_to_string(name_list):
    result = ""
    for name in name_list:
        result = result + name
    return result

def letter_dict(name_list):
    letter_set = set(name_list_to_string(names).lower())
    dict_list = []
    for letter in sorted(letter_set):
        dict_list.append((letter, 0))   
    return dict(dict_list)

def letter_counter(name_list):
    result = letter_dict(name_list)
    letters = name_list_to_string(name_list).lower()
    for i in letters:
        result[i] += 1
    return result

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = letter_counter(names)

ind = np.arange(len(data))

plt.bar(ind, list(data.values()))
plt.xticks(ind, list(data.keys()))
plt.show()

import wordcloud

wc = wordcloud.WordCloud().generate_from_frequencies(letter_counter(names))
plt.imshow(wc)

plt.axis("off")
plt.tight_layout(pad = 0)
 
plt.show()