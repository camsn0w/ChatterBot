![pychatbot: Machine learning in Python](https://i.imgur.com/b3SCmGT.png)

# pychatbot

pychatbot is a machine-learning based conversational dialog engine build in
Python which makes it possible to generate responses based on collections of
known conversations. The language independent design of pychatbot allows it
to be trained to speak any language.

[![Package Version](https://img.shields.io/pypi/v/pychatbot.svg)](https://pypi.python.org/pypi/pychatbot/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Django 2.0](https://img.shields.io/badge/Django-2.0-blue.svg)](https://docs.djangoproject.com/en/2.1/releases/2.0/)
[![Requirements Status](https://requires.io/github/gunthercox/pychatbot/requirements.svg?branch=master)](https://requires.io/github/gunthercox/pychatbot/requirements/?branch=master)
[![Build Status](https://travis-ci.org/gunthercox/pychatbot.svg?branch=master)](https://travis-ci.org/gunthercox/pychatbot)
[![Documentation Status](https://readthedocs.org/projects/pychatbot/badge/?version=stable)](http://pychatbot.readthedocs.io/en/stable/?badge=stable)
[![Coverage Status](https://img.shields.io/coveralls/gunthercox/pychatbot.svg)](https://coveralls.io/r/gunthercox/pychatbot)
[![Code Climate](https://codeclimate.com/github/gunthercox/pychatbot/badges/gpa.svg)](https://codeclimate.com/github/gunthercox/pychatbot)
[![Join the chat at https://gitter.im/pychatbot/Lobby](https://badges.gitter.im/pychatbot/Lobby.svg)](https://gitter.im/pychatbot/Lobby?utm_source=badge&utm_medium=badge&utm_content=badge)

An example of typical input would be something like this:

> **user:** Good morning! How are you doing?  
> **bot:**  I am doing very well, thank you for asking.  
> **user:** You're welcome.  
> **bot:** Do you like hats?  

## How it works

An untrained instance of pychatbot starts off with no knowledge of how to communicate. Each time a user enters a statement, the library saves the text that they entered and the text that the statement was in response to. As pychatbot receives more input the number of responses that it can reply and the accuracy of each response in relation to the input statement increase. The program selects the closest matching response by searching for the closest matching known statement that matches the input, it then returns the most likely response to that statement based on how frequently each response is issued by the people the bot communicates with.

## Installation

This package can be installed from [PyPi](https://pypi.python.org/pypi/pychatbot) by running:

```
pip install pychatbot
```

## Basic Usage

```
from pychatbot import ChatBot
from pychatbot.trainers import pychatbotCorpusTrainer

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = pychatbotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("pychatbot.corpus.english")

# Get a response to an input statement
chatbot.get_response("Hello, how are you today?")
```

# Training data

pychatbot comes with a data utility module that can be used to train chat bots.
At the moment there is training data for over a dozen languages in this module.
Contributions of additional training data or training data
in other languages would be greatly appreciated. Take a look at the data files
in the [pychatbot-corpus](https://github.com/gunthercox/pychatbot-corpus)
package if you are interested in contributing.

```
from pychatbot.trainers import pychatbotCorpusTrainer

# Create a new trainer for the chatbot
trainer = pychatbotCorpusTrainer(chatbot)

# Train based on the english corpus
trainer.train("pychatbot.corpus.english")

# Train based on english greetings corpus
trainer.train("pychatbot.corpus.english.greetings")

# Train based on the english conversations corpus
trainer.train("pychatbot.corpus.english.conversations")
```

**Corpus contributions are welcome! Please make a pull request.**

# [Documentation](https://pychatbot.readthedocs.io/)

View the [documentation](https://pychatbot.readthedocs.io/)
for pychatbot on Read the Docs.

To build the documentation yourself using [Sphinx](http://www.sphinx-doc.org/), run:

```
sphinx-build -b html docs/ build/
```

# Examples

For examples, see the [examples](https://github.com/gunthercox/pychatbot/tree/master/examples)
directory in this project's git repository.

There is also an example [Django project using pychatbot](https://github.com/gunthercox/pychatbot/tree/master/examples), as well as an example [Flask project using pychatbot](https://github.com/chamkank/flask-pychatbot).

# History

See release notes for changes https://github.com/gunthercox/pychatbot/releases

# Development pattern for contributors

1. [Create a fork](https://help.github.com/articles/fork-a-repo/) of
   the [main pychatbot repository](https://github.com/gunthercox/pychatbot) on GitHub.
2. Make your changes in a branch named something different from `master`, e.g. create
   a new branch `my-pull-request`.
3. [Create a pull request](https://help.github.com/articles/creating-a-pull-request/).
4. Please follow the [Python style guide for PEP-8](https://www.python.org/dev/peps/pep-0008/).
5. Use the projects [built-in automated testing](https://pychatbot.readthedocs.io/en/latest/testing.html).
   to help make sure that your contribution is free from errors.

# License

pychatbot is licensed under the [BSD 3-clause license](https://opensource.org/licenses/BSD-3-Clause).
