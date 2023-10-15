import pickle

if __name__ == '__main__':
    name = ['sufiyan', 'rehan', 'adnan', 'shibban', 'kashfi', 'shadaf', 'kulsoom']
    file = "pickle.pkl"
    f = open(file, "wb")
    pickle.dump(name, f)
    f.close()
