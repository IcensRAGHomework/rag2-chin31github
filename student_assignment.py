from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)
#must comment rich when upload to homework
#from rich import print as pprint

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    docs = loader.load()
    #pprint(docs)
    docs_iterator = iter(docs)
    text_splitter = CharacterTextSplitter(separator='\n', chunk_size=10, chunk_overlap=0)
    #test_doc = docs[0].page_content
    chunks = text_splitter.split_documents(docs_iterator)
    #pprint(chunks)
    return chunks[len(chunks)-1]
    pass

def hw02_2(q2_pdf):
    pass

hw02_1(q1_pdf)