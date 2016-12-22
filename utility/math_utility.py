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
import math


def cosine_similarity(vector1, vector2):
    """
    calculate cosine similarity between two vectors
    :param vector1:
    :param vector2:
    :return: normalize value of cosine similarity
    """
    dot_product = sum(p * q for p, q in zip(vector1, vector2))
    magnitude = math.sqrt(sum([val ** 2 for val in vector1])) * math.sqrt(sum([val ** 2 for val in vector2]))
    if not magnitude:
        return 0
    return dot_product / magnitude


def jaccard_similarity(query, document):
    """
    calculate Jaccard similarity between query and document
    :param query:
    :param document:
    :return:
    """
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    return len(intersection) / len(union)
