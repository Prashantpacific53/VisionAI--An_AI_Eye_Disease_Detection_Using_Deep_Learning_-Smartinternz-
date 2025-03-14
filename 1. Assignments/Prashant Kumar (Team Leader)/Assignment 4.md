# Assignment No - 4
- Take any Dataset from Kaggle, data.gov.in, data.gov, etc
- Diplay the first 5 rows of the data using pandas. Copy it.

- Prompt:
This is a sample dataset. My complete data shape is data.shape.

Insert your 5 rows here.

Give me 100 real world questions based on my data which I can solve using Numpy, Pandas, Matplotlib, Seaborn.

# 🏥 COVID-19 Vaccination Data Analysis

## 📖 Project Overview
This project analyzes COVID-19 vaccination trends across different **States/UTs in India** using Python and data visualization techniques. The dataset provides insights into the number of vaccine doses administered, distribution across different population groups, and overall vaccination trends.

**Author:** Prashant Kumar 

## 📂 Dataset Information
The dataset contains **vaccination details of Indian states and union territories**, with columns such as:

- **State/UTs** – Name of the state or union territory.
- **Total Vaccination Doses** – Total number of vaccine doses administered.
- **Dose1** – Number of first doses given.
- **Dose 2** – Number of second doses given.
- **Dose 1 (15-18 Age Group)** – First dose administered for the 15-18 age group.
- **Dose 2 (15-18 Age Group)** – Second dose administered for the 15-18 age group.
- **Dose 1 (12-14 Age Group)** – First dose administered for the 12-14 age group.
- **Dose 2 (12-14 Age Group)** – Second dose administered for the 12-14 age group.
- **Precaution Dose (18-59 Age Group)** – Booster doses administered to the 18-59 age group.
- **Population** – Estimated population for each state/UT.

## 📊 Data Analysis & Visualization
The project includes various **data analysis and visualization techniques** using `Pandas`, `Matplotlib`, and `Seaborn`.

### 🔹 Key Analysis:
1. **Handling Missing Values**  
   - Checking for null values and handling data inconsistencies.
2. **Top 10 States with Highest Vaccinations**  
   - Visualized using a **bar chart**.
3. **Dose 1 vs. Dose 2 Distribution**  
   - Visualized using a **pie chart**.
4. **Correlation Between Vaccination Data**  
   - Analyzed using a **heatmap**.
5. **Vaccination Trends Across Top 5 States**  
   - Represented using a **line graph**.
6. **Distribution of Total Vaccination Doses**  
   - Analyzed using a **box plot**.

## 🚀 Technologies Used
- **Python**
- **Pandas** – Data manipulation
- **NumPy** – Numerical computations
- **Matplotlib** – Data visualization
- **Seaborn** – Statistical graphics







# 🔹 Step 1: Choose a Dataset
First, we select a dataset from Kaggle

COVID-19 Cases Dataset (Pandemic trends)
- https://surl.li/robwff

# 🔹 Step 2: Load & Understand the Dataset in Jupyter Notebook
Before solving any questions, analyze the dataset:

- Shape of data → How many rows & columns?
- Columns available → What information does it contain?
- Missing values? → Any data cleaning required?
  
