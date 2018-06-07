- [Tricks](#tricks)
- [WeChall](#wechall)
    - [Stegano 1](#stegano-1)
        - [Challenge](#challenge)
        - [Solution](#solution)
- [Useful Links](#useful-links)

# Tricks
* `hexdump -C`

# WeChall
## Stegano 1
### Challenge
http://www.wechall.net/challenge/training/stegano1/index.php\
Provides Stegano_1.bmp

### Solution
First, tried `file` and `identify` to get the information of this file.
```
[root@9de0ec75d005 WeChall]# file Stegano_1.bmp 
Stegano_1.bmp: PC bitmap, Windows 3.x format, 4 x 4 x 24

[root@9de0ec75d005 WeChall]# identify Stegano_1.bmp 
Stegano_1.bmp BMP 4x4 4x4+0+0 8-bit DirectClass 102B 0.000u 0:00.000
```

Then, tried to see the hex information in this file.
```
[root@9de0ec75d005 WeChall]# hexdump -C Stegano_1.bmp 
00000000  42 4d 66 00 00 00 00 00  00 00 36 00 00 00 28 00  |BMf.......6...(.|
00000010  00 00 04 00 00 00 04 00  00 00 01 00 18 00 00 00  |................|
00000020  00 00 30 00 00 00 00 00  00 00 00 00 00 00 00 00  |..0.............|
00000030  00 00 00 00 00 00 4c 6f  6f 6b 20 77 68 61 74 20  |......Look what |
00000040  74 68 65 20 68 65 78 2d  65 64 69 74 20 72 65 76  |the hex-edit rev|
00000050  65 61 6c 65 64 3a 20 70  61 73 73 77 64 3a 73 74  |ealed: passwd:st|
00000060  65 67 61 6e 6f 49                                 |eganoI|
00000066

```

# Useful Links
