# DrawGuesser - PACS #

Web application which guesses whether the artist drew a Dog, House, Giraffe, Horse, Elephant or ~~Person~~.

*Note: Guessing for "Person" is very poor due to small training pool, so temporarily disabled*
*Note: Initial guess after launching server may take a minute or two (has to download pre-trained model)*

Model was generated using pre-trained ResNext101_32x8d weights and additional Linear and ReLu layers. Model was trained on subset of PACS dataset. These pre-trained weights were used based off the data presented in *https://openreview.net/pdf?id=z-LBrGmZaNs* . Follow-up to work completed for University of Waterloo SYDE522.

# Installation/Getting Started #
The web app was developed using simple implementations of Flask, PyTorch and Javascript/HTML.
To get the web-app running locally, I suggest using Docker-Compose. However, a requirements.txt file is included to specify the python libraries necessary to get the project running without containerization as well.

1\. Clone the repository  
2\. Download the model from DropBox (model.pt): https://www.dropbox.com/s/yb0uhrl2al87jai/model.pt?dl=0  
3\. Save the file as [repo root]/app/model.pt  

## Using Docker Containers ##
4\. Navigate to repo root folder  
5\. `docker-compose up [-d]`  
6\. Open a browser and navigate to http://127.0.0.1:4000  

## Local Installation ##
*Note: I used Python 3.9.6 and I suggest making sure pip is upgraded before proceeding*  
4\. Navigate to repo root folder  
5\. `pip install -r requirements.txt`  
6\. `python app/app.py 127.0.0.1 54321`  
    - Can replace the localhost IP and Port as you need  
7\. Open a browser and navigate to http://127.0.0.1:54321  
