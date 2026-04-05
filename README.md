# 📲 WhatsApp Message Automation using Python & Twilio

## 📌 Project Overview

Developed an automated WhatsApp messaging system using Python and Twilio API that allows users to schedule and send messages at a specific date and time.

## 🚀 Key Features

* Schedule WhatsApp messages for future delivery
* Real-time user input for recipient details
* Automated delay calculation using datetime
* Error handling for API failures and invalid inputs
* Uses Twilio Sandbox for WhatsApp integration

## 🛠️ Tech Stack

* Python
* Twilio API
* Datetime Module
* Time Module

## ⚙️ How It Works

1. User enters recipient name, number, and message
2. Inputs scheduled date and time
3. System calculates time difference
4. Program waits using time.sleep()
5. Message is sent automatically at scheduled time

## 📂 Project Structure

* `main.py` → Core logic for scheduling and sending messages
* `requirements.txt` → Required libraries

## ▶️ Setup Instructions

1. Install dependencies:
   pip install -r requirements.txt

2. Add your Twilio credentials:
   Replace ACCOUNT_SID and AUTH_TOKEN in code

3. Run the program:
   python main.py

## 📈 Key Learning Outcomes

* API Integration (Twilio)
* Automation using Python
* Working with datetime and scheduling logic
* Error handling and debugging
