# FILE: deploy.sh

# SERVER SPECIFIC VARIABLES
SERVER=class3.eecs.umich.edu 						# TODO set your server here!
PORT1=4550											# TODO set your ports here!

# GROUP VARIABLES
GROUP=group23										# TODO set you group number
SECRET=jag_password						# TODO set your secret

# STATIC RESOURCE paths									# TODO make sure you have a backup folder
IMAGES=static/images									# and that the paths are correct
IMAGES_BACKUP=static/images_copy

# SQL SCRIPT PATH										# TODO make sure paths are correct
SQL_CREATE=sql/tbl_create.sql
SQL_LOAD=sql/load_data.sql

# ASSIGNMENT VARIABLES
PROJECT=p2
DB=db											# TODO project number here (for sql)

# SCRIPT COMMANDS
echo "Searching for gunicorn process on $(whoami)..."
GUNI_PID=$(ps aux | grep $(whoami) | grep '[g]unicorn' | awk '{print $2}')
if [ -z "$GUNI_PID" ]; then
	echo "No gunicorn process found"
else
	kill $GUNI_PID
	echo "Gunicorn process terminated"
fi

echo "Resetting static resources from backup..."
rm $IMAGES/*
cp $IMAGES_BACKUP/* $IMAGES/
echo "Done."

echo "Resetting SQL database..."
SQL_QUERY="drop database $GROUP$DB; create database $GROUP$DB; use $GROUP$DB; source $SQL_CREATE; source $SQL_LOAD;"
mysql -u $GROUP -p"$SECRET" -e "$SQL_QUERY"
echo "Done."

echo "Starting server on $SERVER at port $PORT1..."
gunicorn -b  $SERVER:$PORT1 -D --debug --access-logfile access.log --error-logfile error.log app:app
echo "Done."