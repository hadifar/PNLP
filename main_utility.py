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

from utility import general_utility
from models import tfidf

file_path = "/Users/mac/PycharmProjects/PNLP/wiki.txt"
file_result_path = "/Users/mac/PycharmProjects/PNLP/_result/"

if __name__ == "__main__":
    # Utility
    # ================================================================================================
    # get stop word hand-design
    stop_word_list = general_utility.get_stop_word_list()

    # get 10 most common words from corpus
    general_utility.get_most_commons_words(file_path, 10)

    # remove punctuation
    punctuation_result_path = file_result_path + "removed_punctuation.txt"
    general_utility.remove_punctuation(file_path, punctuation_result_path)

    # remove stop words from corpus
    stop_word_path = file_result_path + "removed_stopping.txt"
    general_utility.remove_stop_words(file_path, stop_word_path)

    # Models
    # ================================================================================================
    # calculate tf-idf
    docs = []
    tfidf_representation = tfidf.tfidf_naive(docs)
    tfidf_scikit_representation = tfidf.tfidf_pro(docs)
