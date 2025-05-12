# 🌱 Crop Recommendation System

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/haylemeskel/crop-recommendation)](https://github.com/Hayle-HB/cropRecommendationSystem/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/haylemeskel/crop-recommendation)](https://github.com/Hayle-HB/cropRecommendationSystem)

## 📝 Description

A machine learning-based crop recommendation system that helps farmers and agricultural experts determine the most suitable crop to grow based on various soil and climate parameters. The system uses a Random Forest Classifier to predict crop recommendations with high accuracy.

## ✨ Features

- **Data Preprocessing**: Handles missing values, removes duplicates, and manages outliers
- **Exploratory Data Analysis**: Comprehensive analysis of soil and climate parameters
- **Machine Learning Model**: Random Forest Classifier with 99.5% accuracy
- **Model Evaluation**: Detailed performance metrics and visualizations
- **Feature Importance Analysis**: Identifies key factors affecting crop selection
- **Easy-to-use Interface**: Simple command-line interface for predictions

## 🛠️ Technologies Used

- Python 3.8+
- Pandas & NumPy for data manipulation
- Scikit-learn for machine learning
- Matplotlib & Seaborn for visualization
- Joblib for model persistence

## 📊 Dataset

The system uses a comprehensive dataset containing:

- Soil parameters (N, P, K, pH)
- Climate parameters (temperature, humidity, rainfall)
- 22 different crop types
- 2200+ samples

## 🚀 Getting Started

### Prerequisites

```bash
pip install -r requirements.txt
```

### Installation

1. Clone the repository:

```bash
git clone https://github.com/haylemeskel/crop-recommendation.git
cd crop-recommendation
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the complete workflow:

```bash
python main.py
```

## 📁 Project Structure

```
crop-recommendation/
├── data/
│   ├── Crop_recommendation (2).csv
│   └── cleanCrop_rec_DataSet.csv
├── Data Wrangling/
│   └── DataWrangling.py
├── Analyze Data/
│   └── AnalyzeData.py
├── ML_Model/
│   ├── mode.py
│   └── trained_model.joblib
├── model_results/
│   ├── test_report.txt
│   └── confusion_matrix.png
├── logs/
├── main.py
└── README.md
```

## 📈 Model Performance

- **Accuracy**: 99.5%
- **Top Features**:
  1. Humidity (21.93%)
  2. Rainfall (21.25%)
  3. Potassium (19.12%)
  4. Phosphorus (15.30%)
  5. Nitrogen (9.95%)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📫 Student Name

**Haylemeskel Haylemariam Bantiyerga**  
Section: B  
Email: [haylemeskelhaylemariam@gmail.com](mailto:haylemeskelhaylemariam@gmail.com)

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Hayle-HB)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Hayle_HB)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/haylemeskel-haylemariam-b9212b298/)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

⭐️ From [Haylemeskel](https://github.com/haye-HB)
