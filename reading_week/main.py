import json

# Countries in each continent
africa = [
    "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi",
    "Cabo Verde", "Cameroon", "Central African Republic", "Chad",
    "Comoros", "Congo, Republic of the", "Congo, Democratic Republic of the",
    "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia",
    "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Ivory Coast",
    "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi",
    "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia",
    "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe", "Senegal",
    "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan",
    "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"
]

asia = [
    "Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh",
    "Bhutan", "Brunei", "Cambodia", "China", "Cyprus", "Georgia",
    "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan",
    "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", "Malaysia",
    "Maldives", "Mongolia", "Myanmar", "Nepal", "North Korea", "Oman",
    "Pakistan", "Palestine", "Philippines", "Qatar", "Saudi Arabia",
    "Singapore", "South Korea", "Sri Lanka", "Syria", "Tajikistan",
    "Thailand", "Timor-Leste", "Turkmenistan", "United Arab Emirates",
    "Uzbekistan", "Vietnam", "Yemen"
]

europe = [
    "Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus",
    "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus",
    "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Georgia",
    "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Latvia",
    "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco",
    "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland",
    "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia",
    "Slovenia", "Spain", "Sweden", "Switzerland", "Ukraine", "United Kingdom",
    "Vatican City"
]

north_america = [
    "Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada",
    "Costa Rica", "Cuba", "Dominica", "Dominican Republic", "El Salvador",
    "Grenada", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico",
    "Nicaragua", "Panama", "Saint Kitts and Nevis", "Saint Lucia",
    "Saint Vincent and the Grenadines", "United States"
]

oceania = [
    "Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia",
    "Nauru", "New Zealand", "Palau", "Papua New Guinea", "Samoa",
    "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu"
]

south_america = [
    "Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador",
    "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"
]

def check_continent(country):
    if country in africa:
        return 'Africa'
    elif country in asia:
        return 'Asia'
    elif country in europe:
        return 'Europe'
    elif country in north_america:
        return 'North America'
    elif country in oceania:
        return 'Oceania'
    elif country in south_america:
        return 'South America'
    else:
        return 'Unknown'

data = []

with open('data.json') as f:
    data = json.load(f)

no_pending = 0
no_active = 0
no_inactive = 0
countries = []
country_stats = []

continents = []
continent_stats = []

for user in data:
    if user['enrolment_status'] == 'pending':
        no_pending += 1
    elif user['enrolment_status'] == 'active':
        no_active += 1
    else:
        no_inactive += 1
    if user['country'] not in countries:
        countries.append(user['country'])
        country_stats.append({'name': user['country'], 'count': 1})
    else:
        country_stats[countries.index(user['country'])]['count'] += 1
    continent = check_continent(user['country'])
    if continent not in continents:
        continents.append(continent)
        continent_stats.append({'name': continent, 'count': 1})
    else:
        continent_stats[continents.index(continent)]['count'] += 1

print(f'There are {no_pending} users who are pending enrolment')
print(f'There are {no_active} users who are enrolled')
print(f'There are {no_inactive} users who are not enrolled')

print("")

country_stats.sort(key=lambda x: x['count'], reverse=True)
print("Top 10 countries by enrolment status:")

for i in range(10):
    print(f'{i+1}: {country_stats[i]['name']} ({country_stats[i]["count"]})')

print("")

continent_stats.sort(key=lambda x: x['count'], reverse=True)
print("Continents by enrolment status:")

for i in continent_stats:
    print(f'{i['name']}: {i["count"]}')
