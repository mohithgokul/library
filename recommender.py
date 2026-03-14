import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class BookRecommender:

    def __init__(self, books_df):

        self.books_df = books_df

        # Combine features into one text
        self.books_df["content"] = (
            self.books_df["title"] + " " +
            self.books_df["author"] + " " +
            self.books_df["genre"]
        )

        # Convert text into numerical vectors
        vectorizer = TfidfVectorizer()

        self.matrix = vectorizer.fit_transform(self.books_df["content"])

        # Compute similarity matrix
        self.similarity = cosine_similarity(self.matrix)

    def recommend(self, isbn, top_n=3):

        # find book index
        book_index = self.books_df[self.books_df["isbn"] == isbn].index

        if len(book_index) == 0:
            return []

        book_index = book_index[0]

        scores = list(enumerate(self.similarity[book_index]))

        scores = sorted(scores, key=lambda x: x[1], reverse=True)

        recommendations = []

        for i in scores[1:top_n+1]:
            title = self.books_df.iloc[i[0]]["title"]
            recommendations.append(title)

        return recommendations