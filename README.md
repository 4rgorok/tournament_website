# Website for Kyokushin tournament display

### Start server

1. Clone this repo:
```
git clone https://github.com/4rgorok/tournament_website.git
```

```
cd turnament_website
```

2. Setup database environmental variables in `AkaServer/AkaServer/.env`. Example:
```
DB_NAME=super_secret_db
DB_USER_NAME=admin
DB_USER_PASSWORD=admin
DB_HOST=super_secret_host
```

3. For Linux setup, run `run_backend.sh`. For Windows setup, run `run_backend.bat`. The server runs on default port `8000`.

### Start client

1. For Linux setup, run `run_frontend.sh`. For Windows setup, run `run_frontend.bat`. The client runs on default port `3000`.
