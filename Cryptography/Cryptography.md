- [Tricks](#tricks)
    - [Convertion](#convertion)
    - [Cipher](#cipher)
        - [Caesar Cipher](#caesar-cipher)
        - [Substitution Cipher](#substitution-cipher)
        - [Transposition Cipher](#transposition-cipher)
- [WeChall](#wechall)
    - [Caesar Cipher I](#caesar-cipher-i)
        - [Challenge](#challenge)
        - [Solution](#solution)
    - [Caesar Cipher II](#caesar-cipher-ii)
        - [Challenge](#challenge)
        - [Solution](#solution)
    - [Digraph Cipher](#digraph-cipher)
        - [Challenge](#challenge)
        - [Solution](#solution)
    - [Transposition Cipher I](#transposition-cipher-i)
        - [Challenge](#challenge)
        - [Solution](#solution)
    - [Substitution Cipher I](#substitution-cipher-i)
        - [Challenge](#challenge)
        - [Solution](#solution)
    - [Encoding ASCII](#encoding-ascii)
        - [Challenge](#challenge)
        - [Solution](#solution)
    - [Encoding Binary](#encoding-binary)
        - [Challenge](#challenge)
        - [Solution](#solution)
    - [Encoding URL](#encoding-url)
        - [Challenge](#challenge)
        - [Solution](#solution)
- [Useful Links](#useful-links)

# Tricks
## Convertion
```
# Convert Binary String to ASCII String
4c3275941bd7:~ hanzx$ python -c "import sys;print ''.join([chr(int(sys.argv[1][i:i+8], 2)) for i in range(0, len(sys.argv[1]), 8)])" 0111000001100101011000010110001101100101
peace

# Convert ASCII String to Hex String
4c3275941bd7:CTFs hanzx$ python -c "import sys;print(sys.argv[1].encode('hex'))" peace
7065616365

# Convert Hex String to ASCII
4c3275941bd7:CTFs hanzx$ python -c "import sys;print(int(sys.argv[1], 16))" 7065616365
482737218405
```
* Count the size of the binary string. ASCII chatacters usually use 7 or 8.
* Use the encoding_ascii.py script to convert a list of integers to ASCII characters.
* Use the encoding_url.py script to convert a list of URL code to characters.

## Cipher
### Caesar Cipher
* Use the caesar_cipher.py script to get all 26 possible combination (letters).
* Use the caesar_cipher_2.py script to get all 128 possible combination (ASCII).
### Substitution Cipher
* Use https://quipqiup.com/ to solve simple substitution cipher
### Transposition Cipher
* Try to find the pattern since characters are not changed. Only position is changed.

# WeChall
## Caesar Cipher I
In cryptography, a Caesar Cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
### Challenge
http://www.wechall.net/challenge/training/crypto/caesar/index.php\
`DRO AESMU LBYGX PYH TEWZC YFOB DRO VKJI NYQ YP MKOCKB KXN IYEB EXSAEO CYVEDSYX SC MLPMZNYWPQYL`

### Solution
Uses the script.
```
[root@8ec61c642185 Cryptography]# ./caesar_cipher.py
esp bftnv mczhy qzi ufxad zgpc esp wlkj ozr zq nlpdlc lyo jzfc fytbfp dzwfetzy td nmqnaozxqrzm
ftq cguow ndaiz raj vgybe ahqd ftq xmlk pas ar omqemd mzp kagd gzucgq eaxgfuaz ue onrobpayrsan
gur dhvpx oebja sbk whzcf bire gur ynml qbt bs pnrfne naq lbhe havdhr fbyhgvba vf pospcqbzstbo
hvs eiwqy pfckb tcl xiadg cjsf hvs zonm rcu ct qosgof obr mcif ibweis gczihwcb wg qptqdrcatucp
iwt fjxrz qgdlc udm yjbeh dktg iwt apon sdv du rpthpg pcs ndjg jcxfjt hdajixdc xh rquresdbuvdq
jxu gkysa rhemd ven zkcfi eluh jxu bqpo tew ev squiqh qdt oekh kdygku iebkjyed yi srvsftecvwer
kyv hlztb sifne wfo aldgj fmvi kyv crqp ufx fw trvjri reu pfli lezhlv jfclkzfe zj tswtgufdwxfs
lzw imauc tjgof xgp bmehk gnwj lzw dsrq vgy gx uswksj sfv qgmj mfaimw kgdmlagf ak utxuhvgexygt
max jnbvd ukhpg yhq cnfil hoxk max etsr whz hy vtxltk tgw rhnk ngbjnx lhenmbhg bl vuyviwhfyzhu
nby kocwe vliqh zir dogjm ipyl nby futs xia iz wuymul uhx siol ohckoy mifoncih cm wvzwjxigzaiv
ocz lpdxf wmjri ajs ephkn jqzm ocz gvut yjb ja xvznvm viy tjpm pidlpz njgpodji dn xwaxkyjhabjw
pda mqeyg xnksj bkt fqilo kran pda hwvu zkc kb ywaown wjz ukqn qjemqa okhqpekj eo yxbylzkibckx
qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald lc zxbpxo xka vlro rkfnrb plirqflk fp zyczmaljcdly
rfc osgai zpmul dmv hsknq mtcp rfc jyxw bme md aycqyp ylb wmsp slgosc qmjsrgml gq azdanbmkdemz
sgd pthbj aqnvm enw itlor nudq sgd kzyx cnf ne bzdrzq zmc xntq tmhptd rnktshnm hr baebocnlefna

the quick brown fox jumps over the lazy dog of caesar and your unique solution is cbfcpdomfgob

uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph pg dbftbs boe zpvs vojrvf tpmvujpo jt dcgdqepnghpc
vjg swkem dtqyp hqz lworu qxgt vjg ncba fqi qh ecguct cpf aqwt wpkswg uqnwvkqp ku edherfqohiqd
wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj ri fdhvdu dqg brxu xqltxh vroxwlrq lv feifsgrpijre
xli uymgo fvsar jsb nyqtw sziv xli pedc hsk sj geiwev erh csyv yrmuyi wspyxmsr mw gfjgthsqjksf
ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl tk hfjxfw fsi dtzw zsnvzj xtqzynts nx hgkhuitrkltg
znk waoiq hxuct lud pasvy ubkx znk rgfe jum ul igkygx gtj euax atowak yurazout oy ihlivjuslmuh
aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn vm jhlzhy huk fvby bupxbl zvsbapvu pz jimjwkvtmnvi
bpm ycqks jzwev nwf rcuxa wdmz bpm tihg lwo wn kimaiz ivl gwcz cvqycm awtcbqwv qa kjnkxlwunowj
cqn zdrlt kaxfw oxg sdvyb xena cqn ujih mxp xo ljnbja jwm hxda dwrzdn bxudcrxw rb lkolymxvopxk
dro aesmu lbygx pyh tewzc yfob dro vkji nyq yp mkockb kxn iyeb exsaeo cyvedsyx sc mlpmznywpqyl
```

## Caesar Cipher II
### Challenge
http://www.wechall.net/challenge/training/crypto/caesar2/index.php\
```
34 5C 5C 51 20 57 5C 4F 19 20 66 5C 62 20 60 5C
59 63 52 51 20 5C 5B 52 20 5A 5C 5F 52 20 50 55
4E 59 59 52 5B 54 52 20 56 5B 20 66 5C 62 5F 20
57 5C 62 5F 5B 52 66 1B 20 41 55 56 60 20 5C 5B
52 20 64 4E 60 20 53 4E 56 5F 59 66 20 52 4E 60
66 20 61 5C 20 50 5F 4E 50 58 1B 20 44 4E 60 5B
14 61 20 56 61 2C 20 1E 1F 25 20 58 52 66 60 20
56 60 20 4E 20 5E 62 56 61 52 20 60 5A 4E 59 59
20 58 52 66 60 5D 4E 50 52 19 20 60 5C 20 56 61
20 60 55 5C 62 59 51 5B 14 61 20 55 4E 63 52 20
61 4E 58 52 5B 20 66 5C 62 20 61 5C 5C 20 59 5C
5B 54 20 61 5C 20 51 52 50 5F 66 5D 61 20 61 55
56 60 20 5A 52 60 60 4E 54 52 1B 20 44 52 59 59
20 51 5C 5B 52 19 20 66 5C 62 5F 20 60 5C 59 62
61 56 5C 5B 20 56 60 20 4F 52 53 52 56 56 54 50
4F 5B 5F 4E 1B
```

### Solution
First, convert those Hex into corresponding character via `chr(int("34", 16))`.\
Then, do the 128 possible shifts on them, so result that has non-printable charactor, just ignore them.
```
[root@5afe7ad7c386 Cryptography]# ./caesar_cipher_2.py 
@hh]5ch[%5rhn5lheo^]5hg^5fhk^5\aZee^g`^5bg5rhnk5chnkg^r'5Mabl5hg^5pZl5_Zbker5^Zlr5mh5\kZ\d'5PZlg m5bm85*+15d^rl5bl5Z5jnbm^5lfZee5d^rliZ\^%5lh5bm5lahne]g m5aZo^5mZd^g5rhn5mhh5ehg`5mh5]^\krim5mabl5f^llZ`^'5P^ee5]hg^%5rhnk5lhenmbhg5bl5[^_^bb`\[gkZ'
Aii^6di\&6sio6mifp_^6ih_6gil_6]b[ff_ha_6ch6siol6diolh_s(6Nbcm6ih_6q[m6`[clfs6_[ms6ni6]l[]e(6Q[mh!n6cn96+,26e_sm6cm6[6kocn_6mg[ff6e_smj[]_&6mi6cn6mbiof^h!n6b[p_6n[e_h6sio6nii6fiha6ni6^_]lsjn6nbcm6g_mm[a_(6Q_ff6^ih_&6siol6mifoncih6cm6\_`_cca]\hl[(
Bjj_7ej]'7tjp7njgq`_7ji`7hjm`7^c\gg`ib`7di7tjpm7ejpmi`t)7Ocdn7ji`7r\n7a\dmgt7`\nt7oj7^m\^f)7R\ni"o7do:7,-37f`tn7dn7\7lpdo`7nh\gg7f`tnk\^`'7nj7do7ncjpg_i"o7c\q`7o\f`i7tjp7ojj7gjib7oj7_`^mtko7ocdn7h`nn\b`)7R`gg7_ji`'7tjpm7njgpodji7dn7]`a`ddb^]im\)
Ckk`8fk^(8ukq8okhra`8kja8ikna8_d]hhajca8ej8ukqn8fkqnjau*8Pdeo8kja8s]o8b]enhu8a]ou8pk8_n]_g*8S]oj#p8ep;8-.48gauo8eo8]8mqepa8oi]hh8gauol]_a(8ok8ep8odkqh`j#p8d]ra8p]gaj8ukq8pkk8hkjc8pk8`a_nulp8pdeo8iaoo]ca*8Sahh8`kja(8ukqn8okhqpekj8eo8^abaeec_^jn]*
Dlla9gl_)9vlr9plisba9lkb9jlob9`e^iibkdb9fk9vlro9glrokbv+9Qefp9lkb9t^p9c^foiv9b^pv9ql9`o^`h+9T^pk$q9fq<9./59hbvp9fp9^9nrfqb9pj^ii9hbvpm^`b)9pl9fq9pelriak$q9e^sb9q^hbk9vlr9qll9ilkd9ql9ab`ovmq9qefp9jbpp^db+9Tbii9alkb)9vlro9plirqflk9fp9_bcbffd`_ko^+
Emmb:hm`*:wms:qmjtcb:mlc:kmpc:af_jjclec:gl:wmsp:hmsplcw,:Rfgq:mlc:u_q:d_gpjw:c_qw:rm:ap_ai,:U_ql%r:gr=:/06:icwq:gq:_:osgrc:qk_jj:icwqn_ac*:qm:gr:qfmsjbl%r:f_tc:r_icl:wms:rmm:jmle:rm:bcapwnr:rfgq:kcqq_ec,:Ucjj:bmlc*:wmsp:qmjsrgml:gq:`cdcggea`lp_,
Fnnc;ina+;xnt;rnkudc;nmd;lnqd;bg`kkdmfd;hm;xntq;intqmdx-;Sghr;nmd;v`r;e`hqkx;d`rx;sn;bq`bj-;V`rm&s;hs>;017;jdxr;hr;`;pthsd;rl`kk;jdxro`bd+;rn;hs;rgntkcm&s;g`ud;s`jdm;xnt;snn;knmf;sn;cdbqxos;sghr;ldrr`fd-;Vdkk;cnmd+;xntq;rnktshnm;hr;adedhhfbamq`-

Good<job,<you<solved<one<more<challenge<in<your<journey.<This<one<was<fairly<easy<to<crack.<Wasn't<it?<128<keys<is<a<quite<small<keyspace,<so<it<shouldn't<have<taken<you<too<long<to<decrypt<this<message.<Well<done,<your<solution<is<befeiigcbnra.

Hppe=kpc-=zpv=tpmwfe=pof=npsf=dibmmfohf=jo=zpvs=kpvsofz/=Uijt=pof=xbt=gbjsmz=fbtz=up=dsbdl/=Xbto(u=ju@=239=lfzt=jt=b=rvjuf=tnbmm=lfztqbdf-=tp=ju=tipvmeo(u=ibwf=ublfo=zpv=upp=mpoh=up=efdszqu=uijt=nfttbhf/=Xfmm=epof-=zpvs=tpmvujpo=jt=cfgfjjhdcosb/
Iqqf>lqd.>{qw>uqnxgf>qpg>oqtg>ejcnngpig>kp>{qwt>lqwtpg{0>Vjku>qpg>ycu>hcktn{>gcu{>vq>etcem0>Ycup)v>kvA>34:>mg{u>ku>c>swkvg>uocnn>mg{urceg.>uq>kv>ujqwnfp)v>jcxg>vcmgp>{qw>vqq>nqpi>vq>fget{rv>vjku>oguucig0>Ygnn>fqpg.>{qwt>uqnwvkqp>ku>dghgkkiedptc0
Jrrg?mre/?|rx?vroyhg?rqh?pruh?fkdoohqjh?lq?|rxu?mrxuqh|1?Wklv?rqh?zdv?idluo|?hdv|?wr?fudfn1?Zdvq*w?lwB?45;?nh|v?lv?d?txlwh?vpdoo?nh|vsdfh/?vr?lw?vkrxogq*w?kdyh?wdnhq?|rx?wrr?orqj?wr?ghfu|sw?wklv?phvvdjh1?Zhoo?grqh/?|rxu?vroxwlrq?lv?ehihlljfequd1
Kssh@nsf0@}sy@wspzih@sri@qsvi@gleppirki@mr@}syv@nsyvri}2@Xlmw@sri@{ew@jemvp}@iew}@xs@gvego2@[ewr+x@mxC@56<@oi}w@mw@e@uymxi@wqepp@oi}wtegi0@ws@mx@wlsyphr+x@lezi@xeoir@}sy@xss@psrk@xs@higv}tx@xlmw@qiwweki2@[ipp@hsri0@}syv@wspyxmsr@mw@fijimmkgfrve2
LttiAotg1A~tzAxtq{jiAtsjArtwjAhmfqqjsljAnsA~tzwAotzwsj~3AYmnxAtsjA|fxAkfnwq~Ajfx~AytAhwfhp3A\fxs,yAnyDA67=Apj~xAnxAfAvznyjAxrfqqApj~xufhj1AxtAnyAxmtzqis,yAmf{jAyfpjsA~tzAyttAqtslAytAijhw~uyAymnxArjxxflj3A\jqqAitsj1A~tzwAxtqzyntsAnxAgjkjnnlhgswf3
```

## Digraph Cipher
### Challenge
http://www.wechall.net/challenge/training/crypto/digraph/index.php\
`qtigazcektdrxfaynfdrxfkgigazjaid thigay hpctofktzxznxfcthp xfebkgja bfctjajadrcect jaayofofctjajajwaynfnfzxid eadrja azigxf xfigig hpkgjwjwkgofaynfxf ctkgxfebctktao ewdrja kgxfzt eactnfnfao ceigighp pwigkiid ljazxfctkt xfebkgja rmctzxewigkthp drja jaignfayxfkgigazbd ofkgnfnfofigigebigjahpigid`

### Solution
There must be "solution:" at the end and length should be 18. "jaignfayxfkgigazbd" is just 18.\
Then slowly find the map and we will get the result.
```
[root@5afe7ad7c386 Cryptography]# ./digraph_cipher.py 
Congratulations. You decrypted this message successfully. Was not too difficult either, was it? Well, good job. Enter this keyword as solution: cillcoohosdo.
```

## Transposition Cipher I
In cryptography, a transposition cipher is a method of encryption by which the positions held by units of plaintext (which are commonly characters or groups of characters) are shifted according to a regular system, so that the ciphertext constitutes a permutation of the plaintext.
### Challenge
http://www.wechall.net/challenge/training/crypto/transposition1/index.php\
`oWdnreuf.lY uoc nar ae dht eemssga eaw yebttrew eh nht eelttre sra enic roertco drre . Ihtni koy uowlu dilekt  oes eoyrup sawsro don:wm hscaparfca.d`

### Solution
Looking at the first part, it looks like "wonderful". Then read more about that and find out that every 2 characters are swapped.
```
message = "oWdnreuf.lY uoc nar ae dht eemssga eaw yebttrew eh nht eelttre sra enic roertco drre . Ihtni koy uowlu dilekt  oes eoyrup sawsro don:wm hscaparfca.d"
print(''.join([pair[1] + pair[0] for pair in zip(message[::2], message[1::2])]))

'Wonderful. You can read the message way better when the letters are in correct order. I think you would like to see your password now: mshacapfracd.'
```

## Substitution Cipher I
In cryptography, a substitution cipher is a method of encrypting by which units of plaintext are replaced with ciphertext, according to a fixed system; the "units" may be single letters (the most common), pairs of letters, triplets of letters, mixtures of the above, and so forth.
### Challenge
http://www.wechall.net/challenge/training/crypto/simplesub1/index.php\
`ZH WGM IPUVEGWH EYN HYC FID SMIN WGVK UH RSVMDN V IU VUJSMKKMN TMSH OMPP NYDM HYCS KYPCWVYD LMH VK PSUPEZDZVPGI WGVK PVWWPM FGIPPMDEM OIK DYW WYY GISN OIK VW`

### Solution
Put into https://quipqiup.com/ gives the result\
`BY THE ALMIGHTY GOD YOU CAN READ THIS MY FRIEND I AM IMPRESSED VERY WELL DONE YOUR SOLUTION KEY IS LRMLGBNBILHA THIS LITTLE CHALLENGE WAS NOT TOO HARD WAS IT`

## Encoding ASCII
### Challenge
http://www.wechall.net/challenge/training/encodings/ascii/index.php\
84, 104, 101, 32, 115, 111, 108, 117, 116, 105, 111, 110, 32, 105, 115, 58, 32, 103, 109, 98, 114, 108, 98, 98, 101, 110, 97, 99, 97

### Solution
Uses the script.
```
[root@8ec61c642185 Cryptography]# ./encoding_ascii.py
The solution is: gmbrlbbenaca
```

## Encoding Binary
### Challenge
http://www.wechall.net/challenge/training/encodings1/index.php\
```
10101001101000110100111100110100
00011101001100101111100011101000
10000011010011110011010000001101
11010110111000101101001111010001
00000110010111011101100011110111
11100100110010111001000100000110
00011110011110001111010011101001
01011100100000101100111011111110
10111100100100000111000011000011
11001111100111110111110111111100
10110010001000001101001111001101
00000110010111000011110011111100
11110011111010011000011110010111
0100110010111100100101110
```

### Solution
Looking at the binary, the length is 441 which is a multiple of 7. And ASCII numbers and letters usually use 7 bits. Therefore, use the script.
```
[root@eae8fdf9766f Cryptography]# ./encoding_binary.py
This text is 7-bit encoded ascii. Your password is easystarter.
```

## Encoding URL
### Challenge
http://www.wechall.net/challenge/training/encodings/url/index.php\
%59%69%70%70%65%68%21%20%59%6F%75%72%20%55%52%4C%20%69%73%20%63%68%61%6C%6C%65%6E%67%65%2F%74%72%61%69%6E%69%6E%67%2F%65%6E%63%6F%64%69%6E%67%73%2F%75%72%6C%2F%73%61%77%5F%6C%6F%74%69%6F%6E%2E%70%68%70%3F%70%3D%64%61%67%6D%6D%6D%6D%6E%66%72%61%69%26%63%69%64%3D%35%32%23%70%61%73%73%77%6F%72%64%3D%66%69%62%72%65%5F%6F%70%74%69%63%73%20%56%65%72%79%20%77%65%6C%6C%20%64%6F%6E%65%21

### Solution
Uses the script.
```
[root@8ec61c642185 Encoding]# ./encoding_url.py
Yippeh! Your URL is challenge/training/encodings/url/saw_lotion.php?p=dagmmmmnfrai&cid=52#password=fibre_optics Very well done!
```
Then go to http://www.wechall.net/challenge/training/encodings/url/saw_lotion.php?p=dagmmmmnfrai&cid=52#password=fibre_optics

# Useful Links
* [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
* [Transposition Cipher](https://en.wikipedia.org/wiki/Transposition_cipher)
* [Substitution Cipher](https://en.wikipedia.org/wiki/Substitution_cipher)