from twython import Twython
import datetime,time,sys,os,random,encodings,signal,Settings,unicodedata,chardet,ftfy,codecs,ftfy.bad_codecs,hashlib,urllib2,getopt,subprocess,collections
from os import path
from urllib import urlencode
from re import search, findall
from random import seed, randint
from base64 import decodestring, encodestring
from cookielib import LWPCookieJar
from httplib2 import Http
from libxml2 import parseDoc
from Settings import *
from unidecode import unidecode
from FindMagicNumber import findmagicnumber, countermagic
from FindHdcp import findhdcp
from functools import wraps
from TwitterApiKeys import CONSUMER_KEY,CONSUMER_SECRET



twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET)


###some defs

class TimeoutError(Exception):
	pass


def timeout(seconds=10, error_message="Error : No time to waste !"):
    def decorator(func):
        def _handle_timeout(signum, frame):
		try:
        		raise TimeoutError(error_message)
		except:
#			print ""
#			print error_message
			print ""
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator

@timeout(2)
class SCHWETT:
	
	name = 		"schwett"
	url = 		"http://schwett.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://schwett.com/md5/index.php?md5value=%s&md5c=Hash+Match" % (hashvalue)
		
		# Make the request
		response = do_HTTP_request ( url )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r"<h3><font color='red'>No Match Found</font></h3><br />", html)
		if match:
			return None
		else:
			return "The hash is broken, please contact with La X marca el lugar and send it the hash value to add the correct regexp."


@timeout(2)
class NETMD5CRACK:

	name = 		"netmd5crack"
	url = 		"http://www.netmd5crack.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://www.netmd5crack.com/cgi-bin/Crack.py?InputHash=%s" % (hashvalue)
		
		# Make the request
		response = do_HTTP_request ( url )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		regexp = r'<tr><td class="border">%s</td><td class="border">[^<]*</td></tr></table>' % (hashvalue)
		match = search (regexp, html)
		
		if match:
			match2 = search ( "Sorry, we don't have that hash in our database", match.group() )
			if match2:
				return None
			else:
				return match.group().split('border')[2].split('<')[0][2:]

@timeout(2)
class BENRAMSEY:
	
	name = 		"benramsey"
	url = 		"http://tools.benramsey.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://tools.benramsey.com/md5/md5.php?hash=%s" % (hashvalue)
		
		# Make the request
		response = do_HTTP_request ( url )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
			
		match = search (r'<string><!\[CDATA\[[^\]]*\]\]></string>', html)
		
		if match:
			return match.group().split(']')[0][17:]
		else:
			return None


@timeout(2)
class GROMWEB: 
	
	name = 		"gromweb"
	url = 		"http://md5.gromweb.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://md5.gromweb.com/query/%s" % (hashvalue)
		
		# Make the request
		response = do_HTTP_request ( url )
		
		# Analyze the response
		if response:
			return response.read()
			
		return response
		
		

@timeout(2)
class HASHCRACKING:
	
	name = 		"hashcracking"
	url = 		"http://md5.hashcracking.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://md5.hashcracking.com/search.php?md5=%s" % (hashvalue)
		
		# Make the request
		response = do_HTTP_request ( url )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'\sis.*', html)
		
		if match:
			return match.group()[4:]
			
		return None


@timeout(2)
class VICTOROV:
	
	name = 		"hashcracking"
	url = 		"http://victorov.su"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://victorov.su/md5/?md5e=&md5d=%s" % (hashvalue)
		
		# Make the request
		response = do_HTTP_request ( url )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r': <b>[^<]*</b><br><form action="">', html)
		
		if match:
			return match.group().split('b>')[1][:-2]
			
		return None

@timeout(2)
class THEKAINE: 
	
	name = 		"thekaine"
	url = 		"http://md5.thekaine.de"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://md5.thekaine.de/?hash=%s" % (hashvalue)
		
		# Make the request
		response = do_HTTP_request ( url )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<td colspan="2"><br><br><b>[^<]*</b></td><td></td>', html)
		
		if match:
			
			match2 = search (r'not found', match.group() )
			
			if match2:
				return None
			else:
				return match.group().split('b>')[1][:-2]
			

@timeout(2)
class TMTO:
	
	name = 		"tmto"
	url = 		"http://www.tmto.org"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://www.tmto.org/api/latest/?hash=%s&auth=true" % (hashvalue)
		
		# Make the request
		response = do_HTTP_request ( url )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'text="[^"]+"', html)
		
		if match:
			return decodestring(match.group().split('"')[1])
		else:
			return None

@timeout(2)
class MD5_DB:
	
	name = 		"md5-db"
	url = 		"http://md5-db.de"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://md5-db.de/%s.html" % (hashvalue)
		
		# Make the request
		response = do_HTTP_request ( url )
		
		# Analyze the response
		if not response:
			return None
			
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<strong>Es wurden 1 m.gliche Begriffe gefunden, die den Hash \w* verwenden:</strong><ul><li>[^<]*</li>', html)
		
		if match:
			return match.group().split('li>')[1][:-2]
		else:
			return None

@timeout(2)
class MD5PASS:
	
	name = 		"md5pass"
	url = 		"http://md5pass.info"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = self.url
		
		# Build the parameters
		params = { "hash" : hashvalue,
			   "get_pass" : "Get Pass" }
		
		# Make the request
		response = do_HTTP_request ( url, params )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r"Password - <b>[^<]*</b>", html)
		
		if match:
			return match.group().split('b>')[1][:-2]
		else:
			return None


@timeout(2)
class MD5DECRYPTION:
	
	name = 		"md5decryption"
	url = 		"http://md5decryption.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = self.url
		
		# Build the parameters
		params = { "hash" : hashvalue,
			   "submit" : "Decrypt It!" }
		
		# Make the request
		response = do_HTTP_request ( url, params )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r"Decrypted Text: </b>[^<]*</font>", html)
		
		if match:
			return match.group().split('b>')[1][:-7]
		else:
			return None


@timeout(2)
class MD5CRACK:
	
	name = 		"md5crack"
	url = 		"http://md5crack.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://md5crack.com/crackmd5.php"
		
		# Build the parameters
		params = { "term" : hashvalue,
			   "crackbtn" : "Crack that hash baby!" }
		
		# Make the request
		response = do_HTTP_request ( url, params )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'Found: md5\("[^"]+"\)', html)
		
		if match:
			return match.group().split('"')[1]
		else:
			return None

@timeout(2)
class MD5ONLINE:
	
	name = 		"md5online"
	url = 		"http://md5online.net"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = self.url
		
		# Build the parameters
		params = { "pass" : hashvalue,
			   "option" : "hash2text",
			   "send" : "Submit" }
		
		# Make the request
		response = do_HTTP_request ( url, params )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<center><p>md5 :<b>\w*</b> <br>pass : <b>[^<]*</b></p></table>', html)
		
		if match:
			return match.group().split('b>')[3][:-2]
		else:
			return None



@timeout(2)
class MD5_DECRYPTER:
	
	name = 		"md5-decrypter"
	url = 		"http://md5-decrypter.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = self.url
		
		# Build the parameters
		params = { "data[Row][cripted]" : hashvalue }
		
		# Make the request
		response = do_HTTP_request ( url, params )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = findall (r'<b class="res">[^<]*</b>', html)
		
		if match:
			return match[1].split('>')[1][:-3]
		else:
			return None


@timeout(2)
class AUTHSECUMD5:
	
	name = 		"authsecu"
	url = 		"http://www.authsecu.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://www.authsecu.com/decrypter-dechiffrer-cracker-hash-md5/script-hash-md5.php"
		
		# Build the parameters
		params = { "valeur_bouton" : "dechiffrage",
			   "champ1" : "",
			   "champ2" : hashvalue,
			   "dechiffrer.x" : "78",
			   "dechiffrer.y" : "7" }
		
		# Make the request
		response = do_HTTP_request ( url, params )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = findall (r'<td><p class="chapitre---texte-du-tableau-de-niveau-1">[^<]*</p></td>', html)
		
		if len(match) > 2:
			return match[1].split('>')[2][:-3]
		else:
			return None


@timeout(2)
class HASHCRACK:
	
	name = 		"hashcrack"
	url = 		"http://hashcrack.com"
	supported_algorithm = [MD5, SHA1, MYSQL, LM, NTLM]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://hashcrack.com/indx.php"
		
		hash2 = None
		if alg in [LM, NTLM] and ':' in hashvalue:
			if alg == LM:
				hash2 = hashvalue.split(':')[0]
			else:
				hash2 = hashvalue.split(':')[1]
		else:
			hash2 = hashvalue
		
		# Delete the possible starting '*'
		if alg == MYSQL and hash2[0] == '*':
			hash2 = hash2[1:]
		
		# Build the parameters
		params = { "auth" : "8272hgt",
			   "hash" : hash2,
			   "string" : "",
			   "Submit" : "Submit" }
		
		# Make the request
		response = do_HTTP_request ( url, params )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<div align=center>"[^"]*" resolves to</div><br><div align=center> <span class=hervorheb2>[^<]*</span></div></TD>', html)
		
		if match:
			return match.group().split('hervorheb2>')[1][:-18]
		else:
			return None


@timeout(2)
class OPHCRACK:
	
	name = 		"ophcrack"
	url = 		"http://www.objectif-securite.ch"
	supported_algorithm = [LM, NTLM]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Check if hashvalue has the character ':'
		if ':' not in hashvalue:
			return None
			
		# Ophcrack doesn't crack NTLM hashes. It needs a valid LM hash and this one is an empty hash.
		if hashvalue.split(':')[0] == "aad3b435b51404eeaad3b435b51404ee":
			return None
		
		# Build the URL and the headers
		url = "http://www.objectif-securite.ch/en/products.php?hash=%s" % (hashvalue.replace(':', '%3A'))
		
		# Make the request
		response = do_HTTP_request ( url )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<table><tr><td>Hash:</td><td>[^<]*</td></tr><tr><td><b>Password:</b></td><td><b>[^<]*</b></td>', html)
		
		if match:
			return match.group().split('b>')[3][:-2]
		else:
			return None
	

@timeout(2)
class C0LLISION:
	
	name = 		"c0llision"
	url = 		"http://www.c0llision.net"
	supported_algorithm = [MD5, LM, NTLM]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Check if hashvalue has the character ':'
		if alg in [LM, NTLM] and ':' not in hashvalue:
			return None
			
		# Look for "hash[_csrf_token]" parameter
		response = do_HTTP_request ( "http://www.c0llision.net/webcrack.php" )
		html = None
		if response:
			html = response.read()
		else:
			return None
		match = search (r'<input type="hidden" name="hash._csrf_token." value="[^"]*" id="hash__csrf_token" />', html)
		token = None
		if match:
			token = match.group().split('"')[5]
		
		# Build the URL
		url = "http://www.c0llision.net/webcrack/request"
		
		# Build the parameters
		params = { "hash[_input_]" : hashvalue,
			   "hash[_csrf_token]" : token }
		
		# Make the request
		response = do_HTTP_request ( url, params )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = None
		if alg in [LM, NTLM]:
			html = html.replace('\n', '')
			result = ""
			
			match = search (r'<table class="pre">.*?</table>', html)
			if match:
				try:
					doc = parseDoc ( match.group() )
				except:
					print "INFO: You need libxml2 to use this plugin."
					return None
				lines = doc.xpathEval("//tr")
				for l in lines:
					doc = parseDoc ( str(l) )
					cols = doc.xpathEval("//td")
					
					if len(cols) < 4:
						return None
					
					if cols[2].content:
						result = " > %s (%s) = %s\n" % ( cols[1].content, cols[2].content, cols[3].content )
				
				#return ( result and "\n" + result or None )
				return ( result and result.split()[-1] or None )
			
		else:
			match = search (r'<td class="plaintext">[^<]*</td>', html)
		
			if match:
				return match.group().split('>')[1][:-4]
		
		return None


