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

collection_path = "/Users/mac/PycharmProjects/PNLP/wiki.txt"

if __name__ == "__main__":

    # convert document file to collection
    input_file = open(collection_path, 'r')
    all_documents = [line for line in input_file.readlines()]

    # part 1 of quesion
    print('\npart 1 of question\n')
    recommended_items_1 = recommender.get_recommended_news(all_documents, 0, 4, False)
    for x in recommended_items_1:
        print(x)


    # part 2 of question
    print('\npart 2 of question\n')
    user_rated_item = [0, 1, 2, 3]
    user_rated_score = [4, 4, 10, 2]
    recommended_items_2 = recommender.get_recommended_news(all_documents, user_rated_item, user_rated_score, 4, True)
    for x in recommended_items_2:
        print(x)
