import sys
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

# Loading the test data
test_data_path = sys.argv[1] if len(sys.argv) > 1 else "sample_test_data.csv"
   #allow pandas to read data
test_data = pd.read_csv(test_data_path)

# Data Preprocessing for Test Data
# Drop irrelevant columns (same preprocessing steps as training data)
test_data_processed = test_data.drop(columns=['uuid', 'datasetId'])
test_data_processed = pd.get_dummies(test_data_processed, columns=['condition'])
test_data_processed = test_data_processed.dropna()

# Load the pre-trained model
rf_model = joblib.load('heart_rate_prediction_rf_model.joblib')

# Suppress the warning about feature names
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Make predictions on the test data
pred = rf_model.predict(test_data_processed)

# Create a DataFrame with only 'uuid' and 'HR' columns
result_df = pd.DataFrame({
    'uuid': test_data['uuid'],  # Include 'uuid' column
    'Predicted_HR': pred  # Add the predicted heart rate column
})

# Save the result to a CSV file
result_df.to_csv('results.csv', index=False)
print("Predictions saved to 'results.csv'")