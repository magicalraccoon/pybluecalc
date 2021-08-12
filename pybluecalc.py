import eve_simple_esi as esi
import sys

print("Test: Beginning")

user_client = str(sys.argv[1])
user_secret = str(sys.argv[2])

settings={
	'client_id':user_client, #"<Client ID>", # go to https://developers.eveonline.com/ create app and get Client ID
	'client_secret':user_secret, #"<Secret Key>", # go to https://developers.eveonline.com/ create app and get Secret Key
	'client_callback_url':"eveauth-app://callback/", #"<Callback URL>", # default http://localhost:8635/ need to be same as in your app in https://developers.eveonline.com/
	'user_agent':"pybluecalc", #"<User Agent string>",
    # deliberately overscoped
	'scopes':['publicData', 'esi-calendar.respond_calendar_events.v1', 'esi-calendar.read_calendar_events.v1', 'esi-location.read_location.v1', 'esi-location.read_ship_type.v1', 'esi-mail.organize_mail.v1', 'esi-mail.read_mail.v1', 'esi-mail.send_mail.v1', 'esi-skills.read_skills.v1', 'esi-skills.read_skillqueue.v1', 'esi-wallet.read_character_wallet.v1', 'esi-wallet.read_corporation_wallet.v1', 'esi-search.search_structures.v1', 'esi-clones.read_clones.v1', 'esi-characters.read_contacts.v1', 'esi-universe.read_structures.v1', 'esi-bookmarks.read_character_bookmarks.v1', 'esi-killmails.read_killmails.v1', 'esi-corporations.read_corporation_membership.v1', 'esi-assets.read_assets.v1', 'esi-planets.manage_planets.v1', 'esi-fleets.read_fleet.v1', 'esi-fleets.write_fleet.v1', 'esi-ui.open_window.v1', 'esi-ui.write_waypoint.v1', 'esi-characters.write_contacts.v1', 'esi-fittings.read_fittings.v1', 'esi-fittings.write_fittings.v1', 'esi-markets.structure_markets.v1', 'esi-corporations.read_structures.v1', 'esi-characters.read_loyalty.v1', 'esi-characters.read_opportunities.v1', 'esi-characters.read_chat_channels.v1', 'esi-characters.read_medals.v1', 'esi-characters.read_standings.v1', 'esi-characters.read_agents_research.v1', 'esi-industry.read_character_jobs.v1', 'esi-markets.read_character_orders.v1', 'esi-characters.read_blueprints.v1', 'esi-characters.read_corporation_roles.v1', 'esi-location.read_online.v1', 'esi-contracts.read_character_contracts.v1', 'esi-clones.read_implants.v1', 'esi-characters.read_fatigue.v1', 'esi-killmails.read_corporation_killmails.v1', 'esi-corporations.track_members.v1', 'esi-wallet.read_corporation_wallets.v1', 'esi-characters.read_notifications.v1', 'esi-corporations.read_divisions.v1', 'esi-corporations.read_contacts.v1', 'esi-assets.read_corporation_assets.v1', 'esi-corporations.read_titles.v1', 'esi-corporations.read_blueprints.v1', 'esi-bookmarks.read_corporation_bookmarks.v1', 'esi-contracts.read_corporation_contracts.v1', 'esi-corporations.read_standings.v1', 'esi-corporations.read_starbases.v1', 'esi-industry.read_corporation_jobs.v1', 'esi-markets.read_corporation_orders.v1', 'esi-corporations.read_container_logs.v1', 'esi-industry.read_character_mining.v1', 'esi-industry.read_corporation_mining.v1', 'esi-planets.read_customs_offices.v1', 'esi-corporations.read_facilities.v1', 'esi-corporations.read_medals.v1', 'esi-characters.read_titles.v1', 'esi-alliances.read_contacts.v1', 'esi-characters.read_fw_stats.v1', 'esi-corporations.read_fw_stats.v1', 'esi-characterstats.read.v1'], #<list of scopes>, # ['publicData','esi-location.read_location.v1',...etc.]
	'port':8635 #<port for local web server for authorization>, # default 8635
}

ESI=esi.ESI(settings)

# TODO: check to see if a User_Data_*.json file exists already
# 	If not, run the initial GUI Authentication window
# ESI.gui_auth()

print("Client ID: ", user_client)
print("Secret ID: ", user_secret)

####
# TODO: print all manufacturing info for a Rifter:
# https://www.fuzzwork.co.uk/dump/latest/industryActivityMaterials.csv
#  typeID,activityID,materialTypeID,quantity
#  691,1,34,32000 # Tritanium
#  691,1,35,6000  # Pyerite
#  691,1,36,2500  # Mexallon
#  691,1,37,500   # Isogen
#  691,8,20172,2  # copy/invention?
#  691,8,20424,2  # copy/invention?
#
# activityID: https://www.fuzzwork.co.uk/dump/latest/ramActivities.csv
# materialTypeID: May need to be hardcoded
#
# https://stackoverflow.com/questions/16283799/how-to-read-a-csv-file-from-a-url-with-python


print("Printing rifter materials \n")
import csv, urllib.request

bill_of_materials = []
url = 'https://www.fuzzwork.co.uk/dump/latest/industryActivityMaterials.csv'
response = urllib.request.urlopen(url)
lines = [l.decode('utf-8') for l in response.readlines()]
for line in lines:
    if line.startswith('691'):
        bill_of_materials.append(line.strip())
csv_lookup = csv.reader(bill_of_materials)
for item in csv_lookup:
    print(item)
####

print("Test: Completed")