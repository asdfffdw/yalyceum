phrases = set()


def parrot(phrase):
    if phrase in phrases:
        print(phrase)
    else:
        phrases.add(phrase)