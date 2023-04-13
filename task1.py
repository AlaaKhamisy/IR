Doc_1 = "An inverted index is an index data structure storing a mapping from content, such as words or numbers, to its locations in a document or a set of documents"
Doc_2 = "In simple words, it is a hashmap like data structure that directs you from a word to a document or a web page."
Doc_3 = "The purpose of an inverted index is to allow fast full-text searches, at a cost of increased processing when a document is added to the database"
Doc_4 = "The inverted index data structure is a central component of a typical search engine indexing algorithm"

Docs =[Doc_1,Doc_2,Doc_3,Doc_4]
print(Docs)

Not_repeated_words= set()
for doc in Docs:
    for word in doc.split():
        Not_repeated_words.add(word)
print(Not_repeated_words)

inverted_index = {}
for i, doc in enumerate(Docs):
    for word in doc.split():
        if word in inverted_index:
            inverted_index[word].add(i)
        else: inverted_index[word] = {i}
print(inverted_index)


posting_list = inverted_index['document']
print(posting_list)