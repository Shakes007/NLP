# This program is designed to read in a list of movie descriptions and
# compare it an input description. Based on its similarity score the 
# next movie will be recommended.

# Import the spaCy library
import spacy

# Load the spaCy English module with its vectors.
nlp = spacy.load('en_core_web_md')


# Read in movie.txt
def load_movie_descriptions(file_path):
    '''
    Read in the contents of a file and returns a list of lines
    
    Parameteres:
    - file_path (str): The path to the file to be read.
     
    Returns:
    - A list containing the lines read from the file.
    
    Raises:
    - FileNotFoundError: if file is not found the current directory. '''

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        print('File not found in current directory.')


# Function to find the most similar movie:
def find_most_similar_movie(input_description, movie_descriptions):
    '''
    Find the most similar movie description to the given input description
    
    Parameters:
    - input_description (str): the description of the movie to compare.
    - movie_descriptions (list): A list of movie descriptions to compare.
    
    Returns:
    - str: The title of the most similar movie.
    
    Note:
    The function uses spaCy's NLP to calculate the similarity scores between
    input_description and each movie_description. It returns the title of the
    movie with the highest similarity score.
    '''

    # process the input description:
    input_doc = nlp(input_description)

    # Calculate the similarity scores for each movie description:
    similarity_scores = []

    for movie_description in movie_descriptions:
        movie_doc = nlp(movie_description)
        similarity_score = input_doc.similarity(movie_doc)
        similarity_scores.append(similarity_score)
    
    # Find the index of the most similar movie:
    most_similar_index = similarity_scores.index(max(similarity_scores))

    # Return the title of the most similar movie:
    return movie_descriptions[most_similar_index].strip()


file_path = 'movies.txt'

input_description = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk lands on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""

# Load movie descriptions:
movie_descriptions = load_movie_descriptions(file_path)

# Find most similar movie:
most_similar_movie = find_most_similar_movie(input_description, movie_descriptions)

# Print Result:
print(f'User should watch next: {most_similar_movie}')

