essentials_v3 = {
    "code": 200,
    "message": "Request was processed successfully!",
    "took": 24,
    "time": "2020-01-01T01:01:01:01.000Z",
    "results_count": 2541,
    "page_count": 67,
    "errors": ["string"],
    "hits": [
        {
            "organization": {
                "organization_id": "7578046",
                "ein": "39-1731296",
                "organization_name": "Candid",
                "also_known_as": "Foundation Center, Guidestar",
                "mission": "Get you the information to do good",
                "website_url": "candid.org",
                "logo_url": "candid.org",
                "contact_name": "John smith",
                "contact_email": "help@orgnam.org",
                "contact_phone": "(555) 111-5555",
                "contact_title": "Support lead",
                "number_of_employees": 55,
            },
            "properties": {
                "relationship_type": {
                    "parent": True,
                    "subordinate": False,
                    "independent": False,
                    "headquarters": True,
                }
            },
            "geography": {
                "address_line_1": "1 Financial Sq",
                "address_line_2": "Floor 24",
                "city": "New York",
                "state": "NY",
                "zip": 10005,
                "msa": "IL - Peoria-Pekin",
                "congressional_district": "District 45, CA",
                "county": "Peoria, IL",
                "latitude": 40.9052,
                "longitude": -89.5866,
            },
            "taxonomies": {
                "subject_codes": [
                    {"subject_code": "SP030000", "subject_code_description": "SP030000"}
                ],
                "population_served_codes": [
                    {
                        "population_served_code": "PG030000",
                        "population_served_description": "People with Physical Disabilities  ",
                    }
                ],
                "ntee_codes": [
                    {"ntee_code": "A00", "ntee_code_description": "Humanities"}
                ],
                "subsection_code": {
                    "subsection_code": "03",
                    "subsection_code_description": "501(c)(3) Public Charity",
                },
                "foundation_code": {
                    "foundation_code": "15",
                    "foundation_code_description": "50% tax deductible",
                },
            },
            "financials": {
                "most_recent_year": {
                    "form_types": "990",
                    "fiscal_year": 2020,
                    "total_revenue": 2349999,
                    "total_expenses": 22224499,
                    "total_assets": 57426592,
                },
            },
        }
    ],
}


essentials_lookup = {
    "code": 200,
    "message": "Request was processed successfully!",
    "took": 20,
    "errors": [],
    "data": [
        [
            "ntee_minor",
            "msa_codes",
            "ntee_major",
            "subsections",
            "filing_type",
            "foundation_type",
        ]
    ],
}