**📌 Code to Load the Data**
```
import pandas as pd

#Load the dataset
df = pd.read_csv("C:/Users/prash/Downloads/COVID-19 India Statewise Vaccine Data.csv")

#Display dataset information
print("Dataset Shape:", df.shape)
print("\nColumn Names:", df.columns)
print("\nMissing Values:\n", df.isnull().sum())

#Display first 5 rows
df.head()

```
**Output of the Loaded Data**
```
Dataset Shape: (36, 10)

Column Names: Index(['State/UTs', 'Total Vaccination Doses', 'Dose1', 'Dose 2',
       'Dose 1 15-18', 'Dose 2 15-18', 'Dose 1 12-14', 'Dose 2 12-14',
       'Precaution 18-59', 'Population'],
      dtype='object')

Missing Values:
 State/UTs                  0
Total Vaccination Doses    0
Dose1                      0
Dose 2                     0
Dose 1 15-18               0
Dose 2 15-18               0
Dose 1 12-14               0
Dose 2 12-14               0
Precaution 18-59           0
Population                 0
dtype: int64
```


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>State/UTs</th>
      <th>Total Vaccination Doses</th>
      <th>Dose1</th>
      <th>Dose 2</th>
      <th>Dose 1 15-18</th>
      <th>Dose 2 15-18</th>
      <th>Dose 1 12-14</th>
      <th>Dose 2 12-14</th>
      <th>Precaution 18-59</th>
      <th>Population</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Andaman And Nicobar</td>
      <td>991264</td>
      <td>313284</td>
      <td>320383</td>
      <td>19208</td>
      <td>18860</td>
      <td>15124</td>
      <td>14042</td>
      <td>236936</td>
      <td>399001</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Andhra Pradesh</td>
      <td>110957430</td>
      <td>40645695</td>
      <td>43555744</td>
      <td>2535344</td>
      <td>2527613</td>
      <td>1523375</td>
      <td>1495445</td>
      <td>12054868</td>
      <td>91702478</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Arunachal Pradesh</td>
      <td>1924584</td>
      <td>861396</td>
      <td>748505</td>
      <td>59100</td>
      <td>44869</td>
      <td>40852</td>
      <td>28445</td>
      <td>81191</td>
      <td>1711947</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Assam</td>
      <td>50335778</td>
      <td>22550941</td>
      <td>20575569</td>
      <td>1262520</td>
      <td>972402</td>
      <td>999552</td>
      <td>602283</td>
      <td>2108179</td>
      <td>35998752</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bihar</td>
      <td>157293015</td>
      <td>62956601</td>
      <td>59160917</td>
      <td>6240650</td>
      <td>5348480</td>
      <td>4288630</td>
      <td>3403195</td>
      <td>12022637</td>
      <td>128500364</td>
    </tr>
  </tbody>
</table>
</div>


# 🔹 Step 3: 100 Questions Based on the Dataset
Here are **100 real-world questions** we can solve using *NumPy, Pandas, Matplotlib,* and *Seaborn*.

***1️⃣ Data Analysis (Pandas & NumPy)***

**📌 1. Basic Data Exploration (Pandas)**
- What are the total number of rows and columns in the dataset?
- What are the names of all the columns in the dataset?
- What is the datatype of each column?
- Are there any duplicate rows in the dataset?
- How many unique states/UTs are there in the dataset?
- What are the first five rows of the dataset?
- What are the last five rows of the dataset?
- What is the summary of the dataset using .describe()?
- How many missing values are there in each column?
- What percentage of the dataset has missing values?
  
**📌 2. Data Cleaning & Handling Missing Values**
- Which columns have missing values?
- How can we handle missing values in categorical columns?
- How can we handle missing values in numerical columns?
- Can we replace missing values with the mean/median/mode?
- How do we remove rows with missing values?
- How do we remove columns with too many missing values?
- Are there any inconsistent state names?
- How can we standardize state names to avoid inconsistencies?
- Are there any negative values in the dataset?
- How can we remove or correct negative values?
  
**📌 3. Data Filtering & Grouping**
- How many states have administered more than 5 million doses?
- How many states have administered less than 1 million doses?
- How many states have vaccinated more than 50% of their population?
- What is the average number of total doses administered per state?
- What is the total number of first doses administered across all states?
- What is the total number of second doses administered across all states?
- Which state has administered the most total doses?
- Which state has administered the least total doses?
- Which states have vaccinated more healthcare workers than frontline workers?
- What is the median number of precaution doses given across all states?

**📌 4. Statistical Analysis (Using NumPy & Pandas)**
- What is the mean number of first doses administered?
- What is the standard deviation of second doses administered?
- What is the maximum number of total doses administered?
- What is the minimum number of total doses administered?
- What is the 25th percentile of precaution doses?
- What is the 75th percentile of total doses administered?
- What is the correlation between first and second doses?
- What is the correlation between precaution doses and total doses?
- How many states fall within one standard deviation of the mean?
- How many states are outliers in terms of total doses administered?

