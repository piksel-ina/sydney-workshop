# Docker Workshop

## Contents

* Docker 101: what is Docker (containerisation) and why is it important
* Building a docker image: it's a recipe for a repeatable software environment
* Running a docker image: it's a fancy process, not a virtual machine
* Using Docker Compose: configure a small networked environment to run an app or apps
* From development to production: dev/prod parity saves time
* Argo workflows: running many containers all at once.

The [presentation for this workshop is available here](https://docs.google.com/presentation/d/16shRDw2n2cL5FY-9eQt9pZccri23HgT8znoQm20Xf1w/edit).

## Example commands

### Build the Docker image

```bash
docker build --tag local:squares .
```

### Run the Docker image

```bash
docker run --rm local/squares
```

### Re-tag the image

```bash
docker tag local/squares alexgleith/squares
```

### Run the Postgres DB

```bash
docker compose up
```


## Extra examples

### Build and push a multi-architecture image

```bash
docker buildx create --use || docker buildx use default

docker buildx build --platform linux/amd64,linux/arm64 -t alexgleith/squares:latest -f docker/Dockerfile --push docker/
```
