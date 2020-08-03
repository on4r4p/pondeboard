import os
import sys
import time
import datetime
print ""

User = "pondeboard" ## you can try on pondeboard1 too 
nbrloop = 16 ##Max number 16 cause Twitter's api can only get the last 3200 tweets
nbrtweet = 200 ## Max 200 (16 x 200 = 3200)

totaltwt = nbrloop * nbrtweet

##Preset##
all = 0 ##if 1 show all test
simple = 0 ##if show bin to uni + magic numbers
simple2 = 0 ## if show bin to uni in Twitter-Order + magic numbers
bothsimple = 0 ##if show bin to uni + magic numbers both in normal and Twitter-Order
#########

log = 1 ## log file
showtime = 1 ## timestamp
showtweetcounter = 1 ##if 1 show tweets counter
showpressenter = 0 ## if 1 ask if you want to continue before each test
showbintweet = 1 ##if 1 write original tweets
showlis = 1 ##if 1 write list of tweetId to files
showbinary = 1 ## if 1 show all binary tweets
showbinary2 = 1 ## if 1 show all binary tweets in reverse order
showhexa = 1 ## if 1 show all hexa
showhexa2 = 1 ## if 1 show all hexa in reversed order
showuni = 1 ## if 1 show all unicode
showuni2 = 1 ## if 1 show all uicode in reversed order
showhexatest = 1 ## if 1 show some testing (Add fff first)
showhexatest2 = 1 ## if 1 show some testing(Add fff in reversed list)
showbintest = 0 ## if 1 show some testing (Add 111 first )
showbintest2 = 0 ## if 1 show some testing (Add 111 in reversed list)
showchardet = 1 ## if 1 ask chardet to guess current encoding
showftfy = 1 ## if 1 ask Ftfy to guess current encoding
showencoding = 1 ## if 1 show results through all encoding
showencoding2 = 1 ## if 1 show reversed results through all encoding
showonlycp = 0 ## if 1 show both reversed and normal results through all cp~ encodings only
showmagicnumber = 1 ## if 1 Try to find a matching magic number anywhere in all unicode file created
showreplace = 1 ## if 1 replace encoded char to another char in another encoding
showreplace2 = 1 ## if 1 replace encoded char to another char in another encoding(Twitter-Order)
showhdcp = 1 ## if 1 check if it is the hdcp master key
showmd5only = 0 ## if 1 try to find md5 only
showhash = 0 ## if 1 Try to find hashes in all hexa Result
showhashtweet = 0 ## if 1 Try to find hash for each tweets
showhashtweet2 = 0 ## if 1 Try to find hash for each tweets Twitter-Order
showrainbow = 0 ## if 1 Try to find occurence in my rainbow table
showmatrix = 1 ## if 1 show how bored i am at this time
showdebug = 1 ## lenght test


## some var


show = "" 
one = 1
zero = 0
MD4 = "md4"
MD5 = "md5"
SHA1 = "sha1"
SHA224 = "sha224"
SHA256 = "sha256"
SHA384 = "sha384"
SHA512 = "sha512"
RIPEMD = "rmd160"
LM = "lm"
NTLM = "ntlm"
MYSQL = "mysql"
CISCO7 = "cisco7"
JUNIPER = "juniper"
GOST = "gost"
WHIRLPOOL = "whirlpool"
LDAP_MD5 = "ldap_md5"
LDAP_SHA1 = "ldap_sha1"
listalgo = ("md4","md5","sha1","sha224","sha384","sha512","rmd160","lm","ntlm","mysql","cisco7","juniper","gost","whirlpool","ldap_md5","ldap_sha1")
USER_AGENTS = [
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Crazy Browser 1.0.5)",
	"curl/7.7.2 (powerpc-apple-darwin6.0) libcurl 7.7.2 (OpenSSL 0.9.6b)",
	"Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
	"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b8pre) Gecko/20101213 Firefox/4.0b8pre",
	"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0) chromeframe/10.0.648.205",
	"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)",
	"Opera/9.80 (Windows NT 6.1; U; sv) Presto/2.7.62 Version/11.01",
	"Opera/9.80 (Windows NT 6.1; U; pl) Presto/2.7.62 Version/11.00",
	"Opera/9.80 (X11; Linux i686; U; pl) Presto/2.6.30 Version/10.61",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.861.0 Safari/535.2",
	"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.872.0 Safari/535.2",
	"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.812.0 Safari/535.1",
	"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
	]
