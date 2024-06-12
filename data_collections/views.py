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
import math

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
        lastPage = 0
        limit = 0
        size = 25
        # isLastLogged = False

        # check logs of history if data is already fetched
        # if yes then return response
        # current page = last page + 1
        # else continue fetching data
        # current page = 1

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

        history = fetchHistory(search_terms)
        print("History ", history)

        if history["success"]:
            lastPage = history["data"]["lastPage"]
            limit = history["data"]["limit"]
            size = history["data"]["size"]

        while not isLastPage:
            print("last page ", lastPage)
            print("Limit ", limit)
            print("Size ", size)

            # fetch data step start here:

            # fetch data from api
            data = fetchEssentialsData(
                search_terms=search_terms, limit=limit, size=size
            )
            if not data["success"]:
                isLastPage = True
                return Response(data)
            print("data fetched successfully ...")

            # check if data is already fetched
            # if lastPage == data["data"]["page_count"]:
            #     # isLastPage = True
            #     return Response({"message": "Data already featched!", "success": True})

            # fetch data step ends here :

            # filter data if already exists in the database
            orgList = []
            for org in data["data"]["hits"]:
                payload = generatePayload(org, search_terms)
                print("Payload ", payload["ein"])
                orgList.append(payload)

            filteredData = filterEssentialsData(data["data"]["hits"], search_terms)
            if not filteredData["success"]:
                return Response(filteredData)

            # print("filteredData :: ", filteredData)

            print("data filtered successfully ...")

            # orgList = filteredData["data"]

            # if no data found in the page or data is not unique
            print("fetched data :: ", len(orgList))

            if len(orgList) != 0:
                print("Saving data to the database ...")
                resp = saveEssentialsToDb(orgList, search_terms=search_terms)
                if not resp["success"]:
                    isLastPage = True
                    return Response(resp)

            print("Data saved successfully ...")
            # generate history
            lastPage += 1
            history = createHistory(search_terms, size, limit, lastPage)
            if not history["success"]:
                isLastPage = True
                return Response(history)
            print("history created successfully ...")

            # if lastpage is equal to page_count this is last page to fetch so we can end loop here.
            # if data["data"]["page_count"] == lastPage:
            # isLastPage = True

            limit += size

            if len(orgList) != 0:
                # generate csv
                isGenerated = generateCSV(orgList, search_terms)
                if not isGenerated:
                    isLastPage = True
                    return Response(
                        {"message": "Error in generating CSV", "success": False}
                    )
                print("saving to csv file ...")

            print(f"Page {lastPage} fetched successfully")

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


@api_view(["POST"])
def getNonProfitBySearchTerm(request):
    try:
        search_terms = request.data["search_terms"]
        page = request.data["page"]
        print("Search terms ", search_terms)
        print("Page ", page)
        limit = 25

        if page < 1:
            return Response(
                {"message": "Page number must be greater than 1", "success": False}, 400
            )

        if not search_terms or search_terms.strip() == "":
            return Response(
                {"message": "search_terms is required", "success": False}, 400
            )

        first = (page - 1) * limit
        last = page * limit

        orgListSerilizer = EssentialsOrganizationUpdate.objects.filter(
            search_terms=search_terms
        ).values("id", "ein", "organization_name", "website_url", "mission", "county")[
            first:last
        ]

        # print("Org list serilizer ", orgListSerilizer)

        if not orgListSerilizer:
            return Response({"message": "No data found", "success": False})
        # orgList = EssentialsOrganizationSerializer(orgListSerilizer, many=True).data
        # print("Org list ", orgList)

        # totol number of pages
        total = EssentialsOrganizationUpdate.objects.filter(
            search_terms=search_terms
        ).count()

        total_page = math.ceil(total / limit)

        if last >= total_page:
            next_page = False
        else:
            next_page = True

        return Response(
            {
                "message": "Data fetched successfully!",
                "success": True,
                "data": orgListSerilizer,
                "next_page": next_page,
                "total_page": total_page,
                "current_page": page,
            }
        )

    except Exception as err:
        return Response({"error": str(err), "success": False})


@api_view(["POST"])
def getNonProfitProfile(request):
    try:
        ein = request.data["ein"]
        print("EIN ", ein)

        if not ein:
            return Response({"message": "EIN is required", "success": False}, 400)

        orgListSerilizer = EssentialsOrganizationUpdate.objects.filter(ein=ein).values(
            "id",
            "ein",
            "organization_name",
            "website_url",
            "mission",
            "total_revenue",
            "total_expenses",
            "total_assets",
            "address_line_1",
            "city",
            "state",
            "county",
            "zip",
            "msa",
        )

        print("Org list serilizer ", orgListSerilizer)

        if not orgListSerilizer:
            return Response({"message": "No data found", "success": False})
        # orgList = EssentialsOrganizationSerializer(orgListSerilizer, many=True).data
        # print("Org list ", orgList)

        return Response(
            {
                "message": "Data fetched successfully!",
                "success": True,
                "data": orgListSerilizer[0],
            }
        )

    except Exception as err:
        return Response({"error": str(err), "success": False})
