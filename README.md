# AI Logistics Cost Estimator

## Problem
Small logistics operators, transporters, and local businesses often misprice trips due to lack of simple and reliable cost estimation tools. Existing solutions are either too complex, expensive, or inaccessible to small-scale users.
Incorrect cost estimation leads to financial losses, underquoting, or uncompetitive pricing.

## Solution
AI Logistics Cost Estimator is a lightweight, user-friendly application that estimates logistics trip costs using:
- Real-world city-to-city distance
- Vehicle-specific mileage heuristics
- User-adjustable fuel prices
The system automates distance calculation and applies rule-based AI logic to generate an instant and transparent cost breakdown.

## Key Features
- City-to-city distance calculation using geospatial data
- Vehicle-based cost estimation
- Adjustable fuel price input
- Clear cost breakdown (distance, fuel cost, total cost)
- Simple and intuitive UI for non-technical users

## How It Works
1. User enters **Source City** and **Destination City**
2. Selects a **Vehicle Type**
3. Inputs current **Fuel Price**
4. Application calculates real-world distance and estimates trip cost instantly


## Tech Stack
- **Python**
- **Streamlit** (UI & rapid prototyping)
- **Geopy / OpenStreetMap** (geocoding & distance calculation)
- **Rule-based AI heuristics** for cost estimation


## How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py

Assumptions :
Average mileage is used per vehicle category
Fixed margin is applied
Traffic, tolls, and dynamic demand are not included
Fuel price is provided by the user for flexibility

Use Cases :
Small transporters and truck owners
Local shop owners estimating delivery costs
Logistics startups testing pricing models
Students and learners exploring applied AI solutions

Future Scope :
Real-time fuel price integration
Traffic and toll-aware routing
Demand-based dynamic pricing
Analytics dashboard for logistics operators
Cloud deployment and scaling using Microsoft Azure services

License :
This project is developed as part of the Microsoft Imagine Cup submission.
