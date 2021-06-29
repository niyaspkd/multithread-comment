pip install -r requirements.txt

install postgresql 
sudo su postgres
CREATEDB commentdb;
rename .env.example to .env and use your configration
python manage.py makemigrations 
python manage.py migrate
python manage.py runserver

#Hav'e a Nice Day

all urls listed in homepage
to delete all comments of a post please add ?post_id to the end of url 