# 12 Teach: Team Activity
# Jaelee

# read file
open('books_and_chapters.txt')

largestChapter = 0
largestBook = ''

# read contents
with open('books_and_chapters.txt') as text:
    for line in text:
        x = line.split(':')
        book = x[0].strip()
        chapter = int(x[1])
        scripture = x[2].strip()

        print(f'Scripture: {scripture}, Book: {book}, Chapters: {chapter}')
    
        if chapter > largestChapter:
            largestChapter = chapter
            largestBook = book

print(f'The book of {largestBook} has the most chapters.')
print(f'There are {largestChapter} chapters.')


