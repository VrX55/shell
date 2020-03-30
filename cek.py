#!/usr/bin/python2.7

import sys,urllib2,os
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
banner ="""
############################
#  SHELL CHECKER FASTv1.0  #
#       coded by Vrx       #
############################

"""
os.system('clear')
print(banner)

def cms(url):
 try:
 
   op =urllib2.urlopen(url,timeout=7)
   if "Upload" in op.read():
     print( "[\x1b[32mLIVE\x1b[37m]: "+url)
     open("found.txt","a").write(url)

  
 except:
    print( "[\x1b[31mDIEE\x1b[37m]: "+ url)
    pass


def main():    
   
    for i in ListPass:
        try:
            i = i.strip()
            data=cms(i)
        except:
            pass
ListPass = open(sys.argv[1],'r').readlines()      
pool = ThreadPool(250)
pool.map(cms, ListPass)
pool.close()
pool.join()
 
if __name__ == '__main__': 
 
    print("Program Finished..!")

