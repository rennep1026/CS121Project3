import json
import nltk
import sys

if __name__ == '__main__':
    i = 0
    id2docfreq = {}
    term2id={}
    id2term={}
    doc2termlist = []
    while i<500:
        try:
            f = open("FileDump/"+str(i)+".txt")
        except:
            print(sys.exc_info()[0])
            break
        jobj = json.load(f)
        x = nltk.tokenize.word_tokenize(jobj['text'].lower())
        doc2termlist.append([])
        for w in x:
            if w not in term2id.keys():
                id2term[len(term2id)] = w
                term2id[w] = len(term2id)
        for w in x:
            doc2termlist[i].append(term2id[w])
            if term2id[w] in id2docfreq.keys():
                if i in id2docfreq[term2id[w]].keys():
                    id2docfreq[term2id[w]][i] += 1
                else:
                    id2docfreq[term2id[w]][i] = 1
            else:
                id2docfreq[term2id[w]] = {i: 1}
        f.close()
        i+=1

    # TODO: Add tf-idf calculation.

    print(json.dumps(id2docfreq))
    print("----------------------")
    print(json.dumps(id2term))

    with open('id2docfreq.json', 'w') as f:
        json.dump(id2docfreq, f)

    with open('id2term.json', 'w') as f:
        json.dump(id2term, f)