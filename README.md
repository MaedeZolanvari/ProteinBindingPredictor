# Protein-Molecule Binding Prediction

This repository contains the steps and methodologies used to predict binding and estimate kiba score for protein and molecule pairs. Follow the folders in the order below for a structured understanding of the approach:


1. **[Dataset Overview](dataset-overview/README.md)**:  
   Explore the dataset, including insights and preprocessing steps.

2. **[Synthetic Negative Samples](synthetic-negative-samples/README.md)**:  
   Learn how synthetic negative samples were created to balance the dataset.

3. **[Adding Extra Features](create-extra-features/README.md)**:  
   Understand the feature engineering process, including embeddings and chemical structure integration.

4. **[Model Training](model-training/README.md)**:  
   Dive into the model training process, challenges, and key decisions made.

Each folder includes a detailed `README.md` explaining the steps and decisions taken. Start with [Dataset Overview](dataset-overview/README.md) and proceed sequentially for clarity.

## What would I have done if I had more time:

1. Expand my domain knowledge, ask a professional, take a course! I would say one of the big hurdles was lack of familarity with the domain and the data.
2. Use more complext models to capture the structure of the data! I would even look to find pre-trained model on Hugging Face (my go-to model repository) and fine-tune an already established model.
3. Train for way more epochs!
5. Use proper embedings for the chemicals and work with SMILES not random embeddings!
6. Definitely utilize an extrenal database to mitigate the problem of extreme skewness of the kiba scores for a well trained regression model.



---

## Final Note

Finally, I would like to thank you for this opportunity! As someone with zero prior knowledge in biology or the mechanisms of proteins and drugs, this challenge was a great learning experience.

---

## Created by
Maede Zolanvari 
*s.maede.zolanvar@gmail.com*  
