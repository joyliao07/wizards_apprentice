import random


colors = ['red', 'green', 'blue']
nouns = ['pipe', 'fruit', 'table', 'chair', 'car', 'ball', 'door', 'button', 'mug', 'pen', 'bike']


def random_generator(colors, nouns):
    """To generate random pairs of colors and nouns."""
    ran_noun = (random.randint(0, len(nouns)-1))
    ran_color = (random.randint(0, len(colors)-1))
    print(colors[ran_color], nouns[ran_noun])
    return(colors[ran_color], nouns[ran_noun])


random_generator(colors, nouns)
