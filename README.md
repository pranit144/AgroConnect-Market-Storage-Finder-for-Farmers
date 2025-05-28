
# 🌾 Farmer Resource Finder

**Farmer Resource Finder** is a web-based platform that enables farmers to discover nearby markets to sell their produce and find appropriate storage facilities to preserve their harvest. Built using **Flask** and **CSV-based datasets**, the application empowers farmers with easy access to critical post-harvest resources.

---

## 🚀 Features

- 🧭 **Landing Page** with intuitive navigation for market and storage searches.
- 🏪 **Market Finder**:
  - Choose a district to view local markets.
  - Displays market name, type, commodities traded, market days, and volume.
- 🏬 **Storage Finder**:
  - Select a district to list storage options.
  - Displays storage name, type, capacity (MT), and address.
- 📊 **CSV-Based Data Integration**:
  - Dynamic district-based filtering using Pandas.
- 🎨 **Responsive UI**:
  - Built using HTML, CSS, Font Awesome, and JQuery.

---

## 🗂️ Project Structure

```
farmer-resource-finder/
│
├── app.py                 # Main Flask application
├── df10.csv               # Market dataset
├── main.csv               # Storage dataset
│
├── templates/             # HTML templates
│   ├── index.html         # Landing page
│   ├── INDEX2.html        # Market search and results
│   └── storage.html       # Storage search and results
│
├── static/                # (Optional) Static files for CSS/JS
└── README.md              # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. 🐍 Install Dependencies
Make sure Python is installed, then run:
```bash
pip install flask pandas
```

### 2. 📁 Ensure the Following Files Exist

- **df10.csv** – Market dataset with columns:
  ```
  District Name, Market Name, Market Type, Commodity, Market Days, Volume
  ```
- **main.csv** – Storage dataset with columns:
  ```
  District, Storage name, Address, Type, Capacity in MT
  ```
- **templates/** – Folder containing HTML files:
  - `index.html`
  - `INDEX2.html`
  - `storage.html`

### 3. ▶️ Run the Application
```bash
python app.py
```

Visit the app at:  
**http://127.0.0.1:5000/**

---

## 💡 How It Works

### 🏠 Landing Page (`/`)
- Offers two options: **Find Markets** or **Find Storage**
- Routes to `/markets` and `/storage`

### 🏪 Market Finder (`/markets`)
- Dropdown of districts
- On selection, filters and displays matching market details

### 🏬 Storage Finder (`/storage`)
- Dropdown of districts
- On form submit, shows available storage with capacity and location

---

## 📦 Sample Data Format

**df10.csv**
| District Name | Market Name | Market Type | Commodity | Market Days | Volume |
|---------------|-------------|--------------|------------|--------------|--------|
| Pune          | Market A    | Retail       | Onion      | Mon-Wed      | High   |

**main.csv**
| District | Storage name | Address              | Type | Capacity in MT |
|----------|---------------|----------------------|------|----------------|
| Pune     | Storage A     | 123 Farm Lane, Pune  | Cold | 500            |

---

## 🎯 Future Improvements

- 🔍 Filter by commodity or volume
- 📱 Mobile-first responsive design using Bootstrap or Tailwind
- 📊 Dashboard with agricultural statistics
- 🌐 Integration with live government APIs

---

## 🙌 Contribution

Feel free to fork this repo, open issues, or submit pull requests to enhance its features or UI. Your contributions are welcome and appreciated!

---

## 🧑‍💻 Author

**Farmer Resource Finder Project** – 2025  
Made with ❤️ to support the agricultural community.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
