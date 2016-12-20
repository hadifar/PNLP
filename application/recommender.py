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

from multipledispatch import dispatch
import numpy as np

from model import tfidf
from utility.math_utility import cosine_similarity

tokenize = lambda doc: doc.split(" ")


@dispatch(list, int, int, bool)
def get_recommended_news(all_documents, doc_index, num_rec_items=4, naive=True):
    """
    get top-k recommended news based on a document
    :param all_documents: all documents (our collection)
    :param doc_index: index of a document which we find recommended item based on that
    :param num_rec_items: number of recommended items which return
    :param naive: use naive tf-idf algorithm or not?
    :return: list of recommended items
    """

    # calculate tf-idf
    if naive:
        tfidf_representation = tfidf.tfidf_naive(all_documents)
    else:
        tfidf_representation = tfidf.tfidf_pro(all_documents)

    return get_top_k_similar(tfidf_representation, tfidf_representation[doc_index], num_rec_items)


@dispatch(list, list, list, int, bool)
def get_recommended_news(all_documents, user_rated_items, user_rated_score, num_rec_items=4, naive=True):
    """
    :param all_documents: all documents (our collection)
    :param user_rated_items: index of items which user rate
    :param user_rated_score: score of items which user rate
    :param num_rec_items: number of recommended items which return
    :param naive: use naive tf-idf algorithm or not?
    :return: list of recommended items
    """
    # calculate TF-IDF
    if naive:
        tfidf_representation = tfidf.tfidf_naive(all_documents)
    else:
        tfidf_representation = tfidf.tfidf_pro(all_documents)

    # calculate user-profile vector
    # average user score
    average_rate_score = sum(user_rated_score) / len(user_rated_score)
    user_profile_vector = np.zeros(len(tfidf_representation[0]))
    for i, item_number in enumerate(user_rated_items):
        diff = average_rate_score - user_rated_score[i]
        user_profile_vector += diff * np.array(tfidf_representation[item_number])

    return get_top_k_similar(tfidf_representation, user_profile_vector, num_rec_items)


def get_top_k_similar(tfidf_representation, single_vector, num_rec_items=4):
    """
    calculate similarity between tfidf_representation and single_vector and return top-k similar items
    :param tfidf_representation: tf-idf matrix
    :param single_vector: a vector that want to find most similar item to it
    :param num_rec_items: number of recommended items which return
    :return: most similar items
    """
    comparisons = []
    for count_0, doc_0 in enumerate(tfidf_representation):
        comparisons.append((cosine_similarity(doc_0, single_vector), count_0, 999))

    comparisons = sorted(comparisons, key=lambda a_entry: a_entry[0], reverse=True)
    return comparisons[:num_rec_items]
