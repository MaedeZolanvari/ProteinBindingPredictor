# Synthetic Negative Samples

Related file: [generate_negative_samples.ipynb](generate_negative_samples.ipynb)

(An augmented_dataset_with_estimates.csv file was created to use for classification)

I created synthetic negative samples with the following in mind:

1. **Random Sampling**:
   - Instead of generating all possible pairs (a computationally expensive process), proteins and chemicals were randomly sampled to create synthetic pairs.
   - I made sure these synthetic pairs do not overlap with the original positive pairs in the dataset.

2. **Balanced Dataset**:
   - The number of synthetic negative samples (`num_negatives`) was set equal to the number of positive pairs to maintain a balanced dataset.

## Usage in Training
- **Regression Problem**:
  - Synthetic negative samples were **not used** for the regression task. Since the original data was already skewed towards low values of `kiba_score`, adding synthetic data with a score of zero would not be meaningful and just make it worse.
- **Classification Problem**:
  - Synthetic negative samples were used for training a classifier, ensuring a robust dataset for distinguishing between binding and non-binding pairs.
