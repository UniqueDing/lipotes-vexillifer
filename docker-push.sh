#!/bin/bash

set -e

npm run build

rm -r dist/article
rm -r dist/note/*
rm -r dist/ebook/*
rm -r dist/picture/*

docker build -t uniqueding/lipotes-vexillifer .
docker push uniqueding/lipotes-vexillifer