**📌 5. Data Visualization (Using Matplotlib & Seaborn)**
- Can we create a bar chart showing total doses per state?
- Can we create a line chart for total vaccinations over time?
- Can we create a pie chart showing first vs. second vs. precaution doses?
- How does vaccine distribution vary across states? (bar plot)
- Can we create a scatter plot of first doses vs. second doses?
- Can we create a heatmap of correlation between different dose types?
- How does vaccine distribution vary for different population groups?
- What trends can we identify from a histogram of total doses?
- Which states have the highest and lowest total vaccinations? (horizontal bar plot)
- Can we visualize the missing values in the dataset?

**📌 6. Sorting & Aggregation**
- Can we sort states by total doses administered in descending order?
- Can we sort states by precaution doses in ascending order?
- Can we group states into "high", "medium", and "low" vaccination groups?
- What is the average number of first doses given per state?
- What is the sum of second doses given across all states?
- Can we find the top 5 states with the highest number of total doses?
- Can we find the bottom 5 states with the lowest number of total doses?
- How does the number of vaccinated healthcare workers compare across states?
- What is the median number of frontline workers vaccinated?
- Can we create a frequency table of total doses per state?

**📌 7. Advanced Insights & Real-World Impact**
- Which state has the highest ratio of second doses to first doses?
- Which state has the lowest ratio of precaution doses to total doses?
- Are there states that have vaccinated more people than their total population?
- Can we predict which states will reach full vaccination first?
- How does vaccination coverage compare between large and small states?
- Are states with more total doses administering proportionally more precaution doses?
- Can we estimate the total number of doses needed to vaccinate all of India?
- How does India's vaccination progress compare to global trends?
- What are the key factors influencing vaccination rates?
- Can we find anomalies or errors in the dataset?


***2️⃣ Data Visualization (Matplotlib & Seaborn)***

**📌 8. Comparing Categories**
- Which states have the highest number of healthcare workers vaccinated?
- Which states have the lowest number of frontline workers vaccinated?
- Which states have vaccinated the highest percentage of 18+ population?
- Which states have vaccinated the lowest percentage of 18+ population?
- How does vaccination coverage compare between urban and rural states?
- Which states have a higher proportion of second doses than first doses?
- How does the distribution of precaution doses vary across states?
- Are there states with unusually high or low vaccine distribution?
- How does India's overall vaccination compare to major states individually?
- Which states have a good balance between first, second, and precaution doses?

**📌 9. Advanced Data Manipulation**
- Can we create a new column for the percentage of people fully vaccinated?
- Can we calculate the percentage of precaution doses relative to total doses?
- How does the ratio of vaccinated vs. unvaccinated population look per state?
- Can we calculate the total number of vaccines left to administer?
- What is the percentage of second doses out of total doses given?
- What is the difference in first doses between the top and bottom states?
- Can we classify states into “high”, “medium”, and “low” vaccination groups?
- How many states have administered at least 1 million precaution doses?
- Can we create a new column for the ratio of second doses to first doses?
- Can we normalize vaccination numbers across different population sizes?

**📌 10. Predictive Analysis & Hypothetical Scenarios**
- If the current vaccination rate continues, when will full vaccination be achieved?
- What happens if the vaccination rate drops by 20%?
- How many doses are needed to reach full coverage in each state?
- Which states are on track to reach full vaccination first?
- What happens if precaution doses are doubled in the next month?
- What is the expected total vaccination coverage in 6 months?
- What happens if booster shots become mandatory?
- Can we estimate the vaccine wastage percentage based on current trends?
- If a new vaccine is introduced, how will it affect current distribution?
- Can we build a simple prediction model to estimate future vaccinations?


Here are the **Python code** to answer the **top questions** from **Assignment 4** using **Pandas, NumPy, Matplotlib,** and **Seaborn**.

**# 1. Total number of missing values**

