from django.db import models
from uuid import uuid4

# Create your models here.


# essentials v3 models
# class EssentialsOrganization(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
#     organization_id = models.CharField(max_length=100)
#     ein = models.CharField(max_length=100)
#     organization_name = models.CharField(max_length=100)
#     also_known_as = models.CharField(max_length=100)
#     mission = models.CharField(max_length=200)
#     website_url = models.CharField(max_length=100)
#     logo_url = models.CharField(max_length=100)
#     profile_level = models.CharField(max_length=100)
#     profile_year = models.CharField(max_length=100)
#     profile_link = models.CharField(max_length=300)
#     profile_logo = models.CharField(max_length=300)
#     contact_name = models.CharField(
#         max_length=100,
#     )
#     contact_email = models.EmailField()
#     contact_phone = models.CharField(max_length=100)
#     contact_title = models.CharField(max_length=100)
#     number_of_employees = models.IntegerField(default=0)
#     ruling_year = models.CharField(max_length=100)
#     bmf_status = models.BooleanField(default=False)
#     pub78_verified = models.BooleanField(default=False)
#     allow_online_giving = models.BooleanField(default=True)
#     dei_submitted = models.BooleanField(default=False)
#     revoked = models.BooleanField(default=False)
#     defuncted_or_merged = models.BooleanField(default=False)
#     relationship_type = models.JSONField(null=True, blank=True)
#     address_line_1 = models.CharField(max_length=255)
#     address_line_2 = models.CharField(max_length=255, blank=True)
#     city = models.CharField(max_length=255)
#     state = models.CharField(max_length=2)
#     zip = models.IntegerField()
#     msa = models.CharField(max_length=255, blank=True)
#     county = models.CharField(max_length=255, blank=True)
#     latitude = models.DecimalField(max_digits=10, decimal_places=6)
#     longitude = models.DecimalField(max_digits=10, decimal_places=6)
#     subject_codes = models.JSONField()
#     population_served_codes = models.JSONField()
#     ntee_codes = models.JSONField()
#     subsection_code = models.CharField(max_length=100)
#     subsection_code_description = models.CharField(max_length=100)
#     foundation_code = models.CharField(max_length=100)
#     foundation_code_description = models.CharField(max_length=100)
#     form_types = models.CharField(max_length=255)
#     fiscal_year = models.IntegerField()
#     total_revenue = models.DecimalField(max_digits=15, decimal_places=2)
#     total_expenses = models.DecimalField(max_digits=15, decimal_places=2)
#     total_assets = models.DecimalField(max_digits=15, decimal_places=2)
#     bmf_gross_receipts = models.DecimalField(max_digits=15, decimal_places=2)
#     bmf_assets = models.DecimalField(max_digits=15, decimal_places=2)
#     required_to_file_990t = models.BooleanField(default=False)
#     a_133_audit_performed = models.BooleanField(default=False)
#     seal_last_modified = models.DateTimeField()
#     profile_last_modified = models.DateTimeField()
#     dei_last_modified = models.DateTimeField()
#     financials_last_modified = models.DateTimeField()
#     last_published = models.DateTimeField()

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_deleted = models.BooleanField(default=False)

#     class Meta:
#         db_table = "candid_essentials_organization"

#     def __str__(self):
#         return str(self.id)


class EssentialsOrganizationUpdate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    search_terms = models.CharField(max_length=255)
    organization_id = models.CharField(max_length=20)
    ein = models.CharField(max_length=20)
    organization_name = models.CharField(max_length=255)
    also_known_as = models.CharField(max_length=255, blank=True, null=True)
    group_exemption = models.CharField(max_length=100, null=True, blank=True)
    mission = models.TextField(null=True, blank=True)
    website_url = models.URLField(blank=True, null=True)
    logo_url = models.URLField(blank=True, null=True)
    donation_page = models.URLField(blank=True, null=True)
    profile_level = models.CharField(max_length=20, null=True, blank=True)
    profile_year = models.PositiveIntegerField(null=True, blank=True)
    profile_link = models.URLField(null=True, blank=True)
    profile_logo = models.URLField(null=True, blank=True)
    leader_name = models.CharField(max_length=255, null=True, blank=True)
    leader_title = models.CharField(max_length=255, null=True, blank=True)
    contact_name = models.CharField(max_length=255, null=True, blank=True)
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    contact_title = models.CharField(max_length=255, blank=True, null=True)
    number_of_employees = models.CharField(max_length=255, blank=True, null=True)
    ruling_year = models.PositiveIntegerField(blank=True, null=True)
    bmf_status = models.BooleanField(null=True, blank=True)
    pub78_verified = models.BooleanField(null=True, blank=True)
    allow_online_giving = models.BooleanField(null=True, blank=True)
    dei_submitted = models.BooleanField(null=True, blank=True)
    revoked = models.BooleanField(null=True, blank=True)
    defunct_or_merged = models.BooleanField(null=True, blank=True)
    relationship_type = models.JSONField(null=True, blank=True)
    address_line_1 = models.CharField(max_length=255, null=True, blank=True)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zip = models.CharField(max_length=10, null=True, blank=True)
    msa = models.CharField(max_length=255, blank=True, null=True)
    congressional_district = models.CharField(max_length=255, blank=True, null=True)
    county = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    subject_codes = models.JSONField(null=True, blank=True)
    population_served_codes = models.JSONField(null=True, blank=True, )
    ntee_codes = models.JSONField(blank=True, null=True)
    subsection_code = models.CharField(max_length=100, null=True, blank=True)
    subsection_code_description = models.CharField(
        max_length=255, null=True, blank=True
    )
    foundation_code = models.CharField(max_length=100, null=True, blank=True)
    foundation_code_description = models.CharField(
        max_length=255, null=True, blank=True
    )
    form_type = models.CharField(max_length=255, null=True, blank=True)
    fiscal_year = models.PositiveIntegerField(null=True, blank=True)
    total_revenue = models.FloatField(null=True, blank=True)
    total_expenses = models.FloatField(null=True, blank=True)
    total_assets = models.FloatField(null=True, blank=True)
    bmf_gross_receipts = models.FloatField(null=True, blank=True)
    bmf_assets = models.FloatField(null=True, blank=True)
    required_to_file_990t = models.BooleanField(null=True, blank=True)
    a_133_audit_performed = models.BooleanField(null=True, blank=True)
    seal_last_modified = models.CharField(max_length=255, null=True, blank=True)
    profile_last_modified = models.CharField(max_length=255, null=True, blank=True)
    dei_last_modified = models.CharField(max_length=255, null=True, blank=True)
    financials_last_modified = models.CharField(max_length=255, null=True, blank=True)
    last_modified = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "candid_essentials_organization"

    def __str__(self):
        return str(self.id)


class EssentialsOrganizationUpdateHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    size = models.PositiveIntegerField()
    search_terms = models.CharField(max_length=255)
    limit = models.PositiveIntegerField()
    page = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "candid_essentials_organization_update_history"

    def __str__(self):
        return str(self.id)
