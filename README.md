# AIWolfPy

Create python agents that can play Werewolf, following the specifications of the [AIWolf Project](http://aiwolf.org)

# Information

## Tutorial

A video tutorial for the AIWolf project was recently published at IEEE Conference on Games. You can see the tutorial in the three videos below. The tutorial uses code from this repository.

* [Video 1: What is AIwolf?](https://youtu.be/MUXrUR9DmMM) (15 minutes)
* [Video 2: How to program an AIwolf agent in Python](https://youtu.be/gavJtpRH9bw) (30 minutes)
* [Video 3: Research directions in AIwolf](https://youtu.be/BZQXLKL6mVk) (25 minutes)

## Bibliography

This tutorial includes a [bibliography of research works on the werewolf game](Bibliography.md). We'll be happy to add more papers to the bibliography, so send us an issue with new references! 

# Changelog:

## Version 0.4.9a
* Added support material in English

## Version 0.4.9
* Changed differential structure (diff_data) into a DataFrame

## Version 0.4.4
* removed daily_finish
* Added update callback (with request parameter)
* Connecting is now done through a instance, not a class

## Version 0.4.0
* Support for python3
* Made file structure much simpler

# Running the agent and the server locally:
* Download the AIWolf platform from the [AIWolf public website] (http://www.aiwolf.org/server/)
	* Don't forget that the local AIWolf server requires JDK 11
* Start the server with `./StartServer.sh`
	* This runs a Java application. Select the number of players, the connection port, and press "Connect".
* In another terminal, run the client management application `./StartGUIClient.sh`
	* Another Java application is started. Select the client jar file (sampleclient.jar), the sample client pass, and the port configured for the server.
	* Press "Connect" for each instance of the sample agent you wish to connect.
* Run the python agent from this repository, with the command: `./python_sample.py -h [hostname] -p [port]`
* On the server application, press "Start Game".
  * The server application will print the log to the terminal, and also to the application window. Also, a log file will be saved on "./log".
* You can see a fun visualization using the "log viewer" program.

# Running the agent on the AIWolf competition server:
* After you create your account in the competition server, make sure your client's name is the same as your account's name.
* The python packages available at the competition server are listed in this [page](http://aiwolf.org/python_modules)
* You can expect that the usual packages + numpy, scipy, pandas, scikit-learn are available.
	* Make sure to check early with the competition runners, specially if you want to use something like an specific version of tensorflow.
	* The competition rules forbid running multiple threads. Numpy and Chainer are correctly set-up server side, but for tensorflow you must make sure that your program follows this rule. Please see the following [post](http://aiwolf.org/archives/1951)
* For more information, a tutorial from the original author of this package can be seen in this [slideshare](https://www.slideshare.net/HaradaKei/aiwolfpy-v049) (in Japanese).

# About:

This repository is an unofficial fork of the official repository of the AIWolf project, and was originally created by [Kei Harada](https://github.com/k-harada), with the objective of adding more detailed information for English speakers.

