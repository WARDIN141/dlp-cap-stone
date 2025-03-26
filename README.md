# dlp-cap-stone
The above files in the repository are rendition of programs of a data loss prevention module.
The module is is created using python and implementing regex patterns to identify sensitive data inside files 
To start this project I divided it into 4 renditions of the same program
which are namely:
1) regex_patterns.py
2) alert + killswitch.py
3) logger.py
4) cli.py

To start off the first program demonstrates the regex patterns I created in order to attain maximum accuracy in parsing through data and achieving the desired results ,for the second program as mentioned in the task, i was given to add an alerting as well as an blocking mechanism for which i designed an alerting function and a killswitch which terminates the entire program as soon as any sensitive data is found in the provided file ,for the third program which is logger.py i was asked to add logging functionalities to the program such that we recieve proper logs with timestamps inside a seperate .txt file which is appended by the program itself and for the final rendition of the program i was asked to add an cli interface into the program

These programs are hardcoded to to file locations on the device they were concieved on for any third party testing ,make sure you make the required changes in the file path and names to avoid any runtime error

Another point to note is that these programs are bare bone shells of the aligned tasks,since they are succesful in establishing a base logic ,they are subject to change when being upscaled for any other uses 
