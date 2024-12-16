# NLP Summariser

**Index:**
1. [Problem Statement](#problem-statement)
2. [Approach](#approach)
3. [Results](#results)
   - [Training logs](#training-logs)
   - [Word cloud](#visualization-of-key-themesexrestaurant-reviews)
   - [Performance metrics (ROGUE and BLEU scores)](#performance-metrics)
4. [Challenges](#challenges)
5. [Instructions to run the REST API](#instructions-to-run-the-rest-api)
6. [Screenshots of REST API results](#api-results)

## Problem Statement
The objective of this project is to build a model that generates concise summaries of feedback or reviews, enabling the identification of key themes. This tool aims to help businesses or researchers quickly understand customer feedback and derive actionable insights.

Here's the link to my google colab notebook - https://colab.research.google.com/drive/1RIv7L6kGMDObuWA-n7Zzfre2bYmz_iHR?usp=sharing

## Approach
The following methodology was followed to solve the problem:

1. **Data Collection**:
   - Gathered a yelp dataset of reviews from kaggle.
   - Preprocessed the text by removing noise (e.g., special characters, stopwords).

2. **Model Selection and Training**:
   - Utilized the T5 model (t5-small)for its ability to generate concise and meaningful summaries from longer review texts.
   - Used the Hugging Face transformers library to utilize the pre-trained T5 model via the pipeline function(T5 is the model itself,
     while pipeline is an interface for quickly applying models like T5 to common NLP tasks)

3. **Evaluation**:
   - Evaluated summaries using ROUGE and BLEU metrics to assess quality.
   - Compared generated summaries with human-written summaries.

4. **Visualization of key themes in data**:
   - Generated word clouds that highlight the most frequently used words in the dataset
   - For deeper insights, reviews categorized under "Restaurants" were filtered and combined to generate a category-specific word cloud.

## Results
### Training Logs
![training logs](/images/training%20logs.png)
### Visualization of Key Themes(ex:restaurant reviews)
![word cloud](/images/restaurant%20word%20cloud.png)

### Performance Metrics
- **ROUGE Scores (Average):**
  - **ROUGE-1**: Precision: `0.9869`, Recall: `0.3455`, F-Measure: `0.4801`
  - **ROUGE-L**: Precision: `0.9540`, Recall: `0.3353`, F-Measure: `0.4655`
  ![rouge](/images/rouge%20score.png)
- **BLEU Score**: Average BLEU score across all reviews: `0.1556`
  ![bleu](/images/bleu%20score.png)

### Observations
- The model achieved higher precision but struggled with recall, indicating it performed well at identifying relevant information 
- Shorter and well-structured reviews were summarized more effectively compared to longer, unstructured ones.
- BLEU scores revealed that some summaries closely aligned with the original text, while others had lesser alignment.

## Challenges
1. **Data Quality**:
   - Challenge: The raw feedback data from the Yelp dataset contained noise and inconsistencies.
   - Solution: Implemented robust text preprocessing techniques like tokenization (splitting sentences into words), removal of stop words (using NLTK's stop word list containing words like "is," "and," "the"), and keyword filtering.

2. **Data Mapping**:
   - Challenge: We needed to assign a "feedback" category to each review, which required mapping reviews to their corresponding business categories from two large datasets (`yelp_academic_dataset_review.json` and `yelp_academic_dataset_business.json`). 
   - Solution: Created a mapping of `business_id` to categories by processing the business dataset and storing it in a dictionary.

3. **Model Training**:
   - Challenge: Training large transformer models required significant computational resources.
   - Solution: Used cloud-based GPUs (Google Colab) for model fine-tuning and batch processing (by processing batches of 5000 lines) to optimize resource usage.

4. **Evaluation**:
   - Challenge: Aligning machine-generated summaries with human-written summaries was subjective.
   - Solution: Used multiple evaluation metrics (ROUGE, BLEU) to ensure balanced assessment.


## Instructions to run the REST API
1. Clone the repository:
   ```bash
   git clone https://github.com/andarna1/NLPsummariser.git

2. Run the flask server (contains path to trained model saved from jupyter notebook)
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   pip install -r requirements.txt
   python3 main.py

3. Use Postman to test the REST API, make POST requests to `http://127.0.0.1:5000/summarize` and supply as input the product reviews you want to summarise.

## API Results

1. Product Review Example
![product](/images/product.png)
2. Restaurant Review Example
![restaurant](/images/restaurant.png)
3. News Article Summary
![news](/images/news.png)
