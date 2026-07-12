import pickle

# ----------------------------
# Load Saved Artifacts
# ----------------------------

with open("artifacts/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("artifacts/book_pivot.pkl", "rb") as f:
    book_pivot = pickle.load(f)

with open("artifacts/books_name.pkl", "rb") as f:
    books_name = pickle.load(f)

with open("artifacts/final_rating.pkl", "rb") as f:
    final_rating = pickle.load(f)


# ----------------------------
# Create Title -> ISBN Mapping
# ----------------------------

title_to_isbn = (
    final_rating[["Title", "ISBN"]]
    .drop_duplicates(subset="Title")
    .set_index("Title")["ISBN"]
    .to_dict()
)


# ----------------------------
# Recommendation Function
# ----------------------------

def recommend_book(book_name, n_recommendations=5):
    """
    Returns a list of ISBNs of recommended books.
    """

    # Convert books_name to list if required
    if hasattr(books_name, "tolist"):
        book_list = books_name.tolist()
    else:
        book_list = list(books_name)

    # Book not found
    if book_name not in book_list:
        return {
            "error": "Book not found in ML model",
            "received_title": book_name,
            "sample_titles": book_list[:10]
        }

    # Index of selected book
    index = book_list.index(book_name)

    # KNN Prediction
    distances, suggestions = model.kneighbors(
        book_pivot.iloc[index, :].values.reshape(1, -1),
        n_neighbors=n_recommendations + 1
    )

    recommended_isbns = []

    # Skip the first recommendation (same book)
    for i in suggestions[0][1:]:

        title = book_pivot.index[i]

        isbn = title_to_isbn.get(title)

        if isbn:
            recommended_isbns.append(isbn)

    return recommended_isbns

def search_recommendable_books(query, limit=10):
    """
    Returns book titles that exist in the ML model.
    """

    if hasattr(books_name, "tolist"):
        titles = books_name.tolist()
    else:
        titles = list(books_name)

    query = query.lower()

    matched = [
        title for title in titles
        if query in title.lower()
    ]

    matched.sort()

    return matched[:limit]