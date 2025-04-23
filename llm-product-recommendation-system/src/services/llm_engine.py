# filepath: src/services/llm_engine.py
import torch
from transformers import AutoTokenizer, AutoModel

# Load BERT model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

def get_recommendations(user_preferences, product_descriptions):
    """
    Generate product recommendations based on user preferences and product descriptions.

    Args:
        user_preferences (str): A description of the user's preferences.
        product_descriptions (list): A list of product descriptions.

    Returns:
        list: A list of recommended products.
    """
    try:
        # Tokenize and encode user preferences
        user_inputs = tokenizer(
            user_preferences,
            padding=True,
            truncation=True,
            return_tensors="pt",
        )
        user_embedding = model(**user_inputs).last_hidden_state.mean(dim=1)

        # Compute embeddings for each product description
        product_embeddings = []
        for description in product_descriptions:
            product_inputs = tokenizer(
                description,
                padding=True,
                truncation=True,
                return_tensors="pt",
            )
            product_embedding = model(**product_inputs).last_hidden_state.mean(dim=1)
            product_embeddings.append(product_embedding)

        # Compute cosine similarity between user preferences and product descriptions
        similarities = [
            torch.nn.functional.cosine_similarity(user_embedding, product_embedding).item()
            for product_embedding in product_embeddings
        ]

        # Sort products by similarity
        sorted_products = [
            product
            for _, product in sorted(
                zip(similarities, product_descriptions), reverse=True
            )
        ]

        return sorted_products

    except Exception as e:
        print(f"Error generating recommendations: {e}")
        return []