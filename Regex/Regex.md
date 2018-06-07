- [Tricks](#tricks)
- [WeChall](#wechall)
    - [Regex I](#regex-i)
        - [Challenge](#challenge)
        - [Solution](#solution)
- [Useful Links](#useful-links)

# Tricks

# WeChall
## Regex I
### Challenge
http://www.wechall.net/challenge/training/regex/index.php\
1. Regex to match only empty string
2. Regex to match "wechall" without quotes.
3. Your pattern shall match all images with the name wechall.ext or wechall4.ext and a valid image extension.\
Valid image extensions are .jpg, .gif, .tiff, .bmp and .png.\
Here are some examples for valid filenames: wechall4.tiff, wechall.png, wechall4.jpg, wechall.bmp
4. It is nice that we have valid images now, but could you please capture the filename, without extension, too?\
As an example: wechall4.jpg should capture/return wechall4 in your pattern now.

### Solution
1. Since we want empty String, we will just start and end: `/^$/`
2. Only match specific String: `/^wechall$/`
3. We start with `wechall`, then there is 0 or 1 `4`, so we have `4?`. `\.` will be . and we will have choices of `(jpg|gif|tiff|bmp|png)`. `?:` is non-capturing group, which tells program to not treat that as a group of match. Therefore, the solution is: `/^wechall4?\.(?:jpg|gif|tiff|bmp|png)$/`
4. Same as above, but we need to add a capturing group for filename without extension. Solution: `/^(wechall4?)\.(?:jpg|gif|tiff|bmp|png)$/`

# Useful Links