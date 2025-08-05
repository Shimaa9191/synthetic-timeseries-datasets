# Synthetic Time-Series Datasets

Three synthetic time-series datasets, plus the generation code.

| Dataset              | Description & Parameters                                                                                       |
|----------------------|----------------------------------------------------------------------------------------------------------------|
| **Local Spike**      | 100× length-200 Markov sequences; 5× spikes at 5% random time points                                           |
| **Drift**            | 100× length-200 sinusoids with phase shifts + baseline drift of 0.5 every 50 steps                              |
| **Segment Corruption** | 100× length-200 uniform series; random 5-step segments replaced with IID noise 𝒩(0,1)                         |

## How to regenerate

```bash
python generate_datasets.py
