import pandas
import sys  
import collections
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

reload(sys)  
sys.setdefaultencoding('utf8')
stop_words = set(stopwords.words('english'))
#result=collections.defaultdict(list)

io = pandas.read_csv('Reviews_min.csv',sep=",",usecols=('ProductId','Text')) 
new = io.Text
mai = []
for line in new:
	result = word_tokenize(line)
	for w in result:
		    if w not in stop_words:
		    	mai.append(w)
	#mai.append(result)
print mai

#filtered_sentence = []

#for w in mai:
 #   if w not in stop_words:
  #      filtered_sentence.append(w)

#print w

