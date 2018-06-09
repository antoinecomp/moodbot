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

<div align="center">
  <h3>
	<!--
    <a href="https://choo.io">
      Website
    </a>
    <span> | </span>
    <a href="https://github.com/choojs/choo-handbook">
      Handbook
    </a>
    <span> | </span>
    <a href="https://github.com/YerkoPalma/awesome-choo">
      Ecosystem
    </a>
    <span> | </span>-->
    <!-- <a href="https://github.com/trainyard/choo-cli"> -->
    <!--   CLI -->
    <!-- </a> -->
    <!-- <span> | </span> -->
	<!--
    <a href="https://github.com/choojs/choo/blob/master/.github/CONTRIBUTING.md">
      Contributing
    </a>
    <span> | </span>-->
	Come discuss with us 
    <a href="https://www.reddit.com/r/Moodbot/">
      @Reddit
    </a>
	<!--
    <span> | </span>
    <a href="https://webchat.freenode.net/?channels=choo">
      Chat
    </a>-->
  </h3>
</div>


This project from Queen Mary University of London is a bot application for personal goals/motivation support. So far it is a rule-based platform recognizing up to seven emotions.

Technically it is a locally designed flask application that has a Client, which is a Simple UI chat interface, and ServerCLI backend that fetches users and chat understanding details with Rasa, an open source NLU tool.

![chatbot photo is comming back soon!](https://i.stack.imgur.com/sAtgy.png)

<h2> Installation </h2>

<h3> Requirements</h3>

`pip install -r requirements.txt` The above command may fail for few packages like spacy. So you have to install the following pip install spacy and those which might lack.

 - rasa-nlu, please follow the [official documentation](https://nlu.rasa.com/tutorial.html)
 - rasa_core `pip install rasa-core==0.9.0a3`
 - for the weather you might need `pip install git+https://github.com/apixu/apixu-python.git`

<h3> Settings to change</h3>

This is a locally designed chatbot, you will probably have to change the credentials.

In app.py
 - MySQL credentials 
 - app secret key in the main

You may be able to ask the weather to the bot ! For that you must first create you own credentials on [apixu.com](https://www.apixu.com/).


<h2> Running the app </h2>

Don't forget to build your model first with `python train_init.py`.
You have to run both the client and the server.
You may then run in two terminals in your project directory the following command :

 - `python app.py` which launch the client.
 - `python -m rasa_core.server -d models/dialogue/ -u models/nlu/default/moodnlu/ --debug -o out.log --cors *` which launch the server.

<h2> Modifying the NLU model </h2>

This chatbot is a totally open-source project, you are free to modify it in every way

<h3>Modifying the domain</h3>

The domain specifies the universe in which the bot's policy acts.
A Domain subclass provides the actions the bot can take, the intents and entities it can recognise

<h3>Create more stories</h3>

If the model is done you may want to add more stories. In order to do that you may run `python train_online.py`
You will be able to stack new stories to the old ones but pay attention to where you save it !

<h2> Contribution </h2>

We will be happy to let you join the team! We would like to :

 - have more data in data/data.json. Indeed, the more data you have here, the more the bot will be able to understand.
 - have more stories in data/stories.md for better answers.
 - have more mood, actions and templates in the domain.yml.
 - enable people to talk to each other and store their conversation as anonymous data which could then be used for ML NLU for furthering the dialog agent. Today this is provided by the article systems, which isn't the best way to do chat.

Do not hesitate to fork the project.

<h2> Reporting Issues</h2>

We love feedback from our former padawans, feel free to raise an issue for any problem. 

