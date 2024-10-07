{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "155bcf89-7b81-4241-a015-2ae7302a23f8",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "class Book:\n",
    "    def __init__(self, title, author, year, price, stoplist, genre):\n",
    "        self.title = title\n",
    "        self.author = author\n",
    "        self.year = year\n",
    "        self.price = price\n",
    "        self.stoplist = stoplist\n",
    "        self.genre = genre\n",
    "        self.quality = quality\n",
    "\n",
    "    def get_info(self):\n",
    "        print(f\"Author: {self.author}, Title: {self.title}, Year: {self.year}, Price: ${self.price}, censored: {self.stoplist}\")\n",
    "\n",
    "    def most_expensive_book(cls, book_list):\n",
    "        return max(book_list, key=lambda book: book.price)\n",
    "\n",
    "    def set_stoplist(self, boolean):  # not sure that this is correct to be honest but it was offered as solution without using clunky RNG generator with true/false assignemnt based on addity of number( it was my idea but a difficult one to implement)\n",
    "        self.stoplist = boolean\n",
    "\n",
    "    def censor(self, author_name, boolean):\n",
    "        if self.author == author_name:\n",
    "            self.stoplist = boolean"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
