# trello-uploader

https://github.com/YumNumm/trello-uploader/assets/73390859/ba8ea8a7-2ca6-4be8-b215-d80315ba0ba0

## HOW TO USE
### GET TRELLO KEY AND TOKEN
1. Login to Trello
1. Go to [Power-Up Admin Portal]
1. Click `New`
1. Fill in the form
1. Copy `API Key` and paste it to `TRELLO_API_KEY` in `.env`
1. Click `Generate Token (Manually)` and paste it to `TRELLO_API_TOKEN` in `.env`

## Install dependencies
```bash
# Install Rye package manager
curl -sSf https://rye-up.com/get | bash

# Install dependencies
rye sync
rye shell
python ./src/main.py

```

[Power-Up Admin Portal]: https://trello.com/power-ups/admin
[
