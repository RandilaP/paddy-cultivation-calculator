import pandas as pd

# Function to calculate total yield
def calculate_total_yield(df):
    return df["Yield"].sum()

# Function to calculate average water and fertilizer usage per hectare
def calculate_average_usage(df):
    df["Water_Per_Hectare"] = df["Water_Usage"] / df["Hectares"]
    df["Fertilizer_Per_Hectare"] = df["Fertilizer_Usage"] / df["Hectares"]
    avg_water = df["Water_Per_Hectare"].mean()
    avg_fertilizer = df["Fertilizer_Per_Hectare"].mean()
    return avg_water, avg_fertilizer

# Function to find fields with the highest and lowest productivity scores
def find_extreme_productivity(df):
    highest = df.loc[df["Productivity_Score"].idxmax()]
    lowest = df.loc[df["Productivity_Score"].idxmin()]
    return highest, lowest

# Bonus: Function to simulate changes in water or fertilizer usage
def simulate_changes(df, field_id, water_change=0, fertilizer_change=0):
    df.loc[df["Field_ID"] == field_id, "Water_Usage"] += water_change
    df.loc[df["Field_ID"] == field_id, "Fertilizer_Usage"] += fertilizer_change
    # Recalculate productivity score (simplified example)
    df["Productivity_Score"] = (
        df["Yield"] / (df["Water_Usage"] + df["Fertilizer_Usage"]) * 100
    ).round(2)
    return df

# Main analysis
if __name__ == "__main__":
    # Load the data from the CSV file
    csv_file = "paddy_data.csv"  # Replace with the path to your CSV file
    df = pd.read_csv(csv_file)
    
    # Calculate total yield
    total_yield = calculate_total_yield(df)
    print(f"Total Yield: {total_yield} kg")
    
    # Calculate average water and fertilizer usage
    avg_water, avg_fertilizer = calculate_average_usage(df)
    print(f"Average Water Usage per Hectare: {avg_water:.2f} liters")
    print(f"Average Fertilizer Usage per Hectare: {avg_fertilizer:.2f} kg")
    
    # Find highest and lowest productivity fields
    highest, lowest = find_extreme_productivity(df)
    print(f"Highest Productivity Field:\n{highest}")
    print(f"Lowest Productivity Field:\n{lowest}")
    
    # Simulate changes (Bonus)
    field_id_to_change = 3
    updated_df = simulate_changes(df, field_id_to_change, water_change=50, fertilizer_change=5)
    print(f"Updated DataFrame:\n{updated_df}")
    
    # Save updated data back to a CSV file
    updated_df.to_csv("updated_paddy_data.csv", index=False)
    print("Updated data saved to 'updated_paddy_data.csv'")
