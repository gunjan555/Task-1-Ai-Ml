# Task-1

# Task 1: Data Cleaning & Preprocessing (Titanic Dataset)

## Objective
The goal of this task was to learn how to *clean and preprocess raw data* before applying Machine Learning.  
We used the *Titanic dataset* to demonstrate the steps.

---

## 🛠 Tools Used
- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- scikit-learn  

---

## Steps Performed

### 1. Import & Explore Data
- Loaded Titanic dataset (titanic.csv)  
- Checked data types, shape, null values, and basic statistics  

### 2. Handle Missing Values
- Age → filled with *median*  
- Embarked → filled with *mode*  

### 3. Encode Categorical Variables
- Converted Sex and Embarked into numeric form using *One-Hot Encoding*  

### 4. Feature Scaling
- Standardized Age and Fare using *Z-score standardization*  

### 5. Outlier Detection & Removal
- Used *IQR method* to detect and remove outliers in Age  
- Reduced dataset size from *891 rows → 825 rows*  

### 6. Save Cleaned Dataset
- Final dataset saved as titanic_cleaned.csv  

---

## Results
- *Initial Shape:* (891, 12)  
- *Final Shape after cleaning:* (825, 13)  
- ✅ Cleaned dataset is ready for ML tasks  

---

## 📝 Interview Prep (Key Learnings)

1. *Types of Missing Data* → MCAR, MAR, MNAR  
2. *Categorical Handling* → One-hot encoding, Label encoding  
3. *Normalizati*
