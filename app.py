from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
import requests
import json
from langchain_text_splitters import RecursiveJsonSplitter

#loading data
text_loader = TextLoader('note.txt', encoding='utf-8')
text = text_loader.load()
content = text[0].page_content

#text splitting (recursive character mode)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200,chunk_overlap=50)
final_docs = text_splitter.split_documents(text)

#text splitting (character splitter mode)
char_splitter = CharacterTextSplitter(chunk_size=100,chunk_overlap=50)
docs = char_splitter.split_documents(text)

#text splitting (recurrsive json mode)
json_data = requests.get("https://api.smith.langchain.com/openapi.json").json()
json_splitter = RecursiveJsonSplitter(max_chunk_size=300)
json_chunks = json_splitter.split_json(json_data=json_data)
docsin = json_splitter.create_documents(texts=json_data)
print(docsin)