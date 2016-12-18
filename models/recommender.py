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
from sklearn.feature_extraction.text import TfidfVectorizer

from models import tfidf
from utility.math_utility import cosine_similarity

tokenize = lambda doc: doc.split(" ")


def get_recommended_news(document_path, doc_index, recommended_items=4, naive=True):
    """
    get top5 recommended news to user
    :param document_path: path of collection
    :param doc_index: find recommended items for  doc_index
    :return:
    """
    # convert document file to collection
    input_file = open(document_path, 'r')
    all_documents = [line for line in input_file.readlines()]

    if naive:
        return get_naive_recommended(all_documents, doc_index, recommended_items=recommended_items)
    else:
        return get_pro_recommended(all_documents, doc_index, recommended_items=recommended_items)


def get_naive_recommended(all_documents, doc_index, recommended_items):
    """
    this function is implemented naive and not use scikit-learn
    :param all_documents:
    :param doc_index:
    :param recommended_items:
    :return:
    """
    tfidf_representation = tfidf.tfidf_naive(all_documents)
    naive_comparisons = []
    for count_0, doc_0 in enumerate(tfidf_representation):
        naive_comparisons.append((cosine_similarity(doc_0, tfidf_representation[doc_index]), doc_index, count_0))

    naive_comparisons = sorted(naive_comparisons, key=lambda a_entry: a_entry[0], reverse=True)
    return naive_comparisons[:recommended_items]


def get_pro_recommended(all_documents, doc_index, recommended_items):
    """
    this function is used scikit-learn library
    :param all_documents:
    :param doc_index:
    :param recommended_items:
    :return:
    """
    sklearn_tfidf = TfidfVectorizer(norm='l2', min_df=0, use_idf=True, smooth_idf=False, sublinear_tf=True,
                                    tokenizer=tokenize)
    sklearn_representation = sklearn_tfidf.fit_transform(all_documents)

    scikit_comparisons = []
    for count_0, doc_0 in enumerate(sklearn_representation.toarray()):
        scikit_comparisons.append(
            (cosine_similarity(doc_0, sklearn_representation.toarray()[doc_index]), doc_index, count_0))

    return sorted(scikit_comparisons, key=lambda a_entry: a_entry[0], reverse=True)[:recommended_items]
