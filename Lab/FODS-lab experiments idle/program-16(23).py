
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

control = np.array([2.1, 2.5, 1.8, 2.3, 2.0,
                    2.4, 1.9, 2.2, 2.1, 2.0])

treatment = np.array([4.2, 4.5, 3.8, 4.7, 4.1,
                      4.4, 3.9, 4.6, 4.3, 4.0])

# Hypothesis testing
t_stat, p_value = ttest_ind(treatment, control)

print("Control Mean:", np.mean(control))
print("Treatment Mean:", np.mean(treatment))
print("P-value:", p_value)

if p_value < 0.05:
    print("Significant treatment effect")
else:
    print("No significant treatment effect")

# Visualization
plt.boxplot([control, treatment], tick_labels=["Control", "Treatment"])
plt.title("Treatment Effectiveness")
plt.ylabel("Blood Pressure Reduction")
plt.show()
