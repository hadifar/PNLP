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
from __future__ import division
from models import recommender
from utility.math_utility import cosine_similarity
from models import tfidf

file_path = "/Users/mac/PycharmProjects/PNLP/wiki.txt"

document_0 = "China has a strong economy that is growing at a rapid pace. However politically it differs greatly from the US Economy."
document_1 = "At last, China seems serious about confronting an endemic problem: domestic violence and corruption."
document_2 = "Japan's prime minister, Shinzo Abe, is working towards healing the economic turmoil in his own country for his view on the future of his people."
document_3 = "Vladimir Putin is working hard to fix the economy in Russia as the Ruble has tumbled."
document_4 = "What's the future of Abenomics? We asked Shinzo Abe for his views"
document_5 = "Obama has eased sanctions on Cuba while accelerating those against the Russian Economy, even as the Ruble's value falls almost daily."
document_6 = "Vladimir Putin is riding a horse while hunting deer. Vladimir Putin always seems so serious about things - even riding horses. Is he crazy?"

all_documents = [document_0, document_1, document_2, document_3, document_4, document_5, document_6]


# def augmented_term_frequency(term, tokenized_document):
#     max_count = max([term_frequency(t, tokenized_document) for t in tokenized_document])
#     return (0.5 + ((0.5 * term_frequency(term, tokenized_document)) / max_count))


if __name__ == "__main__":

    # print(recommender.get_recommended_news(file_path, 1))

    tfidf_representation = recommender.get_naive_recommended(all_documents,0,3)

    # print(tfidf_representation)

    # str = 'china speaker'

    # response = sklearn_tfidf.transform([str])
    # print(response)




    # for count_0, doc_0 in enumerate(sklearn_representation.toarray()):
    #     for count_1, doc_1 in enumerate(response.toarray()):
    #         print(count_0, count_1, cosine_similarity(doc_0, doc_1))

    our_tfidf_comparisons = []
    for count_0, doc_0 in enumerate(tfidf_representation):
        for count_1, doc_1 in enumerate(tfidf_representation):
            our_tfidf_comparisons.append((cosine_similarity(doc_0, doc_1), count_0, count_1))


    # skl_tfidf_comparisons = []
    # for count_0, doc_0 in enumerate(sklearn_representation.toarray()):
    #     for count_1, doc_1 in enumerate(sklearn_representation.toarray()):
    #         skl_tfidf_comparisons.append((cosine_similarity(doc_0, doc_1), count_0, count_1))
    #
    #
    # for x in zip(sorted(our_tfidf_comparisons, reverse=True), sorted(skl_tfidf_comparisons, reverse=True)):
    #     print(x)
