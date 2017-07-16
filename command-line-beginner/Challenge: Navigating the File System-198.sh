## 1. Introduction ##

/home/dq$ ls -l

## 2. Moving Problematic Files to a Separate Folder ##

/home/dq$ mv /home/dq/legislators /home/dq/problematic/legislators

## 3. Fixing File Extensions ##

/home/dq/problematic$ mv legislators legislators.csv

## 4. Consolidating Files ##

/home/dq$ mv problematic/ csv_datasets/

## 5. Restricting Permissions ##

/home/dq$ cd /home/dq/csv_datasets