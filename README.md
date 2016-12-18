
# msa-image-python

This Docker image can be used to create Python RESTful microservices. It includes the following components :

- Alpine Linux 3.4
- Python 3.5.2
- Nginx 1.10.2
- [msa-nginx-dashboard](https://github.com/TheMicroservicesAgency/msa-nginx-dashboard) ( custom dashboard for Nginx stats collected via nginx-module-vts )
- [msa-swagger-ui](https://github.com/TheMicroservicesAgency/msa-swagger-ui) ( API documentation )
- [msa-readme-parser](https://github.com/TheMicroservicesAgency/msa-readme-parser) (Simple Readme.md to html converter)

## Nginx configuration

Nginx is preconfigured to listen on the port **80**, and act as a reverse proxy to any HTTP application running on the port **8080**.

Nginx will foward every HTTP request to the port 8080, except for the following URLs, since they are reserved by convention.

Any microservice built with this image should overrite the following files via the COPY command in the Dockerfile, to update these endpoints.

| File                          | URL                           |
|-------------------------------|-------------------------------|
| /opt/ms/VERSION               | /ms/version                   |
| /opt/ms/NAME                  | /ms/name                      |
| /opt/ms/Readme.md             | /ms/readme.md                 |
| /opt/swagger/swagger.json     | /swagger/swagger.json         |


Other endpoints available :

| Component             | URL                 | Description                    |
|-----------------------|---------------------|--------------------------------|
| msa-readme-parser     | /ms/readme.html     | HTML version of the Readme     |
| msa-swagger-ui        | /swagger/#/         | Swagger-UI                     |
| msa-nginx-dashboard   | /nginx/stats.html   | Dashboard with stats on Nginx  |
| msa-nginx-dashboard   | /nginx/stats.json   | Stats on Nginx as JSON         |

Also included in the default Nginx configuration  :

- CORS headers
- Gzip compression
- Keep-alive
- 50 MB cache

## Usage

To use this image simply this line at the top of your Dockerfile :

```
FROM msagency/gmsa-image-python:latest
```

An example can be found here : [msa-template-python](https://github.com/TheMicroservicesAgency/msa-template-python)

## Todo

- Simplify the Nginx config


## About

A project by the [Microservices Agency](http://microservices.agency).
