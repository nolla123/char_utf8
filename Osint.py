import re,  operator, csv


class osint_utf8:
	busPol = dict()
	politicsPol= dict()
	entPol = dict()
	confPol = dict()
	confCount = dict()
	entCount = dict()
	busCount = dict()
	busCount['total'] = 0
	confCount['total'] = 0
	entCount['total'] = 0
	wcount=dict()
	wcount['total']  = 0
	pcount=dict()
	pcount['total']  = 0
	filePath = ''	
	filePath2 = "politics.txt"
	filePath3  = "entertainment.txt"
	filePath4 = 'business.txt'
	filePath5 = 'conflict.txt'
	freqlist={}



	def setup(self,Fpath):
		self.filePath = Fpath
		self.word_freq_counter(Fpath)
		self.politics_keywords_freq_counter(self.filePath2)
		self.entertainment_keywords_freq_counter(self.filePath3)
		self.conflict_keywords_freq_counter(self.filePath5)
		self.business_keywords_freq_counter(self.filePath4)


	def read_file(self,Fpath):

		f = open(Fpath, 'rb')	
		encF = unicode(f.read(),encoding='utf-8')

		return encF


		
	def read_csv(self,Fpath):

		encF =''
		cvs = open(Fpath,'rb')
		df = csv.reader(cvs)
		for row in df:
			encF = unicode(row[1], encoding='utf-8')
		return encF



	def prepare_list(self,encF,flag):
		#encF = encF.replace()
		if flag == 'w':
			encF = encF.split()
		else:
			#encF = encF.split(',')
			encF = encF.split()
		retVal = []

		for sm in encF:
			sm = sm
			sm = sm.strip('*=-!#:_",')
			sm = sm.strip()
			retVal.append(sm)
		return retVal
	#returns wordcount dict and frequency list dict
	def word_freq_counter(self,wordListfPath):
		wordlist = self.prepare_list(self.read_csv(wordListfPath),'w')
		for wd in wordlist:
			if self.freqlist.has_key(wd):
				self.freqlist[wd]= self.freqlist[wd] + 1
			else:
				self.freqlist[wd]= 1
			self.wcount['total'] = self.wcount['total'] + 1
		return self.freqlist,self.wcount['total']

	def politics_keywords_freq_counter(self,wordListfPath):
		politics = self.prepare_list(self.read_file(wordListfPath),'p')
		for v in politics:
			if self.freqlist.has_key(v):
				self.politicsPol[v] = self.freqlist[v]
				self.pcount['total'] = self.pcount['total'] + self.freqlist[v] 
			else:
				self.politicsPol[v] = 1
				self.pcount['total'] = self.pcount['total'] + 1

		return self.politicsPol,self.pcount['total']

	def entertainment_keywords_freq_counter(self,wordListfPath):
		entertainment = self.prepare_list(self.read_file(wordListfPath),'e') 
		for v in entertainment:
			if self.freqlist.has_key(v):
				self.entPol[v] = self.freqlist[v]

				self.entCount['total'] = self.entCount['total'] + self.freqlist[v]
			else:
				self.entPol[v]=1
				self.entCount['total'] = self.entCount['total'] + 1
		return self.entPol,self.entCount['total']


	def conflict_keywords_freq_counter(self,wordListfPath):
		conflict = self.prepare_list(self.read_file(wordListfPath),'c')
		for v in conflict:
			if self.freqlist.has_key(v):
				self.confPol[v] = self.freqlist[v]

				self.confCount['total'] = self.confCount['total'] + self.freqlist[v]
			else:
				self.confPol[v]=1
				self.confCount['total'] = self.confCount['total'] + 1
		return self.confPol,self.confCount['total']
		

	def business_keywords_freq_counter(self,wordListfPath):
		business = self.prepare_list(self.read_file(wordListfPath),'b')
		
		for v in business:
			
			if self.freqlist.has_key(v):
				self.busPol[v] = self.freqlist[v]

				self.busCount['total'] = self.busCount['total'] + self.freqlist[v]
			else:
				self.busPol[v]=1
				self.busCount['total'] = self.busCount['total'] + 1
		return self.busPol,self.busCount['total']

	def report(self):
		'''
		print 'Entertainment Keywords Percentage % :- ' + str(float(self.entCount['total'])/float(self.wcount['total'])) 
		print 'Politcs Keywords Percentage % :- ' + str(float(self.pcount['total'])/float(self.wcount['total']))
		print 'Conflict Keywords Percentage % :- ' + str(float(self.confCount['total'])/float(self.wcount['total']))
		print 'Business Keywords Percentage % :- ' + str(float(self.busCount['total'])/float(self.wcount['total']))
		
		print 'Total Word Count :  ' + str(self.wcount['total'])	
		'''
		top = []
		cat = 0
		top.append(self.pcount['total'])
		top.append(self.entCount['total'])
		top.append(self.confCount['total'])
		top.append(self.busCount['total'])
		big = max(top)
		doubles = dict()
		for x in range(len(top)):
			if big == top[x]:
				doubles[x] = big
				cat = x
		if len(doubles) == 1:

			if cat == 0:
				print "Its Politics"
			elif cat == 1:
				print "Its Entertainment"
			elif cat == 2:
				print "Its Conflict"
			else: 
				print "Its Business"
		else: 
			for y in doubles:
				if y == 0:
					print "Its Politics"
				elif y == 1:
					print "Its Entertainment"
				elif y == 2:
					print "Its Conflict"
				else: 
					print "Its Business"




