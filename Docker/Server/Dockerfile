#####################################
# Build image: docker build -t lnestelroad/flask-demo .
# Run image: docker run -d -p 5000:5000 lnestelroad/flask-demo 
#####################################


FROM ubuntu

RUN apt-get update -y && \
    apt-get install -y \
    python3 \
    python3-dev \
    python3-pip \
    libpq-dev \
    apt-utils

RUN pip3 install --upgrade pip 

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

# CMD [ "app.py" ]
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
CMD ["flask", "run", "--host", "0.0.0.0"]