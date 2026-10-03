from fastapi import APIRouter, Depends, HTTPException

from backend.services.auth_service import get_current_user
from backend.repositories.user_repository import get_user_by_id

from backend.services.github_service import (
    get_github_stats,
)


router = APIRouter(
    prefix="/devxp/github",
    tags=["GitHub"],
)


@router.get("/stats")
def github_stats(
    user_id: int = Depends(get_current_user),
):
    user = get_user_by_id(user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found.",
        )

    if not user.github_access_token:
        raise HTTPException(
            status_code=400,
            detail="GitHub account is not connected.",
        )

    try:

        return get_github_stats(
            user.github_access_token
        )

    except HTTPException:
        raise

    except Exception as error:

        raise HTTPException(
            status_code=502,
            detail=f"GitHub API error: {str(error)}",
        )