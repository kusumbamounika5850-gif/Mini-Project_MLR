                          # Mini-Project_MLR

<h1 align="center">🏠 House Price Prediction Project</h1>

<p align="center">
Machine Learning Web Application using Linear Regression<br>
Built with Flask • Deployed on Render
</p>

<hr>

<h2>🙏 Acknowledgements</h2>

<ul>
<li><strong>📊 Dataset:</strong> House Sales in King County, USA</li>
<li><strong>🌍 Location:</strong> King County, Washington</li>
<li><strong>📅 Period:</strong> May 2014 – May 2015</li>
<li><strong>🏘 Records:</strong> 21,613 Houses</li>
<li><strong>👩 Contributor:</strong> Shreya Chaudhary (Kaggle)</li>
</ul>

<hr>

<h2>🛠 Technology Stack</h2>

<h3>Backend</h3>
<ul>
<li>🐍 Python</li>
<li>🌐 Flask</li>
<li>📚 Scikit-learn</li>
<li>🐼 Pandas</li>
<li>🔢 NumPy</li>
<li>📦 Pickle</li>
</ul>

<h3>Frontend</h3>
<ul>
<li>🎨 HTML5</li>
<li>💅 CSS3</li>
</ul>

<h3>Deployment</h3>
<ul>
<li>☁ Render</li>
<li>🔧 Git & GitHub</li>
</ul>

<hr>

<h2>📌 Project Overview</h2>

<p>
This project builds a <strong>Machine Learning web application</strong> 
to predict house prices based on property features such as size, location, 
condition, and time of sale.
</p>

<h3>🎯 Objective</h3>
<p>
To develop an automated system that predicts house prices using Linear Regression.
</p>

<h3>⭐ Key Features</h3>
<ul>
<li>🌐 User-friendly interface</li>
<li>⚡ Real-time predictions</li>
<li>📊 17 input features</li>
<li>☁ Live deployment</li>
</ul>

<hr>

<h2>📂 Dataset Description</h2>

<ul>
<li>🏘 Total Records: 21,613</li>
<li>📑 Features: 18 columns</li>
<li>📅 Period: 2014–2015</li>
<li>🌍 Location: King County</li>
</ul>

<h3>🔄 Data Preprocessing</h3>
<ul>
<li>✔ Handled missing values</li>
<li>📅 Extracted Year, Month, Day</li>
<li>🔢 Encoded categorical features</li>
<li>📊 Selected 17 relevant features</li>
</ul>

<hr>

<h2>🧮 Model Development</h2>

<h3>🤖 Model Used: Linear Regression</h3>

<p><strong>Mathematical Equation:</strong></p>

<p>
$$ \hat{y} = mX + c $$
</p>

<ul>
<li>ŷ = Predicted Price</li>
<li>m = Weights</li>
<li>X = Features</li>
<li>c = Intercept</li>
</ul>

<hr>

<h2>📉 Loss Functions Used</h2>

<h3>1️⃣ Mean Squared Error (MSE)</h3>

<p>$$
MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$</p>

<h3>2️⃣ Root Mean Squared Error (RMSE)</h3>

<p>$$
RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
$$</p>

<h3>3️⃣ Mean Absolute Error (MAE)</h3>

<p>$$
MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
$$</p>

<h3>4️⃣ R² Score</h3>

<p>$$
R^2 =
1 -
\frac{\sum (y_i - \hat{y}_i)^2}
{\sum (y_i - \bar{y})^2}
$$</p>

<h3>Cost Function (Least Squares)</h3>

<p>$$
J(m,c) =
\frac{1}{2n}
\sum_{i=1}^{n}
(y_i - \hat{y}_i)^2
$$</p>

<hr>

<h2>🌐 Web Application Routes</h2>

<ul>
<li><strong>/</strong> → Home page (Input Form)</li>
<li><strong>/predict</strong> → Prediction endpoint</li>
</ul>

<hr>

<h2>📝 Input Features</h2>

<ul>
<li>🛏 Bedrooms</li>
<li>🛁 Bathrooms</li>
<li>📐 sqft_living</li>
<li>🌳 sqft_lot</li>
<li>🏢 Floors</li>
<li>🌊 Waterfront</li>
<li>👀 View</li>
<li>🏠 Condition</li>
<li>⬆ sqft_above</li>
<li>⬇ sqft_basement</li>
<li>🏗 yr_built</li>
<li>🔧 yr_renovated</li>
<li>🏙 City</li>
<li>🌎 Country</li>
<li>📅 Year</li>
<li>📅 Month</li>
<li>📅 Day</li>
</ul>

<hr>

<h2>🚀 Deployment</h2>

<ul>
<li>Upload to GitHub</li>
<li>Connect repository to Render</li>
<li>Build: <code>pip install -r requirements.txt</code></li>
<li>Start: <code>gunicorn app:app</code></li>
</ul>

<p><strong>Live URL:</strong> https://house-price-predictor.onrender.com</p>

<hr>

<h2>📊 Example Prediction</h2>

<p><strong>Input:</strong></p>
<ul>
<li>Bedrooms: 4</li>
<li>Bathrooms: 4</li>
<li>Floors: 3</li>
<li>Waterfront: 1</li>
</ul>

<p><strong>Output:</strong></p>
<p>💰 Estimated Price: ₹ 2,484,185.65</p>

<hr>

<h2>🔮 Future Enhancements</h2>

<ul>
<li>🌲 Random Forest</li>
<li>⚡ Gradient Boosting</li>
<li>🧠 Neural Networks</li>
<li>📊 Add Data Visualizations</li>
<li>📱 Mobile App Version</li>
</ul>

<hr>

<h2>🎓 Conclusion</h2>

<ul>
<li>✅ Complete ML Pipeline</li>
<li>✅ Custom Linear Regression Implementation</li>
<li>✅ Flask Web Integration</li>
<li>✅ Cloud Deployment</li>
</ul>

<hr>

<h3 align="center">👩‍💻 Project By: K. Mounika</h3>

