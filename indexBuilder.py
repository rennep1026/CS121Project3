import json
import nltk
import sys
import time

if __name__ == '__main__':
    i = 0
    id2docfreq = {}
    term2id={}
    id2term={}
    doc2termlist = []
    start = time.time()
    while True:
        try:
            f = open("FileDump/"+str(i)+".txt")
        except:
            #print(sys.exc_info()[0])
            break
        jobj = json.load(f)
        x = nltk.tokenize.word_tokenize(jobj['text'].lower())
        doc2termlist.append([])
        for w in x:
            if w not in term2id:
                id2term[len(term2id)] = w
                term2id[w] = len(term2id)
        for w in x:
            doc2termlist[i].append(term2id[w])
            if term2id[w] in id2docfreq:
                if i in id2docfreq[term2id[w]]:
                    id2docfreq[term2id[w]][i] += 1
                else:
                    id2docfreq[term2id[w]][i] = 1
            else:
                id2docfreq[term2id[w]] = {i: 1}
        f.close()
        i+=1

    # TODO: Add tf-idf calculation.
    # tf[termID][docID] = log(1 + id2docfreq[termID][docID]) # log of 1 + the number of times that word appears in that document, or 0 if it does not appear
    # idf[termID][docID] = log(len(doc2termlist) / len(id2docfreq[termID])) # log of number of documents over the number of documents that term appears in

    with open('id2docfreq.json', 'w') as f:
        json.dump(id2docfreq, f)

    with open('id2term.json', 'w') as f:
        json.dump(id2term, f)

    stop = time.time()

    print("Time to run: " + str(stop-start))