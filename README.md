# 🛰️ The Dimension Defender: SVM Hyperplane Commander

An interactive Machine Learning simulation designed to teach **Support Vector Machines (SVM)** and geometric classification boundaries from scratch[span_0](start_span)[span_0](end_span). You play as a Planetary Defense Officer calibrating long-range tactical sensors, using vector algebra to calculate a maximum-margin hyperplane that splits incoming hostile space debris from friendly cargo pods[span_1](start_span)[span_1](end_span).

## 🎓 Learning Objectives

This project focuses on teaching:
* **Support Vector Machines (SVM):** A classification algorithm that seeks the mathematically optimal boundary to cleanly segregate vector spaces[span_2](start_span)[span_2](end_span).
* **The Hyperplane Equation:** Understanding how weights ($W_1, W_2$) and biases ($b$) establish decision boundaries across multi-dimensional features.
* **Support Vectors:** Highlighting the critical, borderline data points that dictate the placement and orientation of the decision boundary.
* **Margin Maximization:** Seeing how minimizing the geometric norm of a weight vector increases the "buffer zone" (margin width) between classes to improve model robustness.

---

## ✨ Features

* **Sci-Fi Aerospace Scenario:** Contextualizes abstract vector geometry into a tactical, high-stakes trajectory defense mission.
* **Geometric Trace Analysis:** Computes and prints the precise margin separation width ($2 / ||w||$) based on your manual vector adjustments.
* **Interactive Matrix Interface:** Allows live parameter tuning to let users visually map out how changing vector weights rotates and scales a decision line.
* **Zero Engine Dependencies:** Written using core Python logic natively, mapping linear decision functions (`sign(w · x + b)`) without heavy mathematics frameworks.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You only need **Python 3** installed.

### 2. Setup and Execution
1.  **Clone the Repo:**
    
```bash
    git clone [https://github.com/YOUR_USERNAME/dimension-defender-svm.git](https://github.com/YOUR_USERNAME/dimension-defender-svm.git)
    cd dimension-defender-svm
    ```
2.  **Save the Code:** Save the provided script as `space_defense.py`.
3.  **Run the Script:**
    
```bash
    python space_defense.py
    ```

### 3. Gameplay Instructions
1.  **Analyze the Sensor Feed:** Observe the mass and velocity profiles of historical friendly vs. hostile telemetry.
2.  **Calibrate Vectors:** Input your spatial weights and bias offsets to draw a line through the data.
3.  **Track the Margin Width:** Observe how your vector magnitudes inversely affect the width of your classification safety buffer.
4.  **Evaluate Interception Metrics:** Watch the system process an unknown borderline contact to see if your hyperplane successfully isolates the threat.

---

## 🧠 Code Structure Highlights

### Geometric Margin Computation
The maximum-margin boundary framework calculates space separation by processing the magnitude (Euclidean norm) of your weight configurations.

```python
weight_norm = math.sqrt(w1**2 + w2**2)
margin_width = 2.0 / weight_norm
