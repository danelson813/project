from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import sqlite3
from sqlite3 import connect
import pandas as pd

def initialize_webdriver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')   
    return webdriver.Chrome(options=chrome_options)


def get_soup(url):
    driver = initialize_webdriver()

    driver.get(url)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    return soup

def send_to_sqlite3(df):
    conn = connect('data/football.db')
    df.to_sql(name='passing', con=conn, if_exists="replace", index=False)
    conn.close()


def read_the_sqlite3(filename):
    conn = sqlite3.connect('data/football.db')
    res = pd.read_sql_query("SELECT * FROM passing", conn)
    conn.close()
    
    return res