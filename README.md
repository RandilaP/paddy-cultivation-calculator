# Paddy Cultivation Analysis

This project analyzes paddy cultivation data to provide actionable insights. It processes data from a CSV file to calculate total yield, average resource usage, and identify the most and least productive fields. It also allows users to simulate changes in resource usage and observe their impact on productivity scores.

---

## Purpose

The purpose of this script is to:

1. Calculate the total cultivated area for paddy fields.
2. Determine the average water and fertilizer usage per hectare.
3. Compute productivity scores for fields and identify the most and least productive ones.
4. Simulate changes in water and fertilizer usage to analyze their impact on productivity.

---

## Instructions for Running the Code

1. **Set up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the Dataset**:
   - Ensure you have a CSV file named `paddy_data.csv` in the project directory.
   - The file should contain the following columns: `Field_ID`, `Area`, `Water_Usage`, `Fertilizer_Usage`, and `Soil_Quality`.

4. **Run the Script**:
   ```bash
   python paddy_analysis_csv.py
   ```

5. **Check the Results**:
   - Insights will be printed to the terminal.
   - An updated CSV file, `updated_paddy_data.csv`, will be generated with recalculated productivity scores.

---

## Key Findings and Recommendations

- **Key Findings**:
  - The total cultivated area can be determined efficiently, providing insights into land usage.
  - Productivity scores help identify fields needing optimization.
  - Simulations reveal how changes in resource usage impact field productivity.

- **Recommendations**:
  - Focus resources on fields with low productivity scores to improve yields.
  - Use the simulation tool to test resource allocation strategies before implementation.
  - Regularly update soil quality and resource usage data for accurate analysis.

---