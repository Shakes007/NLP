# NLP repository

- This repository holds two project files and one text file.
- These files are garden.py and movie_recommendation.py coupled with movies.txt.

**Both programs import spaCy as it is an import librabry and ensures that it works correctly**

## garden.py
- Takes a list of sentences and splits it up into tokens.
- These sentences can then be checked against other sentences for similarity.
- The tokens that was made can also be checked for simiarity against other words.
- Thereafter, I use spacy.explain() to check all unknown entities.

## movie_recommendation.py and movie.txt
- This program will read in a list of movie descriptions and compare it against an input description.
- Based on its similarity score the next movie will be recommended.
- This program uses two user-defined functions:
  * load_movie_descriptions()
  * find_most_similar_movie()
- The first function loads the movie descriptions from a file called movie.txt
- Then with the second function it calculates the similarity score of the input description
  against the movie descriptions within the text.file.
- Thereafter, it will find the most similar movie description in the list and return the name and description.
