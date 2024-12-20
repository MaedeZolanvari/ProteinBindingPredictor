# Dataset Overview and Insights

#### Unique Entities
- **Proteins**: 4,480  
- **Chemicals**: 683,413  
- **Positive Pairs**: 1,107,113  
#### KIBA Score Statistics
- **Mean**: ~24,967  
- **Median (50th percentile)**: ~176  
- **Minimum**: ~0.000000928  
- **Maximum**: ~868,000,000
- 

## Data Cleansing
Related file: [clean_dataset.ipynb](clean_dataset.ipynb)

(a cleaned_data.csv file was created to use in the rest of the challenge)

To tackle this challenge the first step was to look and analyze the dataset:
- Rows with empty values in the columns `pubchecm_cid`, `kiba_score`, and `kiba_score_estimated` (with the latter two being correlated).

#### Steps Taken:
1. **Empty `pubchecm_cid` Values**:
   - Rows without a `pubchecm_cid` do not carry any meaningful context, therefore, these rows were removed from the dataset.

2. **Empty `kiba_score` Values**:
   - For rows with missing `kiba_score`, I considered two potential approaches:
     - **Option 1**: Remove these rows entirely.
     - **Option 2**: Train a regression model on the dataset (excluding these rows) to estimate and impute the missing values, adding them back to the training set.
   - **Current Approach**: I started by removing rows with missing `kiba_score` and also made sure there is no nageative or zero values in this column.



## Analysis of the `kiba_score` Column
Related file: [kiba_score_distribution.ipynb](kiba_score_distribution.ipynb)

In a regression problem to calculate the `kiba_score`, this column is a critical, but it exhibits significant skewness. Below is a summary of the steps taken to address this issue:

### Key Observations
- **Range**: The `kiba_score` column ranges from approximately **9.28 × 10⁻⁷** to **868,000,000.0**.
- **Initial Skewness**: The `kiba_score` column is highly skewed, with a skewness score of **509.90**.
- **Outlier Removal**: Removing outliers (values above the 99th percentile) reduced the skewness to **59.7**, which is still extremely high.
- **Target Scaling**: To stabilize training and bring `kiba_score` values into a comparable range, I applied a **Log Transformation** and used **gradient clipping** during model training. The transformation further improved the skewness score to **0.26**, which is acceptable.

### Considerations for Outliers
- **Deleting High Values**: I thought about removing rows with `kiba_score > 5` but it wouldn't be a good idea. These extreme values represent real-world cases and should not be ignored.
- **What I would do next:**:
  - **Oversampling**: Oversampling data points with extremely high `kiba_score` could help balance the distribution.
  - **External Data**: Supplementing the dataset with additional samples in the high `kiba_score` range from external databases could enhance the model’s ability to generalize. I explored a bit and found the following repository, which I believe contains relevant data for this task: [DeepDTA KIBA Dataset](https://github.com/hkmztrk/DeepDTA/tree/master/data/kiba)
However, due to time constraints, I couldn't try it.


