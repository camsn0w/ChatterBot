import spacy


def sourceLanguageModel():
    from spacy.cli.download import download
    download(model="en_core_web_sm")


def CheckAndGetNlp():
    try:
        return spacy.load('en_core_web_sm')
    except OSError:
        sourceLanguageModel()
    return None
