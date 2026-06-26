# Data Cleaning & Reporting Automation

## 📌 Project Overview

This project automates the process of cleaning sales data and generating interactive reports using Python and Power BI. It demonstrates how raw data containing missing values and duplicate records can be transformed into clean, reliable data for business analysis.

---

## 🎯 Objectives

- Clean and preprocess raw sales data.
- Remove duplicate records.
- Handle missing values.
- Generate a cleaned dataset automatically.
- Build an interactive Power BI dashboard.
- Improve reporting accuracy and efficiency.

---

## 🛠️ Tools & Technologies

- Python
- Pandas
- Microsoft Excel
- Power BI Desktop
- Power Query

---

## 📂 Project Files

```
Data-Cleaning-Reporting-Automation/
│
├── Sales_Dataset.xlsx
├── Cleaned_Sales_Dataset.xlsx
├── data_cleaning.py
├── Data_Cleaning_Reporting_Automation.pbix
├── Project_Report.docx
└── README.md
```

---

## 📊 Dataset

The dataset contains customer sales information with the following columns:

- CustomerID
- Name
- Age
- Gender
- Product
- Region
- Sales
- Revenue

The raw dataset contains:
- Missing values
- Duplicate records
- Inconsistent data

The Python script automatically cleans the data and creates a new cleaned dataset.

---

## 🧹 Data Cleaning Process

- Removed duplicate records
- Filled missing Age values
- Replaced missing Gender values with "Unknown"
- Generated a cleaned Excel dataset

---

## 📈 Power BI Dashboard

### KPI Cards

- Total Customers
- Total Sales
- Total Revenue
- Average Revenue

### Visualizations

- Sales by Product (Bar Chart)
- Revenue by Region (Pie Chart)
- Customer Distribution by Gender (Donut Chart)
- Sales Trend (Line Chart)

### Interactive Slicers

- Product
- Region
- Gender

---

## 🚀 How to Run

1. Open the Python script (`data_cleaning.py`).
2. Run the script to generate `Cleaned_Sales_Dataset.xlsx`.
3. Open Power BI Desktop.
4. Import the cleaned dataset.
5. Create KPI cards, charts, and slicers.
6. Save the dashboard as `Data_Cleaning_Reporting_Automation.pbix`.

---

## 📋 Business Insights

- Duplicate records were successfully removed.
- Missing values were handled automatically.
- Clean data improves reporting accuracy.
- Interactive dashboards support better business decisions.

---

## 🔮 Future Enhancements

- Automatic scheduled data refresh
- Email report automation
- Real-time dashboard integration
- Machine Learning for anomaly detection

---

## 👩‍💻 Author

**Tejasree Jami**

---

## ⭐ Conclusion

This project demonstrates how Python and Power BI can be combined to automate data cleaning and create interactive business reports. It improves data quality, reduces manual effort, and helps organizations make informed decisions through accurate reporting.
