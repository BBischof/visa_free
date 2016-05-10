import sys, re, os, json

def create_continents_dictionary():
  conts = {"Africa" : ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Cape Verde", "Central African Republic", "Chad", "Comoros", "Cote dIvoire", "Democratic Republic of the Congo", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Republic of the Congo", "Rwanda", "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "Asia" : ["Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei", "Cambodia", "East Timor", "French Polynesia", "Guam", "Hong Kong", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", "Macau", "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", "North Korea", "Northern Mariana Islands", "Oman", "Pakistan", "Palestine", "Peoples Republic of China", "Philippines", "Qatar", "Republic of China Taiwan", "Russia", "Saudi Arabia", "Singapore", "South Korea", "Sri Lanka", "Syria", "Tajikistan", "Thailand", "Turkmenistan", "United Arab Emirates", "Uzbekistan", "Vietnam", "Yemen"], "Europe" : ["Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany", "Gibraltar", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Macedonia", "Malta", "Mayotte", "Moldova", "Monaco", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Reunion", "Romania", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "United Kingdom", "Vatican City"], "North America" : ["Anguilla", "Aruba", "Bermuda", "British Virgin Islands", "Canada", "Cayman Islands", "Curacao", "French West Indies", "Mexico", "Montserrat", "Turks and Caicos Islands", "United States Virgin Islands", "United States"], "Central America and the Antilles" : ["Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Costa Rica", "Cuba", "Dominica", "Dominican Republic", "El Salvador", "Grenada", "Guatemala", "Haiti", "Honduras", "Jamaica", "Nicaragua", "Panama", "Puerto Rico", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Trinidad and Tobago", "Turks and Caicos Islands"], "South America" : ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "French Guiana", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"], "Oceania" : ["American Samoa", "Australia", "Cook Islands", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru", "New Caledonia", "New Zealand", "Niue", "Norfolk Island", "Palau", "Papua New Guinea", "Samoa", "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu" ]}
  lookup_conts = {}
  for cont in conts:
    for i,country in enumerate(conts[cont]):
      country_rank = (float(i+1))/len(conts[cont])
      lookup_conts[country] = (cont, country_rank)
  return lookup_conts

def parse_lines_into_links(filename, cont_dict):
  '''out_United_States'''
  source_name = " ".join(re.sub(r'out_','',filename).split("_"))[12:]
  source = {"name": source_name, "continent": cont_dict[source_name][0], 'y': cont_dict[source_name][1]}
  d = {}
  link_types = {"free":[], "required": [], "onarrival": [], "refused": []}
  for i,line in enumerate(open(filename).readlines()):
    line = line.rstrip()
    if (i%3==0):
      target_name = line.replace("'", "").replace("&#039;", "").replace("(Taiwan)", "Taiwan").replace("\xc3\xa7", "c")
      target = {"name": target_name, "continent": cont_dict[target_name][0], 'y': cont_dict[target_name][1]}
    elif (i%3==1):
      status = line.split(":")[0].split("-")[1]
      term = line.split(":")[1].rstrip() if len(line.split(":"))>1 else ""
    else:
      notes = line.split(":")[1] if len(line.split(":"))>1 else ""
      link_types[status].append({"source": source, "target": target, "term": term, "notes": notes})
  return link_types

def main(data_folder):
  nodes = []
  countries = create_continents_dictionary()
  for x in countries:
    nodes.append({"name": x, "continent": countries[x][0], "y": countries[x][1]})
  files = os.listdir(data_folder)
  links = {"free":[], "required": [], "onarrival": [], "refused": []}
  for f in files:
    out = parse_lines_into_links("output_data/" + f, countries)
    for s in links:
      links[s] += out[s]
  return json.dumps({"nodes": nodes, "links": links["onarrival"]}) 

if __name__=="__main__":
  print main(sys.argv[1])
  # print create_continents_dictionary()