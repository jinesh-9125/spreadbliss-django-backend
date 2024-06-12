from django.urls import path
from .views import (
    index,
    fetch_candid_essentials_v3,
    generate_csv,
    getNonProfitBySearchTerm,
    getNonProfitProfile,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "fetch-candid-essentials-v3",
        fetch_candid_essentials_v3,
        name="fetch-candid-essentials-v3",
    ),
    path(
        "generate-csv",
        generate_csv,
        name="generate_csv",
    ),
    path("get-organizations", getNonProfitBySearchTerm, name="get-organizations"),
    path(
        "get-organization-profile", getNonProfitProfile, name="get-organization-by-ein"
    ),
]
