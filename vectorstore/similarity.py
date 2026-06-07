from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

text1 = "dog"
text2 = "puppy"
text3 = "airplane"

embedding1 = model.encode(text1)
embedding2 = model.encode(text2)
embedding3 = model.encode(text3)

score1 = cosine_similarity([embedding1], [embedding2])[0][0]

score2 = cosine_similarity([embedding1], [embedding3])[0][0]

print(f"dog vs puppy    : {score1}")
print(f"dog vs airplane : {score2}")
