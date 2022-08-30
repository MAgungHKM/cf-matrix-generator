import numpy  as np
from cf_matrix import make_confusion_matrix


cf_matrix = np.array([[23,  5],
                      [ 3, 30]])

labels = ['True Neg','False Pos','False Neg','True Pos']
categories = ['Zero', 'One']
make_confusion_matrix(cf_matrix, group_names=labels, categories=categories, cmap='binary', title='My Two-class CF Matrix')