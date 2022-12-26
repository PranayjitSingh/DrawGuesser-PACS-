# DrawGuesser #

Web application which guesses whether the artist drew a Dog, House, Giraffe, Horse, Elephant or ~~Person~~.

*Note: Guessing for "Person" is very poor due to small training pool, so temporarily disabled*

Model was generated using pre-trained ResNext101_32x8d weights and additional Linear and ReLu layers. Model was trained on subset of PACS dataset. These pre-trained weights were used based off the data presented in *https://openreview.net/pdf?id=z-LBrGmZaNs* . Follow-up to work completed for University of Waterloo SYDE522.

# Installation/Getting Started #
The web app was developed using simple implementations of Flask, PyTorch and Javascript/HTML.
To get the web-app running locally, I suggest using Docker-Compose. However, a requirements.txt file is included to specify the python libraries necessary to get the project running without containerization as well.

## Using Docker Containers ##
1. Navigate to repo root folder
2. `docker-compose up [-d]`
3. Open a browser and navigate to http://127.0.0.1:4000

## Local Installation ##
*Note: I used Python 3.9.6 and I suggest making sure pip is upgraded before proceeding*
1. Navigate to repo root folder
2. `pip install -r requirements.txt`
3. `python app/app.py 127.0.0.1 54321`
  - Can replace the localhost IP and Port as you need
4. Open a browser and navigate to http://127.0.0.1:54321 