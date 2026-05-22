import math

def svm_defense_game():
    # 1. Scenario: Planetary Space Defense
    print("--- 🛰️ THE DIMENSION DEFENDER: SVM HYPERPLANE COMMANDER 🛰️ ---")
    print("Mission: Establish a spatial decision boundary to intercept hostile space debris.")
    print("Goal: Maximize the geometric margin between two distinct classes of space objects.")

    # 2. Training Data: [Velocity, Mass] -> Class (1 = Hostile Debris, -1 = Friendly Pod)
    # The true optimal dividing line is Velocity = Mass (or Velocity - Mass = 0)
    objects = [
        {"coords": [2.0, 5.0], "label": -1, "type": "Friendly Pod"},
        {"coords": [3.0, 7.0], "label": -1, "type": "Friendly Pod"},
        {"coords": [7.0, 3.0], "label": 1, "type": "Hostile Debris"},
        {"coords": [8.0, 4.0], "label": 1, "type": "Hostile Debris"}
    ]
    
    print("\n--- 🖥️ TACTICAL SENSOR FEED (TRAINING DATA) ---")
    for idx, obj in enumerate(objects):
        print(f"Object {idx+1}: Velocity = {obj['coords'][0]} mach | Mass = {obj['coords'][1]} tons -> [{obj['type']}]")

    # 3. Interactive Inputs: Slope/Weights (W1, W2) and Bias (b)
    print("\n--- STEP 1: DEFINE THE HYPERPLANE EQUATION ---")
    print("Equation form: (Velocity * W1) + (Mass * W2) + Bias = 0")
    try:
        w1 = float(input("Enter Weight 1 / Velocity Vector (Recommended: 1.0): "))
        w2 = float(input("Enter Weight 2 / Mass Vector (Recommended: -1.0): "))
        bias = float(input("Enter Bias / Intercept Offset (Recommended: 0.0): "))
    except ValueError:
        w1, w2, bias = 1.0, -1.0, 0.0

    # 4. Math Processing: Finding Support Vectors and Margin Width
    print("\n--- 🔄 COMPUTING GEOMETRIC MARGIN DEPTH ---")
    
    # Calculate the norm/magnitude of the weight vector: ||w|| = sqrt(w1^2 + w2^2)
    weight_norm = math.sqrt(w1**2 + w2**2)
    
    if weight_norm == 0:
        print("💥 CRITICAL GEOMETRIC ERROR: Weight magnitude cannot be zero!")
        return

    # In a linear SVM, the total geometric margin width between support vectors is 2 / ||w||
    margin_width = 2.0 / weight_norm
    print(f"Calculated Margin Separation Width: {margin_width:.4f} units")

    # 5. Incoming Unidentified Target
    test_object = [5.0, 4.0] # High velocity, lower mass -> true label is Hostile (1)
    print(f"\n--- 🚨 VECTOR ALERT: INCOMING BORDERLINE CONTACT ---")
    print(f"Unidentified Object Profile -> Velocity: {test_object[0]} mach | Mass: {test_object[1]} tons")

    # 6. Evaluation: Decision Function f(x) = sign(w * x + b)
    raw_functional_distance = (test_object[0] * w1) + (test_object[1] * w2) + bias
    
    if raw_functional_distance >= 0:
        prediction_label = 1
        prediction_str = "💥 HOSTILE DEBRIS (TARGET LOCKED)"
    else:
        prediction_label = -1
        prediction_str = "✅ FRIENDLY POD (ALLOW ENTRY)"

    print(f"\n--- 📊 SYSTEM CLASSIFICATION OUTPUT ---")
    print(f"Functional Distance Score: {raw_functional_distance:.2f}")
    print(f"Defense Matrix Prediction: {prediction_str}")

    # 7. Ground Truth Validation
    actual_label = 1 # The testing coordinate belongs to the hostile domain space
    
    if prediction_label == actual_label:
        print("\n🏆 SUCCESS: Your SVM hyperplane successfully separated the threat profile!")
        print("The threat was neutralized while protecting the incoming supply lanes.")
    else:
        print("\n💥 SYSTEM BREACH: Misclassification error! Friendly vectors were compromised or threats leaked through.")

if __name__ == "__main__":
    svm_defense_game()
