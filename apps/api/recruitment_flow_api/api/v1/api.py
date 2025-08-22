"""
Main API router for version 1 endpoints.

This module combines all API endpoints into a single router
for the FastAPI application.
"""

from fastapi import APIRouter

from recruitment_flow_api.api.v1 import auth, roles, candidates, interviews, offers, analytics

# Create main API router
api_router = APIRouter()

# Include all endpoint modules
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(roles.router, prefix="/roles", tags=["Roles"])
api_router.include_router(candidates.router, prefix="/candidates", tags=["Candidates"])
api_router.include_router(interviews.router, prefix="/interviews", tags=["Interviews"])
api_router.include_router(offers.router, prefix="/offers", tags=["Offers"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])
