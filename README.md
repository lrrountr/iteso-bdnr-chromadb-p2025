# iteso-bdnr-chromadb

A place to share chromadb app code

### Setup a python virtual env with python chromadb installed
```
# If pip is not present in you system
sudo apt update
sudo apt install python3-pip

# Install and activate virtual env (Linux/MacOS)
python3 -m pip install virtualenv
python3 -m venv ./venv
source ./venv/bin/activate

# Install and activate virtual env (Windows)
python3 -m pip install virtualenv
python3 -m venv ./venv
.\venv\Scripts\Activate.ps1

# Install project python requirements
pip install -r requirements.txt
```

### The examples directory have a couple of intro scripts to familiarize yourself with ChromaDB
Local run
```
cd examples
python chromadb_local.py
```

Docker run needs the container to be running
```
docker run -d -v ./chroma-data:/data -p 8000:8000 --name chromadb chromadb/chroma
cd examples
python chromadb_docker.py 
```
### To run the API service
```
python -m uvicorn app:app --reload
```
