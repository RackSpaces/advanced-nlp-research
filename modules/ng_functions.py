#
# Network Graph Helper Functions
#
# The Python Quants GmbH
#
import pandas as pd
import networkx as nx
from pyvis.network import Network

def create_graph(data, labels=False):
    '''Create a NetworkX graph object from a pandas DataFrame.
    '''
    G = nx.DiGraph()
   
    vals = data[['Node1', 'Relation', 'Node2']].values
    G.add_edges_from([(v[0], v[2], {'relation': v[1]}) for v in vals])
   
    if labels:
        vals = data[['Label1', 'Node1', 'Label2', 'Node2']].values
        for v in vals:
            G.node[v[1]]['type'] = v[0]
            G.node[v[3]]['type'] = v[2]
    return G

def plot_graph(graph, background_color='white', 
   