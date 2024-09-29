# Movie Recommender System

## Project Overview
The Movie Recommender System is a personalized recommendation engine designed to suggest movies based on users' past ratings and preferences. It employs content-based filtering techniques to analyze movie attributes and user behavior, delivering tailored suggestions

### Key Features
* **Personalized Recommendations:** Recommends movies based on users' historical ratings and preferences, analyzing movie attributes and computing similarities.
* **Genre Filtering:** Users can filter recommendations by specific genres, with the system dynamically adapting to their selections.
* **Similar Titles:** Provides similar movie suggestions based on content-based similarity metrics.
* **Web Application Integration:**  Powered by Django and FastAPI, providing a user-friendly interface and high-performance backend API for real-time recommendations.
* **Scalable Deployment:** Containerized with Docker for easy deployment and scalability across different environments.

## Technologies Used
* **Python:** Core programming language.
* **Keras/TensorFlow:** For developing and training recommendation models.
Sci-kit Learn: Utilized for data preprocessing and machine learning utilities.
* **NumPy/Pandas:** Data manipulation and handling.
* **Matplotlib:** Visualization of loss curves and training progress.
* **Django:** Web framework for building the user interface and integrating the recommendation engine.
* **FastAPI:** API framework for handling backend operations and serving recommendations.
* **Docker:** Containerization for easy deployment and scalability.

## Project Structure
```
.
├── Model/                  # Recommendation System Implementation
│   ├── dataset/
│   │   ├── movies.csv              # Dataset containing movie info
│   │   ├── ratings.csv             # Dataset containing user ratings
|   |   └── ...                     # Generated utililty files
│   ├── movie/                  # Generated utililty files and models
│   ├── recommend/              # Generated utililty files and models
│   ├── user/                   # Generated utililty files and models
│   └── Model.ipynb             # Jupyter Notebook for model
├── Movie Recommender/      # Generated dataset from facial images
│   ├── API/                    # Single image for each person in the database
│   │   ├── utils/                  # Utility files
│   │   ├── api.py                  # File for initialising a FASTAPI api
│   │   ├── Dockerfile              # Docker file for creating image for the api
│   │   └── requirements.txt        # Python dependencies for the api for Docker image
│   ├── APP/                    # Single image for each person in the database
│   │   ├── Dockerfile              # Docker file for creating image for the django web app
│   │   └── requirements.txt        # Python dependencies for the django web app for Docker image
│   │   └── ...                     # Django Web-App and utility files
│   └── docker-compose.yaml     # Docker Compose file for the entire Movie Recommender web app
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Installation
1. **Clone Repository**
   ```
   git clone https://github.com/Blaze-DSP/Movie-Recommender.git
   cd Movie-Recommender
   ```
2. **Install Dependencies (Optional, since dependencies will directly be installed in Docker image)**
   ```bash
   pip install -r requirements.txt
   ```
3.  **Run Movie Recommender System**
    ```bash
    cd Movie-Recommender
    docker-compose up --build
    ```

## Dataset
The dataset is uploaded on Google Drive. To use the dataset:

1. **Download the Dataset**
   Download the data.zip file from the [Google Drive](https://drive.google.com/file/d/1DWVNleOK8bDxbQRcpFMF9r6WnRGAUiEd/view?usp=drive_link) link.
2. **Extract the Dataset**
   After downloading, extract the zip file into the Model/dataset/ directory
3. **Dataset Structure**
   The extracted dataset should be organized into subfolders where each subfolder corresponds to an individual's images:
   ```
   dataset/
   │   ├── movies.csv              
   │   └── ratings.csv                               
   ```
   
This dataset is used for training the neural network for recommendation system.

## Usage
* **Access Web Interface:** Open your web browser and go to http://localhost:8000/
* **Register/Login:** Create an account or log in to start receiving movie recommendations.
* **Explore Movies:** Search, filter by genre, and discover personalized movie suggestions.
* **Get Recommendations:** View recommended movies based on your preferences and historical ratings.

## Future Enhancements
* Incorporate collaborative filtering alongside content-based filtering to improve recommendation accuracy by considering similar users' preferences in addition to content similarity.
* Allow users to rate movies and write reviews within the platform, using this data to enhance recommendations with sentiment analysis.
* Introduce a feature where users can collaborate and create movie playlists based on group preferences, integrating both content-based and collaborative filtering for group recommendations.
* Expand the web platform to a mobile app for more accessible user interaction, leveraging frameworks like React Native or Flutter.
* Integrate real-time face recognition using a camera feed.