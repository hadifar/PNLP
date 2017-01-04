# -*- coding: utf-8 -*-

# Copyright 2017 Amir Hadifar.
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
import logging
import os
from utility import clean_utility

clean_file_path = "/Users/mac/PycharmProjects/PNLP/_data/d_wiki.fa.text"
clean_file_result_path = "/Users/mac/PycharmProjects/PNLP/_data/clean_wiki.fa.text"

gen_file_result_path = "/Users/mac/PycharmProjects/PNLP/_data/d_hamshahri.fa.text"
gen_file_path = "/Users/mac/PycharmProjects/PNLP/_data/Hamshahri"


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


# def get_most_commons_words(file_path, number_of_commons=10):
#     input = open(file_path, 'r')
#     text = input.read()
#     tokens = nltk.word_tokenize(text)
#     counter = Counter(tokens)
#     return counter.most_common(number_of_commons)


# generate reversed sorted frequency of document
# def get_sorted_doc_frequency(document):
#     frequency = get_doc_frequency(document)
#     return reversed(sorted(frequency.items(), key=operator.itemgetter(1)))


# save dictionary keys into file
# def save_dictionary_key(saved_file_path, dictionary):
#     output = open(saved_file_path, 'w')
#     for word in dictionary:
#         output.write(word[0] + '\n')
#     output.close()




def clean_example():
    print('clean wikipedia...')
    with open(clean_file_path, 'r') as input_file:
        clean_utility.clean_all_save(input_file, clean_file_result_path)


def generate_text_example():
    with open(gen_file_result_path, 'w') as output:
        for subdir, dirs, files in os.walk(gen_file_path):
            for file in files:
                if file.endswith(".xml"):
                    document = open(os.path.join(subdir, file)).read()
                    text = clean_utility.clean_all(document, r'<TEXT>(.*?)</TEXT>')
                    output.write(text)


if __name__ == '__main__':
    # clean WikiPedia
    # clean_example()

    # clean hamshari
    generate_text_example()

    i = 0
    with open(gen_file_result_path,'r') as input_file:
        for sen in input_file:
            print(sen + '\n')
            if i > 5:
                break
