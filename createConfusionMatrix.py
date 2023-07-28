import numpy as np
import matplotlib.pyplot as plt

def confusion_matrix(fp, fn, tp, tn):
  

  confusion_matrix = np.array([[tp, fn], [fp, tn]])

  # Set the color scheme for the confusion matrix.
  colors = ["green", "red", "orange"]
  cmap = plt.cm.BuPu

  # Plot the confusion matrix.
  plt.imshow(confusion_matrix, cmap=cmap, interpolation="nearest")
  plt.title("Confusion Matrix")
  plt.xlabel("Predicted")
  plt.ylabel("True")

  # Add labels to the confusion matrix.
  for i in range(2):
    for j in range(2):
      text = confusion_matrix[i, j]
      if text != 0:
        plt.text(j, i, text, color=colors[i], fontsize=10)

  plt.savefig("confusion_matrix.png")

if __name__ == "__main__":
  fp = 4
  fn = 5
  tp = 15
  tn = 44

  confusion_matrix(fp, fn, tp, tn)
