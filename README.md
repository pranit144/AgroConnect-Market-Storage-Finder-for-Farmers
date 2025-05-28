# 🌾 Farmer Resource Finder

**Farmer Resource Finder** is a web-based platform that helps farmers discover local markets to sell their produce and find suitable storage facilities to preserve their harvest.

---

## 🚀 Features

- 🧭 **Landing Page** with clear navigation options to search for markets or storage.
- 🏪 **Market Finder**:
  - Select a district to view available markets.
  - Displays market name, type, primary commodities, trading volume, and days.
- 🏬 **Storage Finder**:
  - Select a district to find storage facilities.
  - Displays storage name, type, capacity in metric tons, and address.
- 📊 **CSV-based Data Integration** for dynamic district-based filtering.
- 🎨 Responsive UI using HTML, CSS, Font Awesome, and JQuery.

---

## 🗂️ Project Structure

farmer-resource-finder/
│
├── app.py # Main Flask application
├── df10.csv # Market dataset
├── main.csv # Storage dataset
├── templates/
│ ├── index.html # Landing page
│ ├── INDEX2.html # Market search and results
│ └── storage.html # Storage search and results
├── static/ # Static files (optional for custom CSS/JS)
└── README.md # Project documentation

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. 🐍 Install Python dependencies

```bash
pip install flask pandas
2. 📁 File Requirements
Ensure you have the following files in the correct locations:

df10.csv – Contains market information (columns like District Name, Market Name, Market Type, Commodity, Market Days, Volume)

main.csv – Contains storage data (columns like District, Storage name, Address, Type, Capacity in MT)

templates/ – Contains HTML files (index.html, INDEX2.html, storage.html)

3. ▶️ Run the Application
bash
Copy
Edit
python app.py
Access the app at: http://127.0.0.1:5000/

💡 How It Works
Landing Page (/)
Provides options to find markets or storage.

Routes to /markets or /storage.

Market Finder (/markets)
Displays a dropdown of districts.

Upon selection, filters and shows unique markets in that district.

Storage Finder (/storage)
Dropdown of districts.

On form submission, lists available storage facilities by type and capacity.

📦 Sample Data Format
df10.csv
District Name	Market Name	Market Type	Commodity	Market Days	Volume
Pune	Market A	Retail	Onion	Mon-Wed	High

main.csv
District	Storage name	Address	Type	Capacity in MT
Pune	Storage A	123 Farm Lane, Pune	Cold	500

🎯 Future Improvements
🔍 Add search filters like commodity type or market volume.

📱 Make fully mobile-friendly using Bootstrap or Tailwind CSS.

📊 Dashboard for statistics and reports.

🌐 Integration with real-time government APIs.

🙌 Contribution
Feel free to fork this project, open issues, or submit pull requests to improve the functionality or design!

🧑‍💻 Author
Farmer Resource Finder Project – 2025

Made with ❤️ to support the agricultural community.

📄 License
This project is open-source and available under the MIT License.
