from sentence_transformers import SentenceTransformer, InputExample, losses
from torch.utils.data import DataLoader
import json

# python -m fine_tuning.train_embeddings


def load_data(path):
    examples = []

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)

            anchor = item["anchor"]
            positive = item["positive"]

            examples.append(InputExample(texts=[anchor, positive]))

    return examples


def train():

    print("Loading base model...")

    model = SentenceTransformer("BAAI/bge-small-en-v1.5")

    train_data = load_data("fine_tuning/triplets.jsonl")

    train_dataloader = DataLoader(train_data, shuffle=True, batch_size=8)

    loss = losses.MultipleNegativesRankingLoss(model)

    print("Starting training...")

    model.fit(
        train_objectives=[(train_dataloader, loss)],
        epochs=1,  # start small
        warmup_steps=10,
        show_progress_bar=True,
    )

    model.save("fine_tuned_embedding_model")

    print("Model saved!")


if __name__ == "__main__":
    train()
