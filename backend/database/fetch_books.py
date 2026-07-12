from database.db_connection import connect_db


def get_book_by_title(title):
    """
    Fetch details of a selected book using its title.
    Returns a dictionary.
    """

    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT
        ISBN,
        Title,
        Author,
        Publication_Year,
        Average_Rating,
        Image_url
    FROM book_details
    WHERE Title = %s
    LIMIT 1
    """

    cursor.execute(query, (title,))
    book = cursor.fetchone()

    cursor.close()
    conn.close()

    return book


def get_books_details(isbn_list):
    """
    Fetch details of multiple recommended books.
    Returns a list of dictionaries.
    """

    if not isbn_list:
        return []

    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    placeholders = ",".join(["%s"] * len(isbn_list))

    query = f"""
    SELECT
        ISBN,
        Title,
        Author,
        Publication_Year,
        Average_Rating,
        Image_url
    FROM book_details
    WHERE ISBN IN ({placeholders})
    """

    cursor.execute(query, isbn_list)

    books = cursor.fetchall()

    cursor.close()
    conn.close()

    # Preserve recommendation order
    books_dict = {book["ISBN"]: book for book in books}

    ordered_books = []

    for isbn in isbn_list:
        if isbn in books_dict:
            ordered_books.append(books_dict[isbn])

    return ordered_books


def get_popular_books(limit=12):
    """
    Fetch popular books for the home page.
    """

    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT
        ISBN,
        Title,
        Author,
        Publication_Year,
        Average_Rating,
        Image_url
    FROM book_details
    ORDER BY Average_Rating DESC
    LIMIT %s
    """

    cursor.execute(query, (limit,))

    books = cursor.fetchall()

    cursor.close()
    conn.close()

    return books

def search_books(query, limit=10):
    """
    Search books by title.
    Returns matching book titles.
    """

    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    sql = """
    SELECT Title
    FROM book_details
    WHERE Title LIKE %s
    LIMIT %s
    """

    cursor.execute(sql, (f"%{query}%", limit))

    books = cursor.fetchall()

    cursor.close()
    conn.close()

    return books

def search_books(query, limit=10):
    """
    Returns matching book titles.
    """

    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    sql = """
    SELECT Title
    FROM book_details
    WHERE Title LIKE %s
    ORDER BY Average_Rating DESC
    LIMIT %s
    """

    cursor.execute(sql, (f"%{query}%", limit))

    books = cursor.fetchall()

    cursor.close()
    conn.close()

    # Return only titles
    return [book["Title"] for book in books]

def get_book_details(title):
    """
    Returns complete details of one selected book.
    """

    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    sql = """
    SELECT
        ISBN,
        Title,
        Author,
        Publication_Year,
        Average_Rating,
        Image_url
    FROM book_details
    WHERE Title=%s
    LIMIT 1
    """

    cursor.execute(sql, (title,))

    book = cursor.fetchone()

    cursor.close()
    conn.close()

    return book