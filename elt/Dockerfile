FROM python:3.8-slim

RUN apt-get update && apt-get install -y postgresql-client cron

COPY start.sh /app/start.sh  

# used to copy start.sh to in app directory of docker. docker now has .sh file within directory
COPY elt_script.py .

WORKDIR /app 

RUN echo "6 18 * * * python /app/elt_script.py" | crontab -
# to run the job everyday at 3 AM
CMD [ "python", "elt_script.py" ]