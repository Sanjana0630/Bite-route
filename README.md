# BiteRoute

BiteRoute is a full-stack web application featuring a React frontend and a Django backend. It integrates interactive maps, authentication, and data visualization.

## Features
- **Interactive Maps:** Integration with Google Maps for location-based features.
- **Authentication:** Google OAuth authentication.
- **Data Visualization:** Charts and graphs using Recharts.
- **QR Code Generation:** Built-in QR code functionality.
- **Responsive Design:** Styled with Bootstrap.

## Tech Stack

### Frontend
- **Framework:** React (Vite)
- **Styling:** Bootstrap
- **Key Libraries:** `@react-google-maps/api`, `@react-oauth/google`, `axios`, `lucide-react`, `qrcode.react`, `recharts`, `react-router-dom`

### Backend
- **Framework:** Python / Django
- **Database:** SQLite (default for development)
- **Server:** Gunicorn

## Project Structure
```text
BiteRoute-main/
├── backend/               # Django backend application
│   ├── biteroute_backend/ # Main Django project settings
│   ├── core/              # Main application logic
│   ├── requirements.txt   # Python dependencies
│   └── manage.py          # Django management script
├── frontend/              # Frontend applications
│   └── bite-route/        # React (Vite) frontend application
│       ├── src/           # React source code
│       └── package.json   # Node.js dependencies
├── netlify.toml           # Netlify deployment configuration for frontend
└── render.yaml            # Render deployment configuration for backend
```

## Getting Started

### Prerequisites
- Node.js (v18+ recommended)
- Python (3.13+)

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server (runs on `http://127.0.0.1:8000/` by default):
   ```bash
   python manage.py runserver
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend/bite-route
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```

## Deployment
- **Frontend** configuration is available for deployment on [Netlify](https://www.netlify.com/) via the `netlify.toml` file.
- **Backend** configuration is available for deployment on [Render](https://render.com/) via the `render.yaml` file.
