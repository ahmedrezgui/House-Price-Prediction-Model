# Real Estate Datasets - Tunisia Property Listings

This repository contains datasets related to real estate listings in Tunisia. The datasets include detailed information on properties for sale or rent across various regions, providing insights into property pricing, features, and locations. Below is a description of the datasets and their respective structures.

---

## 1. **tayara.CSV**
### **Source**  
[Download from Kaggle](https://www.kaggle.com/datasets/maryembenyounes/tunisian-houses-for-rent-and-sell?resource=download)

### **Description**  
This dataset contains property listings with columns that are largely self-explanatory.

### **Columns**
- **price**: The listed price of the property in Tunisian Dinar.
- **transaction**: The type of transaction (e.g., for sale, for rent).
- **title**: The title of the listing.
- **city**: The city where the property is located.
- **region**: The region where the property is located.
- **description**: A description of the property in French or Arabic.
- **surface**: The surface area of the property in square meters.
- **bathrooms**: The number of bathrooms in the property.
- **rooms**: The number of rooms in the property.

---

## 2. **DataFullset.csv & DataCleanSet.csv**
### **Source**  
[Download from Kaggle](https://www.kaggle.com/datasets/samermakni/tunisia-house-pricing/data)

### **Description**  
These datasets offer comprehensive property details and additional computed features.

### **Columns**
- **id**: 128-bit universally unique identifier.
- **price_tnd**: The price of the property in Tunisian Dinars.
- **price_eur**: The price of the property in Euros (converted on October 29, 2022, at 1 TND = 0.31 EUR).
- **location**: The neighborhood of the property.
- **city**: The city where the property is located.
- **governorate**: The governorate where the property is located.
- **area**: The property’s area in square meters.
- **room**: The number of rooms.
- **bathroom**: The number of bathrooms.
- **age**: The property’s age in intervals (0 indicates new).
- **state**: The state of the property (0 = new, 1 = normal state, 2 = requires renovation).
- **latt**: Latitude of the property’s location.
- **long**: Longitude of the property’s location.
- **distance_to_capital**: The distance from the property to Tunis.
- **garage**: Boolean indicating if a garage is present.
- **garden**: Boolean indicating if a garden is present.
- **concierge**: Boolean indicating if a concierge is present.
- **beach_view**: Boolean indicating if the property has a beach view.
- **mountain_view**: Boolean indicating if the property has a mountain view.
- **pool**: Boolean indicating if a pool is present.
- **elevator**: Boolean indicating if an elevator is present.
- **furnished**: Boolean indicating if the property is furnished.
- **equipped_kitchen**: Boolean indicating if the kitchen is equipped.
- **central_heating**: Boolean indicating if central heating is available.
- **air_conditioning**: Boolean indicating if air conditioning is available.

---

## 3. **Property Prices in Tunisia.csv**
### **Source**  
[Download from Kaggle](https://www.kaggle.com/datasets/ghassen1302/property-prices-in-tunisia)

### **Description**  
This dataset includes aggregated property data with a focus on pricing and general attributes.

### **Columns**
- **category**: The property type (e.g., apartment, villa).
- **room_count**: The number of rooms.
- **bathroom_count**: The number of bathrooms.
- **size**: The size of the property in square meters.
- **type**: The transaction type (for sale or rent).
- **price**: The property price.
- **city**: The city of the property.
- **region**: The region of the property.
- **log_price**: The logarithm of the property price.

---

## 4. **Datasets Scraped from Technocasa**
### **Description**  
This dataset contains properties scraped from the Technocasa website.

### **Columns**
- **URL**: The URL of the property listing.
- **Image URL**: The URL of the property image.
- **Price**: The property’s price in Tunisian Dinar.
- **Title**: The title of the listing.
- **Subtitle**: A subtitle providing additional details.
- **Surface**: The surface area of the property in square meters.
- **Description**: A detailed description of the property.
- **Features**: Additional features of the property (e.g., standing, year of construction).
- **Points of Interest**: Nearby points of interest (e.g., schools, hospitals, restaurants).

---

## 5. **Datasets Scraped from Tunisie Annonce**
### **Description**  
This dataset contains properties scraped from the Tunisie Annonce website.

### **Columns**
- **Gouvernorat**: The governorate where the property is located.
- **Nature**: The nature of the property (e.g., apartment, villa).
- **Type**: The type of transaction (e.g., sale, rent).
- **Description**: A detailed description of the property.
- **Price**: The price of the property in Tunisian Dinar.
- **Insertion Date**: The date when the listing was created or updated.

---

## **License and Usage**
The datasets have been sourced from Kaggle and publicly available websites. Ensure proper attribution if used for research or projects.

For more details, refer to the source links provided above.