@timeout(2)
class REDNOIZE:
	
	name = 		"rednoize"
	url = 		"http://md5.rednoize.com"
	supported_algorithm = [MD5, SHA1]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = ""
		if alg == MD5:
			url = "http://md5.rednoize.com/?p&s=md5&q=%s&_=" % (hashvalue)
		else:
			url = "http://md5.rednoize.com/?p&s=sha1&q=%s&_=" % (hashvalue)
		
		# Make the request
		response = do_HTTP_request ( url )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		return html
			
			

@timeout(2)
class CMD5:
	
	name = 		"cmd5"
	url = 		"http://www.cmd5.org"
	supported_algorithm = [MD5, NTLM]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Look for hidden parameters
		response = do_HTTP_request ( "http://www.cmd5.org/" )
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="[^"]*" />', html)
		viewstate = None
		if match:
			viewstate = match.group().split('"')[7]
		
		match = search (r'<input type="hidden" name="ctl00.ContentPlaceHolder1.HiddenField1" id="ctl00_ContentPlaceHolder1_HiddenField1" value="[^"]*" />', html)
		ContentPlaceHolder1 = ""
		if match:
			ContentPlaceHolder1 = match.group().split('"')[7]
		
		match = search (r'<input type="hidden" name="ctl00.ContentPlaceHolder1.HiddenField2" id="ctl00_ContentPlaceHolder1_HiddenField2" value="[^"]*" />', html)
		ContentPlaceHolder2 = ""
		if match:
			ContentPlaceHolder2 = match.group().split('"')[7]
		
		# Build the URL
		url = "http://www.cmd5.org/"
		
		hash2 = ""
		if alg == MD5:
			hash2 = hashvalue
		else:
			if ':' in hashvalue:
				hash2 = hashvalue.split(':')[1]
		
		# Build the parameters
		params = { "__EVENTTARGET" : "",
			   "__EVENTARGUMENT" : "",
			   "__VIEWSTATE" : viewstate,
			   "ctl00$ContentPlaceHolder1$TextBoxq" : hash2,
			   "ctl00$ContentPlaceHolder1$InputHashType" : alg,
			   "ctl00$ContentPlaceHolder1$Button1" : "decrypt",
			   "ctl00$ContentPlaceHolder1$HiddenField1" : ContentPlaceHolder1,
			   "ctl00$ContentPlaceHolder1$HiddenField2" : ContentPlaceHolder2 }
			   
		header = { "Referer" : "http://www.cmd5.org/" }
		
		# Make the request
		response = do_HTTP_request ( url, params, header )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<span id="ctl00_ContentPlaceHolder1_LabelResult">[^<]*</span>', html)
		
		if match:
			return match.group().split('>')[1][:-6]
		else:
			return None


@timeout(2)
class AUTHSECUCISCO7:
	
	name = 		"authsecu"
	url = 		"http://www.authsecu.com"
	supported_algorithm = [CISCO7]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL and the headers
		url = "http://www.authsecu.com/decrypter-dechiffrer-cracker-password-cisco-7/script-password-cisco-7-launcher.php"
		
		# Build the parameters
		params = { "valeur_bouton" : "dechiffrage",
			   "champ1" : hashvalue,
			   "dechiffrer.x" : 43,
			   "dechiffrer.y" : 16 }
			   
		# Make the request
		response = do_HTTP_request ( url, params )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = findall (r'<td><p class="chapitre---texte-du-tableau-de-niveau-1">[^<]*</p></td>', html)
		
		if match:
			return match[1].split('>')[2][:-3]
		else:
			return None



@timeout(2)
class CACIN:
	
	name = 		"cacin"
	url = 		"http://cacin.net"
	supported_algorithm = [CISCO7]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL and the headers
		url = "http://cacin.net/cgi-bin/decrypt-cisco.pl?cisco_hash=%s" % (hashvalue)
		
		# Make the request
		response = do_HTTP_request ( url )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<tr>Cisco password 7: [^<]*</tr><br><tr><th><br>Decrypted password: .*', html)
		
		if match:
			return match.group().split(':')[2][1:]
		else:
			return None

@timeout(2)
class IBEAST:
	
	name = 		"ibeast"
	url = 		"http://www.ibeast.com"
	supported_algorithm = [CISCO7]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL and the headers
		url = "http://www.ibeast.com/content/tools/CiscoPassword/decrypt.php?txtPassword=%s&submit1=Enviar+consulta" % (hashvalue)
		
		# Make the request
		response = do_HTTP_request ( url )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<font size="\+2">Your Password is [^<]*<br>', html)
		
		if match:
			return match.group().split('is ')[1][:-4]
		else:
			return None


@timeout(2)
class PASSWORD_DECRYPT:
	
	name = 		"password-decrypt"
	url = 		"http://password-decrypt.com"
	supported_algorithm = [CISCO7, JUNIPER]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL and the parameters
		url = ""
		params = None
		if alg == CISCO7:
			url = "http://password-decrypt.com/cisco.cgi"
			params = { "submit" : "Submit",
				"cisco_password" : hashvalue,
				"submit" : "Submit" }
		else:
			url = "http://password-decrypt.com/juniper.cgi"
			params = { "submit" : "Submit",
				"juniper_password" : hashvalue,
				"submit" : "Submit" }
		
		
		# Make the request
		response = do_HTTP_request ( url, params )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'Decrypted Password:&nbsp;<B>[^<]*</B> </p>', html)
		
		if match:
			return match.group().split('B>')[1][:-2]
		else:
			return None



@timeout(2)
class BIGTRAPEZE:
	
	name = 		"bigtrapeze"
	url = 		"http://www.bigtrapeze.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL and the headers
		url = "http://www.bigtrapeze.com/md5/index.php"
		
		# Build the parameters
		params = { "query" : hashvalue,
			   " Crack " : "Enviar consulta" }
			   
		# Build the Headers with a random User-Agent
		headers = { "User-Agent" : USER_AGENTS[randint(0, len(USER_AGENTS))-1] }

		# Make the request
		response = do_HTTP_request ( url, params, headers )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
			
		match = search (r'Congratulations!<li>The hash <strong>[^<]*</strong> has been deciphered to: <strong>[^<]*</strong></li>', html)
		
		if match:
			return match.group().split('strong>')[3][:-2]
		else:
			return None

@timeout(2)
class HASHCHECKER:
	
	name = 		"hashchecker"
	url = 		"http://www.hashchecker.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL and the headers
		url = "http://www.hashchecker.com/index.php"
		
		# Build the parameters
		params = { "search_field" : hashvalue,
			   "Submit" : "search" }
			   
		# Make the request
		response = do_HTTP_request ( url, params )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
			
		match = search (r'<td><li>Your md5 hash is :<br><li>[^\s]* is <b>[^<]*</b> used charlist :2</td>', html)
		
		if match:
			return match.group().split('b>')[1][:-2]
		else:
			return None


@timeout(2)
class MD5HASHCRACKER:
	
	name = 		"md5hashcracker"
	url = 		"http://md5hashcracker.appspot.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://md5hashcracker.appspot.com/crack"
		
		# Build the parameters
		params = { "query" : hashvalue,
			   "submit" : "Crack" }
		
		# Make the firt request
		response = do_HTTP_request ( url, params )
		
		# Build the second URL
		url = "http://md5hashcracker.appspot.com/status"
		
		# Make the second request
		response = do_HTTP_request ( url )
		
		# Analyze the response
		if response:
			html = response.read()
		else:
			return None
		match = search (r'<td id="cra[^"]*">not cracked</td>', html)
		
		if not match:
			match = search (r'<td id="cra[^"]*">cracked</td>', html)
			regexp = r'<td id="pla_' + match.group().split('"')[1][4:] + '">[^<]*</td>'
			match2 = search (regexp, html)
			if match2:
				return match2.group().split('>')[1][:-4]
			
		else:
			return None


@timeout(2)
class PASSCRACKING:
	
	name = 		"passcracking"
	url = 		"http://passcracking.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL 
		url = "http://passcracking.com/index.php"
		
		# Build the parameters
		boundary = "-----------------------------" + str(randint(1000000000000000000000000000,9999999999999999999999999999))
		params = [ '--' + boundary, 
			   'Content-Disposition: form-data; name="admin"', 
			   '', 
			   'false', 
			   
			   '--' + boundary, 
			   'Content-Disposition: form-data; name="admin2"', 
			   '', 
			   '77.php', 
			   
			   '--' + boundary, 
			   'Content-Disposition: form-data; name="datafromuser"', 
			   '', 
			   '%s' % (hashvalue) , 
			   
			   '--' + boundary + '--', '' ]
		body = '\r\n'.join(params)

		# Build the headers
		headers = { "Content-Type" : "multipart/form-data; boundary=%s" % (boundary),
		            "Content-length" : len(body) }
		
			   
		# Make the request
		request = urllib2.Request ( url )
		request.add_header ( "Content-Type", "multipart/form-data; boundary=%s" % (boundary) )
		request.add_header ( "Content-length", len(body) )
		request.add_data(body)
		try:
			response = urllib2.urlopen(request)
		except:
			return None
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
			
		match = search (r'<td>md5 Database</td><td>[^<]*</td><td bgcolor=.FF0000>[^<]*</td>', html)
		
		if match:
			return match.group().split('>')[5][:-4]
		else:
			return None

@timeout(2)
class ASKCHECK:
	
	name = 		"askcheck"
	url = 		"http://askcheck.com"
	supported_algorithm = [MD4, MD5, SHA1, SHA256]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://askcheck.com/reverse?reverse=%s" % (hashvalue)
		
		# Make the request
		response = do_HTTP_request ( url )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
			
		match = search (r'Reverse value of [^\s]* hash <a[^<]*</a> is <a[^>]*>[^<]*</a>', html)
		
		if match:
			return match.group().split('>')[3][:-3]
		else:
			return None


