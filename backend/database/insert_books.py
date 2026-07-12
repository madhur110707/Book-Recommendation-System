import pandas as pd
from db_connection import connect_db
import traceback

try:
    # Read CSV
    book_details = pd.read_csv("Data/Book-Details.csv", low_memory = False)
    print("CSV Loaded Successfully!")
    print("Total Books:", len(book_details))

    # Connect to MySQL
    conn = connect_db()
    cursor = conn.cursor()

    print("Connected to MySQL!")

    query = """
    INSERT INTO book_details
    (ISBN, Title, Author, Publication_Year, Average_Rating, Image_url)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    Title = VALUES(Title),
    Author = VALUES(Author),
    Publication_Year = VALUES(Publication_Year),
    Average_Rating = VALUES(Average_Rating),
    Image_url = VALUES(Image_url)
    """

    count = 0


    for _, row in book_details.iterrows():
        cursor.execute(query, (
            row["ISBN"],
            row["Title"],
            row["Author"],
            row["Year"],
            row["Average_Rating"],
            row["Image_url"]
        ))
        count += 1

    conn.commit()

    print(f"{count} books inserted successfully!")

    cursor.close()
    conn.close()



except Exception:
    traceback.print_exc()