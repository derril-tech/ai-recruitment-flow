# API Specification - Recruitment Flow AI

This document provides comprehensive API documentation for the Recruitment Flow AI backend, including endpoints, request/response schemas, authentication, and error handling.

## 🔐 Authentication

All API endpoints require authentication unless explicitly marked as public. Authentication is handled via JWT tokens.

### Authentication Flow

1. **Login**: `POST /api/v1/auth/login`
2. **Refresh Token**: `POST /api/v1/auth/refresh`
3. **Logout**: `POST /api/v1/auth/logout`

### Headers

```
Authorization: Bearer <jwt_token>
Content-Type: application/json
```

## 📊 Response Format

All API responses follow a consistent format:

### Success Response
```json
{
  "success": true,
  "data": {
    // Response data
  },
  "message": "Operation completed successfully",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

### Error Response
```json
{
  "success": false,
  "error": {
    "type": "validation_error",
    "message": "Request validation failed",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ],
    "status_code": 422
  },
  "timestamp": "2024-01-15T10:30:00Z"
}
```

## 🔑 Authentication Endpoints

### POST /api/v1/auth/login

Authenticate user and return JWT tokens.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securepassword"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "token_type": "bearer",
    "expires_in": 3600,
    "user": {
      "id": "user_123",
      "email": "user@example.com",
      "name": "John Doe",
      "role": "recruiter",
      "permissions": ["read:roles", "write:candidates"]
    }
  }
}
```

### POST /api/v1/auth/refresh

Refresh access token using refresh token.

