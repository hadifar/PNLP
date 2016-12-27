# WORD EMBEDDING


**Word Embedding | Word2Vec | Glove | Persian Embedding**

Word Embedding
-------

**History**
  - 1990s Vector Space Models (*LSI & ...*)
  - 2003 (Bengio) *neural language model with model's parameter*
  - 2008 (Collbert & Weston) *natural language modeling*
  - 2012 (Mikolov et.al) *Word2Vec*
  - 2013 (Pennington et.al)  *Glove*


**Word embedding Models**

  - comming soon...




Usage
-------

Train word2Vec & Glove on Wikipedia (Farsi) with Tensorflow and Gensim.

As you can see in the following image, words like 'نماینده', 'مجلس', 'دولت', 'جمهوری' are close together (in [TSNE][1] representation).
Also Vectors of countries and their capitals show another awesome feature of vector representation.
Other properties of vector representation (addition,subtraction) would be added later.

![Embedding with TSNE](https://raw.githubusercontent.com/AmirHadifar/PNLP/master/model/embedding/embedding1.png)

![Countries & Capitals](https://raw.githubusercontent.com/AmirHadifar/PNLP/master/model/embedding/embedding2.png)



References
-------
 * http://sebastianruder.com/word-embeddings-1/index.html



[1]: https://lvdmaaten.github.io/tsne/
