> First I wanted to apolagize for presenting such poor models. I basically do not have any model, they are merely a representation of how the models could have been developed.

# Training Methodology and Challenges

For each regression and classification tasks, I developed two methods of training: One with concatenation and one with attention mechanism and incorporating the column `kiba_score_estimated`:

## Attention Mechanism
- Initially, I used simple concatenation of protein and chemical embeddings to form the feature vector for each data point to create the training set. While straightforward, this approach does not fully capture the complex interactions between proteins and chemicals.
- To address this, I considered using an **attention mechanism** to create a more sophisticated representation that explicitly models these interactions.
- However, since the chemical embeddings do not represent real chemical features (due to being random representation), the **cross-attention mechanism** struggled to extract meaningful relationships. This limitation likely contributed to the model's poor performance.

## Incorporating `kiba_score_estimated`
To integrate the `kiba_score_estimated` column into the training process:
- I modified the loss function to assign higher weights to data points where `kiba_score_estimated` is `False`. I did this to ensures that more reliable data points are given greater importance during training.

# Specifications regarding the regression task:

> In this task, we are trying to estimate `kiba_score`, related files: [deep_learning.ipynb](deep_learning.ipynb) and [deep_learning-attention.ipynb](deep_learning-attention.ipynb)

- I initially trained a **RandomForestRegressor** model. However, due to the dataset's size, training was prohibitively slow.
- To improve efficiency, I transitioned to deep learning models and leveraged **GPU acceleration** for faster training.
- I implemented **gradient clipping** to stabilize training and prevent exploding gradients.
- Since the `kiba_score` is exteremly skewed, and the model uses **ReLU activations**, I employed **He Initialization** (`kaiming_uniform_`) for better weight initialization.
- In some cases, the loss did not change across epochs. This was likely due to poor weight initialization, which can result in uniform or stuck gradients, preventing effective learning.

# Specifications regarding the classification task:

> In this task, we are trying to predict `binding`, related files: [classification.ipynb](classification.ipynb) and [classification-attention.ipynb](classification-attention.ipynb) and [random_forest_regressor.ipynb](random_forest_regressor.ipynb)

- I incorporated the synthetic negative samples to create a robust dataset for distinguishing between binding and non-binding pairs.
- I created a new column called `binding`, where its value was 0 for the synthetic negative samples and 1 for the positive bindings (the data in the original dataset 'Deloitte_DrugDiscovery_dataset.csv')
- The model exhibited significant bias towards labeling data as **No Binding**. Further investigation is needed.