*Input:*
```
print("\nTotal Missing Values:", df.isnull().sum().sum())

```
*Output:*
```
Total Missing Values: 0

```
**# 2. Total vaccinations across all states**

*Input:*
```
print("\nTotal Vaccination Count:", df["Total Vaccination Doses"].sum())
```
*Output:*
```
Total Vaccination Count: 2201473588
```
**# 3. State with highest and lowest vaccinations**

*Input:*
```
max_vac = df.loc[df["Total Vaccination Doses"].idxmax()]
min_vac = df.loc[df["Total Vaccination Doses"].idxmin()]
print("\nState with Highest Vaccinations:\n", max_vac)
print("\nState with Lowest Vaccinations:\n", min_vac)
```
*Output:*
```
State with Highest Vaccinations:
 State/UTs                  Uttar Pradesh
Total Vaccination Doses        392011174
Dose1                          154096960
Dose 2                         147866674
Dose 1 15-18                    14193665
Dose 2 15-18                    13227415
Dose 1 12-14                     8709857
Dose 2 12-14                     7876085
Precaution 18-59                36643273
Population                     231502578
Vaccination Rate                66.56382
Name: 33, dtype: object

State with Lowest Vaccinations:
 State/UTs                  Lakshadweep
Total Vaccination Doses         145313
Dose1                            56914
Dose 2                           56019
Dose 1 15-18                      2911
Dose 2 15-18                      2782
Dose 1 12-14                      1988
Dose 2 12-14                      1724
Precaution 18-59                 15990
Population                       66001
Vaccination Rate             86.232027
Name: 18, dtype: object
```

**# 4. Count of states with missing data**

*Input:*
```
print("\nNumber of States with Missing Data:", (df.isnull().sum(axis=1) > 0).sum())
```

*Output:*
```
Number of States with Missing Data: 0
```

**# 5. Average vaccinations per state**

*Input:*
```
print("\nAverage Vaccinations Per State:", df["Total Vaccination Doses"].mean())
```

*Output:*
```
Average Vaccinations Per State: 61152044.11111111
```

**# 6. Percentage of population vaccinated (at least one dose)**

*Input:*
```
df["Vaccination Rate"] = (df["Dose1"] / df["Population"]) * 100
print("\nVaccination Rate per State:\n", df[["State/UTs", "Vaccination Rate"]])
```

*Output:*
```
Vaccination Rate per State:
                                    State/UTs  Vaccination Rate
0                        Andaman And Nicobar         78.517096
1                             Andhra Pradesh         44.323442
2                          Arunachal Pradesh         50.316745
3                                      Assam         62.643674
4                                      Bihar         48.993325
5                                 Chandigarh         94.127578
6                               Chhattisgarh         58.872353
7   Dadra And Nagar Haveli And Daman And Diu         94.426077
8                                      Delhi         86.031897
9                                        Goa         89.031086
10                                   Gujarat         70.063717
11                                   Haryana         75.996004
12                          Himachal Pradesh         80.536478
13                         Jammu And Kashmir         66.287378
14                                 Jharkhand         53.142589
15                                 Karnataka         71.886628
16                                    Kerala         77.863369
17                                    Ladakh         75.597263
18                               Lakshadweep         86.232027
19                            Madhya Pradesh         63.696851
20                               Maharashtra         67.784104
21                                   Manipur         42.607540
22                                 Meghalaya         35.324221
23                                   Mizoram         60.036655
24                                  Nagaland         40.421567
25                                    Odisha         66.782944
26                                Puducherry         55.468910
27                                    Punjab         73.314363
28                                 Rajasthan         64.294114
29                                    Sikkim         82.053710
30                                Tamil Nadu         67.709529
31                                 Telangana         77.617914
32                                   Tripura         63.537492
33                             Uttar Pradesh         66.563820
34                               Uttarakhand         69.942665
35                               West Bengal         66.707286
```

**# 7. Correlation between population and total vaccinations**

*Input:*

```
print("\nCorrelation between Population and Vaccinations:\n", df[["Population", "Total Vaccination Doses"]].corr())
```

