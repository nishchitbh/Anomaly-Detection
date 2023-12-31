# Anomaly Detection using Gaussian Distribution

## Overview

This repository contains a simple anomaly detection script implemented in Python. The main functionality is encapsulated in the `main.py` file. The script uses Gaussian distribution to detect anomalies in a given dataset. Additionally, there is a folder named `Notes` which includes Markdown and PDF notes providing further insights into anomaly detection.

## Usage

### Prerequisites
- Python 3.x
- NumPy
- Matplotlib
- JSON module

### Installation
1. Clone the repository to your local machine:

```bash
git clone https://github.com/mr0bn0xi0us/Anomaly-Detection.git
cd Anomaly-Detection
```

2. Install dependencies:

```bash
pip install numpy matplotlib
```

### Execution

Run the `main.py` script to perform anomaly detection:

```bash
python main.py
```

The script loads a dataset from the `../dataset-maker/dataset.json` file, calculates the mean and standard deviation, and determines whether a given data point is anomalous or not. The results are displayed using scatter plots and histograms.

## Code Explanation

The script follows these steps:

1. Load dataset from `../dataset-maker/dataset.json`.
2. Calculate mean (`mu`) and standard deviation (`sigma`) of the training dataset.
3. Calculate the probability density functions for each dimension of the test point.
4. Determine whether the test point is anomalous based on a threshold.
5. Display results using scatter plots and histograms.

```python
# Add any additional information or notes about the code here.
```

## Notes

Refer to the `Notes` folder for more detailed documentation on the anomaly detection method, including theoretical explanations and considerations.
