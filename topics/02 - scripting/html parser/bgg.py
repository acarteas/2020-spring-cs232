import urllib
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import datetime
import os
from os.path import isfile, join
import csv
import shutil
import sqlite3


def get_hotness_from_bgg():
    # get BGG hotness data
    # AC Note: may need to update periodically
    geek_url = "http://boardgamegeek.com/geekitem.php?objecttype=thing&instanceid=hotitems&action=hotitems&callback=function%20DoPopupDetails()%0A%7B%0A%09%2F%2Fwait%20for%20the%20DOM%20to%20be%20ready%0A%09popupdetail_collection%20%3D%20new%20PopupDetailCollection(%24%24('.popupdetails')%2C%0A%09%7B%0A%09%09details%3A%20%09popupdetails_hot%2C%0A%09%09template%3A%20%09'popupDetailHTML'%2C%0A%20%20%20%20%20%20%20%20%2F%2Fthe%20rest%20here%20is%20entirely%20optional%0A%20%20%20%20%20%20%20%20popupDetailOptions%3A%20%7B%20%20%20%2F%2Fconfigure%20the%20PopupDetail%20object%0A%20%20%20%20%20%20%20%20%20%20%20%20linkPopup%3A%20true%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20delayOn%3A%20%20%20100%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20delayOff%3A%20%20100%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20stickyWinOptions%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20zIndex%3A%20%20%20%20%20999%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20className%3A%20%20''%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20position%3A%20%20%20'upperRight'%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20offset%3A%20%20%20%20%20%7Bx%3A%205%2C%20y%3A%200%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D)%3B%09%0A%7D&ajax=1"
    response = urllib.request.urlopen(geek_url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")

    # figure out date for file name
    now = datetime.datetime.now()

    # open file for today
    text_file_name = r"unparsed/{0}-{1}-{2}.csv".format(
        now.year, now.month, now.day)
    text_file = open(text_file_name, "w")

    # find all hotness links
    counter = 1
    for link in soup.findAll('a'):
        href = link.get('href')
        text = link.getText().encode('ascii', 'ignore').decode('utf-8')
        urlpieces = href.split('/')
        bgg_id = urlpieces[2]
        if(href.startswith('/boardgame/')):
            text_file.write('"{0}","{1}","{2}","{3}"\n'.format(
                counter, bgg_id, text, href))
            output_str = "{0}. {1}".format(counter, text)
            print(output_str)
            counter += 1

    text_file.close()
    print("parsed", counter, "files.")


def db_import_hotness():
    root_path = r'unparsed'
    parsed_directory = r'parsed'
    try:
        db_conn = sqlite3.connect('bgg.db')
        db_cursor = db_conn.cursor()
    except:
        print("error opening db connection.")
        return
    for item in os.listdir(root_path):
        item_path = join(root_path, item)
        item_name, item_extension = os.path.splitext(item_path)
        file_name = item.split('.')
        file_name = file_name[0]
        if(isfile(item_path) and item_extension == '.csv'):
            csv_file = open(item_path)
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                query = ("INSERT INTO bgg_hotness "
                         "(bgg_id, game_title, hotness_rank, hotness_date) "
                         "VALUES (?, ?, ?, ?)"
                         )
                try:
                    query_data = (row[1], row[2], row[0], file_name)
                    db_cursor.execute(query, query_data)
                    db_conn.commit()
                except sqlite3.Error as e:
                    print("Error making query:", query_data)
                    print("An error occurred:", e.args[0], "\n")
            csv_file.close()
        parsed_path = join(parsed_directory, item)
        shutil.move(item_path, parsed_path)
        print('Done parsing', file_name)
    db_conn.close()


if __name__ == '__main__':
    get_hotness_from_bgg()
    db_import_hotness()
