import os
import pandas as pd

def convert_cricket_data(data, year, category):
    # Split input text into lines
    lines = data.strip().split("\n")
    
    formatted_data = []
    
    i = 0
    while i < len(lines):
        if lines[i].strip().isdigit():  # Detect the rank number
            rank = lines[i].strip()
            player_name = lines[i + 2].strip()
            team = lines[i + 3].strip()
            stats = lines[i + 4].strip()
            
            # Process the stats
            stats_values = stats.split("\t")
            print(stats_values)
            
            # Ensure correct format (position, player + team, matches, innings, NO, runs, HS, avg, BF, SR, 100s, 50s, 4s, 6s, year)
            formatted_line = f"{rank},{player_name}{team},{stats_values[1]},{stats_values[2]},{stats_values[3]},{stats_values[0]},{','.join(stats_values[4:])},{year}"
            formatted_data.append(formatted_line)
            
            i += 5  # Move to next entry
        else:
            i += 1
    
    return "\n".join(formatted_data)

def process_file(input_file, output_file, year, category):
    if os.path.exists(input_file):
        with open(input_file, 'r', encoding='utf-8') as f:
            data = f.read()
        
        formatted_data = convert_cricket_data(data, year, category)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(formatted_data)
        
        print(f"Processed {input_file} -> {output_file}")
    else:
        print(f"File not found: {input_file}")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    year = 2024
    
    input_files = {
        "batting": os.path.join(script_dir, "Data/2024/Season_Data/batting_2024.csv"),
        "bowling": os.path.join(script_dir, "Data/2024/Season_Data/bowling_2024.csv")
    }
    
    output_files = {
        "batting": os.path.join(script_dir, "Data/2024/Season_Data/formatted_batting_2024.csv"),
        "bowling": os.path.join(script_dir, "Data/2024/Season_Data/formatted_bowling_2024.csv")
    }
    
    for category in input_files:
        process_file(input_files[category], output_files[category], year, category)

if __name__ == '__main__':
    main()