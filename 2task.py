{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "64c347cb-cc9d-465a-bd1c-f9e828610047",
   "metadata": {},
   "outputs": [
    {
     "ename": "ImportError",
     "evalue": "cannot import name 'Book' from 'library' (/home/jovyan/8/library.py)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mImportError\u001b[0m                               Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[9], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mlibrary\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m Book\n\u001b[1;32m      3\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mbody\u001b[39m():\n\u001b[1;32m      4\u001b[0m     books \u001b[38;5;241m=\u001b[39m [\n\u001b[1;32m      5\u001b[0m         Book(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mHow to code without understanding\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mme\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;241m2024\u001b[39m, \u001b[38;5;241m15.99\u001b[39m, \u001b[38;5;28;01mFalse\u001b[39;00m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFantasy\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEgcellent\u001b[39m\u001b[38;5;124m\"\u001b[39m),\n\u001b[1;32m      6\u001b[0m         Book(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mRising tie\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124muniper Lee\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;241m1960\u001b[39m, \u001b[38;5;241m12.99\u001b[39m, \u001b[38;5;28;01mFalse\u001b[39;00m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFiction\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mExcellent\u001b[39m\u001b[38;5;124m\"\u001b[39m),\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m      9\u001b[0m         Book(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mAbyss strikes back\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mJoion Genkus\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;241m1951\u001b[39m, \u001b[38;5;241m9.99\u001b[39m, \u001b[38;5;28;01mTrue\u001b[39;00m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFiction\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mAverage\u001b[39m\u001b[38;5;124m\"\u001b[39m),\n\u001b[1;32m     10\u001b[0m     ]\n",
      "\u001b[0;31mImportError\u001b[0m: cannot import name 'Book' from 'library' (/home/jovyan/8/library.py)"
     ]
    }
   ],
   "source": [
    "from library import Book\n",
    "\n",
    "def body():\n",
    "    books = [\n",
    "        Book(\"How to code without understanding\", \"me\", 2024, 15.99, False, \"Fantasy\", \"Egcellent\"),\n",
    "        Book(\"Rising tie\", \"uniper Lee\", 1960, 12.99, False, \"Fiction\", \"Excellent\"),\n",
    "        Book(\"The Great Gambit\", \"That one idiot\", 2010, 100.99, False, \"Classic\", \"average\"),\n",
    "        Book(\"New World\", \"Aldous Benedict\", 2932, 14.99, False, \"Utopian\", \"Good\"),\n",
    "        Book(\"Abyss strikes back\", \"Joion Genkus\", 1951, 9.99, True, \"Fiction\", \"Average\"),\n",
    "    ]\n",
    "\n",
    "\n",
    "    for book in books:\n",
    "        book.get_info()\n",
    "\n",
    "    most_expensive = Book.most_expensive_book(books)\n",
    "    if most_expensive:\n",
    "        print(\"\\nMost Expensive Book:\")\n",
    "        most_expensive.get_info()\n",
    "\n",
    "    books[0].set_stoplist(True)\n",
    "    print(\"\\nAfter setting stoplist for 'Rising tie':\")\n",
    "    books[0].get_info()\n",
    "\n",
    "    books[2].censor(\"That one idiot\", True)\n",
    "    print(\"\\nAfter censoring 'The Great Gambit':\")\n",
    "    books[2].get_info()\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    body()"
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
