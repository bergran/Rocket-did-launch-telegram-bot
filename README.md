# Did The Rocket Launch Yet

Welcome to Did The Rocket Launch Yet!

This project is a game where the bot will send to user an image from
space X rocket launch, on all rounds it will ask if the rocket did launch
until get the last frame that the algorithm guess that the rocket launch.

## How works

Algorithm used is Bisect, this means per user response will get middle frame
between left and right. Left will update state when "no" response is given, in
the other hand, right. Then, it will calculate mid frame.


## Requirements

docker
docker-compose

## Environment variables

- BERNARD_BASE_URL = Servername where Bernard app it will run,
it should be a public servername or Telegram wont send updated.
- TELEGRAM_TOKEN = Telegram bot token, you can create it with @BotFather.

## Deploy with docker

- In the server, execute `docker-compose up -d`

## Docker-Compose containers

Docker compose on up, it will run 2 new containers, Bernard app and Redis app

## Author

Ángel Berhó

