import requests
from bs4 import BeautifulSoup
import random


class Vocabulary:
    def __init__(self):
        self.URL = "https://studynow.ru/dicta/allwords"
        self.dictionary = self.get_dictionary()

    def get_data(self):
        res = requests.get(self.URL)
        if res.status_code == 200:
            return res.text
        else:
            print("Something went wrong!")
            return False

    def get_dictionary(self):
        result = self.get_data()
        if result:
            soup = BeautifulSoup(result, "html.parser")
            words = soup.find_all("tr")
            dict_of_words = dict()
            for word in words:
                word_with_translation = word.find_all("td")
                dict_of_words[word_with_translation[1].text] = word_with_translation[2].text
            return dict_of_words

    def get_random_item(self):
        value = random.choice(list(self.dictionary.keys()))
        return (value, self.dictionary.pop(value))
