import re
import porter_algorithm
p = porter_algorithm.PorterStemmer()
f = open ('IRPA1text.txt', 'r')
stop_words_file = open('stop_words.txt', 'r')
stop_words = stop_words_file.read().split()
result = re.sub("[^A-Za-z]"," ",f.read().lower()).split()
stop = filter(lambda x: not(x in stop_words), result) 
stemmed = map(lambda x: p.stem(x, 0, len(x)-1), stop)
solution = open('result.txt', 'w')
solution.write('\n'.join(stemmed))
f.close()
stop_words_file.close()
solution.close()
