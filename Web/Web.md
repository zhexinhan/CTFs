- [Tricks](#tricks)
- [WeChall](#wechall)
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
    - [PHP 0817](#php-0817)
        - [Challenge](#challenge)
        - [Solution](#solution)
    - [PHP Register Globals](#php-register-globals)
        - [Challenge](#challenge)
        - [Solution](#solution)
- [Useful Links](#useful-links)

# Tricks
* View the source of the page.
* Check the robots.txt file.
* If Register Globals is on for the website, use parameters to pass variables.
* `netstat -rn` can give us the local IP address.

# WeChall
## Get Sourced
### Challenge
http://www.wechall.net/challenge/training/get_sourced/index.php

### Solution
View the source of the page, at the end, there is `html_sourcecode`

## Robots.txt
### Challenge
http://www.wechall.net/challenge/training/www/robots/index.php for looking at robots.txt

### Solution
Goes to http://www.wechall.net/robots.txt
```
User-agent: *
Disallow: /challenge/training/www/robots/T0PS3CR3T

User-agent: Yandex
Disallow: *
```
Next, visits http://www.wechall.net/challenge/training/www/robots/T0PS3CR3T and challenge will be solved.

## Requests
### Challenge
http://www.wechall.net/challenge/training/programming1/index.php\
Submit the message got in http://www.wechall.net/challenge/training/programming1/index.php?action=request to http://www.wechall.net/challenge/training/programming1/index.php?answer=the_message with a time limit of 1.337 seconds.

### Solution
Uses the script.
```
[root@eae8fdf9766f Web]# ./get_post_requests.py 
Response message is vo2S0kiPMx
```

## PHP LFI
### Challenge
http://www.wechall.net/challenge/training/php/lfi/up/index.php
```
$filename = 'pages/'.(isset($_GET["file"])?$_GET["file"]:"welcome").'.html';

include $filename;
```
There is a lot of important stuff in ../solution.php, so please include and execute this file for us.

### Solution
Looking at source code, we can see that it uses `Common::substrUntil($filename, "\\0");`.\
So we use `%00` to end the file string.\
Go to link `http://www.wechall.net/challenge/training/php/lfi/up/index.php?file=../../solution.php%00`

## PHP 0817
### Challenge
http://www.wechall.net/challenge/php0817/index.php
```
<?php
    if (isset($_GET['which'])) {
        $which = $_GET['which'];
        switch ($which) {
            case 0:
            case 1:
            case 2:
                require_once $which.'.php';
                break;
            default:
                echo GWF_HTML::error('PHP-0817', 'Hacker NoNoNo!', false);
                break;
        }
    }
?>
```
Your mission is to include solution.php.

### Solution
Switch/Case in PHP uses loose comparison, therefore, String like "solution" is evaluted to 0 and we will fall into case 0.\
More about PHP types comparisons: `http://php.net/manual/en/types.comparisons.php`\
Go to link `http://www.wechall.net/challenge/php0817/index.php?which=solution`

## PHP Register Globals
### Challenge
http://www.wechall.net/challenge/training/php/globals/index.php

### Solution
Look at the source code provided in the question,
```
if (isset($login)) {
    echo GWF_HTML::message('Register Globals', $chall->lang('msg_welcome_back',
                                                              array(htmlspecialchars($login[0]),
                                                                    htmlspecialchars($login[1]))));
    if (strtolower($login[0]) === 'admin') {
        $chall->onChallengeSolved(GWF_Session::getUserID());
    }
}
```
We can pass in `login` and `login[0]` as parameter to the PHP file.
Go to link `http://www.wechall.net/challenge/training/php/globals/globals.php?login=1&login[0]=admin` and will solve the problem.

# Useful Links
* [Robots Exclusion Standard](https://en.wikipedia.org/wiki/Robots_exclusion_standard)
* [File Inclusion Vulnerability](https://en.wikipedia.org/wiki/File_inclusion_vulnerability#Local_File_Inclusion)
* [Register Globals](http://php.net/manual/en/security.globals.php)