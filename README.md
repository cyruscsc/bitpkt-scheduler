# bitpkt-scheduler

## Introduction

An AI-powered task scheduler with a RESTful API that uses genetic algorithms to intelligently schedule tasks based on available time slots, task durations, and priority levels.

Time is limited, but the workload is endless. We often struggle to efficiently manage tasks, especially when time is tight and we don’t want to give up on the tasks we’re passionate about, even though they may seem impossible to complete within a constrained schedule. Let the AI take over this challenging task for you.

> This app is still in development and may contain bugs or errors.

## Folder structure

```
└── app
    ├── scheduler  # scheduler module
    └── schemas    # pydantic schemas
```

## Tech stack

- [FastAPI](https://fastapi.tiangolo.com)
- DIY genetic algorithm

## Requirements

- [Python](https://www.python.org/) `3.13`
- FastAPI `0.115.11` for high-performance API
- [NumPy](https://numpy.org/doc/stable/) `2.2.3` for efficient array manipulation
- [Docker](https://www.docker.com/) for easy deployment

## Development

1. Run development server

```bash
fastapi dev app/main.py
```

2. View doc and play around

```bash
http://127.0.0.1:8000/docs
# or
http://127.0.0.1:8000/redoc
```

## Deployment

### Prerequisites

- Docker [registry](https://hub.docker.com/_/registry) set up on VPS
- SSL certificate configured for registry's domain
- Replace `<registry-domain>` in `compose.yml` and the following steps with the domain of the private registry

### On local machine

1. Build docker images
```bash
docker build -t <registry-domain>/bitpkt-scheduler:latest .
```

2. Push images to VPS registry
```bash
docker push <registry-domain>/bitpkt-scheduler:latest
```

### On VPS

1. Create a directory for the project and switch to it
```bash
mkdir bitpkt-scheduler
cd bitpkt-scheduler
```

2. Create `compose.yml` and paste the content (copied from `compose.yml` in this repo)
```bash
nano compose.yml
```

3. Pull images and start services
```bash
docker compose pull
docker compose up -d
```