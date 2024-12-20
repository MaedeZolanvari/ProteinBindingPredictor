# Synthetic Negative Samples

(An augmented_dataset_with_estimates.csv file was created to use for classification)

## Overview
To create synthetic negative samples, the following approach was used:

1. **Random Sampling**:
   - Instead of generating all possible pairs (a computationally expensive process), proteins and chemicals were randomly sampled to create synthetic pairs.
   - Care was taken to ensure these synthetic pairs do not overlap with the original positive pairs in the dataset.

2. **Balanced Dataset**:
   - The number of synthetic negative samples (`num_negatives`) was set equal to the number of positive pairs to maintain a balanced dataset.

## Usage in Training
- **Regression Problem**:
  - Synthetic negative samples were **not used** for the regression task. Since the original data was already skewed towards low values of `kiba_score`,
    adding synthetic data with a score of zero would not be meaningful and just make it worse.
- **Classification Problem**:
  - Synthetic negative samples were used for training a classifier, ensuring a robust dataset for distinguishing between binding and non-binding pairs.

This method provides a computationally efficient way to augment the dataset while maintaining the integrity of the original data.
