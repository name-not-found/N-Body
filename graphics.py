#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def plotting2D(fig, ax, time, y1, titulo, filename, caption, xlabel, ylabel):
	ax.plot(time, y1, label=caption)
	ax.set(xlabel=xlabel, ylabel=ylabel,  title=titulo)
	ax.grid()

def plotting3D(fig, ax, y, i):
	c = ["g", "r", "b", "c", "m", "y", "k", "w", "0.75"]
	m = ["o", "*", "d", ".", "v", "p", "P", "h", "D"]
	for point in y:
		ax.scatter(point[0], point[1], point[2], marker=m[i%len(m)], c=c[i%len(c)])

def plotting2D_multiple(fig, ax, y, i):
	c = ["g", "r", "b", "c", "m", "y", "k", "w", "0.75"]
	m = ["o", "*", "d", ".", "v", "p", "P", "h", "D"]
	for point in y:
		ax.scatter(point[0], point[1], marker=m[i%len(m)], c=c[i%len(c)])
