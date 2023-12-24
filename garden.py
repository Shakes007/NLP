# Import spacy for natural language processing.
import spacy

nlp = spacy.load('en_core_web_sm')

gardenSentences = ('The horse raced past the barn fell.',
                   'The chichen is ready to eat was delicious.',
                   'Mary gave the child a Band-Aid.',
                   'That Jill is never here hurts.',
                   'The cotton clothing is made of grows in Mississippi.'
                   )


for sentence in gardenSentences:
    doc = nlp(sentence)

    # Tokenise each sentence in the list:
    print([token.text for token in doc])

    # Get named entity recognition for a sentence in gardenSentences:
    print([(ent.text, ent.label_) for ent in doc.ents])

    print('\n')

# Get an explanation of an entity and print it
entity_GPE = spacy.explain("GPE")
print(f"GPE:{entity_GPE}")

# Get an explanation of an entity and print it
entity_PERSON = spacy.explain("PERSON")
print(f"PERSON:{entity_PERSON}")

# Entity: GPE - explaination: COuntries, cities, states
# Entitiy Person - People, including fictional

# The entity GPE I didn't understand what it was reffering to. However,
# after using space.explain(), I understand now what it means.
# Further, it makes sense within the terms of the sentence and
# how it is associated with the words in the sentence.

# The entity PERSON refers to a person, including fictional people.
# Within context of the sentence it is appropriate because "Jill" and
# "Mary" are indeed names of people.
