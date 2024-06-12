import requests
import os
from dotenv import load_dotenv
from .models import EssentialsOrganizationUpdate, EssentialsOrganizationUpdateHistory
from .serializers import (
    EssentialsOrganizationSerializer,
    EssentialsOrganizationUpdateHistorySerializer,
)
from .helpers.csvgenerator import generateCSV
from .helpers.preprocessing import generatePayload
import time

load_dotenv()

candisApi = "https://api.candid.org/essentials/v3"
# bodyObject = {
#     "search_terms": "Agriculture, fishing and forestry",
#     "size": 20,
#     "filters": {
#         "organization": {
#             "subsection_codes": ["501(c)(3) Public Charity"],
#             "ruling_year": {"min": 2023, "max": 2023},
#         },
#         "financials": {"most_recent_year": {"total_revenue": {"min": 50000}}},
#     },
# }
# subKey = "bearer 5e1b3b7b-7b7b-4b7b-8b7b-7b7b7b7b7b7b"  # replace with your subscription key.need to be passed in the header


def fetchEssentialsData(
    search_terms,
    limit=0,
    size=25,
    subsection_codes="501(c)(3) Public Charity",
    ruling_year=2023,
    min_total_revenue=50000,
):
    try:
        print("==========================> ", limit, size)
        if not search_terms.strip():
            return {
                "success": False,
                "data": None,
                "error": "search_terms is required",
            }

        # body object to be sent to the API
        bodyObject = {
            "search_terms": search_terms,
            "size": size,
            "from": limit,
            "filters": {
                "organization": {
                    "subsection_codes": [subsection_codes],
                    "ruling_year": {"min": ruling_year, "max": ruling_year},
                },
                "financials": {
                    "most_recent_year": {"total_revenue": {"min": min_total_revenue}}
                },
            },
        }

        # load the subscription key from the .env file
        subKey = os.getenv("CANDID_SUBSCRIPTION_KEY")

        response = requests.post(
            candisApi, headers={"subscription-key": subKey}, json=bodyObject
        )
        resp = response.json()
        # print("resp :: ", response.json())

        # if resp["code"] == 429:
        #     print("server is sleeping now ...")
        #     time.sleep(60)
        #     print("server is back in game ...")
        #     response = requests.post(
        #         candisApi, headers={"subscription-key": subKey}, json=bodyObject
        #     )
        #     resp = response.json()
        #     print("error :: ", response.json())

        if resp["code"] != 200:
            return {"success": False, "data": resp, "error": None}
        # return "Data fetched successfully!"
        return {"success": True, "data": response.json(), "error": None}
    except Exception as err:
        print(str(err))
        return {"success": False, "data": None, "error": str(err)}


def saveEssentialsToDb(data, search_terms):
    try:
        # data will an array of objects to be added to the database
        # i save data as bulk in the database
        if not data:
            return {
                "success": True,
                "data": None,
                "error": "data is empty or already exists",
            }

        # save builk data to the database

        print("----------------------------------------------------------")
        # print("data to be saved ", data)
        print("----------------------------------------------------------")

        essentials = EssentialsOrganizationUpdate.objects.bulk_create(
            [EssentialsOrganizationUpdate(**org) for org in data]
        )
        serializer = EssentialsOrganizationSerializer(essentials, many=True)
        return {"success": True, "data": serializer.data, "error": None}

    except Exception as err:
        print("error in saveEssentialsToDb :: ", str(err))
        return {"success": False, "data": None, "error": str(err)}


def fetchHistory(search_terms):
    try:
        historySerilizer = EssentialsOrganizationUpdateHistory.objects.filter(
            search_terms=search_terms,
        ).order_by("-created_at")

        if historySerilizer.count() != 0:
            history = EssentialsOrganizationUpdateHistorySerializer(
                historySerilizer, many=True
            ).data

            return {
                "success": True,
                "data": {
                    "lastPage": history[0]["page"],
                    "limit": history[0]["limit"] + 25,
                    "size": history[0]["size"],
                },
                "error": None,
            }
        return {
            "success": True,
            "data": {
                "lastPage": 0,
                "limit": 0,
                "size": 25,
            },
            "error": "No history found",
        }
    except Exception as err:
        print("error in fetchHistory :: ", str(err))
        return {"success": False, "data": None, "error": str(err)}


def filterEssentialsData(data, search_terms):
    try:
        # filter data if already exists in the database
        # create a org_list
        # print("data to be filtered ", data)
        org_list = []
        for org in data:
            payload = generatePayload(org, search_terms)
            # print("Payload ", payload["ein"])
            # org_list.append(payload)
            orgs = EssentialsOrganizationUpdate.objects.filter(
                ein=payload["ein"]
            ).filter(search_terms=search_terms)
            print("orgs", len(orgs))
            if orgs.count() == 0:
                org_list.append(payload)

        print("org list ::::: -> ", len(org_list))
        return {"success": True, "data": org_list, "error": None}
    except Exception as err:
        print("error in filterEssentialsData :: ", str(err))
        return {"success": False, "data": None, "error": str(err)}


def createHistory(search_terms, size, limit, lastPage):
    try:
        historySerializer = EssentialsOrganizationUpdateHistory.objects.create(
            size=size,
            search_terms=search_terms,
            limit=limit,
            page=lastPage,
        )

        if not historySerializer:
            return {"success": False, "data": None, "error": "history not cretaed."}

        history = EssentialsOrganizationUpdateHistorySerializer(
            historySerializer, many=False
        ).data

        return {"success": True, "data": history, "error": ""}
    except Exception as err:
        print("error form createHistory :: ", str(err))
        return {"success": False, "data": None, "error": str(err)}
