from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("out.csv")
plt.plot(df["elements"], df["bst"], label="BST")
plt.plot(df["elements"], df["avl"], label="AVL")
plt.xlabel("Elements")
plt.ylabel("Level")
plt.title("AVL to BST level")
plt.legend(loc="upper left")
plt.xlim(df["elements"][0],df["elements"].max())
plt.savefig("zadanie2.pdf")