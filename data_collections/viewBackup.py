from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .services import (
    fetchEssentialsData,
    saveEssentialsToDb,
    fetchHistory,
    filterEssentialsData,
    createHistory,
)
from .helpers.csvgenerator import generateCSV
from .helpers.preprocessing import generatePayload
from .models import EssentialsOrganizationUpdate, EssentialsOrganizationUpdateHistory
from .serializers import (
    EssentialsOrganizationSerializer,
    EssentialsOrganizationUpdateHistorySerializer,
)
from .helpers.csvgenerator import generateCSV
from .helpers.constants import header

# Create your views here.


@api_view(["GET"])
def index(request):
    return Response(
        {
            "/": "index page for data_collections app",
            "/fetch-candid-essentials-v3": "collect data form candid essentials v3",
        }
    )


@api_view(["POST"])
def fetch_candid_essentials_v3(request):
    try:
        search_terms = request.data["search_terms"]
        print("Search terms ", search_terms)

        isLastPage = False
        lastPage = 1
        currentPage = 1
        limit = 0
        size = 25

        # check logs of history if data is already fetched
        # if yes then return response
        # current page = last page + 1
        # else continue fetching data
        # current page = 1

        history = fetchHistory(search_terms)
        print("History ", history)

        if history["success"]:
            lastPage = history["data"]["lastPage"]
            currentPage = history["data"]["currentPage"]
            limit = history["data"]["limit"]
            size = history["data"]["size"]

        # historySerilizer = EssentialsOrganizationUpdateHistory.objects.filter(
        #     search_terms=search_terms,
        # ).order_by("-created_at")

        # print("History ", historySerilizer)
        # print("Count ", historySerilizer.count())

        # if historySerilizer.count() != 0:
        #     history = EssentialsOrganizationUpdateHistorySerializer(
        #         historySerilizer, many=True
        #     ).data

        #     print("Is history ", history[0])

        #     # return Response({"message": "Data fetched successfully!", "success": True})
        #     if history:
        #         lastPage = history[0]["page"]
        #         currentPage = history[0]["page"] + 1
        #         limit = history[0]["limit"]
        #         size = history[0]["size"]

        # now we have following data
        # search_terms
        # currentPage
        # limit
        # size

        # call api to fetch data and check lastpage == res.page_count
        # if yes then return response data already fetched
        # else continue fetching data
        # create payload
        # filter data if already exists in the database
        # create a org_list

        # if org_list is empty then increment current page and limit and save history
        # else save data to the database , save history  and add data to csv file.

        # if lastpage == res.page_count

        while not isLastPage:
            print("last page ", lastPage)
            print("currrent page ", currentPage)
            print("Limit ", limit)
            print("Size ", size)

            # fetch data step start here:

            # fetch data from api
            data = fetchEssentialsData(
                search_terms=search_terms, limit=limit, size=size
            )
            if not data["success"]:
                return Response(data)

            # check if page is already fetched
            if lastPage == data["data"]["page_count"]:
                isLastPage = True
                return Response({"message": "Data already featched!", "success": True})

            # fetch data step ends here :

            # filter data if already exists in the database
            filteredData = filterEssentialsData(data["data"]["hits"], search_terms)
            if not filteredData["success"]:
                return Response(filteredData)

            orgList = filteredData["data"]

            # orgList = []

            # for org in data["data"]["hits"]:
            #     payload = generatePayload(org, search_terms)
            #     essentialsOrg = EssentialsOrganizationUpdate.objects.filter(
            #         ein=payload["ein"]
            #     )
            #     print("Essentials org ", essentialsOrg)
            #     if essentialsOrg:
            #         continue
            #     orgList.append(payload)
            # print("Org list ", orgList)

            # if no data found in the page or data is not unique

            if len(orgList) != 0:
                resp = saveEssentialsToDb(orgList, search_terms=search_terms)
                if not resp["success"]:
                    return Response(resp)

            # generate history
            history = createHistory(search_terms, size, limit, lastPage)
            if not history["success"]:
                return Response(history)

            lastPage = currentPage
            currentPage += 1
            limit += size

            # history = EssentialsOrganizationUpdateHistory.objects.create(
            #     size=size,
            #     search_terms=search_terms,
            #     limit=limit,
            #     page=lastPage,
            # )

            # if not history:
            #     return Response(
            #         {"message": "Error in creating history", "success": False}
            #     )

            # if history:
            #     print("History created successfully")

            if len(orgList) != 0:
                # generate csv
                isGenerated = generateCSV(orgList, search_terms)
                if not isGenerated:
                    return Response(
                        {"message": "Error in generating CSV", "success": False}
                    )

            if data["data"]["page_count"] == lastPage:
                isLastPage = True
            print(f"Page {currentPage} fetched successfully")

            # currentPage += 1
            # limit += size

        count = EssentialsOrganizationUpdate.objects.filter(
            search_terms=search_terms
        ).count()

        return Response(
            {
                "message": f"Data fetched successfully! Total records: {count}",
                "success": True,
            }
        )
    except Exception as err:
        return Response({"error": str(err), "success": False})


@api_view(["POST"])
def generate_csv(request):
    try:
        request_data = request.data
        search_terms = request_data["search_terms"]
        print("Search terms ", search_terms)

        if not search_terms:
            return Response({"message": "search_terms is required", "success": False})

        orgListSerilizer = EssentialsOrganizationUpdate.objects.filter(
            search_terms=search_terms
        ).values(*header)

        print("Org list serilizer ", orgListSerilizer)

        if not orgListSerilizer:
            return Response({"message": "No data found", "success": False})
        orgList = EssentialsOrganizationSerializer(orgListSerilizer, many=True).data
        print("Org list ", orgList)

        generateCSV(orgList, search_terms)
        return Response(
            {
                "message": "Data fetched successfully!",
                "success": True,
                "data": len(orgList),
            }
        )

    except Exception as err:
        return Response({"error": str(err), "success": False})
