# 🧠 AI Research Paper Search Engine

An intelligent research paper search engine that uses transformer-based semantic search to retrieve relevant academic papers from multiple open-access sources. The system understands the meaning of queries and returns contextually relevant results instead of relying only on keyword matching.

---

## 🚀 Features

* 🔍 **Semantic Search** using transformer models (MiniLM)
* 🌐 **Multi-source integration** (arXiv API)
* 🧠 **Context-aware retrieval** (understands intent, not just keywords)
* ⚡ **Fast search** using precomputed embeddings
* 🗄️ **MongoDB Atlas integration** for scalable storage
* 🧹 **Optimized preprocessing** for transformer models
* 🧑‍🔬 Search across **title, abstract, and authors**
* 📊 Ranked results using **cosine similarity**
* 📚 Includes **citation data** (from OpenAlex)

---

## 🧠 How It Works

1. Research papers are fetched from APIs (arXiv and OpenAlex).
2. Text fields (title, abstract, authors) are cleaned and preprocessed.
3. A transformer model converts each paper into embeddings (vectors).
4. Embeddings and metadata are stored in MongoDB.
5. When a user enters a query:

   * The query is converted into an embedding
   * Cosine similarity is computed with stored embeddings
   * Top relevant papers are retrieved and displayed

---

## 🏗️ Project Structure

```
AI-Research-Paper-Search-Engine/
│
├── app.py                      # Flask app (entry point)
├── load_data.py                # Fetch + preprocess + embedding storage
│
├── crawler/
│   ├── api_crawler.py        # Fetch papers from arXiv API
│
├── database/
│   └── db.py                   # MongoDB connection and operations
│
├── preprocessing/
│   └── clean_text.py           # Text cleaning logic
│
├── search/
│   ├── transformer.py          # Embedding model handling
│   ├── search_engine.py        # Core search logic
│   └── similarity.py           # Cosine similarity
│
├── templates/                  # HTML templates (UI)
├── static/                     # CSS / JS files
├── requirements.txt            # Dependencies
└── README.md
```

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Machine Learning:** Sentence Transformers (MiniLM)
* **Database:** MongoDB Atlas
* **APIs:** arXiv API, OpenAlex API
* **Frontend:** HTML, CSS
* **Libraries:** NumPy, Scikit-learn

---

## 🤖 Model Used

* **Model:** all-MiniLM-L6-v2
* **Type:** Transformer-based sentence embedding model
* **Output:** 384-dimensional vector embeddings
* **Purpose:** Capture semantic meaning of text for similarity search

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/AI-Research-Paper-Search-Engine.git
cd AI-Research-Paper-Search-Engine
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv .venv
.venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create a `.env` file:

```
MONGO_URI=your_mongodb_connection_string
```

---

### 5️⃣ Load Data (APIs → DB)

```
python load_data.py
```

---

### 6️⃣ Run the Application

```
python app.py
```

---

### 7️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

## 📊 Example Queries

* "AI in healthcare"
* "natural language processing transformers"
* "reinforcement learning robotics"
* "deep learning for image classification"

---

## 🔥 Key Improvements Over Traditional Search

| Feature                | TF-IDF | This Project |
| ---------------------- | ------ | ------------ |
| Keyword Matching       | ✅      | ✅            |
| Semantic Understanding | ❌      | ✅            |
| Context Awareness      | ❌      | ✅            |
| Synonym Handling       | ❌      | ✅            |
| Multi-source Data      | ❌      | ✅            |

---

## ⚡ Future Enhancements

* 🔍 Hybrid search (TF-IDF + Transformers)
* 📈 Display similarity scores in UI
* 🎯 Filtering by author/year/category
* 🚀 MongoDB vector search integration
* 🌐 Cloud deployment (AWS / Render / Railway)
* 🤖 Research paper summarization

---

## 🔐 Security Notes

* `.env` file is excluded from version control
* Sensitive credentials (MongoDB URI) are not exposed

---

## 🤝 Contributing

Feel free to fork the repository and submit pull requests for improvements.

---

## ⭐ Acknowledgements

* Hugging Face Sentence Transformers
* MongoDB Atlas
* arXiv API
* OpenAlex API

---
