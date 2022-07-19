#
from Read_Save import read_file
def jaccard_sim(a, b):
    # jaccard_sim |aub|-|anb|/|aub|.
    unions_charactor = len(set(a).union(set(b)))
    intersections = len(set(a).intersection(set(b)))
    return float(intersections / unions_charactor)

def jaccard_sim_score(resource, target): #resource:list
    jaccard_sim_score_all = []
    for i in range(len(resource)):
        jaccard_sim_score = jaccard_sim(resource[i], target)  #
        jaccard_sim_score_all.append([float(jaccard_sim_score), resource[i]])
        # print('jaccard_sim_score_all',jaccard_sim_score_all)
    print('jaccard_sim_score_all', jaccard_sim_score_all)
    return jaccard_sim_score_all

read_file_path='NLU.txt'
target='test-100.txt'
data=read_file(read_file_path)
jaccard_sim_score(data, target)


