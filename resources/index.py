import pickle


with open('en_science.csv.gz.pkl', 'rb') as f:
    data = pickle.load(f)
    print data