@timeout(2)
class FOX21:
	
	name = 		"fox21"
	url = 		"http://cracker.fox21.at"
	supported_algorithm = [MD5, LM, NTLM]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		hash2 = None
		if alg in [LM, NTLM] and ':' in hashvalue:
			if alg == LM:
				hash2 = hashvalue.split(':')[0]
			else:
				hash2 = hashvalue.split(':')[1]
		else:
			hash2 = hashvalue
		
		
		# Build the URL
		url = "http://cracker.fox21.at/api.php?a=check&h=%s" % (hashvalue)
		
		# Make the request
		response = do_HTTP_request ( url )
		
		# Analyze the response
		xml = None
		if response:
			try:
				doc = parseDoc ( response.read() )
			except:
				print "INFO: You need libxml2 to use this plugin."
				return None
		else:
			return None
		
		result = doc.xpathEval("//hash/@plaintext")
		
		if result:
			return result[0].content
		else:
			return None

@timeout(2)
class NICENAMECREW:
	
	name = 		"nicenamecrew"
	url = 		"http://crackfoo.nicenamecrew.com"
	supported_algorithm = [MD5, SHA1, LM]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		hash2 = None
		if alg in [LM] and ':' in hashvalue:
			hash2 = hashvalue.split(':')[0]
		else:
			hash2 = hashvalue
			
		# Build the URL
		url = "http://crackfoo.nicenamecrew.com/?t=%s" % (alg)
		
		# Build the parameters
		params = { "q" : hash2,
			   "sa" : "Crack" }
			   
		# Make the request
		response = do_HTTP_request ( url, params )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'The decrypted version of [^\s]* is:<br><strong>[^<]*</strong>', html)
		
		if match:
			return match.group().split('strong>')[1][:-2].strip()
		else:
			return None


@timeout(2)
class JOOMLAAA:
	
	name = 		"joomlaaa"
	url = 		"http://joomlaaa.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://joomlaaa.com/component/option,com_md5/Itemid,31/"
		
		# Build the parameters
		params = { "md5" : hashvalue,
			   "decode" : "Submit" }
			   
		# Make the request
		response = do_HTTP_request ( url, params )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r"<td class='title1'>not available</td>", html)
		
		if not match:
			match2 = findall (r"<td class='title1'>[^<]*</td>", html)
			return match2[1].split('>')[1][:-4]
		else:
			return None


@timeout(2)
class MD5_LOOKUP:
	
	name = 		"md5-lookup"
	url = 		"http://md5-lookup.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://md5-lookup.com/livesearch.php?q=%s" % (hashvalue)
		
		# Make the request
		response = do_HTTP_request ( url )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<td width="250">[^<]*</td>', html)
		
		if match:
			return match.group().split('>')[1][:-4]
		else:
			return None

@timeout(2)
class SHA1_LOOKUP:
	
	name = 		"sha1-lookup"
	url = 		"http://sha1-lookup.com"
	supported_algorithm = [SHA1]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://sha1-lookup.com/livesearch.php?q=%s" % (hashvalue)
		
		# Make the request
		response = do_HTTP_request ( url )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<td width="250">[^<]*</td>', html)
		
		if match:
			return match.group().split('>')[1][:-4]
		else:
			return None

@timeout(2)
class SHA256_LOOKUP:
	
	name = 		"sha256-lookup"
	url = 		"http://sha-256.sha1-lookup.com"
	supported_algorithm = [SHA256]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://sha-256.sha1-lookup.com/livesearch.php?q=%s" % (hashvalue)
		
		# Make the request
		response = do_HTTP_request ( url )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<td width="250">[^<]*</td>', html)
		
		if match:
			return match.group().split('>')[1][:-4]
		else:
			return None


@timeout(2)
class RIPEMD160_LOOKUP:
	
	name = 		"ripemd-lookup"
	url = 		"http://www.ripemd-lookup.com"
	supported_algorithm = [RIPEMD]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://www.ripemd-lookup.com/livesearch.php?q=%s" % (hashvalue)
		
		# Make the request
		response = do_HTTP_request ( url )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<td width="250">[^<]*</td>', html)
		
		if match:
			return match.group().split('>')[1][:-4]
		else:
			return None


@timeout(2)
class MD5_COM_CN:
	
	name = 		"md5.com.cn"
	url = 		"http://md5.com.cn"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://md5.com.cn/md5reverse"
		
		# Build the parameters
		params = { "md" : hashvalue,
			   "submit" : "MD5 Crack" }
		
		# Make the request
		response = do_HTTP_request ( url, params )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<b style="color:red;">[^<]*</b><br/><span', html)
		
		if match:
			return match.group().split('>')[1][:-3]
		else:
			return None




@timeout(2)
class DIGITALSUN:
	
	name = 		"digitalsun.pl"
	url = 		"http://md5.digitalsun.pl"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://md5.digitalsun.pl/"
		
		# Build the parameters
		params = { "hash" : hashvalue }
		
		# Make the request
		response = do_HTTP_request ( url, params )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<b>[^<]*</b> == [^<]*<br>\s*<br>', html)
		
		if match:
			return match.group().split('b>')[1][:-2]
		else:
			return None


@timeout(2)
class DRASEN:
	
	name = 		"drasen.net"
	url = 		"http://md5.drasen.net"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://md5.drasen.net/search.php?query=%s" % (hashvalue)
		
		# Make the request
		response = do_HTTP_request ( url )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'Hash: [^<]*<br />Plain: [^<]*<br />', html)
		
		if match:
			return match.group().split('<br />')[1][7:]
		else:
			return None




@timeout(2)
class MD5_NET:
	
	name = 		"md5.net"
	url = 		"http://md5.net"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://www.md5.net/cracker.php"
		
		# Build the parameters
		params = { "hash" : hashvalue }
		
		# Make the request
		response = do_HTTP_request ( url, params )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<input type="text" id="hash" size="32" value="[^"]*"/>', html)
		
		if match:
			return match.group().split('"')[7]
		else:
			return None

@timeout(2)
class MD5HOOD:
	
	name = 		"md5hood"
	url = 		"http://md5hood.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://md5hood.com/index.php/cracker/crack"
		
		# Build the parameters
		params = { "md5" : hashvalue,
			   "submit" : "Go" }
		
		# Make the request
		response = do_HTTP_request ( url, params )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<div class="result_true">[^<]*</div>', html)
		
		if match:
			return match.group().split('>')[1][:-5]
		else:
			return None


@timeout(2)
class STRINGFUNCTION:
	
	name = 		"stringfunction"
	url = 		"http://www.stringfunction.com"
	supported_algorithm = [MD5, SHA1]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = ""
		if alg == MD5:
			url = "http://www.stringfunction.com/md5-decrypter.html"
		else:
			url = "http://www.stringfunction.com/sha1-decrypter.html"
		
		# Build the parameters
		params = { "string" : hashvalue,
			   "submit" : "Decrypt",
			   "result" : "" }
		
		# Make the request
		response = do_HTTP_request ( url, params )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<textarea class="textarea-input-tool-b" rows="10" cols="50" name="result"[^>]*>[^<]+</textarea>', html)
		
		if match:
			return match.group().split('>')[1][:-10]
		else:
			return None




@timeout(2)
class XANADREL:
	
	name = 		"99k.org"
	url = 		"http://xanadrel.99k.org"
	supported_algorithm = [MD4, MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://xanadrel.99k.org/hashes/index.php?k=search"
		
		# Build the parameters
		params = { "hash" : hashvalue,
			   "search" : "ok" }
		
		# Make the request
		response = do_HTTP_request ( url, params )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<p>Hash : [^<]*<br />Type : [^<]*<br />Plain : "[^"]*"<br />', html)
		
		if match:
			return match.group().split('"')[1]
		else:
			return None



@timeout(2)
class SANS:
	
	name = 		"sans"
	url = 		"http://isc.sans.edu"
	supported_algorithm = [MD5, SHA1]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://isc.sans.edu/tools/reversehash.html"
		
		# Build the Headers with a random User-Agent
		headers = { "User-Agent" : USER_AGENTS[randint(0, len(USER_AGENTS))-1] }
		
		# Build the parameters
		response = do_HTTP_request ( url, httpheaders=headers )
		html = None
		if response:
			html = response.read()
		else:
			return None
		match = search (r'<input type="hidden" name="token" value="[^"]*" />', html)
		token = ""
		if match:
			token = match.group().split('"')[5]
		else:
			return None
		
		params = { "token" : token,
			   "text" : hashvalue,
			   "word" : "",
			   "submit" : "Submit" }
		
		# Build the Headers with the Referer header
		headers["Referer"] = "http://isc.sans.edu/tools/reversehash.html"
		
		# Make the request
		response = do_HTTP_request ( url, params, headers )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'... hash [^\s]* = [^\s]*\s*</p><br />', html)
		
		if match:
			print "hola mundo"
			return match.group().split('=')[1][:-10].strip()
		else:
			return None


