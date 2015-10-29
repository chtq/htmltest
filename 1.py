#!/usr/bin/python

import pexpect
import os

os.system('git add .')
os.system('git commit -am "%s"' %('test'))
p=pexpect.spawn('git push')
i=p.expext([pexpect.TIMEOUT, 'Username'])
if i==0:
   print 'error'
   exit(0)
if i==1:
   p.sendline('chtq')
   j=p.expect([pexpect.TIMEOUT,'Password'])
   if j==1:
      p.sendline('1qaz2wsx')
   if j==0:
      print 'error1'
