## 1. Making a File ##

/home/dq$ touch test.txt

## 2. Understanding Standard Streams ##

/home/dq$ echo "All bears should juggle"

## 3. Redirecting Standard Streams ##

/home/dq$ echo "All bears should juggle" > test.txt

## 4. Editing a File ##

/home/dq$ nano test.txt

## 5. Overview of File Permissions ##

/home/dq$ ls -l

## 6. Octal Notation for File Permissions ##

/home/dq$ stat test.txt

## 7. Modifying File Permissions ##

/home/dq$ chmod 0760 test.txt

## 8. Moving Files ##

/home/dq/test$ mv test.txt test

## 9. Copying Files ##

/home/dq/test$ cp test.txt test2.txt

## 10. Overview of File Extensions ##

/home/dq/test$ mv test.txt test_no_extension

## 11. Deleting a File ##

/home/dq/test$ rm test2.txt

## 12. Bypassing Permissions as the Root User ##

/home/dq/test$ sudo echo "Hello"