# To start run these commands form the commandline/terminal:

virirtualenv -p python3.6 .

source bin/activate

pip install django==1.11.2


pip install gunicorn
pip install dj-database-url pillow
pip install django-crispy-forms

in same dir as manage.py run
python manage.py runserver



