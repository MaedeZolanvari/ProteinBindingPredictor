from transformers import EsmTokenizer, EsmModel

# Load ESM model and tokenizer
tokenizer = EsmTokenizer.from_pretrained("facebook/esm2_t6_8M_UR50D")
esm_model = EsmModel.from_pretrained("facebook/esm2_t6_8M_UR50D")
esm_model = esm_model.to(device)
esm_model.eval()

# Function to compute protein embeddings
def get_protein_embedding(uniprot_id):
    inputs = tokenizer(uniprot_id, return_tensors="pt", add_special_tokens=True).to(device)
    with torch.no_grad():
        outputs = esm_model(**inputs)
    embedding = outputs.last_hidden_state.mean(dim=1).squeeze().cpu().numpy()
    return embedding

# Generate random embeddings for chemicals
def generate_random_projections(cids, embedding_dim=256):
    """Generate random embeddings using SparseRandomProjection."""
    random_projector = SparseRandomProjection(n_components=embedding_dim, random_state=42)
    cid_indices = {cid: idx for idx, cid in enumerate(cids)}
    random_matrix = np.random.rand(len(cids), embedding_dim)
    random_embeddings = random_projector.fit_transform(random_matrix)
    return {cid: random_embeddings[cid_indices[cid]] for cid in cids}