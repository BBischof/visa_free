# The clusters from Saeedian et. al.

Manually determining the clusters from Saeedian et. al. was an annoying task; not the least of which due to the fact that the number of countries in their clusters(`213`) seems to be a mystery:

- it is not all countries (`223`)
- it is not only the countries in the reciprocal free network (`197`)
- it is not only the countries that have some free status to some country (`223`; all countries)
- it is not only the countries that have some free status from some country (`200`)

For this reason, we expect that the authors have slightly different data for their reciprocal free network. However, we were still able to find their clusters:

```
{
	"first_cluster" : 
		["United States Virgin Islands", "Puerto Rico", "Australia", "Guam", "Northern Mariana Islands", "Canada", "Brunei", "Japan", "Cayman Islands", "Hong Kong", "United States", "Monaco", "Austria", "American Samoa", "New Zealand", "Denmark", "Finland", "Italy", "United Kingdom", "Malta", "Reunion", "Switzerland", "Norway", "Luxembourg", "Portugal", "Germany", "Hungary", "Bahamas", "Spain", "Liechtenstein", "Netherlands", "Lithuania", "Croatia", "Bulgaria", "New Caledonia", "France", "Belgium", "Sweden", "Iceland", "Norfolk Island", "Slovenia", "Slovakia", "Poland", "French Guiana", "Curacao", "Ireland", "Czech Republic", "Latvia", "Greece", "Israel", "Andorra", "Turks and Caicos Islands", "South Korea", "Estonia", "Cyprus", "Venezuela", "French West Indies", "Aruba", "Gibraltar", "Anguilla", "Montserrat", "Chile", "Mayotte", "French Polynesia", "British Virgin Islands", "Mexico", "Uruguay", "El Salvador", "Brazil", "Romania", "Argentina", "Guatemala", "Paraguay", "Vatican City", "Honduras", "Costa Rica", "Nicaragua", "Panama", "Bolivia"],
	"second_cluster" : 
		["Gabon", "Democratic Republic of the Congo", "Botswana", "Swaziland", "Antigua and Barbuda", "Ethiopia", "Kiribati", "Trinidad and Tobago", "Jamaica", "Zimbabwe", "Namibia", "Nauru", "Marshall Islands", "Vanuatu", "Barbados", "Grenada",  "Rwanda", "Saint Vincent and the Grenadines", "Cuba", "Eritrea", "North Korea", "Tonga", "Malaysia", "South Africa", "Saint Kitts and Nevis", "Fiji", "Saint Lucia", "Cook Islands", "Zambia", "Singapore", "Bermuda", "Niue", "Samoa", "Seychelles", "Tanzania", "Bangladesh", "Lebanon", "Burundi",   "Dominica", "Tuvalu", "Maldives", "Kenya", "Belarus", "Mozambique", "Georgia", "Armenia", "Republic of China Taiwan", "Palau", "Comoros", "Azerbaijan", "Pakistan",  "Micronesia", "Macau", "Madagascar", "Jordan",   "Ecuador", "East Timor", "Egypt", "Laos", "Kosovo", "Djibouti", "Iraq", "Vietnam", "Mongolia", "Sri Lanka", "Sao Tome and Principe", "India", "Bhutan", 'Mauritius', 'San Marino', 'Belize', 'Peru', 'Lesotho', 'Colombia', 'Malawi', 'Philippines', 'Guyana', 'Suriname', 'Uganda', 'Thailand', 'Cote dIvoire', 'Haiti', 'Indonesia', 'Togo', 'Dominican Republic', 'Cambodia', 'Nepal'],
	"third_cluster" : 
		["Yemen", "Gambia", "Liberia", "Sierra Leone", "Algeria", "Guinea", "Ghana", "Libya", "Tunisia", "Mauritania", "Guinea-Bissau", "Morocco", "Mali", "Senegal", "Benin", "Niger", "Cape Verde", "Nigeria", "Burkina Faso", "Angola", "Central African Republic", "Cameroon", "Chad", "Republic of the Congo"],
	"fourth_cluster" : 
		["United Arab Emirates", "Kuwait", "Bahrain", "Sudan", "Saudi Arabia", "Oman", "Syria", "Iran", "Montenegro", "Qatar", "Turkey", "Bosnia and Herzegovina", "Albania", "Serbia", "Macedonia", "Tajikistan", "Kazakhstan", "Kyrgyzstan", "Russia", "Moldova", "Ukraine", "Uzbekistan"], 
	"fifth_cluster": 
		["Peoples Republic of China"]
}
```

In particular, there are 16 countries in these clusters that are not part of the reciprocal free network:

```
{ 
	"first_cluster" :
		['Yemen', 'Guinea-Bissau', 'Republic of the Congo'], 
	"second_cluster" :	
		['Gabon', 'Tonga', 'Samoa', 'Seychelles', 'Tuvalu', 'Maldives', 'Comoros', 'Madagascar', 'East Timor', 'Djibouti', 'Iraq', 'Sri Lanka', 'Sao Tome and Principe']
}
```

And there are 9 countries that are not in their clusters:

```
['Papua New Guinea', 'Solomon Islands', 'Equatorial Guinea', 'Somalia', 'South Sudan', 'Afghanistan', 'Myanmar', 'Palestine', 'Turkmenistan']

```

The countries are not in our reciprocal free network are:

```
['Papua New Guinea', 'Samoa', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Comoros', 'Djibouti', 'Equatorial Guinea', 'Gabon', 'Guinea-Bissau', 'Madagascar', 'Republic of the Congo', 'Sao Tome and Principe', 'Seychelles', 'Somalia', 'South Sudan', 'Afghanistan', 'East Timor', 'Iraq', 'Maldives', 'Myanmar', 'Palestine', 'Sri Lanka', 'Turkmenistan', 'Yemen']
```

Note that the 23 countries that have a free status _from_ no country are:

```
['Papua New Guinea', 'Samoa', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Comoros', 'Djibouti', 'Gabon', 'Madagascar', 'Republic of the Congo', 'Sao Tome and Principe', 'Seychelles', 'Somalia', 'South Sudan', 'Afghanistan', 'Iraq', 'Maldives', 'Myanmar', 'Palestine', 'Sri Lanka', 'Turkmenistan', 'Yemen']
```
