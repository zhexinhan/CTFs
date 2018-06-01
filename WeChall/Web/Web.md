- [Tricks](#tricks)
- [Get Sourced](#get-sourced)
    - [Challenge](#challenge)
    - [Solution](#solution)
- [Robots.txt](#robotstxt)
    - [Challenge](#challenge)
    - [Solution](#solution)
- [Requests](#requests)
    - [Challenge](#challenge)
    - [Solution](#solution)
- [PHP LFI](#php-lfi)
    - [Challenge](#challenge)
    - [Solution](#solution)
- [Useful Links](#useful-links)

# Tricks
* View the source of the page.
* Check the robots.txt file.

# Get Sourced
## Challenge
http://www.wechall.net/challenge/training/get_sourced/index.php

## Solution
View the source of the page, at the end, there is `html_sourcecode`

# Robots.txt
## Challenge
http://www.wechall.net/challenge/training/www/robots/index.php for looking at robots.txt

## Solution
Goes to http://www.wechall.net/robots.txt
```
User-agent: *
Disallow: /challenge/training/www/robots/T0PS3CR3T

User-agent: Yandex
Disallow: *
```
Next, visits http://www.wechall.net/challenge/training/www/robots/T0PS3CR3T and challenge will be solved.

# Requests
## Challenge
Submit the message got in http://www.wechall.net/challenge/training/programming1/index.php?action=request to http://www.wechall.net/challenge/training/programming1/index.php?answer=the_message with a time limit of 1.337 seconds.

## Solution
Uses the script.
```
[root@eae8fdf9766f Web]# ./get_post_requests.py 
Response message is vo2S0kiPMx
```

# PHP LFI
## Challenge
http://www.wechall.net/challenge/training/php/lfi/up/index.php
```
$filename = 'pages/'.(isset($_GET["file"])?$_GET["file"]:"welcome").'.html';

include $filename;
```
There is a lot of important stuff in ../solution.php, so please include and execute this file for us.

## Solution
Looking at source code, we can see that it uses `Common::substrUntil($filename, "\\0");`.\
So we use `%00` to end the file string.\
Go to link `http://www.wechall.net/challenge/training/php/lfi/up/index.php?file=../../solution.php%00`

# Useful Links
* [Robots Exclusion Standard](https://en.wikipedia.org/wiki/Robots_exclusion_standard)
* [File Inclusion Vulnerability](https://en.wikipedia.org/wiki/File_inclusion_vulnerability#Local_File_Inclusion)