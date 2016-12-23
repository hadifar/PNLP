# -*- coding: utf-8 -*-

# Copyright 2016 Amir Hadifar.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
from collections import Counter
import re

import nltk

RE_USELESS = r'[^\w]'  # remove useless characters
RE_DIGIT = r"^\d+\s|\s\d+\s|\s\d+$"  # remove digits
RE_SPACE = r'\s+'  # remove space
RE_EMAILS = r'[\w\.-]+@[\w\.-]+'
RE_URLS = r'http\S+'
RE_WWW = r'www\S+'


# # generate frequency of word in document
# def get_doc_frequency(file_path):
#     frequency = {}
#     for sentence in document:
#         tokens = nltk.word_tokenize(sentence)
#         for word in tokens:
#             if word in frequency:
#                 frequency[word] += 1
#             else:
#                 frequency[word] = 1
#     return frequency


def get_most_commons_words(file_path, number_of_commons=10):
    input = open(file_path, 'r')
    text = input.read()
    tokens = nltk.word_tokenize(text)
    counter = Counter(tokens)
    return counter.most_common(number_of_commons)


# generate reversed sorted frequency of document
# def get_sorted_doc_frequency(document):
#     frequency = get_doc_frequency(document)
#     return reversed(sorted(frequency.items(), key=operator.itemgetter(1)))


# save dictionary keys into file
def save_dictionary_key(saved_file_path, dictionary):
    output = open(saved_file_path, 'w')
    for word in dictionary:
        output.write(word[0] + '\n')
    output.close()


def generate_stopping_from_corpus(file_path, save_file=True, saved_file_path="_result/stop_words_list.txt",
                                  number_of_stopping=10):
    """
    pass a text file and generate stop word list
    :param file_path:
    :param save_file:
    :param saved_file_path:
    :param number_of_stopping:
    :return:
    """
    frequency = get_most_commons_words(file_path, number_of_stopping)

    if save_file:
        save_dictionary_key(saved_file_path, frequency)

    return frequency


def get_stop_word_list():
    """
    list of stop words in persian
    :return:
    """
    return set(open('_data/stop_words_list.txt').read().split())


def remove_stop_words(file_path, file_result_path):
    """
    stop word removal function
    :param file_path:
    :param file_result_path:
    :return:
    """
    stop_words = get_stop_word_list()

    input = open(file_path, 'r')
    output = open(file_result_path, 'w')

    for sentence in input:
        tokenized_sentence = nltk.word_tokenize(sentence)
        reformatted_sentence = [word for word in tokenized_sentence if word not in stop_words]
        for word in reformatted_sentence:
            output.write(word + " ")
        output.write('\n')

    input.close()
    output.close()
    return None


def remove_punctuation(input_document, file_result_path):
    """
    remove punctuation from input_document
    :param input_document:
    :param file_result_path: clean document path
    :return: nothing!
    """
    input = open(input_document, 'r')
    output = open(file_result_path, 'w')

    for sentence in input:
        sentence = re.sub(RE_USELESS, r'', sentence)
        output.write(sentence)

    input.close()
    output.close()
    return None


def remove_english_character(document, save_file_path):
    output = open(save_file_path, 'w')

    for sentence in document:
        sentence = ''.join([i for i in sentence if not i.isalpha()])
        sentence = re.sub(RE_SPACE, r' ', sentence)
        output.write(sentence + '\n')

    output.close()
    return None
