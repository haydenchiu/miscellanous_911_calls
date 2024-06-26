# CPS 911 Call Type X99 - Miscellaneous Capstone Project

## Contributors:
Hayden Chiu
Jarrett MacFarlane
Jingyi Liao
Yuxi Wang

## Mentor:
Dr. Jungyeul Pak

## Project Overview
This project aims to analyze 911 miscellaneous call data for the Calgary Police Service (CPS) to identify prevalent topics and provide actionable insights. By leveraging advanced Natural Language Processing (NLP) techniques, we aim to uncover patterns and trends that can help CPS better understand community issues and allocate resources effectively.

## Methods
1. Topic Modeling with LDA
Latent Dirichlet Allocation (LDA) is a generative probabilistic model used for topic modeling. It identifies topics by finding clusters of words that frequently occur together. This approach helps in understanding the broad themes present in the 911 miscellaneous call data.

2. Sentence Embedding & K-Means Clustering
We used two embedding models, `LaBSE` and `Mistral 7B Instruct`, to convert sentences into dense vector representations. K-Means clustering was then applied to group these vectors into clusters representing different topics.

3. Zero-shot Topic Modeling with BERTopic
BERTopic is an advanced topic modeling technique that leverages BERT embeddings for improved topic coherence. We used the `gte-large` embedding model for its high performance in clustering tasks and incorporated BERTopic's new LLM-based Representation Models for generating concise and relevant topic labels.

## Results
The analysis revealed several key insights:

Identification of common topics in 911 calls.

These insights can help CPS in making data-driven decisions for resource allocation and community interventions.

## Repository Structure
data/: Contains the 911 call data used for the analysis and model training. (Not disclosed)
notebooks/: Jupyter notebooks with detailed analysis and visualizations.
scripts/: Python scripts for preprocessing, modeling, and inference.
models/: Saved models and embeddings used in the project. (Not disclosed)
results/: Output files including topic summaries and visualizations. (Not disclosed)
docs/: Documentation files including the final report and presentation.

## Installation
To run the project locally, follow these steps:

1. Clone the repository:
```{bash}
git clone https://github.ubc.ca/MDS-CL-2023-24/calgary_capstone.git
cd calgary_capstone
```

2. Create a virtual environment and activate it:
```{bash}
python3 -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:
```{bash}
conda env update --file environment.yml --prune
```

4. Download the necessary models:
 - For training:
   1. Meta-Llama-3-8B-Instruct.Q8_0.gguf
 - For inference:
   1. Pre-trained BERTopic model included in `models/`
      (Not disclosed for public use. For CPS, there will be a private email for this kind of information transfer)

## Usage

1. Run inference using BERTopic modeling:
   - open and run `scripts/Inference.ipynb` on jupyternotebook
2. Train a new BERTopic model:
   - open and run `scripts/BERTopic_topic_modeling.ipynb` on jupyternotebook
3. Generate visualizations:
 - placeholder for wordclouds notebooks

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
We would like to thank the Calgary Police Service for providing the data and the support throughout this project.