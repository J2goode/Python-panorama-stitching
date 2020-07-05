## FIND THE PICTURES TO STITCH TOGETHER IN THE FOLDER PROGRAM'S IN ##

# list of things to import
import os
import opencv

# make a list of each picture
picList = os.listdir(os.getcwd())

# find name of file, remove it from list
for i in picList:
    if os.path.basename(__file__) == i:
        picList.remove(i)

## STITCH THE PICS TOGETHER ##

# find similarities in pics

# if they dont have any, say they dont and end the program

# if they do, merge them together


## SAVE THE PICS TO THE FOLDER ##

# self explanatory
