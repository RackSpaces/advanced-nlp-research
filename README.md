
# Advanced Research in NLP with Unstructuctured News Data

This repository provides Python codes and Jupyter Notebooks used in the applied research paper 'Unlocking the Hidden Potential of Unstructured News Data with NLP - Understanding Advanced Analytics through Real-World Case Studies'.

![Cover Page](http://hilpisch.com/images/dna_paper_cover.png)

## Accessing the Applied Research Paper 

To download the PDF version of the research paper, visit [Research Paper](http://go.dowjones.com/dna-research-paper).

## Setup Guidelines

These instructions will help you run a Docker container or a cloud instance (with latest Ubuntu version). You need sufficient compute and memory resources. It is recommended to have at least four CPU cores and 16GB of RAM. 

### Running on a Cloud Instance

Assuming you've set up a cloud instance (eg. DigitalOcean) and logged in as `root`:

    cd /root
    wget http://hilpisch.com/nlp/setup_dna_nlp.sh
    bash setup_dna_nlp.sh

Follow the instructions, provide a password for the Jupyter Notebook server. You can access the server at:

    http://CLOUD_IP_ADDRESS:9999

Use the chosen password to log in.

### Running in a Docker Container

You can start a Docker container locally, ensure it has sufficient resources allocated. You can then execute:

    docker run -ti -h dnanlp -p 9999:9999 ubuntu:latest /bin/bash

Then on the shell of the Docker container, execute the following:

    cd root
    apt-get update
    apt-get upgrade -y
    apt-get install -y wget
    wget http://hilpisch.com/nlp/setup_dna_nlp.sh
    bash setup_dna_nlp.sh

Then you can access the Jupyter Notebook server at:

    http://localhost:9999

Log in with your chosen password.

## Security and Disclaimer

This is for demonstration purposes only. It has no security measures beyond password protection. No SSL encryption is configured. The server runs under `root`, leading to potential security risks. The repository is for illustration purposes only and comes with no representations or warranties, to the extent permitted by law.

## Contact Information

You can find more about RackSpaces at: 

[RackSpaces](http://tpq.io) 

**Python for Finance & Algorithmic Trading online trainings** 

[Online Training](http://training.tpq.io) 

**University Certificate Program in Python for Algorithmic Trading** 

[Certificate Program](http://certificate.tpq.io)