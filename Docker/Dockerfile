######################################################
### ---- Create a Docker image for UCloud Docs ---- ###
#######################################################

FROM python:3.7-alpine3.12 as builder

## Fix issue in Node/Docker as reported here:
## https://stackoverflow.com/questions/52196518/could-not-get-uid-gid-when-building-node-docker
# ENV npm_config_unsafe_perm true

## Dependencies
RUN apk update && \
	apk add --update \
	alpine-sdk \
	gfortran \
	py-pip \
	build-base \
	gcc \
	libcurl \
	pkgconfig \
	libc-dev \
	jpeg-dev \
	libpng \
	libpng-dev \
	freetype \
	freetype-dev \
	zlib-dev --no-cache && \
	pip3 install --upgrade pip

RUN mkdir -p /type3 

WORKDIR /type3

COPY src ./src
COPY ucloud_theme ./ucloud_theme
COPY requirements.txt Makefile ./

RUN pip install cython wheel && \
	pip install -r requirements.txt && \
	make clean && \
	make html 

FROM nginx:alpine

LABEL build_date="2021-03-01" \
	  commit="f8f4f50" \
	  description="Type 3 User Guide" \
	  url="https://docs.hpc-type3.sdu.dk"

MAINTAINER Emiliano Molinaro "molinaro@imada.sdu.dk"

ENV REFRESHED_AT 2021-03-01

## Copy static webserver
COPY --from=builder /type3/_build/html /usr/share/nginx/html/type3

RUN chown -R nginx:nginx /usr/share/nginx/html/type3

## Copy nginx config file
COPY Docker/nginx/conf.d/ /etc/nginx/conf.d/
RUN chown -R nginx:nginx /etc/nginx/conf.d/

WORKDIR /

EXPOSE 8080
