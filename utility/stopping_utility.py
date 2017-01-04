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

#
# def generate_stopping_from_corpus(file_path, save_file=True, saved_file_path="_result/stop_words_list.txt",
#                                   number_of_stopping=10):
#     """
#     pass a text file and generate stop word list
#     :param file_path:
#     :param save_file:
#     :param saved_file_path:
#     :param number_of_stopping:
#     :return:
#     """
#     frequency = get_most_commons_words(file_path, number_of_stopping)
#
#     if save_file:
#         save_dictionary_key(saved_file_path, frequency)
#
#     return frequency

#
# def get_stop_word_list():
#     """
#     list of stop words in persian
#     :return:
#     """
#     return set(open('_data/stop_words_list.txt').read().split())


# def remove_stop_words(file_path, file_result_path):
#     """
#     stop word removal function
#     :param file_path:
#     :param file_result_path:
#     :return:
#     """
#     stop_words = get_stop_word_list()
#
#     input = open(file_path, 'r')
#     output = open(file_result_path, 'w')
#
#     for sentence in input:
#         tokenized_sentence = nltk.word_tokenize(sentence)
#         reformatted_sentence = [word for word in tokenized_sentence if word not in stop_words]
#         for word in reformatted_sentence:
#             output.write(word + " ")
#         output.write('\n')
#
#     input.close()
#     output.close()
#     return None
