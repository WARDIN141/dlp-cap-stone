# dlp-cap-stone
The above files in the repository are rendition of programs of a data loss prevention module.
The module is is created using python and implementing regex patterns to identify sensitive data inside files 
To start this project I divided it into 4 renditions of the same program
which are namely:
1) regex_patterns.py
2) dlp_core.py
3) alert + killswitch.py
4) logger.py
5) cli.py

To start off the first program demonstrates the regex patterns I created in order to attain maximum accuracy in parsing through data and achieving the desired results ,for the second program as mentioned in the task, i added the functionality of parsing through a text file and rigorous proceeded with rigourous and edge case testing of my algorithm,
In my third program I added an alerting as well as an blocking mechanism for which i designed an alerting function and a killswitch which terminates the entire program as soon as any sensitive data is found in the provided file ,for the fourth program which is logger.py i was asked to add logging functionalities to the program such that we recieve proper logs with timestamps inside a seperate .txt file which is appended by the program itself and for the final rendition of the program i was asked to add an cli interface into the program

The logic for regex in these programs is kept generic as for to attain maximum accuracy i.e.
1) for the email regex no unicode emails were considered due to having different characters from different languages or as such , and the legth for domain is from 2-6characters to promote maximum inclusivity
2) for the credti card regex i took the most used credit cards in india i.e VISA , MASTERCARD , AMEX and RUPAY
3) for the pwd regex i again took the generalised format which says that there has to be minimum of 8 characters,one uppercase letter,one lowercase letter,etc
Pls note that the regex patters are subjective to change as per the environment for which the program is deployed in 

These programs are hardcoded to to file locations on the device they were concieved on for any third party testing ,make sure you make the required changes in the file path and names to avoid any runtime error

Another point to note is that these programs are bare bone shells of the aligned tasks,since they are succesful in establishing a base logic ,they are subjective to change when being upscaled for any other uses 
