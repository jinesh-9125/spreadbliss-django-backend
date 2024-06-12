def generatePayload(data, search_terms):
    try:
        organization = data["organization"]
        properties = data["properties"]
        geography = data["geography"]
        dates = data["dates"]

        taxonomies = {
            "subject_codes": data["taxonomies"]["subject_codes"],
            "population_served_codes": data["taxonomies"]["population_served_codes"],
            "ntee_codes": data["taxonomies"]["ntee_codes"],
            "subsection_code": data["taxonomies"]["subsection_code"]["subsection_code"],
            "subsection_code_description": data["taxonomies"]["subsection_code"][
                "subsection_code_description"
            ],
            "foundation_code": data["taxonomies"]["foundation_code"]["foundation_code"],
            "foundation_code_description": data["taxonomies"]["foundation_code"][
                "foundation_code_description"
            ],
        }

        financials = {
            "form_type": data["financials"]["most_recent_year"]["form_type"],
            "fiscal_year": data["financials"]["most_recent_year"]["fiscal_year"],
            "total_revenue": data["financials"]["most_recent_year"]["total_revenue"],
            "total_expenses": data["financials"]["most_recent_year"]["total_expenses"],
            "total_assets": data["financials"]["most_recent_year"]["total_assets"],
            "bmf_gross_receipts": data["financials"]["bmf_gross_receipts"],
            "bmf_assets": data["financials"]["bmf_assets"],
            "required_to_file_990t": data["financials"]["required_to_file_990t"],
            "a_133_audit_performed": data["financials"]["a_133_audit_performed"],
        }

        # destructuring all dictionary objects to the payload object
        payload = {
            **organization,
            **properties,
            **geography,
            **dates,
            **taxonomies,
            **financials,
            "search_terms": search_terms,
        }
        return payload
    except KeyError as e:
        # Handle the KeyError exception
        print("error form generatePayload function :: ", e)
        print(f"KeyError: {e} is missing in the data dictionary.")
        return None
    except Exception as e:
        # Handle any other exceptions
        print("error form generatePayload function :: ", e)
        print(f"An error occurred: {e}")
        return None
