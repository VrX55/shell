#!/usr/bin/python2.7

import sys,urllib2,os
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
banner ="""
\x1b[32m_  _ ____ ____ ____    ____ _  _ ____ _    _    
|\/| |__| [__  [__  __ [__  |__| |___ |    |    
|  | |  | ___] ___]    ___] |  | |___ |___ |___ 
____ _  _ ____ ____ _  _ ____ ____ 
|    |__| |___ |    |_/  |___ |__/ \x1b[33mfajarid05_
\x1b[32m|___ |  | |___ |___ | \_ |___ |  \ \x1b[33mVERSION 2.0
\x1b[31m===============================================\x1b[37m
"""
os.system('clear')
print(banner)

def cms(url):
 try:
 
   op =urllib2.urlopen(url,timeout=7)
   if "Upload" in op.read():
     print( "\x1b[32mFound\x1b[37m --> : "+url)
     open("found.txt","a").write(url)

  
 except:
    print( "\x1b[31mNotFound\x1b[37m -->  "+ url)
    pass


def main():    
   
    for i in ListPass:
        try:
            i = i.strip()
            data=cms(i)
        except:
            pass
shell = raw_input('[?] List: ')
ListPass = open('%s'%shell,'r').readlines()      
pool = ThreadPool(250)
pool.map(cms, ListPass)
pool.close()
pool.join()
 
if __name__ == '__main__': 
 
    print("[*] Program Finished..!")
    print("[+] File Saved To found.txt")

