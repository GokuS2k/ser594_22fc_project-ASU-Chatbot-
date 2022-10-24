import nltk


def to_lower(raw):
    raw = raw.lower()
    return raw


def list_of_sent(raw):
    return nltk.sent_tokenize(raw)


def list_of_word(raw):
    return nltk.sent_tokenize(raw)