## CI/CD by used GitHub Actions, Amazon S3 and AWS Elastic Beanstalk

#### An application is available online
http://flaskbmr-env.eba-de6mxh4k.eu-central-1.elasticbeanstalk.com/

#### GitHub Actions with follow jobs:    [[my-basics.yml]](.github/workflows/my-basics.yml)

- tests(flake8 & pytest)
- build
- deploy

## WEB
GET / - render create page with human body parameters and food required form

POST / - render index page with required and received calories

## How to run manually on local machine
1. ```
   git clone git@github.com:0brain/flask_app_CI_CD.git
   
2. ```
   virtualenv -p python3.9 venv 

3. ```
   source venv/bin/activate

4. ```
   pip install -r requirements.txt

5. ```
   python run.py
6. An application will run locally on http://127.0.0.1:5000 

## How to test (pytest & flake8 )
1. ```
   python3.9 -m pytest -v tests
2. ```
   python3.9 -m flake8
