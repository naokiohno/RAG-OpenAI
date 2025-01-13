# Load libraries
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI
import os


def create_file_paths(folder_path):
    dir_list = os.listdir(folder_path)
    full_dir_list = []
    for i in range(len(dir_list)):
        full_dir_list.append(folder_path + dir_list[i])
    return full_dir_list

def load_and_split_multiple_files(list_of_file_paths):
    output = []
    for i in range(len(list_of_file_paths)):
        loader = PyPDFLoader(list_of_file_paths[i])
        pages = loader.load_and_split()
        output.extend(pages)
    return output

pdf_file_path = 'data/cv_pdf_files/'
full_pdf_file_paths = create_file_paths(pdf_file_path)
final_pages = load_and_split_multiple_files(full_pdf_file_paths)

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(final_pages, embedding=embeddings)

llm = ChatOpenAI(temperature=0.7, model_name="gpt-4")
memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

conversation_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(),
    memory=memory
)

def make_query(query_string):
    result = conversation_chain({"question": query_string})
    answer = result["answer"]
    print("The answer is:\n" + answer)

make_query('Who in the context is best qualified for a Java programmer role?')
make_query('Who in the context has more Python experience?')
make_query('Who in the context has the most management experience?')
make_query('Who in the context has the most data science experience?')


