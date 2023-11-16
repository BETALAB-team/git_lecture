# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 15:43:03 2023

@author: pratenr82256
"""
import matplotlib.pyplot as plt
import pandas as p
data = p.read_excel("data.xlsx", index_col = 0)

data.mean().plot()
plt.gcf().savefig("stupid_plot.png")

data.plot(kind = "bar")
