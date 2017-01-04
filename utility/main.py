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
from utility import clean_utility

file_path = "/Users/mac/PycharmProjects/PNLP/_data/d_wiki.fa.text"
file_result_path = "/Users/mac/PycharmProjects/PNLP/_data/clean_wiki.fa.text"


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



# def remove_english_character(document, save_file_path):
#     output = open(save_file_path, 'w')
#
#     for sentence in document:
#         sentence = ''.join([i for i in sentence if not i.isalpha()])
#         sentence = re.sub(RE_SPACE, r' ', sentence)
#         output.write(sentence + '\n')
#
#     output.close()
#     return None


if __name__ == '__main__':
    # clean Wikipedia
    print('clean wikipedia...')
    with open(file_path, 'r') as input_file:
        clean_utility.clean_all(input_file, file_result_path)
