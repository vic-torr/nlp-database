# VocAPI
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)


| HTTP Method  | Action  |  URI | 
|---|---|---|
|POST | Post text                               | url/post          |
|GET   | Complete vocabulary                    | url/word_vocab    |
|GET   | Complete 2-gram vocabulary             | url/2_gram_vocab  |
|GET   | word array of each and all documents   | url/docs_words    |
|GET   | word 2-gram of each and all documents  | url/docs_2_gram   |




Package Setup
==============
mkvirtualenv vocapi  
python3 -m pip install --upgrade setuptools wheel  
python3 setup.py sdist bdist_wheel  

pip install -e .  

AWS Setup
============

sudo yarn install python3.8 python3-pip python3-dev python-virtualenv   virtualenvwrapper  

pip install -r requirements.txt  

export WORKON_HOME=$HOME/.virtualenvs  
export PROJECT_HOME=$HOME/Devel  
source /usr/local/bin/virtualenvwrapper.sh  
export PIP_REQUIRE_VIRTUALENV=true  
source ~/.bashrc  

git clone https://github.com/vic-torr/vocapi  
mkvirtualenv vocapi --python=3.8  
