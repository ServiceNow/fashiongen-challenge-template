========
Overview
========

This template defines the set of files we need to run and evaluate your models.
For the evaluation, we will replace the `dummy_inputs.csv` file with data from the test set.

Before you run the code you should build your container with `docker-compose`::

    docker-compose build generate

To run your project use the `generate` service with `docker-compose`::

    docker-compose run --rm generate

You will find the results in the `results` folder.
If the images in the `results` folder have the sufficient quality for you to submit, follow the steps from the Quickstart_ in the wiki to get started.

.. _Quickstart: https://github.com/ElementAI/fashiongen-challenge-template/wiki
