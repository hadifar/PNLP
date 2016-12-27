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
from application import recommender

collection_path = "/Users/mac/PycharmProjects/PNLP/_data/HAM2-corpus-all.txt"

if __name__ == "__main__":

    # convert document file to collection
    with open(collection_path, 'r') as input_file:
        all_documents = [line for line in input_file.readlines()]

    # number of recommended items
    number_of_item_return = 5
    print(len(all_documents), "documents read from input file ...")


    # part 1 of quesion
    print('\npart 1 of question\n')
    recommended_items_1 = recommender.get_recommended_news(all_documents, 66428, number_of_item_return)

    with open('q1.txt', 'w') as out_file:
        for x in recommended_items_1:
            print(x)
            out_file.write("similarity:" + str(x[0][0][0]) + " similar_doc_index" + str(x[1]) + "\n")
            out_file.write(all_documents[x[1]] + "\n")


    # part 2 of question
    print('\npart 2 of question\n')
    average_user_rate = 6
    user_rated_item = [47010, 46937, 54258]
    user_rated_score = [8, 5, 7]
    recommended_items_2 = recommender.get_recommended_news(all_documents, user_rated_item, user_rated_score,
                                                           average_user_rate, number_of_item_return)
    with open('q2.txt', 'w') as out_file:
        for x in recommended_items_2:
            print(x)
            out_file.write("similarity:" + str(x[0][0][0]) + " similar_doc_index" + str(x[1]) + "\n")
            out_file.write(all_documents[x[1]] + "\n")
