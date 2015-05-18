# INDEXER CODE
# By: Ciarra Altoveros and Taylor Penner
# ID's: 33218028 and 21029724

import json
import nltk
import time
import math
import collections





def tfidf(word, doc_id):
    # term frequency / normalize by doc length
    tf = id2docfreq[word_id][doc_id]/ doc2doclength[doc_id]
    
    # number of documents containing the word
    containing = len(id2docfreq[word_id])
    
    # idf: log(total_documents / (1+ n_containing(word_id))
    idf = (math.log(len(doc2doclength) / (1 + containing)))
    
    return tf * idf



if __name__ == '__main__':
    i = 0
    id2docfreq = {}     # term -> document: frequency
    term2id={}          # term -> id
    id2term={}          # id -> term
    doc2termlist = []   # document -> [term,...,term]
    doc2doclength = {}  # doc -> total words in doc
    start = time.time()
    while True:
        try:
            f = open("FileDump/"+str(i)+".txt")
        except:
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
        doc2doclength[i] = len(doc2termlist)
        f.close()
        i+=1

    # TODO: Add tf-idf calculation.
    # tf[termID][docID] = log(1 + id2docfreq[termID][docID]) # log of 1 + the number of times that word appears in that document, or 0 if it does not appear
    # idf[termID][docID] = log(len(doc2termlist) / len(id2docfreq[termID])) # log of number of documents over the number of documents that term appears in
    
    # term-> (document: tf-idf)
    tf_idf = collections.defaultdict(dict)
    # for each term:
    #    for each doc in each term:
    #        store tf-idf score.
    for word_id in id2docfreq:
        for doc_id in id2docfreq[word_id]:
            tf_idf[word_id][doc_id] = tfidf(word_id,doc_id)

    
    with open("index.txt", "w") as f:
        for word_id in tf_idf:
            #This sorts but will look different from json file
#             i = sorted(tf_idf[word_id].items())
            f.write(str(word_id) + ": "+ str(tf_idf.get(word_id)) + "\n")
   
    with open("index.json","w") as f:
        json.dump(tf_idf,f)

    with open('id2docfreq.json', 'w') as f:
        json.dump(id2docfreq, f)

    with open('id2term.json', 'w') as f:
        json.dump(id2term, f)

    stop = time.time()

    
    
    print("1: Number of documents: " + str(len(doc2doclength)))
    
    print("2: Number of [unique] words: " + str(len(id2docfreq)))
    
    print("3: Sample index: See index.txt or index.json ");
    
    print("4: -- TOTAL SIZE (KB) of index on disk -- ")
    #the total size (in KB) of your index on disk
    
    print("5: Time taken to create index: " + str(stop-start))


    
