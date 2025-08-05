import numpy as np

def generate_local_spike(n_seq=100, length=200, spike_prob=0.05, spike_mult=5):
    # Two-state Markov chain with equal transition probabilities
    P = np.array([[0.9, 0.1],
                  [0.1, 0.9]])
    seqs = np.zeros((n_seq, length), dtype=int)
    for i in range(n_seq):
        state = np.random.choice([0,1])
        for t in range(length):
            # Markov step
            state = np.random.choice([0,1], p=P[state])
            val = state
            # occasionally spike
            if np.random.rand() < spike_prob:
                val *= spike_mult
            seqs[i,t] = val
    return seqs

def generate_drift(n_seq=100, length=200, drift_amp=0.5):
    seqs = np.zeros((n_seq, length))
    for i in range(n_seq):
        phi = np.random.uniform(0, 2*np.pi)
        for t in range(length):
            base = np.sin(2*np.pi * t / 50 + phi)
            drift = drift_amp * (t // 50)
            seqs[i,t] = base + drift
    return seqs

def generate_segment_corruption(n_seq=100, length=200, seg_len=5):
    seqs = np.random.rand(n_seq, length)
    for i in range(n_seq):
        start = np.random.randint(0, length - seg_len + 1)
        seqs[i, start:start+seg_len] = np.random.normal(0,1, size=seg_len)
    return seqs

if __name__ == "__main__":
    np.random.seed(42)
    local_spike = generate_local_spike()
    drift = generate_drift()
    seg_corr = generate_segment_corruption()

    # Save to CSV
    np.savetxt("local_spike.csv", local_spike, delimiter=",")
    np.savetxt("drift.csv", drift, delimiter=",")
    np.savetxt("segment_corruption.csv", seg_corr, delimiter=",")
    print("Datasets generated and saved as CSV files.")
