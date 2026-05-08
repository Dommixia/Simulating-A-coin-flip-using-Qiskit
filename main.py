print("-----------------------------------------------------------")

# Quantum Coin Flip
print("Quantum Coin FLip")
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
def coin_flip(n_times):
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0,0)
    sim = AerSimulator()
    job = sim.run(qc, shots=n_times)
    result = job.result()
    counts = result.get_counts()
    return counts
n = 1000
q_counts = coin_flip(n)
q_heads = q_counts.get('0', 0)
q_tails = q_counts.get('1', 0)
print(f"q_heads: {q_heads} ({q_heads/n*100:.1f}%)")
print(f"q_tails: {q_tails} ({q_tails/n*100:.1f}%)")

print("-----------------------------------------------------------")

#Classical Coin FLip
print("Classical Coin FLip")
import random
classical = [random.randint(0, 1) for _ in range(n)]
c_heads = classical.count(0)
c_tails = classical.count(1)
print(f"HEADS: {c_heads} ({c_heads/n*100:.1f}%)")
print(f"Tails: {c_tails} ({c_tails/n*100:.1f}%)")

print("-----------------------------------------------------------")

import matplotlib.pyplot as plt
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

ax1.bar(['HEADS', 'TAILS'], [q_heads, q_tails], color=['cyan', 'magenta'])
ax1.set_title("Quantum Coin Flip")
ax1.set_ylabel("Count")
ax1.set_ylim(0, 600)

ax2.bar(['HEADS', 'TAILS'], [c_heads, c_tails], color=['blue', 'red'])
ax2.set_title("Classical Coin Flip")
ax2.set_ylabel("Count")
ax2.set_ylim(0, 600)

plt.suptitle("Quantum vs Classical Coin Flip — 1000 flips")
plt.savefig("comparison.png")
plt.tight_layout()
plt.show()