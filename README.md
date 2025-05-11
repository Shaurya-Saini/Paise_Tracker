# Paise Tracker

**Paise Tracker** is a mobile expense-tracking app built with Python's Kivy and Google Sheets as a serverless backend. It allows users to log, view, and categorize their expenses directly from their mobile devices. Data is stored and synced in real time using the `gspread` library with OAuth2 authentication, enabling shared access and minimal backend maintenance.

## ✨ Features

- Add and categorize expenses
- View and filter past entries
- Real-time sync with Google Sheets
- Simple and responsive Kivy interface
- Serverless backend using Google Sheets

## 📱 Tech Stack

- **Frontend:** [Kivy](https://kivy.org/)
- **Backend:** [Google Sheets](https://www.google.com/sheets/about/) via [gspread](https://github.com/burnash/gspread)
- **Authentication:** [oauth2client](https://github.com/googleapis/oauth2client)
