import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

for filename in os.listdir("b"):
	if not filename.startswith('.'):
		img = cv2.imread("b/{}".format(filename),0)
		edges = cv2.Canny(img,100,200)
		edges = cv2.bitwise_not(edges)
		output_file="a/{}".format(filename)
		cv2.imwrite(output_file,edges)
		