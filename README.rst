========
Overview
========

This template defines the set of files we need to run and evaluate your models.
For the evaluation, we will replace the `dummy_inputs.csv` file with data from the test set.

Before you run the code you should build your container with `docker-compose`::
    docker-compose build generate

To run your project you can use `docker-compose`::
    docker-compose run --rm generate

You can find the results in the `results` folder.
