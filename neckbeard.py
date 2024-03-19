from googleapiclient.discovery import build
import requests
from langchain_community.llms import Ollama
from langchain_community.embeddings import VoyageEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_core.documents import Document
import os
from dotenv import load_dotenv
load_dotenv() 

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
SEARCH_ENGINE_ID = os.getenv('SEARCH_ENGINE_ID')
VOYAGE_API_KEY = os.getenv('VOYAGE_API_KEY') 


def get_reddit_post_and_comments(url):
    post_id = url.split('/')[-3]
    post_url = f"https://old.reddit.com/comments/{post_id}/.json"
    user_agent = 'neckbeard/1.0'
    post_response = requests.get(post_url, headers={'User-agent': user_agent})
    post_data = post_response.json()
    post_body = post_data[0]['data']['children'][0]['data']['selftext']
    comments = []
    for comment in post_data[1]['data']['children']:
        if 'body' in comment['data']:
            comment_body = comment['data']['body']
            comments.append(comment_body)
    return {'post_body': post_body, 'comments': comments}

def google_search(query, site):
    service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
    result = service.cse().list(q=query, cx=SEARCH_ENGINE_ID, num=5, siteSearch=site).execute()
    
    urls = []
    if "items" in result:
        for item in result["items"]:
            urls.append(item["link"])
    
    return {"urls": urls}

search_query = input("Enter your search query: ")
site = "reddit.com"
search_results = google_search(search_query, site)

data = ""
for url in search_results["urls"]:
    post_and_comments = get_reddit_post_and_comments(url)
    formatted_data = f"""
URL: {url}
Post Body:
{post_and_comments['post_body']}
Comments:
"""
    for comment in post_and_comments['comments']:
        formatted_data += f"{comment}\n"
    data += formatted_data + "\n"
    
    print(f"URL: {url}")
    print("Post Body:")
    print(post_and_comments['post_body'])
    print("Comments:")
    for comment in post_and_comments['comments']:
        print(comment)
    

doc = Document(page_content=data)
ollama = Ollama(base_url='http://localhost:11434', model='your_model_name_here')
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=20,
    length_function=len
)
new_docs = text_splitter.split_documents([doc])  # Pass the Document object as a list
embeddings = VoyageEmbeddings(
    voyage_api_key=VOYAGE_API_KEY, model="voyage-2"
)
vectorstore = Chroma.from_documents(documents=new_docs, embedding=embeddings)
qachain = RetrievalQA.from_chain_type(ollama, retriever=vectorstore.as_retriever())
print(qachain.invoke({"query": search_query+" answer in about 1000 words."}))
