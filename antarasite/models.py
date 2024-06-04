from django.db import models

# Create your models here.

class Inquiry(models.Model):
    GENDER_CHOICES = [
        ('', 'Select Gender*'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    ABOUT_US_CHOICES = [
        ('', 'How did you hear about us? *'),
        ('Friend', 'Friend'),
        ('Website', 'Website'),
        ('Advertisement', 'Advertisement'),
        ('Other', 'Other'),
    ]

    COUNTRY_CHOICES = [
        ('', 'Select Country*'),
        ('Afghanistan', 'Afghanistan'),
        ('Åland Islands', 'Åland Islands'),
        ('Albania', 'Albania'),
        ('Algeria', 'Algeria'),
        ('American Samoa', 'American Samoa'),
        ('Andorra', 'Andorra'),
        ('Angola', 'Angola'),
        ('Anguilla', 'Anguilla'),
        ('Antarctica', 'Antarctica'),
        ('Antigua and Barbuda', 'Antigua and Barbuda'),
        ('Argentina', 'Argentina'),
        ('Armenia', 'Armenia'),
        ('Aruba', 'Aruba'),
        ('Australia', 'Australia'),
        ('Austria', 'Austria'),
        ('Azerbaijan', 'Azerbaijan'),
        ('Bahamas', 'Bahamas'),
        ('Bahrain', 'Bahrain'),
        ('Bangladesh', 'Bangladesh'),
        ('Barbados', 'Barbados'),
        ('Belarus', 'Belarus'),
        ('Belgium', 'Belgium'),
        ('Belize', 'Belize'),
        ('Benin', 'Benin'),
        ('Bermuda', 'Bermuda'),
        ('Bhutan', 'Bhutan'),
        ('Bolivia', 'Bolivia'),
        ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'),
        ('Botswana', 'Botswana'),
        ('Bouvet Island', 'Bouvet Island'),
        ('Brazil', 'Brazil'),
        ('British Indian Ocean Territory', 'British Indian Ocean Territory'),
        ('Brunei Darussalam', 'Brunei Darussalam'),
        ('Bulgaria', 'Bulgaria'),
        ('Burkina Faso', 'Burkina Faso'),
        ('Burundi', 'Burundi'),
        ('Cambodia', 'Cambodia'),
        ('Cameroon', 'Cameroon'),
        ('Canada', 'Canada'),
        ('Cape Verde', 'Cape Verde'),
        ('Cayman Islands', 'Cayman Islands'),
        ('Central African Republic', 'Central African Republic'),
        ('Chad', 'Chad'),
        ('Chile', 'Chile'),
        ('China', 'China'),
        ('Christmas Island', 'Christmas Island'),
        ('Cocos (Keeling) Islands', 'Cocos (Keeling) Islands'),
        ('Colombia', 'Colombia'),
        ('Comoros', 'Comoros'),
        ('Congo', 'Congo'),
        ('Congo, The Democratic Republic of The', 'Congo, The Democratic Republic of The'),
        ('Cook Islands', 'Cook Islands'),
        ('Costa Rica', 'Costa Rica'),
        ('Cote D\'ivoire', 'Cote D\'ivoire'),
        ('Croatia', 'Croatia'),
        ('Cuba', 'Cuba'),
        ('Cyprus', 'Cyprus'),
        ('Czech Republic', 'Czech Republic'),
        ('Denmark', 'Denmark'),
        ('Djibouti', 'Djibouti'),
        ('Dominica', 'Dominica'),
        ('Dominican Republic', 'Dominican Republic'),
        ('Ecuador', 'Ecuador'),
        ('Egypt', 'Egypt'),
        ('El Salvador', 'El Salvador'),
        ('Equatorial Guinea', 'Equatorial Guinea'),
        ('Eritrea', 'Eritrea'),
        ('Estonia', 'Estonia'),
        ('Ethiopia', 'Ethiopia'),
        ('Falkland Islands (Malvinas)', 'Falkland Islands (Malvinas)'),
        ('Faroe Islands', 'Faroe Islands'),
        ('Fiji', 'Fiji'),
        ('Finland', 'Finland'),
        ('France', 'France'),
        ('French Guiana', 'French Guiana'),
        ('French Polynesia', 'French Polynesia'),
        ('French Southern Territories', 'French Southern Territories'),
        ('Gabon', 'Gabon'),
        ('Gambia', 'Gambia'),
        ('Georgia', 'Georgia'),
        ('Germany', 'Germany'),
        ('Ghana', 'Ghana'),
        ('Gibraltar', 'Gibraltar'),
        ('Greece', 'Greece'),
        ('Greenland', 'Greenland'),
        ('Grenada', 'Grenada'),
        ('Guadeloupe', 'Guadeloupe'),
        ('Guam', 'Guam'),
        ('Guatemala', 'Guatemala'),
        ('Guernsey', 'Guernsey'),
        ('Guinea', 'Guinea'),
        ('Guinea-bissau', 'Guinea-bissau'),
        ('Guyana', 'Guyana'),
        ('Haiti', 'Haiti'),
        ('Heard Island and Mcdonald Islands', 'Heard Island and Mcdonald Islands'),
        ('Holy See (Vatican City State)', 'Holy See (Vatican City State)'),
        ('Honduras', 'Honduras'),
        ('Hong Kong', 'Hong Kong'),
        ('Hungary', 'Hungary'),
        ('Iceland', 'Iceland'),
        ('India', 'India'),
        ('Indonesia', 'Indonesia'),
        ('Iran, Islamic Republic of', 'Iran, Islamic Republic of'),
        ('Iraq', 'Iraq'),
        ('Ireland', 'Ireland'),
        ('Isle of Man', 'Isle of Man'),
        ('Israel', 'Israel'),
        ('Italy', 'Italy'),
        ('Jamaica', 'Jamaica'),
        ('Japan', 'Japan'),
        ('Jersey', 'Jersey'),
        ('Jordan', 'Jordan'),
        ('Kazakhstan', 'Kazakhstan'),
        ('Kenya', 'Kenya'),
        ('Kiribati', 'Kiribati'),
        ('Korea, Democratic People\'s Republic of', 'Korea, Democratic People\'s Republic of'),
        ('Korea, Republic of', 'Korea, Republic of'),
        ('Kuwait', 'Kuwait'),
        ('Kyrgyzstan', 'Kyrgyzstan'),
        ('Lao People\'s Democratic Republic', 'Lao People\'s Democratic Republic'),
        ('Latvia', 'Latvia'),
        ('Lebanon', 'Lebanon'),
        ('Lesotho', 'Lesotho'),
        ('Liberia', 'Liberia'),
        ('Libyan Arab Jamahiriya', 'Libyan Arab Jamahiriya'),
        ('Liechtenstein', 'Liechtenstein'),
        ('Lithuania', 'Lithuania'),
        ('Luxembourg', 'Luxembourg'),
        ('Macao', 'Macao'),
        ('Macedonia, The Former Yugoslav Republic of', 'Macedonia, The Former Yugoslav Republic of'),
        ('Madagascar', 'Madagascar'),
        ('Malawi', 'Malawi'),
        ('Malaysia', 'Malaysia'),
        ('Maldives', 'Maldives'),
        ('Mali', 'Mali'),
        ('Malta', 'Malta'),
        ('Marshall Islands', 'Marshall Islands'),
        ('Martinique', 'Martinique'),
        ('Mauritania', 'Mauritania'),
        ('Mauritius', 'Mauritius'),
        ('Mayotte', 'Mayotte'),
        ('Mexico', 'Mexico'),
        ('Micronesia, Federated States of', 'Micronesia, Federated States of'),
        ('Moldova, Republic of', 'Moldova, Republic of'),
        ('Monaco', 'Monaco'),
        ('Mongolia', 'Mongolia'),
        ('Montenegro', 'Montenegro'),
        ('Montserrat', 'Montserrat'),
        ('Morocco', 'Morocco'),
        ('Mozambique', 'Mozambique'),
        ('Myanmar', 'Myanmar'),
        ('Namibia', 'Namibia'),
        ('Nauru', 'Nauru'),
        ('Nepal', 'Nepal'),
        ('Netherlands', 'Netherlands'),
        ('Netherlands Antilles', 'Netherlands Antilles'),
        ('New Caledonia', 'New Caledonia'),
        ('New Zealand', 'New Zealand'),
        ('Nicaragua', 'Nicaragua'),
        ('Niger', 'Niger'),
        ('Nigeria', 'Nigeria'),
        ('Niue', 'Niue'),
        ('Norfolk Island', 'Norfolk Island'),
        ('Northern Mariana Islands', 'Northern Mariana Islands'),
        ('Norway', 'Norway'),
        ('Oman', 'Oman'),
        ('Pakistan', 'Pakistan'),
        ('Palau', 'Palau'),
        ('Palestinian Territory, Occupied', 'Palestinian Territory, Occupied'),
        ('Panama', 'Panama'),
        ('Papua New Guinea', 'Papua New Guinea'),
        ('Paraguay', 'Paraguay'),
        ('Peru', 'Peru'),
        ('Philippines', 'Philippines'),
        ('Pitcairn', 'Pitcairn'),
        ('Poland', 'Poland'),
        ('Portugal', 'Portugal'),
        ('Puerto Rico', 'Puerto Rico'),
        ('Qatar', 'Qatar'),
        ('Reunion', 'Reunion'),
        ('Romania', 'Romania'),
        ('Russian Federation', 'Russian Federation'),
        ('Rwanda', 'Rwanda'),
        ('Saint Helena', 'Saint Helena'),
        ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
        ('Saint Lucia', 'Saint Lucia'),
        ('Saint Pierre and Miquelon', 'Saint Pierre and Miquelon'),
        ('Saint Vincent and The Grenadines', 'Saint Vincent and The Grenadines'),
        ('Samoa', 'Samoa'),
        ('San Marino', 'San Marino'),
        ('Sao Tome and Principe', 'Sao Tome and Principe'),
        ('Saudi Arabia', 'Saudi Arabia'),
        ('Senegal', 'Senegal'),
        ('Serbia', 'Serbia'),
        ('Seychelles', 'Seychelles'),
        ('Sierra Leone', 'Sierra Leone'),
        ('Singapore', 'Singapore'),
        ('Slovakia', 'Slovakia'),
        ('Slovenia', 'Slovenia'),
        ('Solomon Islands', 'Solomon Islands'),
        ('Somalia', 'Somalia'),
        ('South Africa', 'South Africa'),
        ('South Georgia and The South Sandwich Islands', 'South Georgia and The South Sandwich Islands'),
        ('Spain', 'Spain'),
        ('Sri Lanka', 'Sri Lanka'),
        ('Sudan', 'Sudan'),
        ('Suriname', 'Suriname'),
        ('Svalbard and Jan Mayen', 'Svalbard and Jan Mayen'),
        ('Swaziland', 'Swaziland'),
        ('Sweden', 'Sweden'),
        ('Switzerland', 'Switzerland'),
        ('Syrian Arab Republic', 'Syrian Arab Republic'),
        ('Taiwan', 'Taiwan'),
        ('Tajikistan', 'Tajikistan'),
        ('Tanzania, United Republic of', 'Tanzania, United Republic of'),
        ('Thailand', 'Thailand'),
        ('Timor-leste', 'Timor-leste'),
        ('Togo', 'Togo'),
        ('Tokelau', 'Tokelau'),
        ('Tonga', 'Tonga'),
        ('Trinidad and Tobago', 'Trinidad and Tobago'),
        ('Tunisia', 'Tunisia'),
        ('Turkey', 'Turkey'),
        ('Turkmenistan', 'Turkmenistan'),
        ('Turks and Caicos Islands', 'Turks and Caicos Islands'),
        ('Tuvalu', 'Tuvalu'),
        ('Uganda', 'Uganda'),
        ('Ukraine', 'Ukraine'),
        ('United Arab Emirates', 'United Arab Emirates'),
        ('United Kingdom', 'United Kingdom'),
        ('United States', 'United States'),
        ('United States Minor Outlying Islands', 'United States Minor Outlying Islands'),
        ('Uruguay', 'Uruguay'),
        ('Uzbekistan', 'Uzbekistan'),
        ('Vanuatu', 'Vanuatu'),
        ('Venezuela', 'Venezuela'),
        ('Viet Nam', 'Viet Nam'),
        ('Virgin Islands, British', 'Virgin Islands, British'),
        ('Virgin Islands, U.S.', 'Virgin Islands, U.S.'),
        ('Wallis and Futuna', 'Wallis and Futuna'),
        ('Western Sahara', 'Western Sahara'),
        ('Yemen', 'Yemen'),
        ('Zambia', 'Zambia'),
        ('Zimbabwe', 'Zimbabwe'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    country = models.CharField(max_length=255, choices=COUNTRY_CHOICES)
    city = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    comment = models.TextField(blank=True)
    aboutus = models.CharField(max_length=20, choices=ABOUT_US_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Home Page - Inquiry"
        verbose_name_plural = "Home Page - Inquiries"

class AboutusInquiry(models.Model):
    GENDER_CHOICES = [
        ('', 'Select Gender*'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    ABOUT_US_CHOICES = [
        ('', 'How did you hear about us? *'),
        ('Friend', 'Friend'),
        ('Website', 'Website'),
        ('Advertisement', 'Advertisement'),
        ('Other', 'Other'),
    ]

    COUNTRY_CHOICES = [
        ('', 'Select Country*'),
        ('Afghanistan', 'Afghanistan'),
        ('Åland Islands', 'Åland Islands'),
        ('Albania', 'Albania'),
        ('Algeria', 'Algeria'),
        ('American Samoa', 'American Samoa'),
        ('Andorra', 'Andorra'),
        ('Angola', 'Angola'),
        ('Anguilla', 'Anguilla'),
        ('Antarctica', 'Antarctica'),
        ('Antigua and Barbuda', 'Antigua and Barbuda'),
        ('Argentina', 'Argentina'),
        ('Armenia', 'Armenia'),
        ('Aruba', 'Aruba'),
        ('Australia', 'Australia'),
        ('Austria', 'Austria'),
        ('Azerbaijan', 'Azerbaijan'),
        ('Bahamas', 'Bahamas'),
        ('Bahrain', 'Bahrain'),
        ('Bangladesh', 'Bangladesh'),
        ('Barbados', 'Barbados'),
        ('Belarus', 'Belarus'),
        ('Belgium', 'Belgium'),
        ('Belize', 'Belize'),
        ('Benin', 'Benin'),
        ('Bermuda', 'Bermuda'),
        ('Bhutan', 'Bhutan'),
        ('Bolivia', 'Bolivia'),
        ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'),
        ('Botswana', 'Botswana'),
        ('Bouvet Island', 'Bouvet Island'),
        ('Brazil', 'Brazil'),
        ('British Indian Ocean Territory', 'British Indian Ocean Territory'),
        ('Brunei Darussalam', 'Brunei Darussalam'),
        ('Bulgaria', 'Bulgaria'),
        ('Burkina Faso', 'Burkina Faso'),
        ('Burundi', 'Burundi'),
        ('Cambodia', 'Cambodia'),
        ('Cameroon', 'Cameroon'),
        ('Canada', 'Canada'),
        ('Cape Verde', 'Cape Verde'),
        ('Cayman Islands', 'Cayman Islands'),
        ('Central African Republic', 'Central African Republic'),
        ('Chad', 'Chad'),
        ('Chile', 'Chile'),
        ('China', 'China'),
        ('Christmas Island', 'Christmas Island'),
        ('Cocos (Keeling) Islands', 'Cocos (Keeling) Islands'),
        ('Colombia', 'Colombia'),
        ('Comoros', 'Comoros'),
        ('Congo', 'Congo'),
        ('Congo, The Democratic Republic of The', 'Congo, The Democratic Republic of The'),
        ('Cook Islands', 'Cook Islands'),
        ('Costa Rica', 'Costa Rica'),
        ('Cote D\'ivoire', 'Cote D\'ivoire'),
        ('Croatia', 'Croatia'),
        ('Cuba', 'Cuba'),
        ('Cyprus', 'Cyprus'),
        ('Czech Republic', 'Czech Republic'),
        ('Denmark', 'Denmark'),
        ('Djibouti', 'Djibouti'),
        ('Dominica', 'Dominica'),
        ('Dominican Republic', 'Dominican Republic'),
        ('Ecuador', 'Ecuador'),
        ('Egypt', 'Egypt'),
        ('El Salvador', 'El Salvador'),
        ('Equatorial Guinea', 'Equatorial Guinea'),
        ('Eritrea', 'Eritrea'),
        ('Estonia', 'Estonia'),
        ('Ethiopia', 'Ethiopia'),
        ('Falkland Islands (Malvinas)', 'Falkland Islands (Malvinas)'),
        ('Faroe Islands', 'Faroe Islands'),
        ('Fiji', 'Fiji'),
        ('Finland', 'Finland'),
        ('France', 'France'),
        ('French Guiana', 'French Guiana'),
        ('French Polynesia', 'French Polynesia'),
        ('French Southern Territories', 'French Southern Territories'),
        ('Gabon', 'Gabon'),
        ('Gambia', 'Gambia'),
        ('Georgia', 'Georgia'),
        ('Germany', 'Germany'),
        ('Ghana', 'Ghana'),
        ('Gibraltar', 'Gibraltar'),
        ('Greece', 'Greece'),
        ('Greenland', 'Greenland'),
        ('Grenada', 'Grenada'),
        ('Guadeloupe', 'Guadeloupe'),
        ('Guam', 'Guam'),
        ('Guatemala', 'Guatemala'),
        ('Guernsey', 'Guernsey'),
        ('Guinea', 'Guinea'),
        ('Guinea-bissau', 'Guinea-bissau'),
        ('Guyana', 'Guyana'),
        ('Haiti', 'Haiti'),
        ('Heard Island and Mcdonald Islands', 'Heard Island and Mcdonald Islands'),
        ('Holy See (Vatican City State)', 'Holy See (Vatican City State)'),
        ('Honduras', 'Honduras'),
        ('Hong Kong', 'Hong Kong'),
        ('Hungary', 'Hungary'),
        ('Iceland', 'Iceland'),
        ('India', 'India'),
        ('Indonesia', 'Indonesia'),
        ('Iran, Islamic Republic of', 'Iran, Islamic Republic of'),
        ('Iraq', 'Iraq'),
        ('Ireland', 'Ireland'),
        ('Isle of Man', 'Isle of Man'),
        ('Israel', 'Israel'),
        ('Italy', 'Italy'),
        ('Jamaica', 'Jamaica'),
        ('Japan', 'Japan'),
        ('Jersey', 'Jersey'),
        ('Jordan', 'Jordan'),
        ('Kazakhstan', 'Kazakhstan'),
        ('Kenya', 'Kenya'),
        ('Kiribati', 'Kiribati'),
        ('Korea, Democratic People\'s Republic of', 'Korea, Democratic People\'s Republic of'),
        ('Korea, Republic of', 'Korea, Republic of'),
        ('Kuwait', 'Kuwait'),
        ('Kyrgyzstan', 'Kyrgyzstan'),
        ('Lao People\'s Democratic Republic', 'Lao People\'s Democratic Republic'),
        ('Latvia', 'Latvia'),
        ('Lebanon', 'Lebanon'),
        ('Lesotho', 'Lesotho'),
        ('Liberia', 'Liberia'),
        ('Libyan Arab Jamahiriya', 'Libyan Arab Jamahiriya'),
        ('Liechtenstein', 'Liechtenstein'),
        ('Lithuania', 'Lithuania'),
        ('Luxembourg', 'Luxembourg'),
        ('Macao', 'Macao'),
        ('Macedonia, The Former Yugoslav Republic of', 'Macedonia, The Former Yugoslav Republic of'),
        ('Madagascar', 'Madagascar'),
        ('Malawi', 'Malawi'),
        ('Malaysia', 'Malaysia'),
        ('Maldives', 'Maldives'),
        ('Mali', 'Mali'),
        ('Malta', 'Malta'),
        ('Marshall Islands', 'Marshall Islands'),
        ('Martinique', 'Martinique'),
        ('Mauritania', 'Mauritania'),
        ('Mauritius', 'Mauritius'),
        ('Mayotte', 'Mayotte'),
        ('Mexico', 'Mexico'),
        ('Micronesia, Federated States of', 'Micronesia, Federated States of'),
        ('Moldova, Republic of', 'Moldova, Republic of'),
        ('Monaco', 'Monaco'),
        ('Mongolia', 'Mongolia'),
        ('Montenegro', 'Montenegro'),
        ('Montserrat', 'Montserrat'),
        ('Morocco', 'Morocco'),
        ('Mozambique', 'Mozambique'),
        ('Myanmar', 'Myanmar'),
        ('Namibia', 'Namibia'),
        ('Nauru', 'Nauru'),
        ('Nepal', 'Nepal'),
        ('Netherlands', 'Netherlands'),
        ('Netherlands Antilles', 'Netherlands Antilles'),
        ('New Caledonia', 'New Caledonia'),
        ('New Zealand', 'New Zealand'),
        ('Nicaragua', 'Nicaragua'),
        ('Niger', 'Niger'),
        ('Nigeria', 'Nigeria'),
        ('Niue', 'Niue'),
        ('Norfolk Island', 'Norfolk Island'),
        ('Northern Mariana Islands', 'Northern Mariana Islands'),
        ('Norway', 'Norway'),
        ('Oman', 'Oman'),
        ('Pakistan', 'Pakistan'),
        ('Palau', 'Palau'),
        ('Palestinian Territory, Occupied', 'Palestinian Territory, Occupied'),
        ('Panama', 'Panama'),
        ('Papua New Guinea', 'Papua New Guinea'),
        ('Paraguay', 'Paraguay'),
        ('Peru', 'Peru'),
        ('Philippines', 'Philippines'),
        ('Pitcairn', 'Pitcairn'),
        ('Poland', 'Poland'),
        ('Portugal', 'Portugal'),
        ('Puerto Rico', 'Puerto Rico'),
        ('Qatar', 'Qatar'),
        ('Reunion', 'Reunion'),
        ('Romania', 'Romania'),
        ('Russian Federation', 'Russian Federation'),
        ('Rwanda', 'Rwanda'),
        ('Saint Helena', 'Saint Helena'),
        ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
        ('Saint Lucia', 'Saint Lucia'),
        ('Saint Pierre and Miquelon', 'Saint Pierre and Miquelon'),
        ('Saint Vincent and The Grenadines', 'Saint Vincent and The Grenadines'),
        ('Samoa', 'Samoa'),
        ('San Marino', 'San Marino'),
        ('Sao Tome and Principe', 'Sao Tome and Principe'),
        ('Saudi Arabia', 'Saudi Arabia'),
        ('Senegal', 'Senegal'),
        ('Serbia', 'Serbia'),
        ('Seychelles', 'Seychelles'),
        ('Sierra Leone', 'Sierra Leone'),
        ('Singapore', 'Singapore'),
        ('Slovakia', 'Slovakia'),
        ('Slovenia', 'Slovenia'),
        ('Solomon Islands', 'Solomon Islands'),
        ('Somalia', 'Somalia'),
        ('South Africa', 'South Africa'),
        ('South Georgia and The South Sandwich Islands', 'South Georgia and The South Sandwich Islands'),
        ('Spain', 'Spain'),
        ('Sri Lanka', 'Sri Lanka'),
        ('Sudan', 'Sudan'),
        ('Suriname', 'Suriname'),
        ('Svalbard and Jan Mayen', 'Svalbard and Jan Mayen'),
        ('Swaziland', 'Swaziland'),
        ('Sweden', 'Sweden'),
        ('Switzerland', 'Switzerland'),
        ('Syrian Arab Republic', 'Syrian Arab Republic'),
        ('Taiwan', 'Taiwan'),
        ('Tajikistan', 'Tajikistan'),
        ('Tanzania, United Republic of', 'Tanzania, United Republic of'),
        ('Thailand', 'Thailand'),
        ('Timor-leste', 'Timor-leste'),
        ('Togo', 'Togo'),
        ('Tokelau', 'Tokelau'),
        ('Tonga', 'Tonga'),
        ('Trinidad and Tobago', 'Trinidad and Tobago'),
        ('Tunisia', 'Tunisia'),
        ('Turkey', 'Turkey'),
        ('Turkmenistan', 'Turkmenistan'),
        ('Turks and Caicos Islands', 'Turks and Caicos Islands'),
        ('Tuvalu', 'Tuvalu'),
        ('Uganda', 'Uganda'),
        ('Ukraine', 'Ukraine'),
        ('United Arab Emirates', 'United Arab Emirates'),
        ('United Kingdom', 'United Kingdom'),
        ('United States', 'United States'),
        ('United States Minor Outlying Islands', 'United States Minor Outlying Islands'),
        ('Uruguay', 'Uruguay'),
        ('Uzbekistan', 'Uzbekistan'),
        ('Vanuatu', 'Vanuatu'),
        ('Venezuela', 'Venezuela'),
        ('Viet Nam', 'Viet Nam'),
        ('Virgin Islands, British', 'Virgin Islands, British'),
        ('Virgin Islands, U.S.', 'Virgin Islands, U.S.'),
        ('Wallis and Futuna', 'Wallis and Futuna'),
        ('Western Sahara', 'Western Sahara'),
        ('Yemen', 'Yemen'),
        ('Zambia', 'Zambia'),
        ('Zimbabwe', 'Zimbabwe'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    country = models.CharField(max_length=255, choices=COUNTRY_CHOICES)
    city = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    comment = models.TextField(blank=True)
    aboutus = models.CharField(max_length=20, choices=ABOUT_US_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "About Us - Inquiry"
        verbose_name_plural = "About Us - Inquiries"
    
class ContactusInquiry(models.Model):
    GENDER_CHOICES = [
        ('', 'Select Gender*'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    ABOUT_US_CHOICES = [
        ('', 'How did you hear about us? *'),
        ('Friend', 'Friend'),
        ('Website', 'Website'),
        ('Advertisement', 'Advertisement'),
        ('Other', 'Other'),
    ]

    COUNTRY_CHOICES = [
        ('', 'Select Country*'),
        ('Afghanistan', 'Afghanistan'),
        ('Åland Islands', 'Åland Islands'),
        ('Albania', 'Albania'),
        ('Algeria', 'Algeria'),
        ('American Samoa', 'American Samoa'),
        ('Andorra', 'Andorra'),
        ('Angola', 'Angola'),
        ('Anguilla', 'Anguilla'),
        ('Antarctica', 'Antarctica'),
        ('Antigua and Barbuda', 'Antigua and Barbuda'),
        ('Argentina', 'Argentina'),
        ('Armenia', 'Armenia'),
        ('Aruba', 'Aruba'),
        ('Australia', 'Australia'),
        ('Austria', 'Austria'),
        ('Azerbaijan', 'Azerbaijan'),
        ('Bahamas', 'Bahamas'),
        ('Bahrain', 'Bahrain'),
        ('Bangladesh', 'Bangladesh'),
        ('Barbados', 'Barbados'),
        ('Belarus', 'Belarus'),
        ('Belgium', 'Belgium'),
        ('Belize', 'Belize'),
        ('Benin', 'Benin'),
        ('Bermuda', 'Bermuda'),
        ('Bhutan', 'Bhutan'),
        ('Bolivia', 'Bolivia'),
        ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'),
        ('Botswana', 'Botswana'),
        ('Bouvet Island', 'Bouvet Island'),
        ('Brazil', 'Brazil'),
        ('British Indian Ocean Territory', 'British Indian Ocean Territory'),
        ('Brunei Darussalam', 'Brunei Darussalam'),
        ('Bulgaria', 'Bulgaria'),
        ('Burkina Faso', 'Burkina Faso'),
        ('Burundi', 'Burundi'),
        ('Cambodia', 'Cambodia'),
        ('Cameroon', 'Cameroon'),
        ('Canada', 'Canada'),
        ('Cape Verde', 'Cape Verde'),
        ('Cayman Islands', 'Cayman Islands'),
        ('Central African Republic', 'Central African Republic'),
        ('Chad', 'Chad'),
        ('Chile', 'Chile'),
        ('China', 'China'),
        ('Christmas Island', 'Christmas Island'),
        ('Cocos (Keeling) Islands', 'Cocos (Keeling) Islands'),
        ('Colombia', 'Colombia'),
        ('Comoros', 'Comoros'),
        ('Congo', 'Congo'),
        ('Congo, The Democratic Republic of The', 'Congo, The Democratic Republic of The'),
        ('Cook Islands', 'Cook Islands'),
        ('Costa Rica', 'Costa Rica'),
        ('Cote D\'ivoire', 'Cote D\'ivoire'),
        ('Croatia', 'Croatia'),
        ('Cuba', 'Cuba'),
        ('Cyprus', 'Cyprus'),
        ('Czech Republic', 'Czech Republic'),
        ('Denmark', 'Denmark'),
        ('Djibouti', 'Djibouti'),
        ('Dominica', 'Dominica'),
        ('Dominican Republic', 'Dominican Republic'),
        ('Ecuador', 'Ecuador'),
        ('Egypt', 'Egypt'),
        ('El Salvador', 'El Salvador'),
        ('Equatorial Guinea', 'Equatorial Guinea'),
        ('Eritrea', 'Eritrea'),
        ('Estonia', 'Estonia'),
        ('Ethiopia', 'Ethiopia'),
        ('Falkland Islands (Malvinas)', 'Falkland Islands (Malvinas)'),
        ('Faroe Islands', 'Faroe Islands'),
        ('Fiji', 'Fiji'),
        ('Finland', 'Finland'),
        ('France', 'France'),
        ('French Guiana', 'French Guiana'),
        ('French Polynesia', 'French Polynesia'),
        ('French Southern Territories', 'French Southern Territories'),
        ('Gabon', 'Gabon'),
        ('Gambia', 'Gambia'),
        ('Georgia', 'Georgia'),
        ('Germany', 'Germany'),
        ('Ghana', 'Ghana'),
        ('Gibraltar', 'Gibraltar'),
        ('Greece', 'Greece'),
        ('Greenland', 'Greenland'),
        ('Grenada', 'Grenada'),
        ('Guadeloupe', 'Guadeloupe'),
        ('Guam', 'Guam'),
        ('Guatemala', 'Guatemala'),
        ('Guernsey', 'Guernsey'),
        ('Guinea', 'Guinea'),
        ('Guinea-bissau', 'Guinea-bissau'),
        ('Guyana', 'Guyana'),
        ('Haiti', 'Haiti'),
        ('Heard Island and Mcdonald Islands', 'Heard Island and Mcdonald Islands'),
        ('Holy See (Vatican City State)', 'Holy See (Vatican City State)'),
        ('Honduras', 'Honduras'),
        ('Hong Kong', 'Hong Kong'),
        ('Hungary', 'Hungary'),
        ('Iceland', 'Iceland'),
        ('India', 'India'),
        ('Indonesia', 'Indonesia'),
        ('Iran, Islamic Republic of', 'Iran, Islamic Republic of'),
        ('Iraq', 'Iraq'),
        ('Ireland', 'Ireland'),
        ('Isle of Man', 'Isle of Man'),
        ('Israel', 'Israel'),
        ('Italy', 'Italy'),
        ('Jamaica', 'Jamaica'),
        ('Japan', 'Japan'),
        ('Jersey', 'Jersey'),
        ('Jordan', 'Jordan'),
        ('Kazakhstan', 'Kazakhstan'),
        ('Kenya', 'Kenya'),
        ('Kiribati', 'Kiribati'),
        ('Korea, Democratic People\'s Republic of', 'Korea, Democratic People\'s Republic of'),
        ('Korea, Republic of', 'Korea, Republic of'),
        ('Kuwait', 'Kuwait'),
        ('Kyrgyzstan', 'Kyrgyzstan'),
        ('Lao People\'s Democratic Republic', 'Lao People\'s Democratic Republic'),
        ('Latvia', 'Latvia'),
        ('Lebanon', 'Lebanon'),
        ('Lesotho', 'Lesotho'),
        ('Liberia', 'Liberia'),
        ('Libyan Arab Jamahiriya', 'Libyan Arab Jamahiriya'),
        ('Liechtenstein', 'Liechtenstein'),
        ('Lithuania', 'Lithuania'),
        ('Luxembourg', 'Luxembourg'),
        ('Macao', 'Macao'),
        ('Macedonia, The Former Yugoslav Republic of', 'Macedonia, The Former Yugoslav Republic of'),
        ('Madagascar', 'Madagascar'),
        ('Malawi', 'Malawi'),
        ('Malaysia', 'Malaysia'),
        ('Maldives', 'Maldives'),
        ('Mali', 'Mali'),
        ('Malta', 'Malta'),
        ('Marshall Islands', 'Marshall Islands'),
        ('Martinique', 'Martinique'),
        ('Mauritania', 'Mauritania'),
        ('Mauritius', 'Mauritius'),
        ('Mayotte', 'Mayotte'),
        ('Mexico', 'Mexico'),
        ('Micronesia, Federated States of', 'Micronesia, Federated States of'),
        ('Moldova, Republic of', 'Moldova, Republic of'),
        ('Monaco', 'Monaco'),
        ('Mongolia', 'Mongolia'),
        ('Montenegro', 'Montenegro'),
        ('Montserrat', 'Montserrat'),
        ('Morocco', 'Morocco'),
        ('Mozambique', 'Mozambique'),
        ('Myanmar', 'Myanmar'),
        ('Namibia', 'Namibia'),
        ('Nauru', 'Nauru'),
        ('Nepal', 'Nepal'),
        ('Netherlands', 'Netherlands'),
        ('Netherlands Antilles', 'Netherlands Antilles'),
        ('New Caledonia', 'New Caledonia'),
        ('New Zealand', 'New Zealand'),
        ('Nicaragua', 'Nicaragua'),
        ('Niger', 'Niger'),
        ('Nigeria', 'Nigeria'),
        ('Niue', 'Niue'),
        ('Norfolk Island', 'Norfolk Island'),
        ('Northern Mariana Islands', 'Northern Mariana Islands'),
        ('Norway', 'Norway'),
        ('Oman', 'Oman'),
        ('Pakistan', 'Pakistan'),
        ('Palau', 'Palau'),
        ('Palestinian Territory, Occupied', 'Palestinian Territory, Occupied'),
        ('Panama', 'Panama'),
        ('Papua New Guinea', 'Papua New Guinea'),
        ('Paraguay', 'Paraguay'),
        ('Peru', 'Peru'),
        ('Philippines', 'Philippines'),
        ('Pitcairn', 'Pitcairn'),
        ('Poland', 'Poland'),
        ('Portugal', 'Portugal'),
        ('Puerto Rico', 'Puerto Rico'),
        ('Qatar', 'Qatar'),
        ('Reunion', 'Reunion'),
        ('Romania', 'Romania'),
        ('Russian Federation', 'Russian Federation'),
        ('Rwanda', 'Rwanda'),
        ('Saint Helena', 'Saint Helena'),
        ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
        ('Saint Lucia', 'Saint Lucia'),
        ('Saint Pierre and Miquelon', 'Saint Pierre and Miquelon'),
        ('Saint Vincent and The Grenadines', 'Saint Vincent and The Grenadines'),
        ('Samoa', 'Samoa'),
        ('San Marino', 'San Marino'),
        ('Sao Tome and Principe', 'Sao Tome and Principe'),
        ('Saudi Arabia', 'Saudi Arabia'),
        ('Senegal', 'Senegal'),
        ('Serbia', 'Serbia'),
        ('Seychelles', 'Seychelles'),
        ('Sierra Leone', 'Sierra Leone'),
        ('Singapore', 'Singapore'),
        ('Slovakia', 'Slovakia'),
        ('Slovenia', 'Slovenia'),
        ('Solomon Islands', 'Solomon Islands'),
        ('Somalia', 'Somalia'),
        ('South Africa', 'South Africa'),
        ('South Georgia and The South Sandwich Islands', 'South Georgia and The South Sandwich Islands'),
        ('Spain', 'Spain'),
        ('Sri Lanka', 'Sri Lanka'),
        ('Sudan', 'Sudan'),
        ('Suriname', 'Suriname'),
        ('Svalbard and Jan Mayen', 'Svalbard and Jan Mayen'),
        ('Swaziland', 'Swaziland'),
        ('Sweden', 'Sweden'),
        ('Switzerland', 'Switzerland'),
        ('Syrian Arab Republic', 'Syrian Arab Republic'),
        ('Taiwan', 'Taiwan'),
        ('Tajikistan', 'Tajikistan'),
        ('Tanzania, United Republic of', 'Tanzania, United Republic of'),
        ('Thailand', 'Thailand'),
        ('Timor-leste', 'Timor-leste'),
        ('Togo', 'Togo'),
        ('Tokelau', 'Tokelau'),
        ('Tonga', 'Tonga'),
        ('Trinidad and Tobago', 'Trinidad and Tobago'),
        ('Tunisia', 'Tunisia'),
        ('Turkey', 'Turkey'),
        ('Turkmenistan', 'Turkmenistan'),
        ('Turks and Caicos Islands', 'Turks and Caicos Islands'),
        ('Tuvalu', 'Tuvalu'),
        ('Uganda', 'Uganda'),
        ('Ukraine', 'Ukraine'),
        ('United Arab Emirates', 'United Arab Emirates'),
        ('United Kingdom', 'United Kingdom'),
        ('United States', 'United States'),
        ('United States Minor Outlying Islands', 'United States Minor Outlying Islands'),
        ('Uruguay', 'Uruguay'),
        ('Uzbekistan', 'Uzbekistan'),
        ('Vanuatu', 'Vanuatu'),
        ('Venezuela', 'Venezuela'),
        ('Viet Nam', 'Viet Nam'),
        ('Virgin Islands, British', 'Virgin Islands, British'),
        ('Virgin Islands, U.S.', 'Virgin Islands, U.S.'),
        ('Wallis and Futuna', 'Wallis and Futuna'),
        ('Western Sahara', 'Western Sahara'),
        ('Yemen', 'Yemen'),
        ('Zambia', 'Zambia'),
        ('Zimbabwe', 'Zimbabwe'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    country = models.CharField(max_length=255, choices=COUNTRY_CHOICES)
    city = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    comment = models.TextField(blank=True)
    aboutus = models.CharField(max_length=20, choices=ABOUT_US_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Contact Us - Inquiry"
        verbose_name_plural = "Contact Us - Inquiries"

class ServiceDCInquiry(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    class Meta:
        verbose_name = "Service Diabetes Consultation - Inquiry"
        verbose_name_plural = "Service Diabetes Consultation - Inquiries"

class ServiceDPInquiry(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    class Meta:
        verbose_name = "Service DC Inquiry"
        verbose_name_plural = "Service DC Inquiries"
    
class ServiceHHInquiry(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    class Meta:
        verbose_name = "Service Men's Health - Inquiry"
        verbose_name_plural = "Service Men's Health - Inquiries"
    
class ServiceKWInquiry(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    class Meta:
        verbose_name = "Service Weight Management - Inquiry"
        verbose_name_plural = "Service Weight Management - Inquiries"
    
class ServiceNCInquiry(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    class Meta:
        verbose_name = "Service Naturopathic Consultations - Inquiry"
        verbose_name_plural = "Service Naturopathic Consultations - Inquiries"
    
class ServiceNDCInquiry(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    class Meta:
        verbose_name = "Service Nutrition and Diet - Inquiry"
        verbose_name_plural = "Service Nutrition and Diet - Inquiries"
    
class ServiceSCInquiry(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    class Meta:
        verbose_name = "Service Senior Care - Inquiry"
        verbose_name_plural = "Service Senior Care - Inquiries"
    
class ServiceWWInquiry(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    class Meta:
        verbose_name = "Service Women Wellness - Inquiry"
        verbose_name_plural = "Service Women Wellness - Inquiries"
    
class ServiceYTInquiry(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    class Meta:
        verbose_name = "Service Yoga Sessions - Inquiry"
        verbose_name_plural = "Service Yoga Sessions - Inquiries"

class AntaraEscapesInquiry(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    class Meta:
        verbose_name = "Antara Escapes - Inquiry"
        verbose_name_plural = "Antara Escapes - Inquiries"