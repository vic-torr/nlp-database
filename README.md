# nlp-database
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)


| HTTP Method  | Action  |  URI | 
|---|---|---|
|POST | Post text                               | url/post          |
|GET   | Complete vocabulary                    | url/word_vocab    |
|GET   | Complete 2-gram vocabulary             | url/2_gram_vocab  |
|GET   | word array of each and all documents   | url/docs_words    |
|GET   | word 2-gram of each and all documents  | url/docs_2_gram   |








setup aws
============





sudo apt-get install python3-pip python3-dev python-virtualenv
virtualenv --system-site-packages -p python3 .env3
source .env3/bin/activate
git clone https://github.com/vic-torr/nlp_db

pip install -r requirements.txt



PYTHONPATH=./ FLASK_ENV=development  python ./nlp-db/app.py