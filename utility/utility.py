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
import re
import operator

import nltk

RE_USELESS = r'[^\w\d\s]+'  # remove useless characters

# generate frequency of word in document
def get_doc_frequency(document):
    frequency = {}
    for sentence in document:
        tokens = nltk.word_tokenize(sentence)
        for word in tokens:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
    return frequency


# generate reversed sorted frequency of document
def get_sorted_doc_frequency(document):
    frequency = get_doc_frequency(document)
    return reversed(sorted(frequency.items(), key=operator.itemgetter(1)))


# save dictionary keys into file
def save_dictionary_key(saved_file_path, dictionary):
    output = open(saved_file_path, 'w')
    for word in dictionary:
        output.write(word[0] + '\n')
    output.close()


# pass a text file and generate stop word list
# def generateStopWordFromCorpus(file_path, save_file=True, saved_file_path="data/stop_words_list.txt"):
#     input = open(file_path, 'r')
#     frequency = get_sorted_doc_frequency(input)
#     input.close()
#
#     if save_file:
#         save_dictionary_key(saved_file_path, frequency)
#
#     return frequency


def get_stop_word_list():
    return set(open('data/stop_words_list.txt').read().split())


def remove_stopping(file_path):
    stop_words = get_stop_word_list()

    input = open(file_path, 'r')
    output = open('result/removed_stopping.txt', 'w')

    for sentence in input:
        tokenized_sentence = nltk.word_tokenize(sentence)
        reformatted_sentence = [word for word in tokenized_sentence if word not in stop_words]
        for word in reformatted_sentence:
            output.write(word + " ")
        output.write('\n')

    input.close()
    output.close()
    return None


def remove_punctuation(file_path):

    input = open(file_path, 'r')
    output = open('result/removed_punctuation.txt', 'w')

    for sentence in input:
        sentence = re.sub(RE_USELESS, r'', sentence)
        output.write(sentence)

    input.close()
    output.close()
    return None
