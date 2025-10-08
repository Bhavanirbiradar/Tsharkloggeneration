from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit.circuit.library import ZZFeatureMap
from qiskit_machine_learning.kernels import QuantumKernel
import pandas as pd
import os

# --- Load data ---
if not os.path.exists("packet_analysis.csv"):
    print("⚠️ packet_analysis.csv not found! Please make sure it exists.")
    exit()

data = pd.read_csv("packet_analysis.csv")

# Use 2 numerical features for quantum demo
X = data[['Length']].copy()
X['Protocol'] = pd.factorize(data['Protocol'])[0]  # encode protocol as number
X = X.head(10)
X = X / X.max()  # normalize

# --- Quantum setup ---
feature_map = ZZFeatureMap(feature_dimension=2, reps=2)
backend = Aer.get_backend('statevector_simulator')
quantum_instance = QuantumInstance(backend)

kernel = QuantumKernel(feature_map=feature_map, quantum_instance=quantum_instance)

matrix = kernel.evaluate(X, X)
print("\n✅ Quantum Kernel Similarity Matrix:\n")
print(matrix)
