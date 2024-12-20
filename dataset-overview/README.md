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
## Analysis of the `kiba_score` Column

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
  - **External Data**: Supplementing the dataset with additional samples in the high `kiba_score` range from external databases could enhance the model’s ability to generalize.

