# BT_TECH_TEST

# Fair Billing

## Description
This script processes a log file containing session start and end times and calculates the total session duration for each user.

## How to execute:
navigate to the same folder which the program and log file is in using terminal (linux) / command line (windows)
follow steps below

## On local PC

### Prerequisites
- python version 3.2 => is installed on machine

#### Run application
```shell
python fair_billing.py {path_to_file_and_name}
```

#### Run test 
```shell
python -m unittest test/*
```

## Using  Docker
The steps below uses docker to run and test 

### Prerequisites
- Docker installed on your machine

### Steps
1. Build the Docker image:
```sh
    docker build -t fair_billing .
```

2. Run the application:
```shell
    docker run --rm -v fair_billing:/app fair_billing /app/<log_file_name>
```

### Running Tests
#### Unit Tests
1. Run the unit tests:
```shell
    docker run --rm -v fair_billing:/app fair_billing python -m unittest test/*
```

## Example
To process a log file named `sample_log.txt`:
```shell
docker run --rm -v fair_billing:/app fair_billing /app/sample_log.txt
```
