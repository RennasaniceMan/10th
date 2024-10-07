{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "7d39d781-22f1-425e-aa17-ebeaa0b825e6",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[17], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01msmall_module\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m small_module\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mintegers\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m list1, list2, list_range\n\u001b[1;32m      3\u001b[0m list_bundle \u001b[38;5;241m=\u001b[39m [list1, list2, list_range]\n",
      "File \u001b[0;32m~/8/small_module.py:28\u001b[0m\n\u001b[1;32m      1\u001b[0m {\n\u001b[1;32m      2\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcells\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[1;32m      3\u001b[0m   {\n\u001b[1;32m      4\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m      5\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m5\u001b[39m,\n\u001b[1;32m      6\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m83811164-10c6-4ca8-8aa1-3e0481ead5f2\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m      7\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[1;32m      8\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtags\u001b[39m\u001b[38;5;124m\"\u001b[39m: []\n\u001b[1;32m      9\u001b[0m    },\n\u001b[1;32m     10\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[1;32m     11\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[1;32m     12\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdef smallest(numbers):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m     13\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    small = float(\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124minf\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m     14\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    small2 = float(\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124minf\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m     15\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m     16\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    for number in numbers:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m     17\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        if number < small:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m     18\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m            small2 = small\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m     19\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m            small = number\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m     20\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        elif small < number < small2:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m     21\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m            small2 = number\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m     22\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m     23\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    return (small, small2)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m     24\u001b[0m    ]\n\u001b[1;32m     25\u001b[0m   },\n\u001b[1;32m     26\u001b[0m   {\n\u001b[1;32m     27\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m---> 28\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[43mnull\u001b[49m,\n\u001b[1;32m     29\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m4cc1e4fa-2510-48c4-956a-9b5b6d715157\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m     30\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[1;32m     31\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[1;32m     32\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: []\n\u001b[1;32m     33\u001b[0m   }\n\u001b[1;32m     34\u001b[0m  ],\n\u001b[1;32m     35\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[1;32m     36\u001b[0m   \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mkernelspec\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[1;32m     37\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdisplay_name\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPython 3 (ipykernel)\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m     38\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mlanguage\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m     39\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython3\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m     40\u001b[0m   },\n\u001b[1;32m     41\u001b[0m   \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mlanguage_info\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[1;32m     42\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcodemirror_mode\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[1;32m     43\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mipython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m     44\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mversion\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m3\u001b[39m\n\u001b[1;32m     45\u001b[0m    },\n\u001b[1;32m     46\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfile_extension\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m.py\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m     47\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmimetype\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/x-python\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m     48\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m     49\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnbconvert_exporter\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m     50\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpygments_lexer\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mipython3\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m     51\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mversion\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m3.10.9\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m     52\u001b[0m   }\n\u001b[1;32m     53\u001b[0m  },\n\u001b[1;32m     54\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnbformat\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m4\u001b[39m,\n\u001b[1;32m     55\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnbformat_minor\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m5\u001b[39m\n\u001b[1;32m     56\u001b[0m }\n",
      "\u001b[0;31mNameError\u001b[0m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "from small_module import small_module\n",
    "from integers import list1, list2, list_range\n",
    "list_bundle = [list1, list2, list_range]\n",
    "with open('result.txt', 'w') as result:\n",
    "    for integers in list_bundle:\n",
    "        try:\n",
    "            smallest = small_module(list_bundle)\n",
    "            result.write(f\"Two smallest values from {list_bundle}: {smallest}\\n\")\n",
    "        except ValueError as e:\n",
    "            print(\"nuh huh\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "305c15b4-b3e9-4c9d-a596-7c75382195c8",
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
