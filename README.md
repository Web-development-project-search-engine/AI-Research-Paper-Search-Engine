# 🧠 AI Research Paper Search Engine

A semantic search engine for research papers powered by transformer-based embeddings. This project enables users to search research papers using natural language queries and retrieves the most relevant results based on meaning rather than exact keyword matches.

---

## 🚀 Features

* 🔍 **Semantic Search** using transformer models (MiniLM)
* 🧠 **Context-aware retrieval** (understands meaning, not just keywords)
* ⚡ **Fast search** using precomputed embeddings
* 🗄️ **MongoDB Atlas integration** for scalable storage
* 🧹 **Optimized preprocessing** tailored for transformer models
* 🧑‍🔬 Search based on **title, abstract, and authors**
* 📊 Ranked results using **cosine similarity**

---

## 🧠 How It Works

1. Research papers are collected and stored in JSON format.
2. Text fields (title, abstract, authors) are cleaned using light preprocessing.
3. A transformer model converts each paper into a numerical vector (embedding).
4. These embeddings are stored in the database.
5. When a user enters a query:

   * The query is converted into an embedding
   * Cosine similarity is computed against stored embeddings
   * Top matching papers are returned

---

## 🏗️ Project Structure

```
AI-Research-Paper-Search-Engine/
│
├── app.py                  # Flask app (entry point)
├── load_data.py            # Data preprocessing & embedding storage
│
├── database/
│   └── db.py               # MongoDB connection and operations
│
├── preprocessing/
│   └── clean_text.py       # Text cleaning logic
│
├── search/
│   ├── vectorizer.py       # Loads embeddings from DB
│   ├── search_engine.py    # Core search logic
│   └── similarity.py       # Cosine similarity (optional)
│
├── templates/              # HTML templates (UI)
├── static/                 # CSS / JS files
├── papers.json             # Dataset
└── README.md
```

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Machine Learning:** Sentence Transformers (MiniLM)
* **Database:** MongoDB Atlas
* **Frontend:** HTML, CSS
* **Libraries:** NumPy, Scikit-learn

---

## 🤖 Model Used

* **Model:** all-MiniLM-L6-v2
* **Type:** Transformer-based sentence embedding model
* **Output:** 384-dimensional vector representations
* **Purpose:** Capture semantic meaning of text

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

### 5️⃣ Load Data into MongoDB

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

## 📊 Example Query

* "AI in healthcare"
* "natural language processing transformers"
* "robotics reinforcement learning"

---

## 🔥 Key Improvements Over Traditional Search

| Feature                | TF-IDF | This Project |
| ---------------------- | ------ | ------------ |
| Keyword Matching       | ✅      | ✅            |
| Semantic Understanding | ❌      | ✅            |
| Context Awareness      | ❌      | ✅            |
| Synonym Handling       | ❌      | ✅            |

---

## ⚡ Future Enhancements

* 🔍 Hybrid search (TF-IDF + Transformers)
* 📈 Display similarity scores in UI
* 🎯 Filtering by author/year/category
* 🚀 MongoDB vector search integration
* 🌐 Deployment

---

## 🔐 Security Notes

* `.env` file is excluded from version control
* Sensitive credentials (MongoDB URI) are not exposed

---

## 🤝 Contributing

Feel free to fork the repository and submit pull requests for improvements!

---

## ⭐ Acknowledgements

* Hugging Face Sentence Transformers
* MongoDB Atlas
* arXiv dataset for research papers

---
