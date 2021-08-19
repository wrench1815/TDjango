# TDjango

## Note: This is just a demo project to test how Django Ckeditor can work and it's moving to another phase where its becoming my Playground

### Usage

- If using Poetry use `Poetry install` to download all the packages else use `pip install -r requirements.txt`
- Time to collect static files run `python manage.py collectstatic` in terminal to collect the static files
- Now in terminal run `python manage.py runserver` and open the url shown in Terminal

### Do it my way

- Create a virtual environment in any location with `python -m venv EnvName` where `EnvName`, is the name of your virtual environment.
- activate the virtual environment.

  - on WIndows use `EnvName\Scripts\Activate.ps1` for Powershell
  - on Linux use `source EnvName\Scripts\Activate`

- Now cd into to Project Directory in terminal and run `poetry install` if Poetry is installed on system else use `pip install -r requirements.txt`
- Run `python manage.py collectstatic` to collect all Static files for the Project
- Now run `python manage.py runserver` or setup Django debug config as if using VSCode

## Default Admin Credentials

**Username**: admin <br/>
**Password**: test@123

# <span stye="color: red">Warning! The `SECRET_KEY` in Application is supposed to be a demo key, never use such weak SECRETS in Production or Hard Code them</span>

Btw, TDjango means TestDajngo :laughing:
