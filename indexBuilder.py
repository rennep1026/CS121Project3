import json
import nltk
import sys

if __name__ == '__main__':
    i = 0
    id2docfreq = {}
    term2id={}
    while i<10:
        try:
            f = open("FileDump/"+str(i)+".txt")
        except:
            print(sys.exc_info()[0])
            break
        jobj = json.load(f)
        x = nltk.tokenize.word_tokenize(jobj['text'])
        for w in x:
            if w not in term2id.keys():
                term2id[w] = len(term2id)
        for w in x:
            if term2id[w] in id2docfreq.keys():
                if i in id2docfreq[term2id[w]].keys():
                    id2docfreq[term2id[w]][i] += 1
                else:
                    id2docfreq[term2id[w]][i] = 1
            else:
                id2docfreq[term2id[w]] = {i: 1}
        f.close()
        i+=1
    print(str(id2docfreq))