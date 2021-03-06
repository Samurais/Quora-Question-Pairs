import pickle

def loadGloveModel(gloveFile):
    print "Loading Glove Model..."
    f = open(gloveFile,'r')
    model = {}
    for i, line in enumerate(f):

        if i % 50000 == 0:
            print(i)

        splitLine = line.split()
        word = splitLine[0]
        embedding = [float(val) for val in splitLine[1:]]
        model[word] = embedding

    print "Done.",len(model)," words loaded!"
    return model

model = loadGloveModel('input/glove.txt')

print('Saving model...')
with open('preproc/model_glove_wiki.pkl', 'wb') as output:
    pickle.dump(model, output, pickle.HIGHEST_PROTOCOL)
print('Done.')
