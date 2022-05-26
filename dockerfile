FROM python:3.8-alpine


COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY ./flaskproject/ /app

EXPOSE 5000

# configure the container to run in an executed manner
ENV FLASK_APP=flaskr
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0" ]