@timeout(2)
class BOKEHMAN:
	
	name = 		"bokehman"
	url = 		"http://bokehman.com"
	supported_algorithm = [MD4, MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://bokehman.com/cracker/"
		
		# Build the parameters from the main page
		response = do_HTTP_request ( url )
		html = None
		if response:
			html = response.read()
		else:
			return None
		match = search (r'<input type="hidden" name="PHPSESSID" id="PHPSESSID" value="[^"]*" />', html)
		phpsessnid = ""
		if match:
			phpsessnid = match.group().split('"')[7]
		else:
			return None
		match = search (r'<input type="hidden" name="key" id="key" value="[^"]*" />', html)
		key = ""
		if match:
			key = match.group().split('"')[7]
		else:
			return None
		
		params = { "md5" : hashvalue,
			   "PHPSESSID" : phpsessnid,
			   "key" : key,
			   "crack" : "Try to crack it" }
		
		# Make the request
		response = do_HTTP_request ( url, params )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<tr><td>[^<]*</td><td>[^<]*</td><td>[^s]*seconds</td></tr>', html)
		
		if match:
			return match.group().split('td>')[1][:-2]
		else:
			return None


@timeout(2)
class GOOG_LI:

	name = 		"goog.li"
	url = 		"http://goog.li"
	supported_algorithm = [MD5, MYSQL, SHA1, SHA224, SHA384, SHA256, SHA512, RIPEMD, NTLM, GOST, WHIRLPOOL, LDAP_MD5, LDAP_SHA1]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
			
		hash2 = None
		if alg in [NTLM] and ':' in hashvalue:
			hash2 = hashvalue.split(':')[1]
		else:
			hash2 = hashvalue
		
		# Confirm the initial '*' character
		if alg == MYSQL and hash2[0] != '*':
			hash2 = '*' + hash2
		
		# Build the URL
		url = "http://goog.li/?q=%s" % (hash2)
		
		# Make the request
		response = do_HTTP_request ( url )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<br />cleartext[^:]*: [^<]*<br />', html)
		
		if match:
			return match.group().split(':')[1].strip()[:-6]
		else:
			return None


@timeout(2)
class WHREPORITORY:

	name = 		"Windows Hashes Repository"
	url = 		"http://nediam.com.mx"
	supported_algorithm = [LM, NTLM]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False

	@timeout(2)
	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
			
		hash2 = None
		if ':' in hashvalue:
			if alg == LM:
				hash2 = hashvalue.split(':')[0]
			else:
				hash2 = hashvalue.split(':')[1]
		else:
			hash2 = hashvalue
		
		# Build the URL, parameters and headers
		url = ""
		params = None
		headers = None
		if alg == LM:
			url = "http://nediam.com.mx/winhashes/search_lm_hash.php"
			params = { "lm" : hash2,
				"btn_go" : "Search" }
			headers = { "Referer" : "http://nediam.com.mx/winhashes/search_lm_hash.php" }
		else:
			url = "http://nediam.com.mx/winhashes/search_nt_hash.php"
			params = { "nt" : hash2,
				"btn_go" : "Search" }
			headers = { "Referer" : "http://nediam.com.mx/winhashes/search_nt_hash.php" }
		
		# Make the request
		response = do_HTTP_request ( url, params, headers )
		
		# Analyze the response
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<tr><td align="right">PASSWORD</td><td>[^<]*</td></tr>', html)
		
		if match:
			return match.group().split(':')[1]
		else:
			return None

CRAKERS = [SCHWETT,NETMD5CRACK,BENRAMSEY,GROMWEB,HASHCRACKING,VICTOROV,THEKAINE,TMTO,REDNOIZE,MD5_DB,MD5PASS,MD5DECRYPTION,MD5CRACK,MD5ONLINE,MD5_DECRYPTER,AUTHSECUMD5,HASHCRACK,OPHCRACK,C0LLISION,CMD5,AUTHSECUCISCO7,CACIN,IBEAST,PASSWORD_DECRYPT,BIGTRAPEZE,HASHCHECKER,MD5HASHCRACKER,PASSCRACKING,ASKCHECK,FOX21,NICENAMECREW,JOOMLAAA,MD5_LOOKUP,SHA1_LOOKUP,SHA256_LOOKUP,RIPEMD160_LOOKUP,MD5_COM_CN,DIGITALSUN,DRASEN,MD5_NET,MD5HOOD,STRINGFUNCTION,XANADREL,SANS,BOKEHMAN,GOOG_LI,WHREPORITORY]

@timeout(2)
def configureCookieProcessor (cookiefile='/tmp/searchmyhash.cookie'):
	'''Set a Cookie Handler to accept cookies from the different Web sites.
	
	@param cookiefile Path of the cookie store.'''
	
	cookieHandler = LWPCookieJar()
	if cookieHandler is not None:
		if path.isfile (cookiefile):
			cookieHandler.load (cookiefile)
			
		opener = urllib2.build_opener ( urllib2.HTTPCookieProcessor(cookieHandler) )
		urllib2.install_opener (opener)


@timeout(2)
def do_HTTP_request (url, params={}, httpheaders={}):
	'''
	Send a GET or POST HTTP Request.
	@return: HTTP Response
	'''

	data = {}
	request = None
	
	# If there is parameters, they are been encoded
	if params:
		data = urlencode(params)

		request = urllib2.Request ( url, data, headers=httpheaders )
	else:
		request = urllib2.Request ( url, headers=httpheaders )
		
	# Send the request
	try:
		response = urllib2.urlopen (request)
	except:
		return ""
	
	return response

@timeout(2)
def crackHash (algorithm, hashvalue=None, hashfile=None):
	tmp = ""
	tmp2 = ""
	"""Crack a hash or all the hashes of a file.
	
	@param alg Algorithm of the hash (MD5, SHA1...).
	@param hashvalue Hash value to be cracked.
	@param hashfile Path of the hash file.
	@return If the hash has been cracked or not."""
	
	global CRAKERS
	
	# Cracked hashes will be stored here
	crackedhashes = []
	
	# Is the hash cracked?
	cracked = False
	
	# Only one of the two possible inputs can be setted.
	if (not hashvalue and not hashfile) or (hashvalue and hashfile):
		return False
	
	# hashestocrack depends on the input value
	hashestocrack = None
	if hashvalue:
		hashestocrack = [ hashvalue ]
	else:
		try:
			hashestocrack = open (hashfile, "r")
		except:
			print "\nIt is not possible to read input file (%s)\n" % (hashfile)
			return cracked
	
	
	# Try to crack all the hashes...
	for activehash in hashestocrack:
		hashresults = []
		
		# Standarize the hash
		activehash = activehash.strip()
		if algorithm not in [JUNIPER, LDAP_MD5, LDAP_SHA1]:
			activehash = activehash.lower()
		
		# Initial message
#		print "\nCracking hash: %s\n" % (activehash)

		# Each loop starts for a different start point to try to avoid IP filtered
		begin = randint(0, len(CRAKERS)-1)
		
		for i in range(len(CRAKERS)):
			
			# Select the cracker
			cr = CRAKERS[ (i+begin)%len(CRAKERS) ]()
			
			# Check if the cracker support the algorithm
			if not cr.isSupported ( algorithm ):
				continue
			
			# Analyze the hash
#			print "Analyzing with %s (%s)..." % (cr.name, cr.url)
			
			# Crack the hash
			result = None

			try:
				result = cr.crack ( activehash, algorithm )
			# If it was some trouble, exit
			except:
#				print "Fail"
				return False
			
			# If there is any result...
			cracked = 0
			if result:
				
				# If it is a hashlib supported algorithm...
				if algorithm in [MD4, MD5, SHA1,  SHA224, SHA384, SHA256, SHA512, RIPEMD]:
					# Hash value is calculated to compare with cracker result
					h = hashlib.new (algorithm)
					h.update (result)
					
					# If the calculated hash is the same to cracker result, the result is correct (finish!)
					if h.hexdigest() == activehash:
						hashresults.append (result)
						cracked = 2
				
				# If it is a half-supported hashlib algorithm
				elif algorithm in [LDAP_MD5, LDAP_SHA1]:
					alg = algorithm.split('_')[1]
					ahash =  decodestring ( activehash.split('}')[1] )
					
					# Hash value is calculated to compare with cracker result
					h = hashlib.new (alg)
					h.update (result)
					
					# If the calculated hash is the same to cracker result, the result is correct (finish!)
					if h.digest() == ahash:
						hashresults.append (result)
						cracked = 2
				
				# If it is a NTLM hash
				elif algorithm == NTLM or (algorithm == LM and ':' in activehash):
					# NTLM Hash value is calculated to compare with cracker result
					candidate = hashlib.new('md4', result.split()[-1].encode('utf-16le')).hexdigest()
					
					# It's a LM:NTLM combination or a single NTLM hash
					if (':' in activehash and candidate == activehash.split(':')[1]) or (':' not in activehash and candidate == activehash):
						hashresults.append (result)
						cracked = 2
				
				# If it is another algorithm, we search in all the crackers
				else:
					hashresults.append (result)
					cracked = 1
			
			# Had the hash cracked?
			if cracked:
				print "\n***** HASH CRACKED!! *****\nThe original string is: %s\n" % (result)
				# If result was verified, break
				if cracked == 2:
					break
			else:
#				print "... hash not found in %s\n" % (cr.name)
				placehold = 1
		
		
		# Store the result/s for later...
		if hashresults:
			
			# With some hash types, it is possible to have more than one result,
			# Repited results are deleted and a single string is constructed.
			resultlist = []
			for r in hashresults:
				#if r.split()[-1] not in resultlist:
					#resultlist.append (r.split()[-1])
				if r not in resultlist:
					resultlist.append (r)
					
			finalresult = ""
			if len(resultlist) > 1:
				finalresult = ', '.join (resultlist)
			else:
				finalresult = resultlist[0]
			
			# Valid results are stored
			crackedhashes.append ( (activehash, finalresult) )
	
	
	# Loop is finished. File can need to be closed
	if hashfile:
		try:
			hashestocrack.close ()
		except:
			pass
		
	# Show a resume of all the cracked hashes
#	print "\nThe following hashes were cracked:\n----------------------------------\n"
	for hashvalue, result in crackedhashes:
		
#		tmp = str(result.strip().split())
		print result
		tmp = "".join ("%s -> %s" % (hashvalue, result.strip()) for hashvalue, result in crackedhashes)
		tmp2 = " Found : "+ tmp
		global allinone
		allinone += tmp2 + " in algo "+ algorithm +"\n"
	print
	
	return cracked

def writehash(mode,alg,hashv,allinone,cntcrck,lnhash):
	if mode == 1:
		a = "======================================"
		b = "Trying to find %s hashes" % alg
		c = "Current Hash :",hashv
		if showhashtweet != 1 and showhashtweet2 !=1 :
			d = "Searching at %d / %d" % (cntcrck,lnhash)
		if showhashtweet == 1 or showhashtweet2 == 1:
			d = "Searching in tweet %d / %d" % (cntcrck,counter-1)
		e = "Hashes found so far :"
		f = "".join(item for item in str(allinone))
		tmp = str(a) +"/n"+ str(b) +"/n"+ str(c) +"/n"+ str(d) + "/n" + str(e) + "/n" + str(f) + "/n"
		hshresult = str(tmp)
	
		if showhashtweet == 1 :
        		file = open(pathhash + "HashTweet-Normal" + dated + ".hash", "w")
        		file.write(hshresult)
        		file.close()

		if showhashtweet != 1 and showhashtweet2 !=1 :
        		file = open(pathhash + "Hash-Normal" + dated + ".hash", "w")
        		file.write(hshresult)
        		file.close()		

	if mode == 2:
		a = "======================================"
		b = "Trying to find %s hashes" % alg
		c = "Current Hash :",hashv
		if showhashtweet != 1 and showhashtweet2 !=1 :
			d = "Searching at %d / %d" % (cntcrck,lnhash)
		if showhashtweet == 1 or showhashtweet2 == 1:
			d = "Searching in tweet %d / %d" % (cntcrck,counter-1)
		e = "Hashes found so far :"
		f = str("".join(item for item in str(allinone)))
		tmp = str(a) +"/n"+ str(b) +"/n"+ str(c) +"/n"+ str(d) + "/n" + str(e) + "/n" + str(f) + "/n"
		hshresult = str(tmp)

		if showhashtweet2 == 1:
        		file = open(pathhash2 + "HashtTweet-Twitter-Order" + dated + ".hash", "w")
        		file.write(hshresult)
        		file.close()

		if showhashtweet != 1 and showhashtweet2 !=1 :
        		file = open(pathhash2 + "Hash-Twitter-Order" + dated + ".hash", "w")
        		file.write(hshresult)
        		file.close()




def searchHash (hashvalue):
	'''Google the hash value looking for any result which could give some clue...
	
	@param hashvalue The hash is been looking for.'''
	
	start = 0
	finished = False
	results = []
	
	sys.stdout.write("\nThe hash wasn't found in any database. Maybe Google has any idea...\nLooking for results...")
	sys.stdout.flush()
	
	while not finished:
		
		sys.stdout.write('.')
		sys.stdout.flush()
	
		# Build the URL
		url = "http://www.google.com/search?hl=en&q=%s&filter=0" % (hashvalue)
		if start:
			url += "&start=%d" % (start)
			
		# Build the Headers with a random User-Agent
		headers = { "User-Agent" : USER_AGENTS[randint(0, len(USER_AGENTS))-1] }
		
		# Send the request
		response = do_HTTP_request ( url, httpheaders=headers )
		
		# Extract the results ...
		html = None
		if response:
			html = response.read()
		else:
			continue
			
		resultlist = findall (r'<a href="[^"]*?" class=l', html)
		
		# ... saving only new ones
		new = False
		for r in resultlist:
			url_r = r.split('"')[1]
			
			if not url_r in results:
				results.append (url_r)
				new = True
		
		start += len(resultlist)
		
		# If there is no a new result, finish
		if not new:
			finished = True
		
	
	# Show the results
	if results:
		print "\n\nGoogle has some results. Maybe you would like to check them manually:\n"
		
		results.sort()
		for r in results:
			print "  *> %s" % (r)
		print
	
	else:
		print "\n\nGoogle doesn't have any result. Sorry!\n"

def hash2hash(dathash,countertwt):
  countercrack = 0
  time.sleep(2)
  
  if showhashtweet == 0 and showhashtweet2 == 0:
	data = [dathash[x:x+32] for x in range(0,len(dathash),1)]
	for sample in data: 
	    countercrack = countercrack + 1	
	    if showmd5only != 1:
	      for algo in listalgo:
		
		###################################################
		# Load input parameters
		algorithm = algo
		hashvalue = sample
		hashfile  = None
		googlesearch = False
		
		###################################################
		# Configure the Cookie Handler
		configureCookieProcessor()
		
		# Initialize PRNG seed
		seed()
		
		cracked = 0
		
		
		###################################################	
		# Crack the hash/es
		print ""
		print "======================================"
		print "Trying to find %s hashes" % algorithm
		print "Current Hash :",hashvalue
		if showhashtweet != 1 and showhashtweet2 !=1 :
			print "Searching at %d / %d" % (countercrack,len(dathash))
		if showhashtweet == 1 or showhashtweet2 == 1:
			print "Searching in tweet %d / %d" % (countercrack,counter-1)
		print "Hashes found so far :"
		print "======================================"
		print allinone
		print "======================================"
		print "Tried to find %s hashes" % algorithm
		print "Hash used :",hashvalue
		if showhashtweet != 1 and showhashtweet2 !=1 :
			print "Searched at %d / %d" % (countercrack,len(dathash))
		if showhashtweet == 1 or showhashtweet2 == 1:
			print "Searched in tweet %d / %d" % (countercrack,counter-1)
		print "======================================"
		print ""

		writehash(1,algorithm,hashvalue,allinone,countercrack,len(dathash))
		cracked = crackHash (algorithm, hashvalue, hashfile)
		time.sleep(3)






  if showhashtweet == 1 or showhashtweet2 == 1:
	data = dathash
    		
    	if showmd5only != 1:
	      for algo in listalgo:
		
		###################################################
		# Load input parameters
		algorithm = algo
		hashvalue = data
		hashfile  = None
		googlesearch = False
		
		###################################################
		# Configure the Cookie Handler
		configureCookieProcessor()
		
		# Initialize PRNG seed
		seed()
		
		cracked = 0
		
		
		###################################################
		# Crack the hash/es
		print ""
		print "======================================"
		print "Trying to find %s hashes" % algorithm
		print "Current Hash :",hashvalue
		if showhashtweet != 1 and showhashtweet2 !=1 :
			print "Searching at %d / %d" % (countertwt,len(dathash))
		if showhashtweet == 1 or showhashtweet2 == 1:
			print "Searching in tweet %d / %d" % (countertwt,counter-1)
		print "Hashes found so far :"
		print "======================================"
		print allinone
		print "======================================"
		print "Tried to find %s hashes" % algorithm
		print "Hash used :",hashvalue
		if showhashtweet != 1 and showhashtweet2 !=1 :
			print "Searched at %d / %d" % (countertwt,len(dathash))
		if showhashtweet == 1 or showhashtweet2 == 1:
			print "Searched in tweet %d / %d" % (countertwt,counter-1)
		print "======================================"
		print ""
		writehash(2,algorithm,hashvalue,allinone,countercrack,len(dathash))
		cracked = crackHash (algorithm, hashvalue, hashfile)
		time.sleep(3)
		
		###################################################
		# Look for the hash in Google if it was not cracked
		if not cracked and googlesearch and not hashfile:
			searchHash (hashvalue)
		
		
		
	if showmd5only == 1:
	
		###################################################
		# Load input parameters
		algorithm = "md5"
		hashvalue = dathash
		hashfile  = None
		googlesearch = False
		
		###################################################
		# Configure the Cookie Handler
		configureCookieProcessor()
		
		# Initialize PRNG seed
		seed()
		
		cracked = 0
		countercrack = countercrack + 1
		
		###################################################
		# Crack the hash/es
		print ""
		print "======================================"
		print "Trying to find %s hashes" % algorithm
		print "Current Hash :",hashvalue
		if showhashtweet != 1 and showhashtweet2 != 1:
			print "Searching at %d / %d" % (countertwt,len(dathash))
		if showhashtweet == 1 or showhashtweet2 == 1:
			print "Searching in tweet %d / %d" % (countertwt,counter-1)
		print "Hashes found so far :"
		print "======================================"
		print allinone
		print "======================================"
		print "Tried to find %s hashes" % algorithm
		print "Hash used :",hashvalue
		if showhashtweet != 1 and showhashtweet2 !=1 :
			print "Searched at %d / %d" % (countertwt,len(dathash))
		if showhashtweet == 1 or showhashtweet2 == 1:
			print "Searched in tweet %d / %d" % (countertwt,counter-1)
		print "======================================"
		print ""


		if showhashtweet == 1 or showhexa == 1 or showuni == 1:
			writehash(1,algorithm,hashvalue,allinone,countercrack,len(dathash))
		if showhashtweet2 == 1 or showhexa2 == 1 or showuni2 == 1:
			writehash(2,algorithm,hashvalue,allinone,countercrack,len(dathash))		
		cracked = crackHash (algorithm, hashvalue, hashfile)
		time.sleep(3)
		
		###################################################
		# Look for the hash in Google if it was not cracked
		if not cracked and googlesearch and not hashfile:
			searchHash (hashvalue)



def rcc(removecontrolchar):
    return "".join(ch for ch in removecontrolchar if unicodedata.category(ch)[0]!="C")

class AlarmException(Exception):
    pass

def alarmHandler(signum, frame):
    raise AlarmException

def pressenter(enable,prompt='Press Enter To Continue or wait 120 sec:', timeout=120):

    if enable == 1:
    	signal.signal(signal.SIGALRM, alarmHandler)
    	signal.alarm(timeout)
    	try:
    	    text = raw_input(prompt)
    	    signal.alarm(0)
    	    return text
    	except AlarmException:
    	    print '\nPrompt timeout. Continuing...'
    	signal.signal(signal.SIGALRM, signal.SIG_IGN)
    	return ''

def counterstr23(position,maxpos,nbrtst):
        print 'BinTest %d (edit Settings.py to disable ) : {0} /%s \r'.format(position) % (nbrtst,maxpos),



def binblockdef():

        print ""
        print "======================================"
        print "All tweets in Binary joined together :"
        print "======================================"
        print ""
        pressenter(showpressenter)
        print BinaryBlock
        
        file = open(pathbin + "bin-" + dated + ".bin", "a")
        file.write(BinaryBlock)
        file.close()
        print ""

def binblockdef2():

        print ""
        print "======================================================"
        print "All tweets in Binary joined together (Twitter-Order) :"
        print "======================================================"
        print ""
        pressenter(showpressenter)
        print BinaryBlock2

        file = open(pathbin2 + "binreversed-" + dated + ".bin", "a")
        file.write(BinaryBlock2)
        file.close()

        print ""



def hexadef():


        print ""
        print "==================================================="
        print "Binary tweets to ascii (look like hexadecimale..) :"
        print "==================================================="
        print ""
        pressenter(showpressenter)
        print HexaBlock

        file = open(pathhexa + "hexa-" + dated + ".hex", "a")
        file.write(HexaBlock)
        file.close()
        print ""
        global rainbowhexa
        rainbowhexa = pathhexa + "hexa-" + dated + ".hex"


def hexadef2():

        print ""
        print "=================================================================="
        print "Binary tweets to ascii (look like hexadecimale..) (Twitter-Order):"
        print "=================================================================="
        print ""
        pressenter(showpressenter)
        print HexaBlock2


        file = open(pathhexa2 + "hexaReversed-" + dated + ".hex", "a")
        file.write(HexaBlock2)
        file.close()
        print ""
	global rainbowhexa2
	rainbowhexa2 = pathhexa2 + "hexaReversed-" + dated + ".hex"




def unidef():

        print ""
        print "======================================"
        print "Convert Hexadecimal result to Unicode:"
        print "======================================"
        print ""
        pressenter(showpressenter)
        HexUni = ''.join(chr(int(HexaBlock[i:i+2], 16)) for i in range(0, len(HexaBlock), 2))
        print HexUni

        file = open(pathuni + "unicode-" + dated + ".uni", "ab")
        file.write(HexUni)
        file.close()
	if simple != 1 and bothsimple != 1:

	        print ""
	        print ""
	        print "========================================================="
	        print "Removing character controls from Unicode:"
	        print "========================================================="
	        print ""
		pressenter(showpressenter)
	        try:
				print ""
	                        print rcc(HexUni.decode("utf-8",errors='ignore'))
				print ""
	        except:
				print ""
	                        print "failed to decoding"
	                        print ""
	
	        if showreplace == 1:
	                                        print ""
	                                        print "==================================================="
	                                        print "Replace Unicode char by its closest equivalent :"
	                                        print "==================================================="
	                                        pressenter(showpressenter)
	                                        try:
	                                                print unidecode(rcc(HexUni.decode("ascii",errors='replace')))
	                                        except:
	                        			print ""
	                        			print "failed to decoding"
	                        			print ""
	                                        print ""


        if showchardet == 1:
                guess(HexUni,1)
	if showftfy == 1:
		guess(HexUni,2)
        if showencoding == 1:
                coding(HexUni,1,uniname)
	if showmatrix == 1:
		matrix(HexUni,100,100)		

def unidef2():


        print ""
        print "========================================================="
        print "Converting Hexadecimal result to Unicode (Twitter-Order):"
        print "========================================================="
        print ""
        pressenter(showpressenter)
        HexUni2 = ''.join(chr(int(HexaBlock2[i:i+2], 16)) for i in range(0, len(HexaBlock2), 2))
        print HexUni2

        file = open(pathuni2 + "unicodeReversed-" + dated + ".uni", "ab")
        file.write(HexUni2)
        file.close()
	if simple2 != 1 and bothsimple != 1:

	        print ""
	        print ""
	        print "========================================================="
	        print "Removing character controls from Unicode (Twitter-Order):"
	        print "========================================================="
	        print ""
		pressenter(showpressenter)
	        try:
				print ""
	                        print rcc(HexUni2.decode("utf-8",errors='ignore'))
				print ""
	        except:
				print ""
	                        print "failed to decoding"
	                        print ""
	
	        if showreplace2 == 1:
	                                        print ""
	                                        print "==================================================="
	                                        print "Replace Unicode char by its closest equivalent (Twitter-Order):"
	                                        print "==================================================="
	                                        pressenter(showpressenter)
	                                        try:
	                                                print unidecode(rcc(HexUni2.decode("ascii",errors='replace')))
	                                        except:
	                                                print ""
	                                                print "failed to decoding"
	                                                print ""
	                                        print ""

        if showchardet == 1:
                guess(HexUni2,1)
	if showftfy == 1:
		guess(HexUni2,2)
	if showencoding2 == 1:
		coding(HexUni2,2,uniname2)
	if showmatrix == 1:
		matrix(HexUni2,100,100)




def bintestdecode(binary,mode):
  addone = ""
  savebin = binary
  if mode == 1: 
	for count in range(4):
		if len(addone) > 4:
			addone = ""
 		addone += str("1")
        	BinTest = addone + savebin
                decode = ""
                tmp = ""
                for i in range(len(BinTest)):
                        tmp += BinTest[i]
                        z = i
                        l = len(BinTest)
                        counterstr23(z,l,count)

                        if i % 8 == 7:
                                tmp += ","
                for binary in tmp.split(",")[:-1]:
                    decimal = int(binary, 2)
                    if decimal > 255:
                         print("can't convert " + binary)
                         continue
                    decode += chr(decimal)
		istr = count
		istr = str(istr)
                file = open(pathbintest + "test-" + istr +"-"+ dated + ".bin", "ab")
                file.write(decode)
                file.close()
		print ""
                print ""
                print "##############"
                print "Bin test %s :" % istr
                print "##############"
		print decode
		if showmagicnumber == 1:
			print ""
			print "##########################################"
                	print "Trying to find magic number in BinTest %s" % istr
			print "##########################################"
    			bintestmagic = pathbintest + "test-" + istr +"-"+ dated + ".bin"
                	fname = "Magic-Number-Bintest-"+istr+"-"
                	findmagicnumber(bintestmagic,pathbintest,dated,fname)
                	print ""
		if showhdcp == 1:

			print "#############################################"
	                print "trying to find hdcp master key in Bintest %s" % istr
			print "#############################################"
	                fname = "hdcpMaster-BinTest-"+istr+"-"
	                findhdcp(bintestmagic,pathbintest,dated,fname)
			print ""
		Bintestname = "Bin Test " + istr
		if showchardet == 1:
			guess(decode,1)
		if showftfy == 1:
			guess(decode,2)

		if showencoding == 1:
			print ""
			coding(decode,3,Bintestname)


  addone =""
  if mode == 2:
	for count in range(4):
		if len(addone) > 4:
			addone = ""
 		addone += str("1")
        	BinTest = addone + savebin
                decode = ""
                tmp = ""
                for i in range(len(BinTest)):
                        tmp += BinTest[i]
                        z = i
                        l = len(BinTest)
                        counterstr23(z,l,count)
                        if i % 8 == 7:
                                tmp += ","
                for binary in tmp.split(",")[:-1]:
                    decimal = int(binary, 2)
                    if decimal > 255:
                         print("can't convert " + binary)
                         continue
                    decode += chr(decimal)
		istr = count
		istr = str(istr)
                file = open(pathbintest2 + "testReversed-" + istr +"-"+ dated + ".bin", "ab")
                file.write(decode)
                file.close()
		print ""
                print ""
                print "##############"
                print "Bin test %s :" % istr
                print "##############"
		print decode
		print ""
		
		print "##########################################################"
                print "Trying to find magic number in BinTest %s (Twitter-Order)" % istr
		print "##########################################################"
		print ""
                bintestmagic2 = pathbintest2 + "testReversed-"+ istr +"-"+ dated + ".bin"
                fname = "Magic-Number-Bintestreversed-"+ istr +"-"
                findmagicnumber(bintestmagic2,pathbintest2,dated,fname)
		print ""
		print "#############################################################"
               	print "trying to find hdcp master key in BinTest %s (Twitter-Order)" % istr
		print "#############################################################"
                fname = "hdcpMaster-BinTestreversed-" + istr +"-"
                findhdcp(bintestmagic2,pathbintest2,dated,fname)
		print ""
		Bintestname = "Bin Test " + istr + " (Twitter-Order)"

		if showchardet == 1:
			guess(decode,1)
		if showftfy == 1:
			guess(decode,2)

		if showencoding2 == 1:
			coding(decode,4,Bintestname)


def hexatestdecode(HX,mode):

  if mode == 1:
	global HexaTestDebut
	HexaTestDebut = "fffff" + HX
        print ""
	if showhexa == 1:

		print "######################################"
        	print "Add FFFFFF before Hexadecimal result :"
        	print "######################################"
        	print ""

        	pressenter(showpressenter)
        	print HexaTestDebut
        	print ""


        print ""
        print "###########################################"
        print "Converting FFFFF + Hexadecimal to unicode :"
        print "###########################################"
        print ""

        pressenter(showpressenter)
        HexTestUni = ''.join(chr(int(HexaTestDebut[i:i+2], 16)) for i in range(0, len(HexaTestDebut), 2))
        print HexTestUni
        print ""

        file = open(pathhexatest + "HexTestunicodedebut-" + dated + ".uni", "ab")
        file.write(HexTestUni)
        file.close()

	if showhexa == 1:

	        file = open(pathhexatest2 + "hexatestdebut-" + dated + ".hex", "a")
	        file.write(HexaTestDebut)
	        file.close()
	        print ""

        print ""
        print ""
        print "========================================================="
        print "Removing character controls from Hexatest:"
        print "========================================================="
        print ""
        pressenter(showpressenter)
        try:
                        print ""
                        print rcc(HexTestUni.decode("utf-8",errors='ignore'))
                        print ""
        except:
                        print ""
                        print "failed to decoding"
                        print ""

        if showreplace == 1:
                                        print ""
                                        print "==================================================="
                                        print "Replace Unicode char by its closest equivalent :"
                                        print "==================================================="
                                        pressenter(showpressenter)
                                        try:
                                                print unidecode(rcc(HexTestUni.decode("ascii",errors='replace')))
                                        except:
                                                print ""
                                                print "failed to decoding"
                                                print ""
                                        print ""





	if showchardet == 1:
		guess(HexTestUni,1)
	if showftfy == 1:
		guess(HexTestUni,2)
	if showreplace or showreplace2 and showencoding == 1:
                coding(HexTestUni,1,hexatestname)
	if showhash == 1:
		print "============================"
		print "HexaTest normal order"
		print "============================"
		pressenter(showpressenter)
		hash2hash(HexTestDebut,counterhash)
	


		




  if mode == 2:
	global HexaTestDebut2
        HexaTestDebut2 = "fffff" + HX
	if showhexa2 == 1:

	        print "#####################################################"
	        print "Add FFFFFF before Hexadecimal result (Twitter-Order):"
	        print "#####################################################"
	        print ""
	        pressenter(showpressenter)
	        print HexaTestDebut2
	        print ""
	
        print "###########################################################"
        print "Converting FFFFF + Hexadecimal to unicode (Twitter-Order):"
        print "###########################################################"
        HexTestUni3 = ''.join(chr(int(HexaTestDebut2[i:i+2], 16)) for i in range(0, len(HexaTestDebut2), 2))
        print ""
        pressenter(showpressenter)
        print HexTestUni3
        print ""

        file = open(pathhexatestreversed + "HexTestunicodedebutReversed-" + dated + ".uni", "ab")
        file.write(HexTestUni3)
        file.close()
	if showhexa2 == 1:

	        file = open(pathhexatestreversed2 + "hexatestdebutReversed-" + dated + ".hex", "a")
	        file.write(HexaTestDebut2)
	        file.close()
	        print ""

        print ""
        print ""
        print "========================================================="
        print "Removing character controls from Hexatest (Twitter-Order):"
        print "========================================================="
        print ""
        pressenter(showpressenter)
        try:
                        print ""
                        print rcc(HexTestUni3.decode("utf-8",errors='ignore'))
                        print ""
        except:
                        print ""
                        print "failed to decoding"
                        print ""


        if showreplace2 == 1:
                                        print ""
                                        print "==================================================="
                                        print "Replace Unicode char by its closest equivalent (Twitter-Order):"
                                        print "==================================================="
                                        pressenter(showpressenter)
                                        try:
                                                print unidecode(rcc(HexTestUni3.decode("ascii",errors='replace')))
                                        except:
                                                print ""
                                                print "failed to decoding"
                                                print ""
                                        print ""



	if showchardet == 1:
		guess(HexTestUni3,1)
	if showftfy == 1:
		guess(HexTestUni3,2)
        if showreplace or showreplace2 == 1 and showencoding2 == 1:
                coding(HexTestUni3,2,hexatestname2)
	if showhash == 1:
		print "============================"
		print "HexaTest Twitter-Order"
		print "============================"
		pressenter(showpressenter)
		hash2hash(HexaTestDebut2,counterhash)

def bindecode(binary,mode):
    if mode == 1:
	bintweet = binary
        decode = "" 
        tmp = ""

        for i in range(len(bintweet)):
        	tmp += bintweet[i]
                if i % 8 == 7:
                	tmp += ","


        for binary in tmp.split(",")[:-1]:
        	decimal = int(binary, 2)
                if decimal > 255:
                	print("can't convert " + binary)
                        continue
                decode += chr(decimal)
	return decode

    if mode == 2:

	bintweet = binary
        decode = "" 
        tmp = ""

        for i in range(len(bintweet)):
        	tmp += bintweet[i]
                if i % 8 == 7:
                	tmp += ","


        for binary in tmp.split(",")[:-1]:
        	decimal = int(binary, 2)
                if decimal > 255:
                	print("can't convert " + binary)
                        continue
                decode += chr(decimal)
	
	ListHexaBlock.append(decode)

    if mode == 3:

	bintweet = binary
        decode = "" 
        tmp = ""

        for i in range(len(bintweet)):
        	tmp += bintweet[i]
                if i % 8 == 7:
                	tmp += ","


        for binary in tmp.split(",")[:-1]:
        	decimal = int(binary, 2)
                if decimal > 255:
                	print("can't convert " + binary)
                        continue
                decode += chr(decimal)
	ListHexaBlock2.append(decode)




def magicdef():

        from FindMagicNumber import countermagic
	magiccounterfull = 0

        if showuni == 1:
                print ""
                print "======================================"
                print "Trying to find magic number in Unicode"
                print "======================================"
                print ""
                pressenter(showpressenter)
                unimagic = pathuni + "unicode-" + dated + ".uni"
                
                fname = "Magic-Number-Unicode-"         
                
                findmagicnumber(unimagic,pathmagic,dated,fname)
        

                magiccounterfull = magiccounterfull + countermagic
                
                print ""

                print "Total number of file signature tested : ",magiccounterfull
                print ""

        if showuni2 == 1:
                print ""
                print "======================================================"
                print "Trying to find magic number in Unicode (Twitter-Order)"
                print "======================================================"
                print ""
                pressenter(showpressenter)
                unimagic2 = pathuni2 + "unicodeReversed-" + dated + ".uni"

                fname = "Magic-Number-Unicode-Reversed-"
                
                findmagicnumber(unimagic2,pathmagic,dated,fname)

                magiccounterfull = magiccounterfull + countermagic
                print ""
                print "Total number of file signature tested : ",magiccounterfull
                print ""
                

        if showhexatest == 1:
                print ""
                print "================================================="
                print "trying to find magic number in modified Unicode "
                print "================================================="
                print ""
                pressenter(showpressenter)
                hexatestmagic = pathhexatest + "HexTestunicodedebut-" + dated + ".uni"          

                fname = "Magic-Number-HexatestMagic-"           
                
                findmagicnumber(hexatestmagic,pathmagic,dated,fname)

                magiccounterfull = magiccounterfull + countermagic
                print ""
                print "Total number of file signature tested : ",magiccounterfull
                print ""

        if showhexatest2 == 1:
                print ""
                print "==============================================================="
                print "Trying to find magic number in modified Unicode (Twitter-Order)"
                print "==============================================================="
                print ""
                pressenter(showpressenter)
                hexatest2magic = pathhexatestreversed + "HexTestunicodedebutReversed-" + dated + ".uni"

                fname = "Magic-Number-HexatestMagic-Reversed-"          
                
                findmagicnumber(hexatest2magic,pathmagic,dated,fname)

                magiccounterfull = magiccounterfull + countermagic
                print ""
                print "Total number of file signature tested : ",magiccounterfull
                print ""
                
        print ""

def hdcpdef():

        if showhexa == 1:
                print ""
                print "============================================="
                print "trying to find hdcp master key in hexa normal"
                print "============================================="
                pressenter(showpressenter)

                hexahdcp = pathhexa + "hexa-" + dated + ".hex"          

                fname = "hdcpMaster-Hexa-"
                
                findhdcp(hexahdcp,pathhexa,dated,fname)



        if showhexa2 == 1:
                print ""
                print "======================================================"
                print "trying to find hdcp master key in hexa (Twitter-Order)"
                print "======================================================"
                pressenter(showpressenter)

                hexa2hdcp = pathhexa2 + "hexaReversed-" + dated + ".hex"

                fname = "hdcpMaster-Hexa2-"             

                findhdcp(hexa2hdcp,pathhexa2,dated,fname)




def guess(data,mode):
	if mode == 1:
		chardt = chardet.detect(data)
        	print "==================================================="
        	print "Chardet Thinks its : ",chardt
        	print "==================================================="
		print ""

	if mode == 2:

		fixtext = ftfy.guess_bytes(data)[1]
		weird = ftfy.badness.sequence_weirdness(unicode(data,errors="ignore"))
	       	print "==================================================="
	        print "Ftfy Thinks its : ",fixtext
		print "Ftfy Says its that weird : ",weird
	        print "==================================================="
	        print ""
                print "==================="
                print "Decoding to %s  :" % fixtext
                print "==================="
                print ""
		pressenter(showpressenter)
		try:
			print rcc(data.decode(fixtext,errors='ignore'))
		except:
			print ""
			print "failed to decode"

		if showreplace == 1 or showreplace2 == 1:

                                print "==================================================="
                                print "Replace %s char by its closest equivalent :" % fixtext
                                print "==================================================="
                                pressenter(showpressenter)
                                try:
                                        print unidecode(rcc(data.decode(fixtext,errors='replace'))).replace('deg',' ').replace('EUR',' ').replace('EU',' ')

                                except:
                                        print ""
                                        print "fail"
                                        print ""


		if showonlycp == 1:


		        for encode in sorted(set(encodings.aliases.aliases.values())):
		          if "cp" in encode :
		                print ""
		                print "==================="
		                print "Decoding to cp~ only :",encode
		                print "==================="
				print ""
				pressenter(showpressenter)
				try:
		                        print rcc(data.decode(encode,errors='ignore'))
		                except:
		                        print "failed to decode"
		                        print ""
		                print "==================================================="
		                print "Replace %s char by its closest equivalent :" % encode
		                print "==================================================="
		                pressenter(showpressenter)
		                try:
		                        print unidecode(rcc(data.decode(encode,errors='replace'))).replace('deg',' ').replace('EUR',' ').replace('EU',' ')

		                except:
					print ""
	        	                print "fail"
		                        print ""


	pressenter(showpressenter)

def coding(hexa,mode,name):
	
        from FindMagicNumber import countermagic
        magiccounterfull = 0

	print ""
	print "==================================================="
	print "Trying all encodings without char control in :"
	print name
	print "==================================================="
	print ""
	pressenter(showpressenter)

	for encode in sorted(set(encodings.aliases.aliases.values())):
	  if not "base64_codec" in encode :
        	print ""
        	print "==================="
        	print "Test : ",name
        	print "Decoding to:",encode
		print "==================="


		pressenter(showpressenter)
        	try:
        		print rcc(hexa.decode(encode,errors='ignore'))
		except:
			print "failed to decode"
			print ""
		if mode == 1:
		 if showencoding == 1:
		   from Settings import pathencode
		   try:
        	        file = codecs.open(pathencode + encode +"-" + dated + "."+ name, "ab", encoding=encode)
        	        file.write(rcc(hexa.decode(encode,errors='ignore')))
        	        file.close()
        	        print ""
			if showmagicnumber == 1 :
                        	print ""
                        	print "======================================================"
                        	print "Trying to find magic number in :",encode
                        	print "======================================================"
                        	print ""
                        	pressenter(showpressenter)
                        	codingpath = pathencode + encode +"-" + dated + "."+ name
                        	fname = "Magic-Number-Encoding-%s"% encode
                       		findmagicnumber(codingpath,pathencode,dated,fname)
                        	magiccounterfull = magiccounterfull + countermagic
                        	print ""
                        	print "Total number of file signature tested : ",magiccounterfull
                        	print ""
		   except:
				print "failed to find magic number in :",encode
				print ""

		if mode == 2:
		 if showencoding2 == 1:
                   from Settings import pathencode2
                   try:
			file = codecs.open(pathencode2 + encode +"-" + dated + "."+ name, "ab",encoding=encode)
        	        file.write(rcc(hexa.decode(encode,errors='ignore')))
        	        file.close()
			if showmagicnumber == 1:
				
                        	print ""
                        	print "======================================================"
                        	print "Trying to find magic number in :",encode
                        	print "======================================================"
                        	print ""
                        	pressenter(showpressenter)
                        	codingpath = pathencode2 + encode +"-" + dated + "."+ name
                        	fname = "Magic-Number-Encoding-%s"% encode
                       		findmagicnumber(codingpath,pathencode2,dated,fname)
                        	magiccounterfull = magiccounterfull + countermagic
                        	print ""
                        	print "Total number of file signature tested : ",magiccounterfull
                        	print ""
                   except:
                                print "failed to find magic number in :",encode
                                print ""
                if mode == 3:
                   from Settings import pathencode2
                   try:
                        file = codecs.open(pathencode3 + encode +"-" + dated + "."+ name, "ab",encoding=encode)
                        file.write(rcc(hexa.decode(encode,errors='ignore')))
                        file.close()
                        if showmagicnumber == 1:
                                
                                print ""
                                print "======================================================"
                                print "Trying to find magic number in :",encode
                                print "======================================================"
                                print ""
                                pressenter(showpressenter)
                                codingpath = pathencode3 + encode +"-" + dated + "."+ name
                                fname = "Magic-Number-Encoding-%s"% encode
                                findmagicnumber(codingpath,pathencode3,dated,fname)
                                magiccounterfull = magiccounterfull + countermagic
                                print ""
                                print "Total number of file signature tested : ",magiccounterfull
                                print ""
                   except:
                                print "failed to find magic number in :",encode
                                print ""
                if mode == 4:
                   from Settings import pathencode4
                   try:
                        file = codecs.open(pathencode4 + encode +"-" + dated + "."+ name, "ab",encoding=encode)
                        file.write(rcc(hexa.decode(encode,errors='ignore')))
                        file.close()
                        if showmagicnumber == 1:
                                
                                print ""
                                print "======================================================"
                                print "Trying to find magic number in :",encode
                                print "======================================================"
                                print ""
                                pressenter(showpressenter)
                                codingpath = pathencode4 + encode +"-" + dated + "."+ name
                                fname = "Magic-Number-Encoding-%s"% encode
                                findmagicnumber(codingpath,pathencode4,dated,fname)
                                magiccounterfull = magiccounterfull + countermagic
                                print ""
                                print "Total number of file signature tested : ",magiccounterfull
                                print ""
                   except:
                                print "failed to find magic number in :",encode
                                print ""



                if showreplace == 1 or showreplace2 == 1 and showencoding == 1 or showencoding2 == 1:
                                        print ""
                                        print "==================================================="
                                        print "Replace %s char by its closest equivalent :" % encode
                                        print "==================================================="
                                        pressenter(showpressenter)
                                        try:
                                                print unidecode(rcc(hexa.decode(encode,errors='replace')))
                                        except:
                                                print "fail"
                                        print ""




def hashdef(counterhash):

	print ""
	print "=============="
	print "Hash Test"
	print "=============="
	print ''
	pressenter(showpressenter)
	

	if showhashtweet != 1 and showhashtweet2 != 1:

		if showuni or showhexa == 1:
			print "============================"
			print "Hexa normal order"
			print "============================"

			pressenter(showpressenter)
			hash2hash(HexaBlock,counterhash)
	
		if showuni2 or showhexa2 == 1:
			print "============================"
			print "Hexa Twitter-Order"
			print "============================"
			pressenter(showpressenter)
			hash2hash(HexaBlock2,counterhash)
	

	if showhashtweet == 1:
		counterhash = 0
		print "============================"
		print "Tweet by Tweet"
		print "============================"
		pressenter(showpressenter)
		

		for item in ListHexaBlock:
				counterhash = counterhash + 1
				hash2hash(item,counterhash)
	if showhashtweet2 == 1:
		counterhash = 0
		print "============================"
		print "Tweet by Tweet Twitter-Order"
		print "============================"
		pressenter(showpressenter)
		

		for item in ListHexaBlock2:
				counterhash = counterhash + 1
				hash2hash(item,counterhash)



def matrix(data,x,y):
  print ""
  print "==================================================="
  print "		     Stop "
  print "		     Hammer Time !"
  print "==================================================="
  pressenter(showpressenter)
  for loop in range(0,1):

     sample = []
     for i in range(0,len(data)):
        onechar = data[i]
        sample.append(onechar)
     
     for i in range(1,2):
            sample.append(str(i))
            sample.append(" "*i)
     for i in range(x):
             string = ''
             for j in range(y): 
                     rnd = random.randrange(len(sample)) 
                     string += sample[rnd]
             for encode in sorted(set(encodings.aliases.aliases.values())):
                try:
			if not "cp" in encode :
                        	print string.decode(encode,errors = "ignore")
                        	time.sleep(0.05) 

                except:
                        placehold = 0
def formattime(TwtTime):
#	print TwtTime
	#Friday May 27 09:08:50 +0000 2016
#	print "Removing +0000"
	TwtTime = TwtTime.replace(" +0000 "," ")
#	print TwtTime
	#Friday May 27 09:20:32 2016
	#Should be 2016-05-27 08:34
#	print "Formating final :"
	TimeFinal = datetime.datetime.strptime(TwtTime,'%a %b %d %H:%M:%S %Y').strftime('%Y-%m-%d %H:%M:%S')
#	print TimeFinal
	return TimeFinal

def rainbowdef(timestamp,output,cntr,total,file2tst,nbrSec):
#	print "\n\n\n\n\n\n\n\n\n\n\n\n"
	bashCommand = "./hashboard.sh " + str(timestamp) + " "+ str(output) +" "+ str(cntr) +" "+ str(total)+" "+ str(file2tst)+" "+ str(nbrSec)
	
	process = subprocess.Popen(bashCommand.split())
	output = process.communicate()[0]

#def doublerainbow(hashline,textline,type,dest):

#def overtherainbow


##some vars

orig_stdout = sys.stdout
allinone = ""
counterhash = 0
lastweet = "meoow" ##Check if the tweet is not the same as the previous one
BinaryBlock = "" ## All binary tweets joined together
ListHexaBlock = []  
HexaBlock = ""  ## Binary tweet to ascii (look like hexadecimal) 
ListHexaBlock2 = []
BinaryBlock2 = "" ## All binary tweets joined together in Twitter-Order)
HexaBlock2 = "" ## The result in ascii.
OldTweetTimestamp = []
hexatestname = "Hexa Test"
hexatestname2 = "Hexa Test (Twitter-Order)"
uniname = "Unicode"
uniname2 = "Unicode (Twitter-Order)"



newtweetlist = [] ## tweet list with no identical tweets
cntrainbow = 0
counter2 = 1
counter = 1
pressenter(showpressenter)



############################################# Fight ######################################



if showtime == 1:

	print "##############"
	print datetime.datetime.now()
	print "##############"


lastid = twitter.get_user_timeline(screen_name=User,count=1)

print ""
for twtid in lastid:
	
	print "First Tweet Id : ",twtid['id'] ## Used as a reference to get more than 200 tweets .
	lisid = twtid['id'] 
	lis = [lisid]
	TweetTimestamp = twtid['created_at']
	print "Tweet Timestamp : ",formattime(TweetTimestamp)


print ""
print "Loading tweets please wait"
print ""
for i in range(0, nbrloop):

	user_timeline = twitter.get_user_timeline(screen_name=User, 
    	count=nbrtweet, include_retweets=False, max_id=lis[-1])
    	time.sleep(1) ##rest between api calls


######################################### First loop normal order #####################
#######################################################################################

    	for tweet in user_timeline: ##reading tweets's content

		print 'Tweet number : {0}\r'.format(str(counter)),
		counter = counter +1

		newtweet = tweet['text'] ## Saving current tweet content

		if showbintweet == 1:

			tid = tweet['id'] 
			tcounter = ["%04d" % counter2 for x in range(1)]
			counter2 = counter2 + 1

        		file = open(pathoriginal + "OriginalTweet-" + str(tcounter) + "-Id-" + str(tid) + ".bin", "ab")
        		file.write(newtweet)
        		file.close()

        	lis.append(tweet['id']) ## append tweet id's


		if showlis == 1:

			tid = tweet['id']
                        file = open(pathlis + "List.id", "a")
                        file.write(str(tid) + "\n")
                        file.close()


		BinaryBlock += tweet['text'] 


		if newtweet != lastweet: ## if not identical continue
			lastweet = tweet['text'] ## last tweet = current tweet
			newtweetlist.append(tweet['text']) ##saving tweet list with no identical tweet [will reverse it later]
        		OldTweetTimestamp.append(tweet['created_at']) ## saving tweet s timestamp to use with rainbow table
			binsample = tweet['text'] 
    			HexaBlock += bindecode(binsample,1)
			if showhashtweet == 1:
				bindecode(binsample,2)
			

		else:
			## if last tweet = current tweet continu without convert
			placeholder = 0


for tweet2 in reversed(newtweetlist): ##Tweet order
 
		BinaryBlock2 += tweet2

		binsample = tweet2
		HexaBlock2 += bindecode(binsample,1)
		if showhashtweet2 == 1:
			bindecode(binsample,3)

##
print ""
print "Messing around please wait ..."
print ""

####################################################################################################################
######################################################################################################################
#######################################################################################################################



## time to see what it look like ##

if showbinary == 1:

	binblockdef()
else:

	print "Binary skipped"

if showbinary2 == 1:

	binblockdef2()
else:
	print "Binary (Twitter-Order) skipped"

if showhexa == 1:

	hexadef()
else:
	print "Ascii Result skipped"

if showhexa2 == 1:

	hexadef2()
else:
	print "Ascii Result (Twitter-Order) skipped"

if showuni == 1:

	unidef()
else:
	print "Unicode skipped"

if showuni2 == 1:

	unidef2()
else:
	print "Unicode (Twitter-Order) skipped"

if showhexatest == 1:

	hexatestdecode(HexaBlock,1)
else:
	print "Hexa Test skipped"


if showhexatest2 == 1:

	hexatestdecode(HexaBlock2,2)
else:
	print "Hexa Test (Twitter-Order) skipped"



if showbintest == 1:


        Bdecode = bintestdecode(BinaryBlock,1)
	pressenter(showpressenter)
else:
	print "Binary Test skipped"

if showbintest2 == 1:


	Bdecode = bintestdecode(BinaryBlock2,2)
	pressenter(showpressenter)
else:
	print "Binary Test (Twitter-Order) skipped"

if showmagicnumber == 1:

        magicdef()

else:
	print "Magic Number Test skipped"

if showhdcp == 1:

        hdcpdef()
else:
	print "Hdcp Test skipped"



if showhash == 1:

	hashdef(counterhash)
else:
	print "Hash Test skipped"

if showrainbow == 1:
	print ""
	print "==================="
	print "Rainbow Table Test"
	print "==================="
	print ""
	print ""
	print ""
	print "According to http://md5decryption.com/"
	print ""
	print "5865b6a13daa2f062dea5517f252c21e "
	print ""
	print "Is the md5 of:"
	print ""
	print "2016-04-12;13:23:59 Matthew 11:2    Now when John had heard in the prison the works of Christ, he sent two of his disciples"
	print ""
	print ""
	print "Found 5865b6a13daa2f06 in a previous test results."
	print ""
	print "This Test will create an md5 hashs list mixed with the tweets timestamps and each lines of the Bible." 
	print "Then try to find any hashs in Hexadecimal results."
	print ""
	print "If the tweets from @Pondeboard have the same pattern as the cracked hash from http://md5decryption.com/ .."
	print "And if @Pondeboard use the date and time from his computer as he is creating the md5 hashes ..."
	print "Then The Tweet's Timestamp may differ slightly from the one used by pondeboard."
	print ""
	print "This is my last try ."
	print ""
	print pressenter(showpressenter)
	print ""

        Sec2Test = ''
        while True:
                Sec2Test = raw_input("Please choose amount of Sec you want to test around the Tweet's Timestamp :")
                if Sec2Test.isdigit():
                        break
                else:
                        print("This is not a number .")
                        continue


	if showhexa ==1 and showhexa2 != 1:
		for timesample in OldTweetTimestamp:

			cntrainbow = cntrainbow +1
			finalstamp = formattime(timesample)
			rainbowdef(finalstamp,pathrainbow,cntrainbow,totaltwt,rainbowhexa,Sec2Test)
	if showhexa2 == 1 and showhexa != 1:

                for timesample in reversed(OldTweetTimestamp):

			cntrainbow = cntrainbow +1
                        finalstamp = formattime(timesample)
                        rainbowdef(finalstamp,pathrainbow,cntrainbow,totaltwt,rainbowhexa2,Sec2Test)

	if showhexa2 == 1 and showhexa == 1:
		 
		for timesample in reversed(OldTweetTimestamp):

                        cntrainbow = cntrainbow +1
                        finalstamp = formattime(timesample)
                        rainbowdef(finalstamp,pathrainbow,cntrainbow,totaltwt,rainbowhexa2,Sec2Test)

	
        print "\n\n\n\n\n\n\n\n\n"

else:
	print "Rainbow Table Test skipped"

if showdebug == 1:

	lavoisier = len(HexaBlock2) == len(HexaBlock)
	print "Lavoisier dit : ",lavoisier
	if len(HexaBlock2) > len(HexaBlock):
		print "Loop 2 is longer"
	if len(HexaBlock2) < len(HexaBlock):
		print "loop 1 is longer"
else:
	print "Debug skipped"




#####################################################Debrief##################################################

print ""

if showbintweet == 1:
	print "Wrote all original tweets in :" + "\n",pathoriginal
if showlis == 1:
	print "Wrote tweets id in:"+"\n",pathlis
if showbinary == 1:
        print "Wrote Binary Block in :" + "\n" ,pathbin
if showbinary2 == 1:
        print "Wrote Binary Block reversed in :"+"\n",pathbin2
if showhexa == 1:
        print "Wrote Hexadecimal Block in :"+"\n",pathhexa
if showhexa2 == 1:
        print "Wrote Hexadecimal Block reversed in :"+"\n",pathhexa2
if showuni == 1:
        print "Wrote unicode Block in :"+"\n",pathuni
if showuni2 == 1:
        print "Wrote unicode Block reversed in :"+"\n",pathuni2
if showhexatest == 1:
	print "Wrote hexa Block testing in :"+"\n",pathhexatest
	print "Wrote hexa Block testing in :"+"\n",pathhexatest2
if showhexatest2 == 1:
	print "Wrote hexa Block testing resversed in :"+"\n",pathhexatestreversed
	print "Wrote hexa Block testing resversed in :"+"\n",pathhexatestreversed2
if showmagicnumber == 1:
	print "Wrote Magic Number in :"+"\n",pathmagic
if showhdcp == 1:
	print "Wrote Hdcp key master in :"+"\n",pathhdcp
if showhash == 1:
	print "Wrote Hash Results in : "+"\n",pathhash
if showhashtweet == 1:
	print "Wrote Hash Tweet by Tweet Results in : "+"\n",pathhash
if showhashtweet2 == 1:
	print "Wrote Hash Tweet by Tweet (Twitter-Order )Results in : "+"\n",pathhash
if showrainbow == 1:
	print "Wrote Rainbow Table Test in : "+"\n",pathrainbow
if showbintest == 1:
	print "Wrote bin Block testing in :"+"\n",pathbintest
if showbintest2 == 1:
	print "Wrote reversed bin Block testing in :"+"\n",pathbintest2
if showencoding == 1:
	print "Wrote encoding results in :"+"\n",pathencode
if showencoding2 == 1:
	print "Wrote encoding results reversed in :"+"\n",pathencode2
print ""
print "See you space cowboy ..."
print ""
if showtime == 1:
	print "#######end#######"
	print datetime.datetime.now()
	print "#######end#######"
	print ""

#################################################TheEnd#############################################################