day = datetime.date.today()
date = datetime.datetime.now()
dated = str(date.hour) + "-" + str(date.minute)
Path = "./tmp/" + User + "/" + str(day) + "/"
PathLogs = Path + "Logs/"
PathData = Path + "data/"
PathDataTime = PathData + dated +"/"

## some if


if all == 1:
	showdebug=showhdcp=showreplace2=showreplace=showmagicnumber=showrainbow=showonlycp=showencoding2=showencoding=showftfy=showchardet=showhash=showbintest2=showbintest=showhexatest2=showhexatest=showuni2=showmatrix=showhash=showuni=showhexa2=showhexa=showbinary2=showbinary=showlis=showbintweet=showtweetcounter=showtime=log=one

if simple == 1:
	showdebug=showhdcp=showreplace2=showreplace=showrainbow=showhashtweet=showmagicnumber=showhash=showmd5only=showonlycp=showencoding2=showencoding=showftfy=showchardet=showbintest2=showbintest=showhexatest2=showhexatest=showuni2=showuni=showhexa2=showhexa=showbinary2=showbinary=showlis=showbintweet=showpressenter=showtweetcounter=showtime=log=zero
	showuni=showhexa=showbinary=showmagicnumber=showpressenter=showtweetcounter=showtime=log=one

if simple2 == 1:
	showdebug=showhdcp=showreplace2=showreplace=showrainbow=showmagicnumber=showhashtweet=showhash=showmd5only=showonlycp=showhash=showencoding2=showencoding=showftfy=showchardet=showbintest2=showbintest=showhexatest2=showhexatest=showuni2=showuni=showhexa2=showhexa=showbinary2=showbinary=showlis=showbintweet=showpressenter=showtweetcounter=showtime=log=zero
        showuni2=showhexa2=showbinary2=showmagicnumber=showpressenter=showtweetcounter=showtime=log=one

if bothsimple == 1:
	showdebug=showhdcp=showreplace2=showreplace=showrainbow=showmagicnumber=showhashtweet=showhash=showmd5only=showonlycp=showhash=showencoding2=showencoding=showftfy=showchardet=showbintest2=showbintest=showhexatest2=showhexatest=showuni2=showuni=showhexa2=showhexa=showbinary2=showbinary=showlis=showbintweet=showpressenter=showtweetcounter=showtime=log=zero
	showuni=showhexa=showbinary=showuni2=showhexa2=showbinary2=showmagicnumber=showpressenter=showtweetcounter=showtime=log=one


if showonlycp == 1:
	showftfy =1

if showmd5only == 1:
	showhash = 1

if showhashtweet == 1 :

	showhexa = 1
	showhash = 1

if showhashtweet2 == 1 :

	showhexa2 = 1
	showhash = 1

if showrainbow == 1 :
	if showhexa == 0 and showuni == 0 and showhexa2 == 0 and showuni2 == 0: 
        	showhexa = 1
		showhexa2 = 1


if showencoding == 1:
        showuni = 1


if showencoding2 == 1:
        showuni2 = 1


############Adding suffix to stout logfile##################
#####################And creating folder####################
skip = 0

if showtime == 1:

        print "Timestamp",showtime

        show += "-Time"
else:
	skip = skip + 1
if showtweetcounter == 1:

        print "Tweet counter :",showtweetcounter

        show += "-Cnt"
else:
	skip = skip + 1

if showpressenter == 1:
	
        print "Will ask if continue : ",showpressenter

        show += "-Enter"
else:
        skip = skip + 1

if showbintweet == 1:
	
        print "write all bin tweets to files :",showbintweet

        show += "-Original"
        pathoriginal = PathDataTime + "Original/"

        if not os.path.exists(pathoriginal):
                os.makedirs(pathoriginal)
