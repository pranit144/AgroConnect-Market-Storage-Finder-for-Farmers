from flask import Flask, render_template, request, jsonify, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Load the CSV files
markets_df = pd.read_csv("df10.csv")
storage_df = pd.read_csv("main.csv")


@app.route('/', methods=['GET'])
def landing():
    """Landing page where users select whether to find markets or storage"""
    return render_template('index.html')


@app.route('/markets', methods=['GET', 'POST'])
def markets():
    """Market selection page that shows unique markets in a district when selected"""
    districts = sorted(markets_df['District Name'].dropna().unique())
    selected_district = None
    market_details = None

    if request.method == 'POST':
        selected_district = request.form.get('district')

        if selected_district:
            # Get district data
            district_data = markets_df[markets_df['District Name'] == selected_district]

            # Group by Market Name to get only unique markets
            # We use the first occurrence of each market for its details
            unique_markets = district_data.groupby('Market Name').first().reset_index()

            # Convert to dictionary for the template
            market_details = unique_markets.to_dict(orient='records')

    return render_template(
        'INDEX2.html',
        districts=districts,
        selected_district=selected_district,
        market_details=market_details
    )

@app.route('/storage', methods=['GET', 'POST'])
def storage():
    """Storage selection page with district dropdown and storage options display"""
    districts = sorted(storage_df['District'].dropna().unique())
    storage_options = []
    selected_district = None

    if request.method == 'POST':
        selected_district = request.form.get('district')
        # Filter storage options by selected district
        if selected_district:
            district_data = storage_df[storage_df['District'] == selected_district]

            # Clean data: handle missing values and convert numeric data
            storage_options = district_data[['Storage name', 'Address', 'Type', 'Capacity in MT']].copy()

            # Fill missing values with appropriate placeholders
            storage_options['Storage name'] = storage_options['Storage name'].fillna('Unnamed Storage')
            storage_options['Address'] = storage_options['Address'].fillna('Address not available')
            storage_options['Type'] = storage_options['Type'].fillna('General Storage')

            # Convert capacity to numeric and handle any non-numeric values
            storage_options['Capacity in MT'] = pd.to_numeric(storage_options['Capacity in MT'], errors='coerce')
            storage_options['Capacity in MT'] = storage_options['Capacity in MT'].fillna(0).astype(int)

            storage_options = storage_options.to_dict(orient='records')

    return render_template(
        'storage.html',
        districts=districts,
        storage_options=storage_options,
        selected_district=selected_district
    )


@app.route('/get_markets', methods=['POST'])
def get_markets():
    """AJAX endpoint to get markets for a selected district"""
    selected_district = request.form.get('district')
    markets = sorted(markets_df[markets_df['District Name'] == selected_district]['Market Name'].dropna().unique())
    return jsonify(markets)


if __name__ == '__main__':
    app.run(debug=True)