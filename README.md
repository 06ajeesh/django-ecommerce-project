
# Django Ecommerce Application

 This is a comprehensive e-commerce application built using Django, designed to provide an intuitive and seamless shopping experience for users. The eKart platform allows users to browse through a variety of products, add items to their cart, and complete their order.

<img src="https://github.com/user-attachments/assets/82809644-5998-4295-b0b9-bca88f1caec6" width="85%" />

## Features

- **Authentication:** Secure user registration and login (Django Authentication)
- **Product Management:** Browse product detailes, Add/remove products from the cart
- **Order Tracking:** Users can view their order history.
- **Messages Framework:** Django's messages framework lets you show quick notifications (like success, error, or info) to users after actions—perfect for things like form submissions or login alerts!

## Screenshots

Here are some screenshots from the application:

- **Homepage & Navigation**  
  <img src="https://github.com/user-attachments/assets/82809644-5998-4295-b0b9-bca88f1caec6" width="75%" />

- **Login Profile**  
  <img src="https://github.com/user-attachments/assets/ed87d24f-4401-4f80-8ffb-7a0f93543817" width="75%" />

- **Register Profile**  
  <img src="https://github.com/user-attachments/assets/b2b20c9d-2f2e-4a91-8cc0-530adbc52084" width="75%" />

- **Orders Page**  
  <img src="https://github.com/user-attachments/assets/74812fde-a85a-4ac2-b3b6-eeac02ec6e66" width="75%" />







## Technologies Used

- **Django:** The web framework used for backend development.
- **Bootstrap:** For responsive, mobile-first design.
- **SQLite:** The default database for storing application data.



## Installation

To set up the project locally, follow these steps:


### 1. Open Folder  
Open a free folder for the project in command-line  

### 2. Clone the Repository  
Run the following command in your terminal:  
  ```bash
  git clone https://github.com/06ajeesh/django-ecommerce-project.git
  ```  



### 3. Create and Activate a Virtual Environment  
**For Windows:**  
```bash
python -m venv .venv
```
```bash
.venv\Scripts\activate
```

**For macOS/Linux:**  
```bash
python3 -m venv .venv
```
```bash
source .venv/bin/activate
```


### 4. Change Directory
```bash
cd django-ecommerce-project
```

### 5. Apply Database Migrations  
```bash
python manage.py migrate
```

### 6. Run the Development Server  
```bash
python manage.py runserver
```

### 7. Open the Application in Your Browser  
```
http://127.0.0.1:8000/
```

Now, your **Django Ecommerce Project** web application is up and running! 🚀
