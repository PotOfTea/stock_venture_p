# Calculates stock allocation

## How to run

Required tools:
* GNU Make
* Docker
* Python (optional, for running tests locally)
* kubectl (optional, for deployment to K8S cluster)

```sh
# To run app
make run
```

```sh
# To delete local app
make delete
```

```sh
# To run test
make test
```

```sh
# To deploy to kubernetes cluster (Assuming k8s context is set in terminal)
make deploy
```


```sh
# To undeploy
make undeploy
```


```sh
# To access deployed app
make port-forward
```

## Routes

* `/` - GET display info message
* `/` - POST parses investor json data
* `/alive` - K8S health checks
* `/docs` - List api, amd provide way to interact from browser

## Info

API was implemented using `Python3` and `Fast Api` framework.
Application is bare-bone and just enough work and serves rest api.

Code that is responsible for generating the stock distribution is located in:


```
website/app/algorithm/stock_distribution.py
```

## Algorithm description

*Same description can be found in a code with code specific comments*

Steps:

1. Investors are divided in 2 groups:
    * Group A who request stock less or equal amount then they can have
    * Group B who request more stock then they have
2. Group A stock allocation is calculated and subtracted from overall pool
3. Group B stock allocation is calculated on remaining stocks

This method will run in O(N) linear time.

## Testing

For testing I used provided samples from `data` to verify algorithm

Test location
```
website/tests
```

## Infrastructure tooling
Local deployment configuration is located in:

```
Dockerfile
deplyment.yaml
```