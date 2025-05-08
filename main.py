import argparse
import json
import requests

from urllib.parse import urljoin

BASE_URL = "http://localhost:8000"
KNOWLEDGE_ENDPOINT = "knowledge"
QUERY_ENDPOINT = "query"


def upload_documents(file_path):
    endpoint = urljoin(BASE_URL, KNOWLEDGE_ENDPOINT)
    try:
        contents = []
        data = {}
        with open(file_path, 'r') as file:
            documents = json.load(file)
            for doc in documents:
                contents.append(doc["content"])
            data["contents"] = contents
            print(data)
            response = requests.post(endpoint, json=data)
        if response.status_code == 200:
            print("Document uploaded successfully.")
        else:
            print(f"Failed to upload documents:\nStatus code: {response.status_code}\n Details: {response.json()}")
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")

def get_documents():
    endpoint = urljoin(BASE_URL, KNOWLEDGE_ENDPOINT)
    response = requests.get(endpoint)
    if response.status_code == 200:
        documents = response.json()
        print(f"{len(documents)} documents retrieved successfully:")
        for doc in documents:
            id = doc["id"]
            content = doc["content"]
            print(f"{id}: {content}")
    else:
        print(f"Failed to get documents.\nStatus code: {response.status_code}\n Details: {response.json()}")

def get_document(doc_id):
    endpoint = urljoin(BASE_URL, KNOWLEDGE_ENDPOINT)
    response = requests.get(f"{endpoint}/{doc_id}")
    if response.status_code == 200:
        document = response.json()
        id = document["id"]
        content = document["content"]
        print(f"{id}: {content}")
    elif response.status_code == 404:
        print("Document not found.")
    else:
        print(f"Failed to get document.\nStatus code: {response.status_code}\n Details: {response.json()}")

def chat_query(query):
    endpoint = urljoin(BASE_URL, QUERY_ENDPOINT)
    response = requests.post(endpoint, json={'query': query})
    if response.status_code == 200:
        answer = response.json().get('answer')
        print(f"Chatbot response: {answer}")
    else:
        print(f"Failed to get chat response.\nStatus code: {response.status_code}\n Details: {response.json()}")
        

def main():
    parser = argparse.ArgumentParser(description="API Interaction Script")    
    subparsers = parser.add_subparsers(dest='action', required=True, help="Action to perform")

    # Subparser for upload action
    upload_parser = subparsers.add_parser('upload', help="Upload a document")
    upload_parser.add_argument('--file-path', required=True, help="Path of the document to upload")

    # Subparser for get documents action
    get_parser = subparsers.add_parser('get', help="Get documents")
    get_parser.add_argument('--doc-id', required=False, help="Document ID to fetch")

    # Subparser for chat query action
    query_parser = subparsers.add_parser('query', help="Chat query")
    query_parser.add_argument('--query', required=True, help="Query string for the chat")

    args = parser.parse_args()

    if args.action == 'upload':
        upload_documents(args.file_path)
    elif args.action == 'get':
        if args.doc_id:
            get_document(args.doc_id)
        else:
            get_documents()
    elif args.action == 'query':
        chat_query(args.query)
    else:
        print("Invalid action. Please use 'upload', 'get', or 'query'.")

if __name__ == "__main__":
    main()

