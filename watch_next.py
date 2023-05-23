import spacy  # loading spacy

nlp = spacy.load('en_core_web_md')  # loading our language model


# function to find movie similarity based on user input
def similar_movie(description):
    try:
        # reading our movie txt file
        file = open("movies.txt", "r")

        # empty list to hold our recommendation
        recommendation = []

        # looping through each line in the file
        for line in file:

            # comparing input description with movies in txt file
            doc1 = nlp(description.lower())
            doc2 = nlp(line.lower())
            similarity_score = doc1.similarity(doc2)

            # if similarity is higher than 0.8 we append to our empty list
            if similarity_score > 0.8:
                recommendation.append(line.strip())
                # returns similar movie in our empty list
            return recommendation
    except FileNotFoundError:
        print("Error: txt file not found!!!")
        exit()


# declaring a variable to hold our user search input
description = input("Enter a movie description to find similar movie: ")

# calling the function to find similarity of user input
recommendations = similar_movie(description)

# display similarity result
print("Movies similar to the input description \n")

for movie in recommendations:
    print(movie)
