# Week-8---DevOps-Core-Practical
A repository for my Core Practical Portion of QA Academy

## Contents
* [Project Brief](#Project_Brief)
* [Risk Assessment](#Risk_Assessment)
* [Technical Design](#Technical_Design)
* [App Design](#App_Design)
* [Pipeline](#Pipeline)
* [Known Issues](#Known_Issues)
* [Future Development](#Future_Development)
* [What would be done differently?](#What_would_be_done_differently?)

## Project Brief

This project, provided by the QA academy, was to create an application of four microservices that interacted with eachother, in order to generate at least three distinct objects using a variety of technologies.

## Risk Assessment

While in the planning stages of this project, this participant developed the following risk assessment:

## Technical Design

A variety of technologies were used in order to fully document and complete this project. These technologies and their rationale will be listed now.

* **Jira:** Jira is a piece of software that allows the user to plan out a project using User Stories and tasks, allowing for a great deal of insight into the develpment including burndown charts and other information. This participant chose Jira not only due to its support of Agile Methodologies, which DevOps is closely related to, but also due to their familiarity with it, using it for several years prior to time at the QA Academy.

* **Git:** A version control system that allows for easy and convenient modification to code and allows access on a variety of systems. This was choosen as an easy way to store code and can also be incoperated into the CI pipeline.

* **Jenkins:** Continuous Intergreation is one of the core tenants of DevOps, Jenkins allows a conenient way of achieving this. Jenkins allows the application to be updated with a simple Git push when connected to Git via the use of Webhooks, going through all the necessary steps before deploying the application to the web.

* **Ansible:** An extremely useful automation tool, Ansible is capable of doing a great many tasks with a single input, including installing and updating software on several machines. Ansible will be used to ensure that the required installations are performed before deploying the application.

* **GCP Virtual Machines:** Google Cloud Platform allows the creation of virtual machines, these machines can be customised for a vast variety of purposes. GCP will be used in this project to host this participants various virtual machines including their docker manager, worker, their ansible files and the NGINX load balancer.

* **Docker & Docker Swarm:** Containerisation is extremely useful and necessary tool in order to ensure that an application can run as smoothly as possible, as such Docker is extremelty useful tool for this, allowing the importing and pushing of images to and from Dockerhub. Docker Swarm expands this by allowing multiple Virutal Machines to have multiple containers to ensure that the application runs smoothly. Additionally, this participant will use Dockerhub for storing their images, while this may be seen as a security risk as Dockerhub has images be public after the first, this participant believes that this is managable as the images should contain no sensitive information and Dockerhub is a more convenient solution than alternatives such as Nexus.

* **NGINX:** A load-balancer, NGINX can be used to balance the load taken by various virutal machines. This participant will use NGINX for this purpose rather than as a Reverse Proxy, as they believe that this method is not only more useful, convenient and simple but also displays a higher understanding of the technology.

* **Visual Studio Code:** A software for writing out code, Visual Studio Code is an essential part of this project as it allows a quick and easy way to write out the code needed for this project.

* **Hardware & Peripherals:** While somewhat obvious, it should be noted that a great variety of hardware is needed in order to complete this project as well as the peripherals needed to work on it.

## App Design

In keeping with the project brief, this application has 4 services:

* **service1-display:** The service that the user interacts with, this service sends requests to the other three in order to generate a random Dungeons and Dragons character.

* **service2-race:** This service recieves an HTTP GET reqest and pulls a random race from a list.

* **service3-classes:** This service recieves an HTTP GET reqest and pulls a random class from a list.

* **service4-name:** This service recieves an HTTP POST request from service 1 and will randomly generate a name and a title based on the race and class respectivly from distincty lists.

The following Screenshots display the application in action: 

## Pipeline

The Pipeline for this project is as follows:

* **Project Tracking:** This project was tracked using Jira. User Stories were assigned based on how difficult this participant felt these individual User Stories were to complete. This Jira board can be found [here](https://ordecaos.atlassian.net/jira/software/projects/DCP/boards/5)

* **Version Control:** Git was used as the version control system for this project, with the repository being Github and can be found [here](https://github.com/Ordecaos/Week-8---DevOps-Core-Practical)

* **Development Environment:** The Deveopment Environment for this project was a Ubuntu 21.10 Virutal Machine what was hosted on GCP and was edited using Visual Studio Code for an easy, more convenient way of coding this project.

* **CI Server:** Jenkins was used as the CI server for this project. Using a webhook from Github, Jenkins will clone down the repository and execute a pipeline script within the Jenkinsfile. The Jenkins file itself first tests the application to ensure it runs correctly with full functionality, then builds the application as well as pushing the various images up to Dockerhub. Finally the deploy section deploys the application to the various Virutal Machines, including an NGINX Load Balancer, a Docker Swarm Manager and a Docker Swarm Worker. If this all works correctly then the application deploys and can be viewed through the load balancer.

## Known Issues

Due to SQLite database being used, data is not persisted between the services. In the future, this would be resolved by using a persistant database on GCP.

## Future Development

If this project were to be taken up in the future, an obvious expansion would be to input a greater variety of Dungeons and Dragons Races, Classes, Names and Titles in order to have a more fleshed out generator, additionally generating gold, statistics and starting equipment would be a wonderful addition.

## What would be done differently?

Given this participants skills and ability at this point of their career, They believe that this is the best project that they could produce in the given time for this project.