**Request Body:**
```json
{
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### POST /api/v1/auth/logout

Logout user and invalidate tokens.

**Request Body:**
```json
{
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

## 👥 User Management

### GET /api/v1/users/me

Get current user profile.

**Response:**
```json
{
  "success": true,
  "data": {
    "id": "user_123",
    "email": "user@example.com",
    "name": "John Doe",
    "role": "recruiter",
    "organization_id": "org_456",
    "permissions": ["read:roles", "write:candidates"],
    "created_at": "2024-01-15T10:30:00Z",
    "updated_at": "2024-01-15T10:30:00Z"
  }
}
```

### PUT /api/v1/users/me

Update current user profile.

**Request Body:**
```json
{
  "name": "John Smith",
  "email": "john.smith@example.com"
}
```

## 🎯 Role Management

### GET /api/v1/roles

List all roles with pagination and filtering.

**Query Parameters:**
- `page`: Page number (default: 1)
- `limit`: Items per page (default: 20, max: 100)
- `search`: Search term for role title
- `status`: Filter by status (active, inactive, draft)
- `department`: Filter by department

**Response:**
```json
{
  "success": true,
  "data": {
    "roles": [
      {
        "id": "role_123",
        "title": "Senior Software Engineer",
        "department": "Engineering",
        "level": "senior",
        "status": "active",
        "candidate_count": 45,
        "created_at": "2024-01-15T10:30:00Z",
        "updated_at": "2024-01-15T10:30:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 150,
      "pages": 8
    }
  }
}
```

### POST /api/v1/roles

Create a new role.

**Request Body:**
```json
{
  "title": "Senior Software Engineer",
  "department": "Engineering",
  "level": "senior",
  "description": "We are looking for a Senior Software Engineer...",
  "requirements": [
    "5+ years of experience in software development",
    "Proficiency in Python, JavaScript, and React",
    "Experience with cloud platforms (AWS, GCP)"
  ],
  "responsibilities": [
    "Design and implement scalable software solutions",
    "Mentor junior developers",
    "Collaborate with cross-functional teams"
  ],
  "compensation_range": {
    "min": 120000,
    "max": 180000,
    "currency": "USD"
  },
  "location": "San Francisco, CA",
  "remote_policy": "hybrid"
}
```

### GET /api/v1/roles/{role_id}

Get role details by ID.

**Response:**
```json
{
  "success": true,
  "data": {
    "id": "role_123",
    "title": "Senior Software Engineer",
    "department": "Engineering",
    "level": "senior",
    "description": "We are looking for a Senior Software Engineer...",
    "requirements": [...],
    "responsibilities": [...],
    "compensation_range": {...},
    "location": "San Francisco, CA",
    "remote_policy": "hybrid",
    "status": "active",
    "candidate_count": 45,
    "created_at": "2024-01-15T10:30:00Z",
    "updated_at": "2024-01-15T10:30:00Z"
  }
}
```

### PUT /api/v1/roles/{role_id}

Update role details.

### DELETE /api/v1/roles/{role_id}

Delete role (soft delete).

## 👤 Candidate Management

### GET /api/v1/candidates

List candidates with pagination and filtering.

**Query Parameters:**
- `page`: Page number (default: 1)
- `limit`: Items per page (default: 20, max: 100)
- `search`: Search term for name or email
- `role_id`: Filter by role
- `status`: Filter by status (applied, screening, interviewing, offered, hired, rejected)
- `source`: Filter by source (linkedin, indeed, referral, etc.)

**Response:**
```json
{
  "success": true,
  "data": {
    "candidates": [
      {
        "id": "candidate_123",
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "phone": "+1-555-0123",
        "role_id": "role_123",
        "status": "screening",
        "source": "linkedin",
        "score": 85,
        "created_at": "2024-01-15T10:30:00Z",
        "updated_at": "2024-01-15T10:30:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 150,
      "pages": 8
    }
  }
}
```

### POST /api/v1/candidates

Create a new candidate.

**Request Body:**
```json
{
  "name": "Jane Smith",
  "email": "jane.smith@example.com",
  "phone": "+1-555-0123",
  "role_id": "role_123",
  "source": "linkedin",
  "resume_url": "https://storage.example.com/resumes/jane-smith.pdf",
  "linkedin_url": "https://linkedin.com/in/janesmith",
  "experience_years": 5,
  "current_company": "Tech Corp",
  "current_title": "Software Engineer"
}
```

### POST /api/v1/candidates/import

Bulk import candidates from various sources.

**Request Body:**
```json
{
  "source": "ats_export",
  "role_id": "role_123",
  "candidates": [
    {
      "name": "John Doe",
      "email": "john.doe@example.com",
      "phone": "+1-555-0124",
      "resume_url": "https://storage.example.com/resumes/john-doe.pdf"
    }
  ]
}
```

### GET /api/v1/candidates/{candidate_id}

Get candidate details by ID.

**Response:**
```json
{
  "success": true,
  "data": {
    "id": "candidate_123",
    "name": "Jane Smith",
    "email": "jane.smith@example.com",
    "phone": "+1-555-0123",
    "role_id": "role_123",
    "status": "screening",
    "source": "linkedin",
    "resume_url": "https://storage.example.com/resumes/jane-smith.pdf",
    "linkedin_url": "https://linkedin.com/in/janesmith",
    "experience_years": 5,
    "current_company": "Tech Corp",
    "current_title": "Software Engineer",
    "score": 85,
    "screening_results": {
      "technical_score": 90,
      "cultural_fit": 85,
      "experience_match": 88
    },
    "created_at": "2024-01-15T10:30:00Z",
    "updated_at": "2024-01-15T10:30:00Z"
  }
}
```

### PUT /api/v1/candidates/{candidate_id}

Update candidate details.

### DELETE /api/v1/candidates/{candidate_id}

Delete candidate (soft delete).

## 🔍 Screening

### POST /api/v1/screen/{role_id}/{candidate_id}

Run AI-powered screening for a candidate.

**Response:**
```json
{
  "success": true,
  "data": {
    "screening_id": "screening_123",
    "candidate_id": "candidate_123",
    "role_id": "role_123",
    "status": "completed",
    "scores": {
      "technical_score": 90,
      "cultural_fit": 85,
      "experience_match": 88,
      "overall_score": 87.7
    },
    "evidence": {
      "technical_evidence": "Strong Python and React experience demonstrated in portfolio",
      "cultural_evidence": "Previous work at collaborative startups shows good cultural fit",
      "experience_evidence": "5 years of relevant experience matches role requirements"
    },
    "risk_flags": [
      {
        "type": "experience_gap",
        "severity": "low",
        "description": "Limited cloud platform experience"
      }
    ],
    "recommendation": "proceed_to_interview",
    "created_at": "2024-01-15T10:30:00Z"
  }
}
```

### GET /api/v1/screen/{screening_id}

Get screening results by ID.

## 📅 Interview Scheduling

### GET /api/v1/interviews

List interviews with pagination and filtering.

**Query Parameters:**
- `page`: Page number (default: 1)
- `limit`: Items per page (default: 20, max: 100)
- `candidate_id`: Filter by candidate
- `role_id`: Filter by role
- `status`: Filter by status (scheduled, completed, cancelled)
- `date_from`: Filter by start date
- `date_to`: Filter by end date

### POST /api/v1/interviews

Schedule a new interview.

**Request Body:**
```json
{
  "candidate_id": "candidate_123",
  "role_id": "role_123",
  "interview_type": "technical",
  "interviewers": ["user_456", "user_789"],
  "scheduled_at": "2024-01-20T14:00:00Z",
  "duration_minutes": 60,
  "location": "San Francisco Office",
  "video_url": "https://zoom.us/j/123456789",
  "notes": "Technical interview focusing on Python and React"
}
```

### GET /api/v1/interviews/{interview_id}

Get interview details by ID.

### PUT /api/v1/interviews/{interview_id}

Update interview details.

### DELETE /api/v1/interviews/{interview_id}

Cancel interview.

### POST /api/v1/interviews/{interview_id}/submit

Submit interview feedback.

**Request Body:**
```json
{
  "interviewer_id": "user_456",
  "scores": {
    "technical_skills": 8,
    "problem_solving": 9,
    "communication": 7,
    "cultural_fit": 8,
    "overall": 8
  },
  "notes": "Strong technical skills, good problem-solving approach...",
  "recommendation": "hire",
  "strengths": ["Excellent Python knowledge", "Good system design skills"],
  "areas_for_improvement": ["Could improve communication clarity"]
}
```

## 💼 Offers

### GET /api/v1/offers

List offers with pagination and filtering.

### POST /api/v1/offers

Create a new offer.

**Request Body:**
```json
{
  "candidate_id": "candidate_123",
  "role_id": "role_123",
  "compensation": {
    "base_salary": 150000,
    "currency": "USD",
    "equity": 0.01,
    "bonus_percentage": 15
  },
  "start_date": "2024-03-01",
  "benefits": ["health_insurance", "dental_insurance", "401k"],
  "notes": "Competitive offer based on market rates and experience"
}
```

### GET /api/v1/offers/{offer_id}

Get offer details by ID.

### PUT /api/v1/offers/{offer_id}

Update offer details.

### POST /api/v1/offers/{offer_id}/send

Send offer to candidate.

### POST /api/v1/offers/{offer_id}/respond

Record candidate response to offer.

**Request Body:**
```json
{
  "response": "accepted",
  "notes": "Excited to join the team!"
}
```

## 📊 Analytics & Reporting

### GET /api/v1/analytics/pipeline

Get pipeline analytics.

**Query Parameters:**
- `date_from`: Start date for analytics
- `date_to`: End date for analytics
- `role_id`: Filter by role

**Response:**
```json
{
  "success": true,
  "data": {
    "total_candidates": 150,
    "pipeline_stages": {
      "applied": 45,
      "screening": 30,
      "interviewing": 20,
      "offered": 10,
      "hired": 5
    },
    "conversion_rates": {
      "screening_to_interview": 0.67,
      "interview_to_offer": 0.50,
      "offer_to_hire": 0.50
    },
    "time_to_hire": {
      "average_days": 25,
      "median_days": 22
    }
  }
}
```

### GET /api/v1/analytics/eeo

Get EEO compliance data.

### GET /api/v1/analytics/adverse-impact

Get adverse impact analysis.

## 🔄 WebSocket Endpoints

### /ws/pipeline/{role_id}

Real-time pipeline updates for a specific role.

**Message Types:**
- `candidate_added`: New candidate added to pipeline
- `status_changed`: Candidate status changed
- `interview_scheduled`: Interview scheduled
- `offer_sent`: Offer sent to candidate

**Example Message:**
```json
{
  "type": "status_changed",
  "data": {
    "candidate_id": "candidate_123",
    "old_status": "screening",
    "new_status": "interviewing",
    "timestamp": "2024-01-15T10:30:00Z"
  }
}
```

## 🚨 Error Codes

| Code | Type | Description |
|------|------|-------------|
| 400 | Bad Request | Invalid request data |
| 401 | Unauthorized | Authentication required |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Resource not found |
| 422 | Validation Error | Request validation failed |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Internal Server Error | Server error |

## 📝 Rate Limiting

- **Authentication endpoints**: 5 requests per minute
- **Read endpoints**: 100 requests per minute
- **Write endpoints**: 20 requests per minute
- **Bulk operations**: 10 requests per minute

## 🔒 Security Headers

All responses include security headers:

```
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Strict-Transport-Security: max-age=31536000; includeSubDomains
Content-Security-Policy: default-src 'self'
```

## 📚 OpenAPI Documentation

Interactive API documentation is available at:
- **Development**: `http://localhost:8000/docs`
- **Production**: Disabled for security

## 🔄 API Versioning

The API uses URL versioning (`/api/v1/`). Breaking changes will be introduced in new versions while maintaining backward compatibility for a reasonable period.
