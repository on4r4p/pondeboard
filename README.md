### Download tweets from the bot @Pondeboard 
### and try to make sense of it .

 By default Pondeboard.py will print a lot of things into your terminal .
 You can choose what you want to see by editing Settings.py

 (Bintest1 & Bintest2 could take hours to complete ..) 
 (ShowHash & Showhashtweet could take weeks to complete..)

### Python 2.7
### apt-get install python-libxml2
### pip install httplib2
### pip install unidecode
### pip install chardet
### pip install ftfy
### Install twython and get some twitter api key .


chmod +x hashboard.sh if subprocess error.

(Note working anymore i have another use for that account)
 https://twitter.com/pondeboard1 is an attempted at recreating the original pondeboard bot.
 Will use it to check how my script is behaving.
 (pondetest.py was used to feed pondeboard1)


At this time i think the best procedure to get a chance to understand what that bot is tweeting about
is to sort all his tweets as they first appeared on twitter (the first at the top of his timeline is the last to be proceded)
then to convert the binary code (always 140 character) to ascii which gives me something that looks like hexadecimal.
Decoding hexadecimal to unicode shows you unreadable random datas for humans it could be anything.
So its either crypted and in this case im fucked or that bot is sending files through twitter truncated in 140 characters
Or maybe im missing something....
So let's try to find if there are any magic numbers in the result.
Magic numbers strenght found are too weak to be true ...
Okay maybe i could mess with the binary ....
No luck there too ...
hum ...
Ok let's try all the enconding with all results we got so far ..
And im lost again ..
Erf im gonna make an extra test for hexadecimal ...As if it wasnt long enough already... 
Now im trying to find known hash in results ..
Could take month !
Found weird hash adf340bf82441edb2930cba62ccfd93c ...
And another one 5865b6a13daa2f062dea5517f252c21e !
OK now im trying to create similare hash results to confirm this is what i m thinking .
The bad news is its going to take a year or more if i do that with 3200 tweets .
So im gona try with 2 tweets .

The settings im using for this task are :


User = "pondeboard" 

nbrloop = 1 
nbrtweet = 2 

log = 1
showtime = 1 
showtweetcounter = 1 
showbinary = 1 
showhexa = 1 
showuni = 1 
showrainbow = 1 
showdebug = 1 



Wish me good luck :)




....So after 3 day 19 hours and 23 seconds 
I didn't found any md5 hash or part of md5 hash
longer than 7 digits in hexadecimal results using a list of md5 created from
another list of timestamps chosen according to the current tweet's timestamp followed by a line from the Bible .
So far iv tried every line of the bible against a range of 30 seconds around the tweet timestamp.
Im going to try to push it to 120 seconds but im starting to believe that the cracked hash from http://md5decryption.com/
was maybe just a coincidence and in this case i think i will give up cause im not even sure if im using at least the right bible file.

Still no results but iv noticed something odd in my previous attempt :

cat ./tmp/pondeboard/2016-06-14/data/8-20/Rainbow/rainbow.table | grep -C 3 90e2a4

=============================================
=============================================
Fucking Found 90e2a4 in ./tmp/pondeboard/2016-06-14/data/8-20/Hexa/hexa-8-20.hex !
Date = 2016-06-14;06:20:43 Tweet Nbr : 1 Current Second : 5
Text = Deuteronomy 1:11 (The LORD God of your fathers make you a thousand times so many more as ye are, and bless you, as he hath promised you!)
Md5sum = 590e2a47a446599041453c24fa63fd42
=============================================
=============================================
Fucking Found 0e2a4f in ./tmp/pondeboard/2016-06-14/data/8-20/Hexa/hexa-8-20.hex !
Date = 2016-06-14;06:20:45 Tweet Nbr : 1 Current Second : 7
Text = 1 Samuel 3:3 And ere the lamp of God went out in the temple of the LORD, where the ark of God was, and Samuel was laid down to sleep;
Md5sum = 6fd2390e2a4f273fae8652fdbf52363b
=============================================
=============================================
Fucking Found 90e2a4 in ./tmp/pondeboard/2016-06-14/data/8-20/Hexa/hexa-8-20.hex !
Date = 2016-06-14;06:20:23 Tweet Nbr : 2 Current Second : 12
Text = Zechariah 8:16 These are the things that ye shall do; Speak ye every man the truth to his neighbour; execute the judgment of truth and peace in your gates:
Md5sum = 37eaaaa4fef28c1c9fd27309a890e2a4
=============================================
=============================================
Fucking Found 90e2a4 in ./tmp/pondeboard/2016-06-14/data/8-20/Hexa/hexa-8-20.hex !
Date = 2016-06-14;06:20:31 Tweet Nbr : 2 Current Second : 20
Text = Deuteronomy 2:12 The Horims also dwelt in Seir beforetime; but the children of Esau succeeded them, when they had destroyed them from before them, and dwelt in their stead; as Israel did unto the land of his possession, which the LORD gave unto them.
Md5sum = 4eeadcbd479e2ba9d55e3390e2a40e6e
=============================================
=============================================

