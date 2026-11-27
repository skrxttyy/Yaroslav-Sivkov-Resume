# Yaroslav Sivkov

### Data Scientist · Machine Learning · Model Evaluation & Validation 
---
## Projects

- [**Concept Drift Detection in Streaming ML**](https://github.com/skrxttyy/Concept-Drift-Detection-in-Streaming-ML) — River, Online Learning, ADWIN, DDM, Page-Hinkley  
  • Developed a concept drift detection pipeline with online ML model adaptation. Implemented Test-Then-Train and benchmarked three detectors across 24 experimental runs using Prequential Accuracy, Detection Delay, F1 and FPR. Improved accuracy from 0.638 to 0.903 under abrupt drift.

- [**Counterfactual Prediction & Uplift**](https://github.com/skrxttyy/Counterfactual-Prediction-Uplift) — DoWhy, EconML, Causal Forests, Cross-Fitting  
  • Developed a pipeline for ATE/CATE estimation and comparative benchmarking of six causal inference models. Implemented Cross-Fitting, independent Train/Test splits and Fold-local Preprocessing. Evaluated performance using PEHE and ATE Error, achieving a PEHE of 0.318 with the PyTorch model.

- [**SupportRAG — RAG Evaluation & Monitoring Framework**](https://github.com/skrxttyy/Support-RAG) — Python, PyTorch, FAISS, Hugging Face, FastAPI, MLflow, DVC, Docker, Grafana  
  • Developed a RAG pipeline with hybrid BM25 + Dense Retrieval, RRF and Cross-Encoder Reranking. Implemented comprehensive evaluation using Recall@K, MRR, nDCG, Bootstrap CI and paired statistical tests. Added LLM-as-Judge with validation against human annotations using Cohen's Kappa, as well as Data Drift monitoring with MMD, PSI and OOV.

- [**ExplainBench — Explainability Benchmarking Framework**](https://github.com/skrxttyy/ExplainBench-Explainability-Benchmarking-Framework) — SHAP, LIME, Permutation Importance  
  • Developed a comparative benchmarking framework for SHAP, LIME and Permutation Importance. Implemented evaluation of explanation quality, consistency and stability, analyzing feature attribution reliability across different models and perturbations.

## Portfolio export

Project links are stored in `data/projects.json`. Generate the static page with `python scripts/export.py`; open `site/index.html`. Run checks with `python -m unittest discover -s tests -v`. Python standard library only. Existing resume text is preserved.
