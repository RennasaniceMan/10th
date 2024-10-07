{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "83811164-10c6-4ca8-8aa1-3e0481ead5f2",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "def smallest(numbers):\n",
    "    small = float('inf')\n",
    "    small2 = float('inf')\n",
    "\n",
    "    for number in numbers:\n",
    "        if number < small:\n",
    "            small2 = small\n",
    "            small = number\n",
    "        elif small < number < small2:\n",
    "            small2 = number\n",
    "\n",
    "    return (small, small2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4cc1e4fa-2510-48c4-956a-9b5b6d715157",
   "metadata": {},
   "outputs": [],
   "source": []
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
