pip install Flask
pip install flask-sqlalchemy
pip install flask-migrate
pip install flask-script

python run.py runserver
python run.py db init
python run.py db migrate
python run.py db upgrade