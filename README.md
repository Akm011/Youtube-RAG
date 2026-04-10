youtube-rag/
│
├── pyproject.toml          # uv managed dependencies
├── uv.lock                 # lockfile
├── README.md
├── .env                    # API keys
├── .gitignore
│
├── src/
│   └── app/
│       ├── main.py         # FastAPI entrypoint
│       │
│       ├── core/           # Core configs
│       │   ├── config.py   # env variables
│       │   └── logger.py
│       │
│       ├── api/            # Routes layer
│       │   ├── routes/
│       │   │   ├── video.py    # process video endpoint
│       │   │   └── chat.py     # chat endpoint
│       │   └── deps.py         # dependency injection
│       │
│       ├── services/       # Business logic
│       │   ├── youtube_service.py     # transcript extraction
│       │   ├── embedding_service.py   # embeddings
│       │   ├── vector_store_service.py
│       │   ├── rag_service.py         # QA pipeline
│       │   └── memory_service.py      # chat memory
│       │
│       ├── models/         # Request/response schemas
│       │   ├── request.py
│       │   └── response.py
│       │
│       ├── db/             # Vector DB / storage
│       │   └── chroma_client.py
│       │
│       ├── utils/
│       │   ├── helpers.py      # video_id extraction etc
│       │   └── text_splitter.py
│       │
│       └── prompts/
│           └── rag_prompt.txt
│
├── frontend/
│   ├── streamlit_app.py    # simple UI
│   └── components/
│
├── tests/
│   ├── test_api.py
│   ├── test_services.py
│   └── test_rag.py
│
├── scripts/
│   ├── ingest_video.py     # CLI ingestion
│   └── run_server.sh
│
└── docker/
    ├── Dockerfile
    └── docker-compose.yml