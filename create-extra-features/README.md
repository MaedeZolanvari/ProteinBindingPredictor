
# Adding Extra Features (embeddings) to the Dataset

To train a proper model, I explored adding extra features to the dataset by incorporating embeddings for both proteins and chemicals.

### Protein and Chemical Embeddings

Related file: [save_embeddings.ipynb](save_embeddings.ipynb)

> (I simply concatenated these embeddings and saved them as a *.npz file, but later during training, I used attention mechanism in hope to get better features)

1. **Proteins**:
   - I used [HuggingFace's **ESM model**](https://huggingface.co/docs/transformers/en/model_doc/esm) to calculate embeddings for the proteins. 

2. **Chemicals**:
   - To generate embeddings for chemicals, I needed molecular structures or **SMILES** representations of the `UniProt_ID`.
   - The plan was to use pre-trained transformers like **ChemBERTa** for this task.
   - Fetching SMILES representations required querying the [NIH **PubChem API**](https://pubchem.ncbi.nlm.nih.gov/), but due to the large number of unique entries, I calculated and it was estimated to take approximately **5 days** to retrieve all the data.
  
   > **If I have 683,413 unique PubChem IDs and each request waits for 0.5 seconds, the total execution time would be approximately:**
   > **341,707 seconds (about 5 days, 22 hours, and 55 minutes).**
   -  So, I took an altarnative approach and generated random embeddings using SparseRandomProjection.

### Partial Experimentation
Related files: [generate_smiles.ipynb](generate_smiles.ipynb) and [pubchem_id_to_smiles.csv](pubchem_id_to_smiles.csv)
- I prioritized rows where `kiba_score_estimated` was negative and fetched SMILES for those entries (21805 samples, took about 3 hours, I ran this in the terminal, hence the unfinished notebook.)
- I wanted to train a model on this subset to see how it would work, but due to time constraints, I couldn't.
