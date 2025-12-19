# sdfghj

Backend API for sdfghj

## Tech Stack

- **Frontend**: React
- **Backend**: FastAPI + SQLAlchemy
- **Frontend Source**: GitHub ([Repository](https://github.com/HimaShankarReddyEguturi/Hotelbookinguidesign))

## Project Structure

```
sdfghj/
├── frontend/          # Frontend application
├── backend/           # Backend API
├── README.md          # This file
└── docker-compose.yml # Docker configuration (if applicable)
```

## Getting Started

### Prerequisites

- Node.js 18+ (for frontend)
- Python 3.11+ (for Python backends)
- Docker (optional, for containerized setup)

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

```bash
cd backend
# Follow backend-specific setup instructions in backend/README.md
```

## Features

- User registration
- User login
- Password reset
- User profile management
- User account deletion

## API Endpoints

- `POST /api/register` - Register a new user account
- `POST /api/login` - Log in to an existing user account
- `POST /api/password-reset` - Reset the password for an existing user account
- `GET /api/profile` - Retrieve the profile information for the current user
- `PUT /api/profile` - Update the profile information for the current user
- `DELETE /api/profile` - Delete the current user account

## License

MIT
