"""
Задача: Анализ статистики книжной библиотеки
Вы библиотекарь небольшой библиотеки, и вам нужно проанализировать статистику книг в вашей коллекции.
У вас есть список книг с их названиями, авторами и жанрами. Ваша задача:
Подсчитайте количество книг каждого автора. Done
Подсчитайте количество книг в каждом жанре. Done
Найдите самого популярного автора и жанр. Done
Отобразить топ-3 самых популярных авторов и жанров.
"""



books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction"},
    {"title": "1984", "author": "George Orwell", "genre": "Dystopian"},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Fiction"},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "genre": "Fantasy"},
    {"title": "The Hunger Games", "author": "Suzanne Collins", "genre": "Dystopian"},
    {"title": "The Handmaid's Tale", "author": "Margaret Atwood", "genre": "Dystopian"},
    {"title": "War and Peace", "author": "Leo Tolstoy", "genre": "Historical Fiction"},
    {"title": "The Picture of Dorian Gray", "author": "Oscar Wilde", "genre": "Gothic Horror"},
    {"title": "The Adventures of Huckleberry Finn", "author": "Mark Twain", "genre": "Adventure"},
    {"title": "The Scarlet Letter", "author": "Nathaniel Hawthorne", "genre": "Historical Fiction"},
    {"title": "Moby-Dick", "author": "Herman Melville", "genre": "Adventure"},
    {"title": "The Count of Monte Cristo", "author": "Alexandre Dumas", "genre": "Adventure"},
    {"title": "Jane Eyre", "author": "Charlotte Brontë", "genre": "Romance"},
    {"title": "Wuthering Heights", "author": "Emily Brontë", "genre": "Romance"},
    {"title": "The Bell Jar", "author": "Sylvia Plath", "genre": "Autobiographical Fiction"},
]


from collections import Counter



author_counts = Counter(book["author"] for book in books)
genre_counts = Counter(book["genre"] for book in books)

print(author_counts.most_common(1)[0][0])
print(genre_counts.most_common(1)[0][0])