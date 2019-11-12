# HandsOn

This project is a human-computer interface that can understand some basic commands given by the user by analyzing with hand gestures with a camera.
Image processing techniques are used to extract the hand from the background, then to try and extract useful information from it by tracking the tip of the fingers. The extracted information could be the number of the raised fingers or the coordinates of a pointing finger.


## Features

There is for features that were developed in this project:

* **extractNumbers.py**: this feature uses image processing to count the number of fingers raised by the user. Therefore, the user have 6 values (from 0 to 5) that he can send to the computer.

* **extractLetter.py**: this feature tracks a pointing finger and uses a drawn keyboard to extract the letters written by the user.

* **PhoneNumbers**: this feature tracks a pointing finger and uses a dialing menu to extract the numbers written bu the user.

* **menu**: this feature tracks a pointing finger and uses a menu to send the user to different parts of an application

