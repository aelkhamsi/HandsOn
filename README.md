# HandsOn
The human-machine interface is the bridge between the human user and the machine. Our aim is to find a way to embed digital information into the real world scene, and to communicate and interact with a machine in a novel way without using traditional Peripherals. 
Through our work, we try to endow computers with a high-level understanding from digital images or  videos , and make them able to acquire informations and requests from the simple mouvement of the hand. In this direction, we will optimize workstation layout, along with providing a easy and efficient communication with machines.

This project is a human-computer interface that can understand some basic commands given by the user by analyzing with hand gestures with a camera.
Image processing techniques are used to extract the hand from the background, then to try and extract useful information from it by tracking the tip of the fingers. The extracted information could be the number of the raised fingers or the coordinates of a pointing finger.


## Features

There is the features that were developed in this project:

* **extractNumbers.py**: this feature uses image processing to count the number of fingers raised by the user. Therefore, the user have 6 values (from 0 to 5) that he can send to the computer.

![Alt Text](extractNumbres/HQ6KSmj.jpeg)
![Alt Text](extractNumbres/l3Zxxkp.jpeg)


* **extractLetter.py**: this feature tracks a pointing finger and uses a drawn keyboard to extract the letters written by the user.

![Alt Text](Keyboard/1111.jpeg)

* **PhoneNumbers**: this feature tracks a pointing finger and uses a dialing menu to extract the numbers written bu the user.

![Alt Text](PhoneNumbers/waZCNaQ.jpeg)

* **menu**: this feature tracks a pointing finger and uses a menu to send the user to different parts of an application

![Alt Text](Menu/ujPdJx6.jpeg)