Maybe its corresponding to "2016-06-14;"


Decided to use the Amazon cloud free offer to test 240 seconds around the tweet timestamp .
Hope it will be enough.

See you in 6d 19h 57m 20s ......

Or was it Six month ?

I dont know i may have made a mistake with the Time Left function cause its been a mounth now
and its still telling me there is 5d 2h 58m 0s left ..

Anyway the program is currently testing the 128 th seconds so im guessing i will need another month or two
to test them all until 240 . (For 2 tweets !) 

But It get weirder at around 110 :


=============================================
Fucking Found fd5fa1 in ./tmp/pondeboard/2016-06-26/data/6-38/Hexa/hexa-6-38.hex !
Date = 2016-06-25;10:11:30 Tweet Nbr : 1 Current Second : 111
Text = Luke 8:55 And her spirit came again, and she arose straightway: and he commanded to give her meat.
Md5sum = 04b6bd9f5d6775143ca96ffd5fa1d198
=============================================
=============================================
Fucking Found 8dc486 in ./tmp/pondeboard/2016-06-26/data/6-38/Hexa/hexa-6-38.hex !
Date = 2016-06-25;10:11:31 Tweet Nbr : 1 Current Second : 112
Text = Joshua 20:7 And they appointed Kedesh in Galilee in mount Naphtali, and Shechem in mount Ephraim, and Kirjatharba, which is Hebron, i
n the mountain of Judah.
Md5sum = bdbdb9a31dedc7505fc4ee368dc486cf
=============================================
=============================================
Fucking Found 8dc486c in ./tmp/pondeboard/2016-06-26/data/6-38/Hexa/hexa-6-38.hex !
Date = 2016-06-25;10:11:31 Tweet Nbr : 1 Current Second : 112
Text = Joshua 20:7 And they appointed Kedesh in Galilee in mount Naphtali, and Shechem in mount Ephraim, and Kirjatharba, which is Hebron, i
n the mountain of Judah.
Md5sum = bdbdb9a31dedc7505fc4ee368dc486cf
=============================================
=============================================
Fucking Found 8dc486cf in ./tmp/pondeboard/2016-06-26/data/6-38/Hexa/hexa-6-38.hex !
Date = 2016-06-25;10:11:31 Tweet Nbr : 1 Current Second : 112
Text = Joshua 20:7 And they appointed Kedesh in Galilee in mount Naphtali, and Shechem in mount Ephraim, and Kirjatharba, which is Hebron, i
n the mountain of Judah.
Md5sum = bdbdb9a31dedc7505fc4ee368dc486cf
=============================================
=============================================
Fucking Found 8dc486cf in ./tmp/pondeboard/2016-06-26/data/6-38/Hexa/hexa-6-38.hex !
Date = 2016-06-25;10:11:31 Tweet Nbr : 1 Current Second : 112
Text = Joshua 20:7 And they appointed Kedesh in Galilee in mount Naphtali, and Shechem in mount Ephraim, and Kirjatharba, which is Hebron, i
n the mountain of Judah.
Md5sum = bdbdb9a31dedc7505fc4ee368dc486cf
=============================================
=============================================
Fucking Found a1259 in ./tmp/pondeboard/2016-06-26/data/6-38/Hexa/hexa-6-38.hex !
Date = 2016-06-25;10:11:32 Tweet Nbr : 1 Current Second : 113
Text = Joshua 15:15 And he went up thence to the inhabitants of Debir: and the name of Debir before was Kirjathsepher.
Md5sum = 980be06c3b96429b9aae6c77634a1259
=============================================


End of mystery :

Some Week ago my friend @Katezlipoka after a bit of crawling found the personal github of the creator of @pondeboard .

https://github.com/hnt-stuff/bibl_tweet


The Good News is :

Inside there was a bash script wich could create md5 from a radom line of the bible .
Which can explain why iv found such md5 hashs in the hexadecimal results of the binary tweet from @pondeboard at first. 
Maybe that bot is just sending binary encoded md5 hash on the top  and then feeding an online database of md5 under the table.
Or maybe someone just found the script and decide to play around with it .
Or even the botmaster for testing purposes .

I don't know in any case thnks to whoever put those hashs online cause without them there no way 
i would have been that far with @pondeboard.

I don't know the very goal of @pondeboard but from what iv seen i think the guy who wrote it is a real poet .

The Bad News is :

I don't fucking care anymore :)
The night after @Katezlipoka gave me that link my daughter was born :)

And there is not enough bits in a quantic computer to tell how much i love her .




