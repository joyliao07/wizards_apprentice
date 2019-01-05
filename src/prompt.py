from random import choice as randchoice

from .models import db, Prompt
from sqlalchemy.exc import IntegrityError


adjectives = ['red', 'green', 'blue']
nouns = ['fruit', 'table', 'chair', 'sofa', 'car', 'ball', 'door', 'laptop', 'mug', 'bicycle', 'bird', 'backpack', 'mouse', 'book']


def random_generator():
    """To generate random pairs of colors and nouns."""
    ran_adjective = randchoice(adjectives)
    ran_noun = randchoice(nouns)

    try:
        prompt = Prompt(adjective=ran_adjective, noun=ran_noun)
        db.session.add(prompt)
        db.session.commit()
        return True

    except IntegrityError:
        return False
