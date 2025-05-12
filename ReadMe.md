# 🌱 Crop Recommendation System

## 👨‍🎓 Student Information

| **Name**    | Haylemeskel Haylemariam Bantiyerga                                          |
| ----------- | --------------------------------------------------------------------------- |
| **ID No.**  | ETS0756/14                                                                  |
| **Section** | B                                                                           |
| **Email**   | [haylemeskelhaylemariam@gmail.com](mailto:haylemeskelhaylemariam@gmail.com) |

### Connect With Me

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Hayle-HB)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Hayle_HB)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/haylemeskel-haylemariam-b9212b298/)

---

## 📊 Project Overview

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/Hayle-HB/cropRecommendationSystem)](https://github.com/Hayle-HB/cropRecommendationSystem/issues)
[![GitHub Pull Requests](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Hayle-HB/cropRecommendationSystem/pulls)

### 📝 Description

This project implements a machine learning-based crop recommendation system designed to assist farmers and agricultural experts in determining the optimal crop selection based on soil and climate parameters. Using a Random Forest Classifier, the system achieves high accuracy in crop predictions, making it a valuable tool for agricultural decision-making.

### 🎯 Project Goals

1. Develop an accurate crop recommendation system
2. Provide clear insights into soil and climate parameters
3. Create an easy-to-use interface for farmers
4. Demonstrate practical application of machine learning in agriculture

## ✨ Key Features

- **Advanced Data Processing**

  - Intelligent handling of missing values
  - Duplicate removal
  - Outlier management
  - Data normalization

- **Comprehensive Analysis**

  - Detailed soil parameter analysis
  - Climate condition evaluation
  - Feature importance visualization
  - Statistical insights

- **High-Performance Model**
  - Random Forest Classifier
  - 99.5% prediction accuracy
  - Real-time recommendations
  - Model persistence

## 🛠️ Technical Stack

- **Programming Language:** Python 3.8+
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Visualization:** Matplotlib, Seaborn
- **Model Storage:** Joblib

## 📊 Dataset Information

The system utilizes a comprehensive agricultural dataset featuring:

- **Soil Parameters:**

  - Nitrogen (N) content
  - Phosphorus (P) content
  - Potassium (K) content
  - pH level

- **Climate Parameters:**

  - Temperature
  - Humidity
  - Rainfall

- **Crop Diversity:**
  - 22 different crop types
  - 2200+ data samples
  - Balanced class distribution

## 🚀 Getting Started

### Prerequisites

```bash
# Clone the repository
git clone https://github.com/Hayle-HB/cropRecommendationSystem.git
cd cropRecommendationSystem

# Install dependencies
pip install -r requirements.txt
```

### Running the Application

```bash
# Execute the main program
python main.py
```

## 📁 Project Structure

```
cropRecommendationSystem/
├── data/                      # Dataset directory
│   ├── Crop_recommendation (2).csv
│   └── cleanCrop_rec_DataSet.csv
├── Data Wrangling/           # Data preprocessing
│   └── DataWrangling.py
├── Analyze Data/             # Data analysis
│   └── AnalyzeData.py
├── ML_Model/                 # Machine learning model
│   ├── mode.py
│   └── trained_model.joblib
├── model_results/            # Model evaluation results
│   ├── test_report.txt
│   └── confusion_matrix.png
├── logs/                     # Application logs
├── main.py                   # Main application file
└── README.md                 # Project documentation
```

## 📈 Model Performance

### Accuracy Metrics

- **Overall Accuracy:** 99.5%
- **Cross-validation Score:** 99.3%
- **F1-Score:** 0.995

### Feature Importance

1. Humidity (21.93%)
2. Rainfall (21.25%)
3. Potassium (19.12%)
4. Phosphorus (15.30%)
5. Nitrogen (9.95%)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

⭐️ Developed by [Haylemeskel Haylemariam Bantiyerga](https://github.com/Hayle-HB)
