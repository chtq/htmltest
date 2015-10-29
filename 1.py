#!/usr/bin/python

import pexpect
import os

os.chdir('/home/ctqi/html/_book')
os.system('git add .')
os.system('git commit -am "%s"' %('test1'))
p=pexpect.spawn('git push')
print 'hhhhhh'
i=p.expect([pexpect.TIMEOUT, 'Username.*'])
if i==0:
   print 'error'
   exit(0)
if i==1:
   print '1111'
   p.sendline('chtq')
   j=p.expect([pexpect.TIMEOUT,'Password.*:'])
   if j==1:
      p.sendline('1qaz2wsx')
   else:
      print j
else:
   print 'error2'
