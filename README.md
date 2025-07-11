# Mathematics Score Prediction with Students Information


![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-Cloud-blue?style=for-the-badge&logo=microsoftazure&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-1.0.0-blue?style=for-the-badge&logo=github-actions&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0.0-blue?style=for-the-badge&logo=flask&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-5-orange?style=for-the-badge&logo=html5&logoColor=white)

 

## Overview
This project aims to predict students' mathematics scores based on various factors influencing their performance. By analyzing data related to students' academic performance, parental education levels, meal consumption, writing and reading scores, and whether or not they have received tuition, we employ machine learning techniques to build a predictive model. 
The project utilizes various technologies and methodologies to enhance the prediction accuracy, ensuring a robust analysis of the factors affecting students performance.


## Table of Contents
- 📚 [Overview](#overview)
- 📦 [Requirements](#requirements)
- ⚙️ [Installation](#installation)
- 🚀 [Usage](#usage)
- 🔍 [Methodology](#methodology)
- 📊 [Results](#results)
- 🐳 [CI/CD Pipeline with GitHub Actions and Azure](#CI/CD-Pipeline-with-github-actions-and-Azure)
- ✍️ [Authors](#authors)
- 🤝 [Contributing](#contributing)
- 📄 [License](#license)



## Requirements
![Requirements](https://img.shields.io/badge/Requirements-Listed-brightgreen?style=flat-square)
![Python Version](https://img.shields.io/badge/Python-3.10-blue?style=flat-square)



To install the required packages, run the following command:

     pip install -r requirements.txt

     
## Installation
To set up the project locally, follow these steps:

- Clone the repository:
   ```bash
   git clone https://github.com/Melina-Singh/Student_Info_ML.git
   cd Student_Info_ML
   
## Usage
-  Start the Flask application by running the following command in the project directory:
   ```bash
   python app.py
   use this link in local device 
   http://127.0.0.1:5000/predictdata




## Methodology
![Methodology](https://img.shields.io/badge/Methodology-Defined-brightgreen?style=flat-square)
![Data](https://img.shields.io/badge/Data-Prepared-blue?style=flat-square)
![EDA](https://img.shields.io/badge/EDA-Completed-brightgreen?style=flat-square)
![Model Training](https://img.shields.io/badge/Model%20Training-Executed-yellow?style=flat-square)
![HTML](https://img.shields.io/badge/HTML-5-orange?style=for-the-badge&logo=html5&logoColor=white)



The project follows a systematic approach to predict students' mathematics scores:

1. **Dataset**: The dataset, located in the `notebook` folder, contains features related to students' performance and external factors influencing their mathematics scores.

2. **Exploratory Data Analysis (EDA)**: Initial analysis involves visualizing distributions and identifying patterns to understand feature impacts on scores.

3. **Data Processing**: The dataset is split into training and testing sets, with categorical encoding, numerical scaling, and missing value handling for data integrity.

4. **Model Training**: Multiple machine learning algorithms are trained, and hyperparameter tuning is performed using techniques like Grid Search to optimize performance.

5. **Model Evaluation**: Performance is assessed using metrics such as Mean Absolute Error (MAE) and R-squared to ensure prediction accuracy.

6. **Predictive Pipeline and Flask Application**: A predictive pipeline is developed for seamless predictions, alongside a Flask app for user interaction, enabling input of features for score predictions.




## CI/CD Pipeline with GitHub Actions and Azure

![Azure](https://img.shields.io/badge/Azure-Deployed-0078D4?style=flat-square)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Enabled-2088FF?style=flat-square)

### Azure Cloud  
Azure Cloud is used as the deployment platform for hosting the application. It provides scalability, reliability, and seamless integration with GitHub Actions, enabling efficient application delivery to end users.

### GitHub Actions  
GitHub Actions is leveraged to automate the Continuous Integration and Continuous Deployment (CI/CD) pipeline. It monitors changes in the repository and automatically builds, tests, and deploys the application to Azure, ensuring rapid and reliable updates.

### Workflow  
The CI/CD workflow is triggered by pushes or pull requests to the `main` branch. It includes the following steps:
- **Build**: The application is prepared for deployment by setting up the required environment.
- **Test**: Automated tests are run to validate code functionality and ensure stability.
- **Linting**: Code quality is checked using tools like Flake8 or pylint to catch errors and enforce coding standards.
- **Deploy**: After passing all checks, the application is deployed to Azure Cloud, making the latest version available to users.


  

## Results
![Results](https://img.shields.io/badge/Results-Available-brightgreen?style=flat-square)
![HTML Flask](https://img.shields.io/badge/HTML%20Flask-Used-blue?style=flat-square)

A Simple Portal made by html

<img width="1732" height="964" alt="Screenshot 2025-07-12 015147" src="https://github.com/user-attachments/assets/c107f371-4dee-4af4-8025-f6347bcca4e5" />



## Authors
![Author](https://img.shields.io/badge/Author-Melina%20Singh-orange?style=for-the-badge)

- **Melina Singh** - Sole author and developer of the project, responsible for all aspects of the development of the project.




## Contributing
![Contributing](https://img.shields.io/badge/Contributing-Welcome-success?style=for-the-badge)


Contributions are welcome! If you have suggestions for improvements, feel free to fork the repository and submit a pull request. To contribute to this project, please follow these steps:

 - **Fork the Repository**: Click on the "Fork" button in the top right corner of the project page to create your own copy of the repository.
 - **Clone Your Fork**: Clone the forked repository to your local machine:
   ```bash
   git clone https://github.com/Melina-Singh/Student_Info_ML.git
   cd Student_Info_ML

## License
![License](https://img.shields.io/badge/License-GPL%20v3-blue?style=for-the-badge)


This project is licensed under the GNU General Public License (GPL). You can freely use, modify, and distribute this project, but any derivative work must also be distributed under the same license. For more details, please refer to the [LICENSE](LICENSE) file included in the repository.





