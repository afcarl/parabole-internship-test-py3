import logging
import os
import pickle
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import math

# Reads and returns the list of files from a directory
def read_directory(mypath):
    current_list_of_files = []

    while True:
        for (_, _, filenames) in os.walk(mypath):
            current_list_of_files = filenames
        logging.info("Reading the directory for the list of file names")
        return current_list_of_files


# Function you will be working with
def creating_subclusters(list_of_terms, name_of_file):

    # I have written it in the main only due to lack of time couldn't clean the code
    # P.S: I started late working on the problem
    pass


# Main function
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
    inp_dir = './input'
    out_dir = './output'
    my_w2v = pickle.load(open( "my_w2v.pickle", "rb" ))
    for _,_,files in os.walk(inp_dir):
        print('reading files')
        for file in files:
            filename = os.path.join(inp_dir,file)
            f = open(filename,'r').read()
            f_list = f.split()
    #         print(f'{len(f_list)} words found in {filename}')
            inp_dir = './input'
            for i,word in enumerate(f_list):
                if i == 0:
    #                 print('word at i = 0')
                    arr = my_w2v[word].reshape(1,-1)
                else:
    #                 print('word i != 0')
                    arr = np.concatenate((arr,my_w2v[word].reshape(1,-1)))
            arr = PCA(n_components=5).fit_transform(arr)
    #         print(arr.shape)
            n_c = int(math.sqrt(len(f_list))/2)
            clf = KMeans(n_clusters=n_c,).fit(arr) #number of clusters !!!
            print(f'Writing to {filename}')
            for j in range(n_c):
                labels = np.array(clf.labels_)
                idx = np.argwhere(labels == j)
                boo = False
                for k in idx:
        #             print(i)
                    with open(os.path.join(out_dir,file),'a') as of:
                        if j == 0 or boo:
                            of.write(f'{f_list[k[0]]} ')
                        else:
                            boo = True
                            of.write(f'\n{f_list[k[0]]} ')


        # End of code