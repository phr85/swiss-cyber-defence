# Volatility


**How to install**

By default Volatility isn't installed on Kali Linux.

* [Install via Docker](https://hub.docker.com/r/phocean/volatility)
* π [volatility-guru.py](assets/volatility-guru.py)

## Volatility Procedure 

### 1. Identify rogue processes


Identify Operation System:β¨π¨βπ» vol.py -f target.img imageinfo

β‘οΈ Now replace profile we found with  βMY_TARGET_PROFILEβ

-------------------------

Print all running processes within the EPROCESS doubly linked list:β¨π¨βπ» vol.py -f target.img --profile=MY_TARGET_PROFILE  pslist

-------------------------

Print all running processes within the EPROCESS doubly linked list:β¨π¨βπ» vol.py -f  target.img --profile=MY_TARGET_PROFILE pslist

-------------------------

Scan physical memory for EPROCESS pool allocations:
π¨βπ»vol.py -f target.img --profile=MY_TARGET_PROFILE psscan

-------------------------

Print process list as a tree showing parent relationship (using EPROCESS linked list):
π¨βπ»vol.py -f target.img --profile=MY_TARGET_PROFILE pstree

-------------------------

Automatically identify suspicious system processes:
π¨βπ»vol.py -f target.img --profile=MY_TARGET_PROFILE malprocfind

-------------------------

Compare processes and loaded DLLs with a basline image
π¨βπ»vol.py -f target.img --profile=MY_TARGET_PROFILE processbl

-------------------------



### 2. Analyze process DLLs and handles


### 3. Review network artifacts


### 4. Look for evidence of code injection



### 5. Check for signs of a rootkit




### 6. Dump suspicious processes and drivers
