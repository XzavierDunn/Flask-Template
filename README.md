To get started create a venv then "pip install -r requirements.txt"
after getting the packages installed set an environment variable for
your database. If you don't have one setup just make it an empty string

Mac/Linux:
export DATABASE_URL=''

Windows:
$env:DATABASE_URL=''

Then run 'python manage.py run'

