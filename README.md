<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>

  <h1>🎯 Student Math Score Prediction - Machine Learning Project</h1>
  <p>
    This project aims to predict the <strong>math score</strong> of students based on various academic and demographic features. 
    It showcases a full <strong>machine learning workflow</strong>, from data preprocessing and EDA to feature engineering and model evaluation.
  </p>

  <div class="section">
    <h2>📂 Dataset Description</h2>
    <table>
      <tr>
        <th>Column</th>
        <th>Description</th>
      </tr>
      <tr><td>gender</td><td>Student's gender (<code>male</code> / <code>female</code>)</td></tr>
      <tr><td>race_ethnicity</td><td>Student group based on race/ethnicity</td></tr>
      <tr><td>parental_level_of_education</td><td>Parent's highest education level</td></tr>
      <tr><td>lunch</td><td>Type of lunch (<code>standard</code> / <code>free/reduced</code>)</td></tr>
      <tr><td>test_preparation_course</td><td>Completion of test preparation course</td></tr>
      <tr><td>reading_score</td><td>Reading test score</td></tr>
      <tr><td>writing_score</td><td>Writing test score</td></tr>
      <tr><td><strong>math_score</strong></td><td><strong>Target variable - score in mathematics</strong></td></tr>
    </table>
  </div>

  <div class="section">
    <h2>📝 Sample Dataset</h2>
    <table>
      <tr>
        <th>gender</th><th>race_ethnicity</th><th>parental_level_of_education</th><th>lunch</th>
        <th>test_preparation_course</th><th>reading_score</th><th>writing_score</th><th>math_score</th>
      </tr>
      <tr><td>female</td><td>group B</td><td>bachelor's degree</td><td>standard</td><td>none</td><td>72</td><td>74</td><td>72</td></tr>
      <tr><td>female</td><td>group C</td><td>some college</td><td>standard</td><td>completed</td><td>90</td><td>88</td><td>69</td></tr>
      <tr><td>female</td><td>group B</td><td>master's degree</td><td>standard</td><td>none</td><td>95</td><td>93</td><td>90</td></tr>
      <tr><td>male</td><td>group A</td><td>associate's degree</td><td>free/reduced</td><td>none</td><td>57</td><td>44</td><td>47</td></tr>
      <tr><td>male</td><td>group C</td><td>some college</td><td>standard</td><td>none</td><td>78</td><td>75</td><td>76</td></tr>
    </table>
  </div>

  <div class="section">
    <h2>🎯 Project Objectives</h2>
    <ul>
      <li>📊 Conduct Exploratory Data Analysis (EDA) to understand distributions and correlations.</li>
      <li>🧹 Preprocess data with encoding, scaling, and transformation techniques.</li>
      <li>🧠 Train and evaluate multiple regression models to predict <code>math_score</code>.</li>
      <li>📈 Evaluate models using R², MAE, and RMSE metrics.</li>
    </ul>
  </div>

  <div class="section">
    <h2>🧪 Machine Learning Techniques Applied</h2>
    <ul>
      <li><strong>Categorical Encoding:</strong> Label & One-Hot Encoding</li>
      <li><strong>Feature Engineering:</strong> Derived features & normalization</li>
      <li><strong>Multiple Regression Models:</strong> Tried various ML regressors</li>
      <li><strong>Evaluation Metrics:</strong> R² Score, MAE, RMSE</li>
    </ul>
  </div>

  <div class="section">
    <h2>📈 Key Insights</h2>
    <ul>
      <li>📚 Students who completed the test preparation course generally scored higher.</li>
      <li>✍️ Reading and writing scores are strongly correlated with math scores.</li>
      <li>🎓 Parental education and lunch type influence student performance.</li>
    </ul>
  </div>

  <div class="section">
    <h2>💻 Technologies Used</h2>
    <ul>
      <li><strong>Python</strong> (Jupyter Notebook)</li>
      <li><strong>Pandas, NumPy</strong> – Data manipulation</li>
      <li><strong>Matplotlib, Seaborn</strong> – Visualizations</li>
      <li><strong>Scikit-learn</strong> – Machine learning</li>
      <li><strong>Flask</strong> – Web app deployment (optional)</li>
    </ul>
  </div>

  <div class="section">
    <h2>▶️ How to Run</h2>
    <ol>
      <li>Clone the repository or download the notebook file.</li>
      <li>Install dependencies:
        <pre><code>pip install -r requirements.txt</code></pre>
      </li>
      <li>Run the notebook step-by-step in Jupyter.</li>
      <li>Optional: Start Flask app using:
        <pre><code>python app.py</code></pre>
      </li>
    </ol>
  </div>

  <div class="section">
    <h2>📬 Feedback & Contributions</h2>
    <p>Feel free to fork the repo, contribute, or share your suggestions!</p>
  </div>

  <div class="section">
    <h2>📜 License</h2>
    <p>This project is licensed under the <strong>MIT License</strong>.</p>
  </div>

</body>
</html>
