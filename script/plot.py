import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from causalnex.structure import StructureModel
from IPython.display import Image
from causalnex.plots import plot_structure, NODE_STYLE, EDGE_STYLE

from causalnex.structure.notears import from_pandas

def plot_histogram(df:pd.DataFrame, column:str, color:str)->None:
    plt.figure(figsize=(9, 7))
    sns.displot(data=df, x=column, color=color, kde=True, height=7, aspect=2)
    plt.title(f'Distribution of {column}', size=20, fontweight='bold')
    plt.show()

def plot_pie(data, column, title:str):
  plt.figure(figsize=(12, 7))
  count = data[column].value_counts()
  colors = sns.color_palette('pastel')[0:5]
  plt.pie(count, labels = count.index, colors = colors, autopct='%.0f%%')
  plt.title(title, size=18, fontweight='bold')
  plt.show()

def plot_heatmap(df:pd.DataFrame, title:str, cbar=False)->None:
    plt.figure(figsize=(12, 7))
    sns.heatmap(df, annot=True, cmap='viridis', vmin=0, vmax=1, fmt='.2f', linewidths=.7, cbar=cbar )
    plt.title(title, size=18, fontweight='bold')
    plt.show()

def plot_bar(df:pd.DataFrame, x_col:str, y_col:str, title:str, xlabel:str, ylabel:str, ax)->None:
    plt.figure(figsize=(12, 7))
    sns.barplot(data = df, x=x_col, y=y_col, ax=ax)
    plt.title(title, size=20)
    plt.xticks(rotation=75, fontsize=14)
    plt.yticks( fontsize=14)
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)
    plt.show()

def plot_structure_1(structure_model):
    viz = plot_structure(
    structure_model,
    graph_attributes={"scale": "0.5"},
    all_node_attributes=NODE_STYLE.WEAK,
    all_edge_attributes=EDGE_STYLE.WEAK)
    return viz

def plot_structure_2(structure_model):
    viz = plot_structure(
    structure_model,
    graph_attributes={"scale": "0.5"},
    all_node_attributes=NODE_STYLE.WEAK,
    all_edge_attributes=EDGE_STYLE.WEAK)
    return viz

def plot_structure_3(structure_model):
    structure_model.remove_edges_below_threshold(0.4)
    viz = plot_structure(
    structure_model,
    graph_attributes={"scale": "0.8"},
    all_node_attributes=NODE_STYLE.WEAK,
    all_edge_attributes=EDGE_STYLE.WEAK)
    return viz

def plot_structure_4(structure_model,df,col1:str, col2:str):
    structure_model = from_pandas(df, tabu_edges=[(col1,col2)], w_threshold=0.8)
    viz = plot_structure(
    structure_model,
    graph_attributes={"scale": "0.5"},
    all_node_attributes=NODE_STYLE.WEAK,
    all_edge_attributes=EDGE_STYLE.WEAK)
    return viz
