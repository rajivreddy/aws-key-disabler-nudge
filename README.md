
```bash
cp config.example config
docker build -t example .
docker run -t --env-file=./config example

```
