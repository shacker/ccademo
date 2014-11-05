from people.models import Medium, Profile, Staff, Instructor, Student, Alumni, Donation, Address, Award, Reference, Experience, Skill, Education, ImporterUsers
from anonymizer import Anonymizer

class MediumAnonymizer(Anonymizer):

    model = Medium

    attributes = [
        ('medium_id', "integer"),
        ('description', "varchar"),
    ]


class ProfileAnonymizer(Anonymizer):

    model = Profile

    attributes = [
        ('user_id', "SKIP"),
        ('person_id', "SKIP"),
        ('datatel_avatar_url', "SKIP"),
        ('suffix', "choice"),
        ('salutation', "choice"),
        ('middle_name', "name"),
        ('title', "varchar"),
        ('about', "lorem"),
        ('email2', "email"),
        ('home_phone1', "phonenumber"),
        ('biz_phone1', "phonenumber"),
        ('mobile_phone1', "phonenumber"),
        ('fax', "phonenumber"),
        ('allow_contact', "bool"),
        ('show_name', "bool"),
        ('url_personal', "varchar"),
        ('url_org', "varchar"),
        ('accepted_terms', "bool"),
        ('email_on_follow', "bool"),
    ]


class StaffAnonymizer(Anonymizer):

    model = Staff

    attributes = [
        ('profile_id', "SKIP"),
        ('office_num', "varchar"),
        ('extension', "varchar"),
    ]


class InstructorAnonymizer(Anonymizer):

    model = Instructor

    attributes = [
        ('profile_id', "SKIP"),
        ('office_num', "varchar"),
        ('extension', "varchar"),
        ('bio_short', "lorem"),
        ('bio_long', "lorem"),
    ]


class StudentAnonymizer(Anonymizer):

    model = Student

    attributes = [
        ('profile_id', "SKIP"),
        ('grad_year', "choice"),
        ('funding_amount', "SKIP"),
        ('enrollment_date', "date"),
        ('program_length', "integer"),
        ('visiting_scholar', "bool"),
    ]


class AlumniAnonymizer(Anonymizer):

    model = Alumni

    attributes = [
        ('profile_id', "SKIP"),
        ('grad_year', "choice"),
        ('third_year', "bool"),
        ('j200_inst', "varchar"),
        ('funding_amount', "SKIP"),
        ('enrollment_date', "date"),
        ('program_length', "integer"),
        ('equipment_balance', "SKIP"),
        ('visiting_scholar', "bool"),
        ('employer', "varchar"),
        ('specialty', "varchar"),
        ('medium', "choice"),
        ('prev_emp1', "varchar"),
        ('prev_emp2', "varchar"),
        ('prev_emp3', "varchar"),
        ('notes_exclude', "bool"),
        ('notes', "lorem"),
        ('mod_date', "date"),
        ('pub_display', "bool"),
        ('freelance', "bool"),
        ('region', "choice"),
        ('prev_intern1', "varchar"),
        ('prev_intern2', "varchar"),
        ('prev_intern3', "varchar"),
        ('first_job', "varchar"),
        ('books', "lorem"),
        ('deceased_notes', "varchar"),
        ('mia', "bool"),
        ('mia_notes', "lorem"),
        ('interview', "bool"),
        ('interview_year', "choice"),
        ('interview_notes', "lorem"),
        ('agents_year', "choice"),
        ('agents_notes', "lorem"),
        ('event_attend_notes', "lorem"),
        ('famous_notes', "lorem"),
        ('volunteer_speak', "bool"),
        ('volunteer_committee', "bool"),
        ('volunteer_interview', "bool"),
        ('volunteer_mentor', "bool"),
        ('volunteer_agent', "bool"),
        ('maillist_class', "bool"),
        ('no_maillists', "bool"),
        ('no_reminder', "bool"),
        ('suggestions', "lorem"),
        ('committee_notes', "lorem"),
        ('inactive', "bool"),
        ('revision', "integer"),
    ]


class DonationAnonymizer(Anonymizer):

    model = Donation

    attributes = [
        ('id', "SKIP"),
        ('profile_id', "SKIP"),
        ('amount', "integer"),
        ('date', "date"),
        ('description', "varchar"),
        ('notes', "lorem"),
    ]


class AddressAnonymizer(Anonymizer):

    model = Address

    attributes = [
        ('id', "SKIP"),
        ('profile_id', "SKIP"),
        ('address_type', "choice"),
        ('street_1', "street_address"),
        ('street_2', "street_address"),
        ('street_3', "street_address"),
        ('city', "city"),
        ('state', "choice"),
        ('state_other', "varchar"),
        ('postal_code', "uk_postcode"),
        ('display', "bool"),
    ]


class AwardAnonymizer(Anonymizer):

    model = Award

    attributes = [
        ('id', "SKIP"),
        ('profile_id', "SKIP"),
        ('title', "varchar"),
        ('description', "lorem"),
        ('date_received', "date"),
        ('display', "bool"),
    ]


class ReferenceAnonymizer(Anonymizer):

    model = Reference

    attributes = [
        ('id', "SKIP"),
        ('profile_id', "SKIP"),
        ('body', "lorem"),
    ]


class ExperienceAnonymizer(Anonymizer):

    model = Experience

    attributes = [
        ('id', "SKIP"),
        ('profile_id', "SKIP"),
        ('experience_type', "choice"),
        ('title', "varchar"),
        ('description', "lorem"),
        ('company', "varchar"),
        ('city', "city"),
        ('state', "choice"),
        ('country', "varchar"),
        ('start_date', "date"),
        ('end_date', "date"),
        ('display', "bool"),
    ]


class SkillAnonymizer(Anonymizer):

    model = Skill

    attributes = [
        ('id', "SKIP"),
        ('profile_id', "SKIP"),
        ('summary', "lorem"),
        ('display', "bool"),
    ]


class EducationAnonymizer(Anonymizer):

    model = Education

    attributes = [
        ('id', "SKIP"),
        ('profile_id', "SKIP"),
        ('diploma', "choice"),
        ('school', "varchar"),
        ('description', "lorem"),
        ('start_date', "date"),
        ('end_date', "date"),
        ('display', "bool"),
    ]


class ImporterUsersAnonymizer(Anonymizer):

    model = ImporterUsers

    attributes = [
        ('id', "SKIP"),
        ('action', "SKIP"),
        ('person_id', "SKIP"),
        ('section_id', "SKIP"),
        ('first_name', "SKIP"),
        ('last_name', "SKIP"),
        ('email', "SKIP"),
        ('photo_url', "SKIP"),
        ('person_type', "SKIP"),
    ]
