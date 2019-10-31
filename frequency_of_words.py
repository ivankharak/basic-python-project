# !/usr/bin/env

# script by Ruchir Chawdhry
# released under MIT License
# github.com/RuchirChawdhry/Python
# ruchirchawdhry.com
# linkedin.com/in/RuchirChawdhry

from click import prompt
from collections import Counter


def _input():
    text = prompt("Text? ", type=str)
    return text


# For validation, if you don't want to use Click: https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response


def word_frequency(text):
    # with a for loop
    l = []
    t_lower = []
    for word in text.split(" "):
        t_lower.append(word.lower())
    for _, word in enumerate(t_lower):
        l.append(t_lower.count(word))
    freq = set(zip(l, t_lower))  # removes duplicates
    sorted_freq = sorted(list(freq), reverse=True)  # sorts in reverse
    return sorted_freq


def word_freq_alt(text):
    text = [word.lower() for word in text.split(" ")]
    word_freq = set(zip((map(text.count, (word.lower() for word in text))), text))
    return sorted(list(word_freq), reverse=True)


def word_freq_collections_counter(text):
    # with collections > Counter
    text = [word.lower() for word in text.split(" ")]
    word_freq = Counter(text)
    return word_freq.most_common(10)  # returns the ten most common words


if __name__ == "__main__":
    # input_ = _input()

    input_ = "A green hunting cap squeezed the top of the fleshy balloon of a head. The green earflaps, full of large ears and uncut hair and the fine bristles that grew in the ears themselves, stuck out on either side like turn signals indicating two directions at once. Full, pursed lips protruded beneath the bushy black moustache and, at their corners, sank into little folds filled with disapproval and potato chip crumbs. In the shadow under the green visor of the cap Ignatius J. Reilly’s supercilious blue and yellow eyes looked down upon the other people waiting under the clock at the D.H. Holmes department store, studying the crowd of people for signs of bad taste in dress. Several of the outfits, Ignatius noticed, were new enough and expensive enough to be properly considered offenses against taste and decency. Possession of anything new or expensive only reflected a person’s lack of theology and geometry; it could even cast doubts upon one’s soul."

    print(word_frequency(input_))
    print(word_freq_collections_counter(input_))
    print(word_freq_alt(input_))
