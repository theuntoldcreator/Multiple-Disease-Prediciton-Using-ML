import matplotlib.pyplot as plt

# create figure and axis objects
fig, ax = plt.subplots(figsize=(10, 10))

# draw the flowchart
ax.text(0.5, 0.95, '+------------------------+', ha='center', va='center')
ax.text(0.5, 0.90, '|                        |', ha='center', va='center')
ax.text(0.5, 0.85, '|   Streamlit Web App    |', ha='center', va='center')
ax.text(0.5, 0.80, '|                        |', ha='center', va='center')
ax.text(0.5, 0.75, '+------------------------+', ha='center', va='center')
ax.text(0.3, 0.70, '           |          ', ha='center', va='center')
ax.text(0.7, 0.70, '          v          ', ha='center', va='center')
ax.text(0.15, 0.60, '+------------------------+', ha='center', va='center')
ax.text(0.5, 0.60, '|    Diabetes Page       |', ha='center', va='center')
ax.text(0.85, 0.60, '| Parkinson\'s Disease    |', ha='center', va='center')
ax.text(0.15, 0.50, '|                        |', ha='center', va='center')
ax.text(0.5, 0.50, '|   Heart Disease Page   |', ha='center', va='center')
ax.text(0.85, 0.50, '|      Page              |', ha='center', va='center')
ax.text(0.15, 0.40, '+------------------------+', ha='center', va='center')
ax.text(0.5, 0.40, '+------------------------+', ha='center', va='center')
ax.text(0.85, 0.40, '+------------------------+', ha='center', va='center')
ax.text(0.15, 0.30, '|                        |', ha='center', va='center')
ax.text(0.5, 0.30, '| Diabetes Pre-processing|', ha='center', va='center')
ax.text(0.85, 0.30, '|Parkinson\'s Pre-process|', ha='center', va='center')
ax.text(0.15, 0.20, '|                        |', ha='center', va='center')
ax.text(0.5, 0.20, '|Heart Disease Pre-process|', ha='center', va='center')
ax.text(0.85, 0.20, '|                        |', ha='center', va='center')
ax.text(0.15, 0.10, '+------------------------+', ha='center', va='center')
ax.text(0.5, 0.10,
'+------------------------+', ha='center', va='center')
ax.text(0.85, 0.10, '+------------------------+', ha='center', va='center')
ax.text(0.15, 0.00, '|                        |', ha='center', va='center')
ax.text(0.5, 0.00, '|  Diabetes Model (SVM)  |', ha='center', va='center')
ax.text(0.85, 0.00, '|Parkinson\'s Model (SVM) |', ha='center', va='center')
ax.text(0.15, -0.10, '|                        |', ha='center', va='center')
ax.text(0.5, -0.10, '|Heart Disease Model (LR)|', ha='center', va='center')
ax.text(0.85, -0.10, '|                        |', ha='center', va='center')
ax.text(0.15, -0.20, '+------------------------+', ha='center', va='center')
ax.text(0.5, -0.20, '+------------------------+', ha='center', va='center')
ax.text(0.85, -0.20, '+------------------------+', ha='center', va='center')
ax.text(0.15, -0.30, '|                        |', ha='center', va='center')
ax.text(0.5, -0.30, '|  Diabetes Prediction   |', ha='center', va='center')
ax.text(0.85, -0.30, '| Parkinson\'s Prediction |', ha='center', va='center')
ax.text(0.15, -0.40, '|                        |', ha='center', va='center')
ax.text(0.5, -0.40, '|   Heart Disease Predic.|', ha='center', va='center')
ax.text(0.85, -0.40, '|                        |', ha='center', va='center')
ax.text(0.15, -0.50, '+------------------------+', ha='center', va='center')
ax.text(0.5, -0.50, '+------------------------+', ha='center', va='center')
ax.text(0.85, -0.50, '+------------------------+', ha='center', va='center')
ax.text(0.15, -0.60, '|                        |', ha='center', va='center')
ax.text(0.5, -0.60, '|   Streamlit Web App    |', ha='center', va='center')
ax.text(0.85, -0.60, '|   Streamlit Web App    |', ha='center', va='center')
ax.text(0.15, -0.70, '| (Display Prediction)   |', ha='center', va='center')
ax.text(0.5, -0.70, '| (Display Prediction)   |', ha='center', va='center')
ax.text(0.85, -0.70, '| (Display Prediction)   |', ha='center', va='center')
ax.text(0.15, -0.80, '|                        |', ha='center', va='center')
ax.text(0.5, -0.80, '+------------------------+', ha='center', va='center')
ax.text(0.85, -0.80, '|                        |', ha='center', va='center')
ax.text(0.5, -0.90, '+------------------------+', ha='center', va='center')

# set axis limits and hide ticks
ax.set_xlim(0, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# show the plot
plt.show()
# ```

# This code will create a Matplotlib figure object and an axis object, and then add text objects to the axis to draw the flowchart. Finally, it will set the axis limits and hide the ticks, and display the plot.

# You can save the plot as a JPEG image using the `savefig()` function:

# ```python
plt.savefig('flowchart.jpg', dpi=300, bbox_inches='tight')
# ```

# This will save the plot as a JPEG image named "flowchart.jpg" with a resolution of 300 DPI and tight bounding box.