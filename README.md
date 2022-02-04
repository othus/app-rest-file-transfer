# REST secure file transfer app

This project contains two independent python apps, app-receiver and app-sender (an HTTP-REST server and client respectively).

**app-receiver** is a simple restful application written in python Flask framework and hosted with gunicorn. It provides two rest interfaces:
- GET '/': Checks the health of the service. Returns 200 with json response when successful.
- POST '/upload/<filename>': Accepts a file in the form of multipart/form-data. Upon successful receipt of the file, it will be decrypted and stored to a location specified with OUTPUT_DIR environment variable.

**app-sender** acts as a client to app-receive. It will:
1. Scan for json files in an input directory and verify if has been processed before (if that is the case, it will skip and move to the next file).
2. Convert the json file to xml, encrypt it with symmetric encryption.
3. Send the encrypted file to the server endpoint '/upload/<filename>' using a POST request. Address and port are specified by env vars.
4. The server (app-receiver) will receive the file and decrypt it using the same key, and save it. If everything went well, it will send back a successful HTTP response.

## Requirements

- Python 3
- Docker & docker-compose
- Pip3 and pipenv

## Built with 
- Python 3 & Flask: webapp development.
- pytest: testing framework.
- [Fernet library](https://cryptography.io/en/latest/fernet/): Python library to encrypt/decrypt files using symmetric encryption. 
- Docker: For the containerization of the app.

## Installation

To create a python virtual enviroment in our machine we can execute in app-receiver and app-sender directories:

```bash
$ pipenv install --dev
```
Or we could just use docker-compose in the following way:
```bash
$ docker-compose -f docker-compose.yml build --no-cache
```

## Usage
- If you want to execute both apps directly on our machine 
do as it follows:

In '*/app-receiver/receiver/'*:
```bash
$ gunicorn server:app
```
In *'/app-sender/'* execute:
```bash
$ python3 server
```
- To run the apps in containers, in the base path run:
```bash
$ docker-compose up --build
```
Put json files in the specified input directory to be processed.

- To run unit tests on app-receiver (server), in *'/app-receiver/'* execute:
```bash
$ pytest -v tests
```