*Output:*
```
Correlation between Population and Vaccinations:
                          Population  Total Vaccination Doses
Population                 1.000000                 0.987285
Total Vaccination Doses    0.987285                 1.000000
```

**# 8. **Bar chart of top 10 states with highest vaccinations****

*Input:*
```
top_10 = df.nlargest(10, "Total Vaccination Doses")
plt.figure(figsize=(12, 6))
sns.barplot(x="Total Vaccination Doses", y="State/UTs", data=top_10, palette="coolwarm")
plt.title("Top 10 States with Highest Vaccinations")
plt.xlabel("Total Vaccinations")
plt.ylabel("States")
plt.show()
```
*Output:*

![Image](https://github.com/user-attachments/assets/7588b5f2-ba42-4a84-89ee-0e3340359ac1)



**# 9. **Pie chart of Dose 1 and Dose 2 distribution****

*Input:*
```
dose_distribution = df[["Dose1", "Dose 2"]].sum()
plt.figure(figsize=(6, 6))
plt.pie(dose_distribution, labels=["Dose 1", "Dose 2"], autopct="%1.1f%%", colors=["blue", "red"])
plt.title("Dose 1 vs Dose 2 Distribution in India")
plt.show()
```
*Output:*

![image](https://github.com/user-attachments/assets/f1078b1e-8f60-42a9-8ad8-d4d5a75e1186)



**# 10. **Heatmap of correlation matrix (Fixed)****

*Input:*
```
plt.figure(figsize=(6, 4))

# Select only numeric columns
numeric_df = df.select_dtypes(include=[np.number])

sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
```
*Output:*

![image](https://github.com/user-attachments/assets/90a56511-b25e-486e-bba9-aae82e591fe1)



**# 11. **Fixed Line Graph (Without "Date" Column)****

*Input:*
```
plt.figure(figsize=(12, 6))

top_5_states = df.nlargest(5, "Total Vaccination Doses")["State/UTs"]

for state in top_5_states:
    state_df = df[df["State/UTs"] == state]
    plt.plot(state_df["Total Vaccination Doses"], label=state)

plt.legend()
plt.xlabel("Data Points")
plt.ylabel("Total Vaccination Doses")
plt.title("Vaccination Trends in Top 5 States (Based on Total Doses)")
plt.show()
```
*Output:*

![image](https://github.com/user-attachments/assets/57f4d252-ae46-4c4c-89c9-ff49931e194f)



**# 12. **Boxplot for vaccine distribution****

*Input:*
```
plt.figure(figsize=(6, 4))
sns.boxplot(x=df["Total Vaccination Doses"])
plt.title("Distribution of Vaccination Doses Across States")
plt.show()
```
*Output:*

![image](https://github.com/user-attachments/assets/a7e5a61b-8d47-4d7b-8ed0-62bdd2dd8219)

***3️⃣ Statistical Analysis (NumPy & Pandas)***

**# 13. Mean, Median, Standard Deviation of Total Vaccinations**

*Input:*
```
print("\nMean Vaccinations:", df["Total Vaccination Doses"].mean())
print("Median Vaccinations:", df["Total Vaccination Doses"].median())
print("Standard Deviation:", df["Total Vaccination Doses"].std())
```
*Output:*
```
Mean Vaccinations: 61152044.11111111
Median Vaccinations: 40642649.5
Standard Deviation: 79455650.5531635
```

**# 14. Identify outliers using IQR method**

*Input:*
```
Q1 = df["Total Vaccination Doses"].quantile(0.25)
Q3 = df["Total Vaccination Doses"].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df["Total Vaccination Doses"] < (Q1 - 1.5 * IQR)) | 
              (df["Total Vaccination Doses"] > (Q3 + 1.5 * IQR))]
print("\nOutlier States Based on Vaccinations:\n", outliers)
```
*Output:*
```
Outlier States Based on Vaccinations:
         State/UTs  Total Vaccination Doses      Dose1     Dose 2  \
33  Uttar Pradesh                392011174  154096960  147866674   

    Dose 1 15-18  Dose 2 15-18  Dose 1 12-14  Dose 2 12-14  Precaution 18-59  \
33      14193665      13227415       8709857       7876085          36643273   

    Population  Vaccination Rate  
33   231502578          66.56382
```

**# 15. State with max difference between Dose 1 and Dose 2**

*Input:*
```
df["Dose Difference"] = abs(df["Dose1"] - df["Dose 2"])
max_diff_state = df.loc[df["Dose Difference"].idxmax()]
print("\nState with Max Difference Between Dose 1 & Dose 2:\n", max_diff_state)
```
*Output:*
```
State with Max Difference Between Dose 1 & Dose 2:
 State/UTs                  Maharashtra
Total Vaccination Doses      177977996
Dose1                         84665105
Dose 2                        71650189
Dose 1 15-18                   4119145
Dose 2 15-18                   3108854
Dose 1 12-14                   2891273
Dose 2 12-14                   1870754
Precaution 18-59               5188711
Population                   124904071
Vaccination Rate             67.784104
Dose Difference               13014916
15-18 Vaccination Rate        3.297847
12-14 Vaccination Rate        2.314795
Name: 20, dtype: object
```


**# 16. 75th percentile of total vaccinations**

*Input:*
```
print("\n75th Percentile of Total Vaccinations:", df["Total Vaccination Doses"].quantile(0.75))
```
*Output:*
```
75th Percentile of Total Vaccinations: 112148450.25
```

**# 17. Compare vaccination rate of 15-18 & 12-14 age groups**

*Input:*
```
df["15-18 Vaccination Rate"] = (df["Dose 1 15-18"] / df["Population"]) * 100
df["12-14 Vaccination Rate"] = (df["Dose 1 12-14"] / df["Population"]) * 100
print("\nVaccination Rate of 15-18 vs 12-14 Age Groups:\n", df[["State/UTs", "15-18 Vaccination Rate", "12-14 Vaccination Rate"]])
```
*Output:*
```
Vaccination Rate of 15-18 vs 12-14 Age Groups:
                                    State/UTs  15-18 Vaccination Rate  \
0                        Andaman And Nicobar                4.814023   
1                             Andhra Pradesh                2.764750   
2                          Arunachal Pradesh                3.452210   
3                                      Assam                3.507122   
4                                      Bihar                4.856523   
5                                 Chandigarh                4.983248   
6                               Chhattisgarh                3.835406   
7   Dadra And Nagar Haveli And Daman And Diu                4.070946   
8                                      Delhi                5.227563   
9                                        Goa                3.399098   
10                                   Gujarat                4.448720   
11                                   Haryana                4.008658   
12                          Himachal Pradesh                4.422572   
13                         Jammu And Kashmir                5.840561   
14                                 Jharkhand                3.980292   
15                                 Karnataka                4.046629   
16                                    Kerala                3.812368   
17                                    Ladakh                3.467221   
18                               Lakshadweep                4.410539   
19                            Madhya Pradesh                4.934716   
20                               Maharashtra                3.297847   
21                                   Manipur                3.190389   
22                                 Meghalaya                2.045305   
23                                   Mizoram                4.591254   
24                                  Nagaland                2.892999   
25                                    Odisha                4.661565   
26                                Puducherry                3.079736   
27                                    Punjab                3.663844   
28                                 Rajasthan                4.498030   
29                                    Sikkim                4.566585   
30                                Tamil Nadu                3.139571   
31                                 Telangana                4.518387   
32                                   Tripura                3.460799   
33                             Uttar Pradesh                6.131105   
34                               Uttarakhand                4.555363   
35                               West Bengal                3.567996   

    12-14 Vaccination Rate  
0                 3.790467  
1                 1.661215  
2                 2.386289  
3                 2.776630  
4                 3.337446  
5                 3.299541  
6                 3.341864  
7                 2.582568  
8                 3.542654  
9                 2.185623  
10                2.757983  
11                1.937488  
12                3.626065  
13                3.692448  
14                2.649925  
15                3.341213  
16                2.337122  
17                2.969789  
18                3.012076  
19                2.836345  
20                2.314795  
21                2.194331  
22                0.991463  
23                3.694516  
24                1.254755  
25                3.399208  
26                1.875581  
27                2.243033  
28                2.948306  
29                3.328019  
30                2.290564  
31                2.903307  
32                2.699310  
33                3.762315  
34                3.438552  
35                2.599200
```

***4️⃣ Advanced Insights***

**# 18. Vaccination trend in top 5 populated states**

*Input:*
```
top_5_pop = df.nlargest(5, "Population")
plt.figure(figsize=(12,6))
sns.barplot(x="Population", y="State/UTs", data=top_5_pop, palette="viridis")
plt.title("Top 5 Populated States and Vaccination Count")
plt.xlabel("Population")
plt.ylabel("States")
plt.show()
```
*Output:*
![image](https://github.com/user-attachments/assets/152aa685-b130-4b78-993a-f32cb410268b)


**# 19. Variation in precaution doses across states**

*Input:*
```
plt.figure(figsize=(12,6))
sns.barplot(x="Precaution 18-59", y="State/UTs", data=df.sort_values("Precaution 18-59", ascending=False), palette="magma")
plt.title("Precaution Dose Distribution Across States")
plt.xlabel("Precaution Doses")
plt.ylabel("States")
plt.show()
```
*Output:*
![image](https://github.com/user-attachments/assets/803a7567-1886-4392-a2da-e4cfcdf1ed3c)


**# 20. Percentage of 18-59 age group receiving precaution doses**

*Input:*
```
df["Precaution Rate"] = (df["Precaution 18-59"] / df["Population"]) * 100
print("\nPrecaution Dose Rate per State:\n", df[["State/UTs", "Precaution Rate"]])
```
*Output:*
```
Precaution Dose Rate per State:
                                    State/UTs  Precaution Rate
0                        Andaman And Nicobar        59.382307
1                             Andhra Pradesh        13.145629
2                          Arunachal Pradesh         4.742612
3                                      Assam         5.856256
4                                      Bihar         9.356111
5                                 Chandigarh         4.406929
6                               Chhattisgarh        17.858614
7   Dadra And Nagar Haveli And Daman And Diu        17.847227
8                                      Delhi        12.109882
9                                        Goa         4.071309
10                                   Gujarat        19.464176
11                                   Haryana         4.521501
12                          Himachal Pradesh        20.258550
13                         Jammu And Kashmir         6.434925
14                                 Jharkhand         3.420599
15                                 Karnataka         9.652365
16                                    Kerala         2.504678
17                                    Ladakh        24.199978
18                               Lakshadweep        24.226906
19                            Madhya Pradesh        11.914682
20                               Maharashtra         4.154157
21                                   Manipur         3.347708
22                                 Meghalaya         0.885209
23                                   Mizoram         6.179529
24                                  Nagaland         1.296480
25                                    Odisha        21.380002
26                                Puducherry        18.480605
27                                    Punjab         2.755337
28                                 Rajasthan         5.826025
29                                    Sikkim        24.057208
30                                Tamil Nadu         7.247720
31                                 Telangana        28.461791
32                                   Tripura         6.524819
33                             Uttar Pradesh        15.828451
34                               Uttarakhand        12.112564
35                               West Bengal        10.266443
```


# 📌 Project Structure
📁 COVID-19-Vaccine-Analysis

│── 📄 README.md

│── 📄 requirements.txt

│── 📄 analysis.py

│── 📂 data

│   ├── vaccination_data.csv

│── 📂 images

│   ├── bar_chart.png

│   ├── pie_chart.png

│   ├── heatmap.png

│   ├── line_graph.png

│   ├── boxplot.png

# 📢 Conclusion
This project provides a comprehensive analysis of India's COVID-19 vaccination data, highlighting trends and correlations between different vaccination metrics.

# 📌 Contributions & Feedback are Welcome!
📩 Feel free to reach out if you have any suggestions or improvements. 🚀