premier_v3 = {
    "code": 200,
    "message": "Request was processed successfully!",
    "took": 24,
    "errors": ["string"],
    "data": {
        "summary": {
            "organization_id": 6908122,
            "organization_name": "Candid",
            "ein": "13-1837418",
            "govt_registered_name": "Candid",
            "affiliation_code": "3",
            "affiliation_description": "This code is used if the organization is an independent organization or an independent auxiliary (i.e., not affiliated with a a National, Regional, or Geographic grouping of organizations).",
            "donation_to_ein": "13-1837418",
            "donation_to_name": "Candid",
            "donation_page": "https://candid.org/about/funding-candid",
            "keywords": "philanthropy, data, transparency, capacity building, research, education, foundations, foundation, charitable giving, data driven decisions, nonprofits, transparency, nonprofit sector, organizational effectiveness, organizational efficiency, nonprofit information hub, Forms 990, GuideStar, Foundation Center",
            "mission": "Candid gets you the information you need to do good.",
            "is_national_hq": False,
            "demographics_status": "This organization has provided Candid demographics data on 06/23/2023",
            "demographics_status_nonprofit": "Your organization has provided Candid demographics data on 06/23/2023",
            "ntee_code": "T50 - Philanthropy, Voluntarism, and Grantmaking",
            "sdg": {"id": 17, "description": "Partnerships for the Goals"},
            "website_url": "candid.org",
            "year_founded": "1956",
            "year_incorporated": "1956",
            "is_non_bmf_org": False,
            "first_on_bmf_date": "1998-07-31T04:00:00Z",
            "last_on_bmf_date": "2021-04-12T04:00:00Z",
            "profile_data_change_dates": {
                "primary_address_last_modified": "2020-11-12T14:28:48",
                "payment_address_last_modified": "2020-11-12T14:28:48",
                "primary_contact_email_last_modified": "2020-11-12T14:28:48",
                "fundraising_contact_email_last_modified": "2020-11-12T14:28:48",
                "org_website_last_modified": "2020-11-12T14:28:48",
                "seal_last_modified": "2020-11-12T14:28:48",
                "dei_last_modified": "2020-11-12T14:28:48",
            },
            "addresses": [
                {
                    "address_line_1": "32 Old Slip",
                    "address_line_2": "24th Floor",
                    "city": "New York",
                    "state": "NY",
                    "postal_code": "10005",
                    "country": "USA",
                    "address_type": "Main Address",
                }
            ],
            "forms_1023_1024": [
                ["https://www.guidestar.org/ViewEdoc.aspx?eDocId=7077922&approved=True"]
            ],
            "letters_of_determination": [
                {
                    "letter_of_determination_doc_name": "Candid IRS Letter of Determination",
                    "letter_of_determination_url": "https://www.guidestar.org/ViewEdoc.aspx?eDocId=6645380&approved=True",
                }
            ],
            "letters_of_dissolution": [
                {
                    "name": "Letter of Dissolution",
                    "year": "2017",
                    "letter_of_dissolution_url": "https://www.guidestar.org/ViewEdoc.aspx?eDocId=6645380&approved=True",
                }
            ],
            "ntee_codes": [
                {
                    "ntee_code": "T50",
                    "primary_code": "T",
                    "primary_description": "Philanthropy, Voluntarism, and Grantmaking",
                    "sub_code": "50",
                    "sub_description": "Philanthropy / Charity / Voluntarism Promotion (General)",
                }
            ],
            "naics_code": {
                "naics_code": "813219",
                "naics_description": "Other Grantmaking and Giving Services",
            },
            "sic_codes": [
                {"sic_code": "8399", "sic_description": "Social Services, NEC"}
            ],
            "platinum_evaluation_documents": [
                {
                    "document_name": "Evaluation.pdf",
                    "document_year": "2017",
                    "document_url": "https://www.guidestar.org/ViewEdoc.aspx?eDocId=6645380&approved=True",
                }
            ],
            "other_documents": [
                {
                    "document_name": "Candid's 2030 Vision",
                    "document_year": "2020",
                    "document_url": "https://www.guidestar.org/ViewEdoc.aspx?eDocId=6645386&approved=True",
                }
            ],
            "photos": [
                {
                    "picture_url": "https://www.guidestar.org/ViewEdoc.aspx?eDocId=5449398&approved=True",
                    "caption": "Jacob Harold",
                }
            ],
            "social_media_urls": ["https://www.facebook.com/CandidDotOrg/"],
            "telephone_numbers": [
                {"telephone_number": "757-941-1444", "telephone_type": "Preferred"}
            ],
            "videos": [
                {
                    "video_caption": "GuideStar: Better Data, for Better Decisions, for a Better World",
                    "video_url": "https://www.youtube.com/embed/W0rUzE6Yms4",
                }
            ],
            "org_collect_feedback": True,
            "org_feedback_example": "We collect org feedback through customer surveys",
            "org_quiz_interest": False,
            "org_learn_more": False,
            "feedback_responses": [
                {
                    "question_text": "How is your organization collecting feedback from the people you serve?",
                    "response_text": "We regularly collect feedback through: Electronic surveys (by email, tablet, etc.), Focus groups or interviews (by phone or in person), Community meetings/Town halls, Constituent (client or resident, etc.) advisory committees, other: Online Chat",
                }
            ],
            "pcs_codes": [
                {
                    "pcs_facet": "Population with Gender/Age",
                    "pcs_code": "PA020000",
                    "pcs_description": "Adults",
                    "pcs_parent_code": "PA000000",
                    "pcs_parent_description": "Age groups",
                }
            ],
            "profile_sdg_codes": [
                {"id": 17, "description": "Partnerships for the Goals"}
            ],
        },
        "programs": {
            "programs": [
                {
                    "name": "Knowledge Tools",
                    "description": "Through data, research, and our collective experience, Candid provides our users with the knowledge they need to make strategic decisions and develop practical solutions to achieve their missions. \n\nOur GuideStar searchable database currently includes data on 1.9 million 501c3 entities, making it easier to understand who they are and what they do. We support ongoing learning and research by gathering, indexing, and sharing the sector’s collective knowledge on IssueLab while also producing our own research that shares insights on issues affecting the social sector. We provide data and knowledge to the philanthropic field by creating new issue-based web portals known as “Foundation Landscapes” on the topics that matter most to the sector. Through Glasspockets we provide the data, resources, examples, and action steps foundations need to understand the value of transparency, be more open in their own communications, and help shed more light on how private organizations are serving the public good. Candid works closely with organizations around the globe to assist them in collecting and organizing their region’s philanthropy data by sharing what we have learned over the past 60 years about data acquisition and data architecture. \n\nCandid’s CF Insights program is the leader in data collection and research for the community foundation field in the U.S. with a reputation for benchmarking and analysis of trends. Through CF Insights, we continue to deliver a high level of service to our members and worked with partners to release groundbreaking research on the need for increased collaboration amongst leaders of community foundations.\n\nWe also have a number of blogs across our platforms (including the GuideStar blog, GrantSpace blog, GrantCraft blog, GlassPockets blog, Philanthropy News Digest Blog, and more!) that shine a light on relevant topics and trends affecting the sector.",
                    "target_population": "General/Unspecified",
                    "target_population2": "General/Unspecified",
                    "budget": "3002061",
                    "areas_served": ["United States"],
                }
            ],
            "charting_impact_answers": [
                {
                    "question": "How would you summarize the problem or need your organization is working to address?",
                    "answer": "As of February 2019, GuideStar joined forces with Foundation Center to become a new organization called Candid. The below reflects GuideStar’s historical programs as of January 31, 2019.\n\nAcross the globe, nonprofits play an important role within the evolving social contract: they provide services, drive innovation, and shape political discourse. Unfortunately, the culture and systems of the nonprofit sector do not always drive excellence, learning, or collaboration. The whole is less than the sum of its parts. For example: \n\n- proven impact rarely draws additional capital; \n- failure seldom drives learning; \n- shared goals rarely inspire collaboration;  \n- the voices of those we try to serve are lost.  \n\nThese obstacles limit the overall impact of the field. Until we fix these problems the nonprofit sector will continue to underperform—with profound consequences across society.",
                }
            ],
        },
        "financials": {
            "most_recent_year_financials": {
                "period_begin": "2019-01-01T05:00:00Z",
                "period_end": "2019-12-31T05:00:00Z",
                "fiscal_year": 2019,
                "assets_total": 1096532,
                "total_liabilities": 37801,
                "total_revenue": 1196844,
                "months_of_cash": "8.1",
                "expenses_total": 1640238,
                "net_gain_loss": -443394,
            }
        },
    },
}

demographics_v1 = {
    "code": 200,
    "message": "Request was processed successfully!",
    "took": 24,
    "errors": ["string"],
    "data": {
        "summary": {
            "organization_name": "Candid",
            "ein": "13-1837418",
            "city": "New York City",
            "state": "NY",
            "demographics_status": "This organization has provided Candid demographics data on 06/23/2023",
            "demographics_status_nonprofit": "Your organization has provided Candid demographics data on 06/23/2023",
            "date_last_modified": "01/02/2023",
        },
        "demographics": {
            "staff_level_totals": {
                "total_board_members": "18",
                "total_staff": "195",
                "total_senior_staff": "8",
            },
            "categories": [
                {
                    "category_id": 1,
                    "category": "Race & Ethnicity",
                    "board_members_not_collected": False,
                    "staff_not_collected": False,
                    "senior_staff_not_collected": False,
                    "subcategories": [
                        {
                            "subcategory_id": 1,
                            "subcategory": "Asian/Asian American",
                            "board_members": 2,
                            "staff": 26,
                            "senior_staff": 4,
                            "reported_by_ceo": False,
                            "reported_by_coceo": None,
                        }
                    ],
                }
            ],
        },
    },
}
