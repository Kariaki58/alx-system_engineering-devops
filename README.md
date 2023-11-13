### Solving All Alx Task Here
**Hi ASK me about linux | c | python**
### Shell Basics

Learning about shell

- ls 
- cd
- pwd
- and others

Example

In order to test your scripts, you will need to use this command: chmod u+x file.
We will see later what does chmod mean and do, but you can have a look at man chmod if you are curious.

Example

```
julien@ubuntu:/tmp$ ls

12-file_type
lll

julien@ubuntu:/tmp$ ls -la lll
-rw-rw-r-- 1 julien julien 15 Sep 19 21:05 lll

julien@ubuntu:/tmp$ cat lll
#!/bin/bash
ls

julien@ubuntu:/tmp$ ls -l lll
-rw-rw-r-- 1 julien julien 15 Sep 19 21:05 lll

julien@ubuntu:/tmp$ chmod u+x lll # you do not have to understand this yet

julien@ubuntu:/tmp$ ls -l lll
-rwxrw-r-- 1 julien julien 15 Sep 19 21:05 lll

julien@ubuntu:/tmp$ ./lll
12-file_type
lll

julien@ubuntu:/tmp$

```

### Shell, permissions

** Learn about shell Permissions **

Resources

[Permissions](https://intranet.alxswe.com/rltoken/aQmRB6ms-SDHUhqY0Rsa3g)

you can study them by using...

### Man Or Help

- chmod
- sudo
- su
- chown
- chgrp
- id
- groups
- whoami
- adduser
- useradd
- addgroup

### Shell, I/O Redirections and filters

**Resources**

Read or Watch:
[Shell, I/O Redirection](https://intranet.alxswe.com/rltoken/fGOQQXRKbvOcd1qLRxHzLQ)
[Special Characters](https://intranet.alxswe.com/rltoken/c1pz13vke3HPH0S8iALbtw)

**man or help:**

- echo
- cat
- head
- tail
- find
- wc
- sort
- uniq
- grep
- tr
- rev
- cut
- passwd (5) (i.e man 5 passwd)

**More Info**

Read your /etc/passwd and /etc/shadow files.

Note: You do not have to learn about fmt, pr, du, gzip, tar, lpr, sed and awk yet.
