# docs

## development

```sh
python -m env venv
source env/bin/activate
pip install -r requirements.txt # for a fully complete dev + test env
# python setup.py install => for container builds only
export PROJECT_ID=$(gcloud config get-value project)
# create a firestore admin service account here
# https://cloud.google.com/firestore/docs/quickstart-servers,
# use that json file here, you dont need this for mock serving for test purposes but 
# if you want to connect to a cloud based firestore, you will have to use the 
# corresponding project credentials 
# export GOOGLE_APPLICATION_CREDENTIALS=./creds/your-credentials.json 
uvicorn main:api --reload
gunicorn main:api -c gunicorn_config.py
```

## testing 

```sh
pytest tests/v1 -s --cov=. --cov-report html:./htmlcov --cov-fail-under 100 --log-cli-level ERROR
```

## docker

```sh
docker build -t firestore-fastapi --file docker/Dockerfile .
docker run -p 8080:8080 -it firestore-fastapi # will throw credentials error locally
docker build -t firestore-fastapi-test --file docker/test/Dockerfile .
```

## deploy to cloud run via cloud build

Follow the docs [here](https://cloud.google.com/cloud-build/docs/automating-builds/create-github-app-triggers) to learn how to automate builds via the Google Cloud Build GitHub App. You will also need to enable a Native Firestore database (not Cloud Datastore!) and enable the Cloud Run Admin API via Cloud Build's settings.
