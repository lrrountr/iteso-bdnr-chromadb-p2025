import os

import chromadb
from chromadb.config import Settings

DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(DIR, 'data')
chroma_client = chromadb.PersistentClient(path=DB_PATH, settings=Settings(allow_reset=True, anonymized_telemetry=False))
sample_collection = chroma_client.get_or_create_collection(name="sample_collection")

documents = [
    "Mars, often called the 'Red Planet', has captured the imagination of scientists and space enthusiasts alike.",
    "The Hubble Space Telescope has provided us with breathtaking images of distant galaxies and nebulae.",
    "The concept of a black hole, where gravity is so strong that nothing can escape it, was first theorized by Albert Einstein's theory of general relativity.",
    "The Renaissance was a pivotal period in history that saw a flourishing of art, science, and culture in Europe.",
    "The Industrial Revolution marked a significant shift in human society, leading to urbanization and technological advancements.",
    "The ancient city of Rome was once the center of a powerful empire that spanned across three continents.",
    "Dolphins are known for their high intelligence and social behavior, often displaying playful interactions with humans.",
    "The chameleon is a remarkable creature that can change its skin color to blend into its surroundings or communicate with other chameleons.",
    "The migration of monarch butterflies spans thousands of miles and involves multiple generations to complete.",
    "Christopher Nolan's 'Inception' is a mind-bending movie that explores the boundaries of reality and dreams.",
    "The 'Lord of the Rings' trilogy, directed by Peter Jackson, brought J.R.R. Tolkien's epic fantasy world to life on the big screen.",
    "Pixar's 'Toy Story' was the first feature-length film entirely animated using computer-generated imagery (CGI).",
    "Superman, known for his incredible strength and ability to fly, is one of the most iconic superheroes in comic book history.",
    "Black Widow, portrayed by Scarlett Johansson, is a skilled spy and assassin in the Marvel Cinematic Universe.",
    "The character of Iron Man, played by Robert Downey Jr., kickstarted the immensely successful Marvel movie franchise in 2008."
]
metadatas = [{'category': "Space"}, {'category': "Space"}, {'category': "Space"}, {'category': "History"}, {'category': "History"}, {'category': "History"}, {'category': "Animals"}, {'category': "Animals"}, {'category': "Animals"}, {'category': "Movies"}, {'category': "Movies"}, {'category': "Movies"}, {'category': "Superheroes"}, {'category': "Superheroes"}, {'category': "Superheroes"}]
ids = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]

sample_collection.add(documents=documents, metadatas=metadatas, ids=ids)

query_result = sample_collection.query(query_texts="Give me some facts about space", n_results=2)
result_documents = query_result["documents"][0]

for doc in result_documents:
    print(doc)
