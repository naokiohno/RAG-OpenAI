
# Load libraries
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI

# Load data
pdf_file_path = 'data/cv_pdf_files/naoki_ohno_cv.pdf'
loader = PyPDFLoader(pdf_file_path)
pages = loader.load_and_split()

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(pages, embedding=embeddings)

llm = ChatOpenAI(temperature=0.7, model_name="gpt-4")
memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

conversation_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(),
    memory=memory
)

query = "Does the applicant have experience with Scikit-learn?"
result = conversation_chain({"question": query})
answer = result["answer"]
print("The answer is:\n" + answer)