# DrawGuesser

Web application which guesses whether the artist drew a Dog, House, Giraffe, Horse, Elephant or ~~Person~~.

*Note: Guessing for "Person" is very poor due to small training pool*

Model was generated using pre-trained ResNext101_32x8d weights and additional Linear and ReLu layers. Model was trained on subset of PACS dataset. These pre-trained weights were used based off the data presented in *https://openreview.net/pdf?id=z-LBrGmZaNs* .

Web Application was developed using simple implementations of Flask, PyTorch and Javascript/HTML.
To get the web-app running locally, I suggest using Docker-Compose. However, a requirements.txt file is included to select the python libraries necessary to get the project running.