else:
        skip = skip + 1

if showlis == 1:
	
        print "write tweet id as a list :",showlis

        show += "-Lis"

        pathlis = PathDataTime + "Id/"

        if not os.path.exists(pathlis):
                os.makedirs(pathlis)
else:
        skip = skip + 1


if showbinary == 1:
	
        print "Show Binary :",showbinary

        show += "-Bn"

        pathbin = PathDataTime + "Bin/"

        if not os.path.exists(pathbin):
                os.makedirs(pathbin)
else:
        skip = skip + 1


if showbinary2 == 1:
	
        print "Show Binary (Twitter-Order) :",showbinary2

        show += "-B2"

        pathbin2 = PathDataTime + "Bin/Twitter-Order/"

        if not os.path.exists(pathbin2):
                os.makedirs(pathbin2)
else:
        skip = skip + 1
if showhexa == 1:
	
        print "Show Hexadecimal :",showhexa

        show += "-Hx"

        pathhexa = PathDataTime + "Hexa/"

        if not os.path.exists(pathhexa):
                os.makedirs(pathhexa)
else:
        skip = skip + 1

if showhexa2 == 1:
	
        print "Show Hexadecimal (Twitter-Order) :",showhexa2

        show += "-Hx2"

        pathhexa2 = PathDataTime + "Hexa/Twitter-Order/"

        if not os.path.exists(pathhexa2):
                os.makedirs(pathhexa2)
else:
        skip = skip + 1

if showuni == 1:
        print "Show unicode :",showuni

        show += "-Uni"

        pathuni = PathDataTime + "Unicode/"

        if not os.path.exists(pathuni):
                os.makedirs(pathuni)
else:
        skip = skip + 1
if showuni2 == 1:
	
        print "Show unicode (Twitter-Order) :",showuni2

        show += "-Uni2"

        pathuni2 = PathDataTime + "Unicode/Twitter-Order/"

        if not os.path.exists(pathuni2):
                os.makedirs(pathuni2)
else:
        skip = skip + 1
if showbintest != 0:
	
        print "Show Binary test :",showbintest

        show += "-BnTest"

        pathbintest = PathDataTime + "Bin/Test/"

        if not os.path.exists(pathbintest):
                os.makedirs(pathbintest)

        pathencode3 = PathDataTime + "Encoding/Bintest/"

        if not os.path.exists(pathencode3):
                os.makedirs(pathencode3)


        pathencode4 = PathDataTime + "Encoding/Bintest/"

        if not os.path.exists(pathencode4):
                os.makedirs(pathencode4)
else:
        skip = skip + 1

if showbintest2 != 0:
	
        print "Show Binary Test (Twitter-Order) :",showbintest2

        show += "-BnTest2"

        pathbintest2 = PathDataTime + "Bin/Test/Twitter-Order/"

        if not os.path.exists(pathbintest2):
                os.makedirs(pathbintest2)
else:
        skip = skip + 1

if showhexatest == 1:
	
        print "Show hexa testing :",showhexatest

        show += "-HxTst"

        pathhexatest = PathDataTime + "Unicode/TEST/FFFFF Test/"
        pathhexatest2 = PathDataTime + "Hexa/TEST/FFFFF Test/"

        if not os.path.exists(pathhexatest):
                os.makedirs(pathhexatest)
                os.makedirs(pathhexatest2)

else:
        skip = skip + 1

if showhexatest2 == 1:
	
        print "Show hexa testing (Twitter-Order) :",showhexatest2

        show += "-HxTst2"

        pathhexatestreversed = PathDataTime + "Unicode/Twitter-Order/TEST/FFFFF Test/"
        pathhexatestreversed2 = PathDataTime + "Hexa/Twitter-Order/TEST/FFFFF Test/"
        if not os.path.exists(pathhexatestreversed):
                os.makedirs(pathhexatestreversed)
                os.makedirs(pathhexatestreversed2)
else:
        skip = skip + 1

if showchardet == 1:
	
        print "Show Chardet best guess:",showchardet

        show += "-Chardet"
else:
        skip = skip + 1


