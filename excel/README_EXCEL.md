
# Excel Data Preparation – Fathalla Market Project

## Overview
This folder contains the Excel-based preprocessing and data cleaning performed before moving to the Python and Power BI stages.  
The main goal of this phase was to transform the raw sales dataset (“مبيعات جملة.csv”) into a structured, validated, and ready-to-analyze dataset.

---

## Steps Performed

### 1. Table Creation and Structuring
- The raw CSV file was imported into Excel and formatted as a structured **Excel Table** named **`Fathalla_Data`**.
- The dataset included key fields such as:
  - Branch Code / Branch Name  
  - Department Code / Main Group / Subgroup  
  - Product Code / Barcode / Product Name  
  - Net Quantity Sold / Net Sales Value  
  - An unnamed numeric column (later identified as invoice-related data).

---

### 2. Data Type Verification
- Using **Power Query**, the data types for each column were reviewed and corrected.
  - Numeric fields were converted to `Decimal Number`.
  - Categorical fields were set to `Text`.
  - Any date fields (added later) were formatted as `Date`.

---

### 3. Column Name and Value Cleaning
- All column headers were checked for consistency and readability.
- Leading and trailing spaces were removed from every text field.
- Replaced all **slash (`/`) characters** with a **hyphen (`-`)** in names to maintain uniform formatting.
- Columns were renamed to use clear, descriptive Arabic names when applicable.

---

### 4. Handling the Unnamed Column
- An unlabeled numeric column was investigated by analyzing its distribution:
  - It contained integer-like sequential or repeated values.
  - The pattern matched expected **invoice numbers**.
- Therefore, this column was renamed to **`رقم الفاتورة`** (*Invoice Number*).

---

### 5. Adding the Date Column
- A new column was added to capture sales dates, named **`تاريخ البيع`** (*Sales Date*).
- Dates were generated systematically to simulate realistic sales transactions, ensuring temporal spread suitable for analysis in Power BI.

---

### 6. Saving and Output
- After validation, the cleaned table was saved in a separate worksheet named **`Fathalla_Clean`** within the Excel workbook.
- The final cleaned file was exported as:
```

excel/Fathalla_Clean.xlsx

```
- This file now represents the **official clean version** of the Fathalla Market dataset to be used in the next stages (Python → Power BI).

---

## Key Notes
- Power Query transformations were documented within Excel for reproducibility.  
- No missing value imputation or numerical aggregations were applied at this stage — that will be handled during the Python data processing.  
- All Arabic column names were preserved for context, as the dataset represents a real Egyptian retail environment.

---

## Next Steps
After completing this stage:
1. Move the cleaned Excel file to the `data/clean/` folder.
2. Use the Python script `src/cleaning.py` to perform further validation or transformations.
3. Load the resulting dataset into Power BI for modeling and visualization.

---

**Prepared by:** Data Team – Fathalla Market Project  
**Phase:** Excel Data Cleaning and Structuring  
**Version:** 1.0  
**Date:** October 2025
```

---
