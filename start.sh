cron &   # used to start cron daemon

python /app/elt_script.py



# The above script would run every single time when it's 10 AM 
# when the docker container is started , the cron job would run in the background and it would run the
# above pythi=on script when it's 10AM