if showftfy == 1:
        
        print "Show Ftfy best guess:",showchardet

        show += "-Ftfy"
else:
        skip = skip + 1

if showencoding == 1:
        
        print "Show all encodings :",showencoding2

        show += "-Encod"

        pathencode = PathDataTime + "Encoding/"
        
        if not os.path.exists(pathencode):
                os.makedirs(pathencode)

        pathencode3 = PathDataTime + "Encoding/"
        
        if not os.path.exists(pathencode3):
                os.makedirs(pathencode3)

else:
        skip = skip + 1

if showencoding2 == 1:
	
        print "Show all encodings in Twitter-Order :",showencoding2

        show += "-Encod2"

        pathencode2 = PathDataTime + "Encoding/Twitter-Order/"
        
        if not os.path.exists(pathencode2):
                os.makedirs(pathencode2)
        pathencode4 = PathDataTime + "Encoding/Twitter-Order/"
        
        if not os.path.exists(pathencode4):
                os.makedirs(pathencode4)

else:
        skip = skip + 1

if showhash == 1:

        print "Show Hash test :",showhash
        show += "-Hash"
        pathhash = PathDataTime + "Hash/"
	pathhash2 = PathDataTime + "Hash/Twitter-Order/"
        if not os.path.exists(pathhash):
                os.makedirs(pathhash)
        if not os.path.exists(pathhash2):
                os.makedirs(pathhash2)



else:
        skip = skip + 1

if showhashtweet == 1:
	
	print "Show Hash test (Tweet by Tweet)"
	show += "-HashTweet"
else:
	skip = skip + 1

if showhashtweet2 == 1:
	
	print "Show Hash test (Tweet by Tweet) in Twitter-Order"
	show += "-HashTweet2"
else:
	skip = skip + 1


if showonlycp == 1:

	print "Show only cp12~ encoding :",showonlycp
	show += "-Cp1"
else:
	skip = skip + 1



if showrainbow == 1:

        print "Show Rainbow Table test :",showrainbow
        show += "-Rainbow"
        pathrainbow = PathDataTime + "Rainbow/"

        if not os.path.exists(pathrainbow):
                os.makedirs(pathrainbow)

else:
        skip = skip + 1

if showmagicnumber == 1:
	
        print "Show Magic Number :",showmagicnumber

        show  += "-Magic"

        pathmagic = PathDataTime + "Magic/"

        if not os.path.exists(pathmagic):
                os.makedirs(pathmagic)

if showreplace == 1:
	
	print "Show Replace Test :",showreplace

	show += "-Replace"
else:
	skip = skip + 1

if showreplace2 == 1:
        
        print "Show Replace Test (Twitter-Order) :",showreplace2

        show += "-Replace2"
else:
        skip = skip + 1



if showhdcp == 1:
	
        print "Show Hdcp master key test :",showhdcp

        show  += "-hdcp"

        pathhdcp = PathDataTime + "Hdcp/"

        if not os.path.exists(pathhdcp):
                os.makedirs(pathhdcp)
else:
        skip = skip + 1

if showmatrix == 1:
	print "Show Hammer Time :",showmatrix 

	show += "-Bored"
else:
        skip = skip + 1

if showdebug == 1:
        print "Show debug :",showdebug

        show += "-Debug"
else:
        skip = skip + 1

print ""
print "Nbr of loop :",nbrloop
print "Nbr of tweet by loop :",nbrtweet
print "Total tweets : ",totaltwt
print ""
print "Nbr of test skipped :",skip
print ""
print "Twitter user :",User
print ""



time.sleep(2)


##  you dont want like 200Mo of log ...
if showbintest == 1 or showbintest2 == 1 or showrainbow == 1 or showhash == 1:
        log = 0


if log == 1:
  class Logger(object):
    def __init__(self):

        self.terminal = sys.stdout
        if not os.path.exists(PathLogs):
                os.makedirs(PathLogs)

        self.log = open(PathLogs + "stout-" + show + dated + ".log", "a") ## Some logfile
        
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  
    def flush(self):
        pass    


if log == 1:
        sys.stdout = Logger()

