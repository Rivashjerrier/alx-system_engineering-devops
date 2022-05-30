Basic shell scripts re I/O redirections and filters.

0- prints "Hello, World”, followed by a new line to the standard output

1- prints confused smiley "(Ôo)'

2- prints content of the /etc/passwd file

3- prints the content of /etc/passwd and /etc/host

4- prints last 10 lines of /etc/passwd

5- prints first 10 lines of /etc/passwd

6- Write a script that displays the third line of the file iacta. The file iacta will be in the working directory

You’re not allowed to use sed
7- Write a shell script that creates a file named exactly *\'"Best School"'\*$?*****:) containing the text Best School ending by a new line.

8- Write a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.

9- duplicates the last line of the file iacta

The file iacta will be in the working directory
10- deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders

11- counts the number of directories and sub-directories in the current directory

The current and parent directories should not be taken into account
Hidden directories should be counted
12- displays the 10 newest files in the current directory Requirements: * One file per line * Sorted from the newest to the oldest

13- takes a list of words as input and prints only words that appear exactly once

Input format: One line, one word
Output format: One line, one word
Words should be sorted
14- prints lines containing the pattern “root” from the file /etc/passwd

15- prints number of lines that contain the pattern “bin” in the file /etc/passwd

16- prints lines containing the pattern “root” and 3 lines after them in the file /etc/passwd

17- prints all lines in the file /etc/passwd that do not contain the pattern “bin”

18- prints all lines of the file /etc/ssh/sshd_config starting with a letter

19- replaces all characters A and c from input to Z and e respectively

20- removes all letters c and C from input

21- reverses its input

22- prints all users and their home directories from /etc/passwd, sorted by users

Based on the the /etc/passwd file
100- finds all empty files and directories in the current directory and all sub-directories

Only the names of the files and directories should be displayed (not the entire path)
Hidden files should be listed
One file name per line
The listing should end with a new line
You are not allowed to use basename, grep, egrep, fgrep or rgrep
101- lists all the files with a .gif extension in the current directory and all its sub-directories

Hidden files should be listed
Only regular files (not directories) should be listed
The names of the files should be displayed without their extensions
The files should be sorted by byte values, but case-insensitive (file aaa should be listed before file bbb, file .b should be listed before file a, and file Rona should be listed after file jay)
One file name per line
The listing should end with a new line
You are not allowed to use basename, grep, egrep, fgrep or rgrep
102- Create a script that decodes acrostics that use the first letter of each line.

The ‘decoded’ message has to end with a new line
You are not allowed to use grep, egrep, fgrep or rgrep
103- parses web servers logs from NASA website (1995) in TSV format as input and displays the 11 hosts or IP addresses which did the most requests

Order by number of requests, most active host or IP at the top
You are not allowed to use grep, egrep, fgrep or rgrep
