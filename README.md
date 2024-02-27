# Beats.AI

Welcome to Beats.AI, an intuitive and efficient solution for training random forest models and generating predictions from your datasets. Our user-friendly tool is designed to streamline your data analysis and predictive modeling tasks

## Description

This project involves the development of a machine learning model that predicts heart rates based on physiological and environmental variables. The model is trained on a dataset containing diverse attributes derived from ECG recordings for various individuals.
The heart rate prediction model utilizes a Random Forest Regressor, chosen for its flexibility and ability to capture complex relationships in the data. The model undergoes data preprocessing, including handling missing values, feature engineering, and standardization.
The training dataset (train_data.csv) includes various features such as MEAN_RR, MEDIAN_RR, SDRR, RMSSD, and more. The model is trained to predict heart rates (HR) based on these features.

## Model Evaluation Metrics

The model's performance is evaluated using Mean Squared Error (MSE) and R-squared metrics on a separate test dataset

## Future Enhancements

Future improvements include fine-tuning the model, exploring additional features, and optimizing hyperparameters for increased accuracy and robustness.

## Technology Used

Python
Pandas
Scikit-Learn(Random Forest Regressor)
Latex
Matplotlib

## How to Use

To use the Heart Rate Prediction Model, follow these steps:
Start by cloning the repository and downloading all necessary files, including beatai.py, run.py, and the relevant CSV data files into your local directory. 
With beatai.py, you can effortlessly train a sophisticated random forest model using given train_data.csv file. This process results in the creation of a joblib file, encapsulating trained model. 
Once the model is trained, run.py comes into play. This script is adeptly crafted to utilize the trained model for predicting outcomes based on sample_test_data.csv. 
The predictions are conveniently saved in a result.csv file, ensuring easy access and analysis. 

## Conclusion

Our Project comes with a comprehensive Report.pdf, detailing the model's architecture, performance metrics, and insights to enhance your understanding and application of the model. 

## Contacts

If you encounter any challenges or have questions, our dedicated support team is readily available at 220120029@iitdh.ac.in or 220010043@iitdh.ac.in.



