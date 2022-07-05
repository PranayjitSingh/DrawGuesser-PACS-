# start by pulling the python base image
FROM python:3

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
RUN pip install torch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113

# copy every content from the local file to the image
COPY . /app /app

# execution command
CMD ["python", "app/app.py"]