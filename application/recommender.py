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
from sklearn.metrics.pairwise import cosine_similarity

from model import tfidf

tokenize = lambda doc: doc.split(" ")


@dispatch(list, int, int)
def get_recommended_news(all_documents, doc_index, number_of_returning_items=4):
    """
    get top-k recommended news based on a document
    :param all_documents: all documents (our collection)
    :param doc_index: index of a document which we find recommended item based on that
    :param number_of_returning_items: number of recommended items which return
    :param naive: use naive tf-idf algorithm or not?
    :return: list of recommended items
    """

    # calculate tf-idf
    tfidf_representation = tfidf.tfidf_pro(all_documents)

    return get_top_k_similar1(tfidf_representation, doc_index, number_of_returning_items)


@dispatch(list, list, list, int, int)
def get_recommended_news(all_documents, user_rated_items, user_rated_score, number_of_returning_items=4,
                         average_rate_score=6,
                         ):
    """
    :param all_documents: all documents (our collection)
    :param user_rated_items: index of items which user rate
    :param user_rated_score: score of items which user rate
    :param number_of_returning_items: number of recommended items which return
    :param naive: use naive tf-idf algorithm or not?
    :return: list of recommended items
    """
    # calculate TF-IDF
    tfidf_representation = tfidf.tfidf_pro(all_documents)

    # calculate user-profile vector
    user_profile_vector = np.zeros(tfidf_representation.shape[1])
    for i, item_number in enumerate(user_rated_items):
        diff = user_rated_score[i] - average_rate_score
        user_profile_vector += diff * np.array(tfidf_representation[item_number])

    return get_top_k_similar2(tfidf_representation, user_profile_vector, number_of_returning_items)


def get_top_k_similar1(tfidf_representation, doc_index, number_of_returning_items=4):
    comparisons = []
    for count_0 in range(tfidf_representation.shape[0]):
        comparisons.append(
            (cosine_similarity(tfidf_representation[count_0], tfidf_representation[doc_index]), count_0))

    comparisons = sorted(comparisons, key=lambda a_entry: a_entry[0], reverse=True)
    return comparisons[1:number_of_returning_items + 1]


def get_top_k_similar2(tfidf_representation, profile_vector, number_of_returning_items=4):
    comparisons = []
    for count_0 in range(tfidf_representation.shape[0]):
        comparisons.append(
            (cosine_similarity(tfidf_representation[count_0], profile_vector), count_0))

    comparisons = sorted(comparisons, key=lambda a_entry: a_entry[0], reverse=True)
    return comparisons[1:number_of_returning_items + 1]
