<h1 align="center">Moodbot</h1> 
<div align="center">
  <strong>Simple mood recognition chatbot application with authentication, and articles.</strong>
</div>


<div align="center">
  <!-- Stability -->
  <a href="https://nodejs.org/api/documentation.html#documentation_stability_index">
    <img src="https://img.shields.io/badge/stability-experimental-orange.svg?style=flat-square"
      alt="API stability" />
  </a>
  <!-- Build Status 
  <a href="https://travis-ci.org/choojs/choo">
    <img src="https://img.shields.io/travis/choojs/choo/master.svg?style=flat-square"
      alt="Build Status" />
  </a>-->
  <!-- Test Coverage 
  <a href="https://codecov.io/github/choojs/choo">
    <img src="https://img.shields.io/codecov/c/github/choojs/choo/master.svg?style=flat-square"
      alt="Test Coverage" />
  </a>-->
  <!-- Downloads 
  <a href="https://npmjs.org/package/choo">
    <img src="https://img.shields.io/npm/dt/choo.svg?style=flat-square"
      alt="Downloads" />
  </a>-->
  <!-- Standard 
  <a href="https://standardjs.com">
    <img src="https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat-square"
      alt="Standard" />
  </a>-->
</div>


This project from Queen Mary University of London is a bot application for personal goals/motivation support. So far it is a rules-based platform recognizing up to seven emotions.

Technically it is a locally designed flask application that has a Client, which is a Simple UI chat interface, and ServerCLI backend that fetches users and chat understanding details with Rasa, an open source NLU tool.

## Installation

### Requirements

`pip install -r requirements.txt` The above command may fail for few packages like spacy. So you have to install the following pip install spacy and those which might lack

### Settings to change

This is a locally designed chatbot, you will probably have to change the credentials.

In app.py
 - MySQL credentials 
 - app secret key in the main

You may be able to ask the weather to the bot ! For that you must first create you own credentials on [apixu.com](https://www.apixu.com/).


## Running the app

If you fancy to test it locally designed application you have to run both the client and the server.
You may run in two terminals
 - `python app.py` which launch the client.
 - `python -m rasa_core.server -d myflaskapp/models/dialogue/ -u myflaskapp/models/nlu/default/moodnlu/ --debug -o out.log --cors *` which launch the server.

# Contribution

We are happy to let you join the team. We would like to :

 - have more data in data/data.json enabling the bot to have more understanding, stories in data/stories.md for better answers and a more answers in the domain.yml.
 - enable people to talk to each other and store their anonymous data which could then be used for ML NLU for furthering the dialog agent.

Do not hesitate to fork the project.

# Reporting Issues

We love feedback from our former padawans, feel free to raise an issue for any problem.

