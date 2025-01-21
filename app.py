{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "52ad5f3c-0197-490e-8bb9-34730c345fdf",
   "metadata": {},
   "outputs": [],
   "source": [
    "%%writefile app.py\n",
    "import streamlit as st\n",
    "import pickle\n",
    "\n",
    "with open('model.pkl', 'rb') as model_file:\n",
    "    model = pickle.load(model_file)\n",
    "\n",
    "with open('count_vectorizer.pkl', 'rb') as vectorizer_file:\n",
    "    vectorizer = pickle.load(vectorizer_file)\n",
    "\n",
    "st.title(\"Fake News Detection\")\n",
    "st.write(\"Enter the news article below to check if it's fake or real:\")\n",
    "\n",
    "news_text = st.text_area(\"News Article\", \"Enter news content here...\")\n",
    "\n",
    "if st.button(\"Check News\"):\n",
    "    if news_text:\n",
    "        input_vector = vectorizer.transform([news_text])\n",
    "\n",
    "        prediction = model.predict(input_vector)\n",
    "\n",
    "        if prediction[0] == 1:\n",
    "            st.error(\"This news is FAKE.\")\n",
    "        else:\n",
    "            st.success(\"This news is REAL.\")\n",
    "    else:\n",
    "        st.warning(\"Please enter some text to check.\")"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
