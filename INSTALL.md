## Flask

    pip install -r requirements.txt
    cp  flaskenv-dist .flaskenv

    flask run

## Apache

### Prerequisites

linux packages

    sudo apt install apache2

    sudo apt-get install libapache2-mod-wsgi-py3 python-dev


Note that the needed wsgi file is `tryflask.wsgi`



## Testing

    sudo apt-get install chromium-chromedriver
    pip install -r requirements-tests.txt

