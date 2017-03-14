from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from anagrams import get_anagrams

USER = ""
PASSW = ""
BOGGLE_URL = "http://www.wordplays.com/boggle"

# Install ublock origin - without ublock it's unbearably slow - thanks Obama
opts = Options()
opts.add_extension('ublock.crx')

driver = webdriver.Chrome(chrome_options=opts)
driver.get(BOGGLE_URL)

# Go to sign in form
signin = driver.find_element_by_id("signin")
signin.click()

# Sign in
userid_field = driver.find_element_by_id("userid")
passw_field = driver.find_element_by_id("pwd")

userid_field.send_keys(USER)
passw_field.send_keys(PASSW)

driver.find_element_by_name("signin").click()

# Go back to boggle
driver.get(BOGGLE_URL)

puzzle = driver.find_element_by_id("pzl")
buttons = driver.find_elements_by_xpath("//table[@id='pzl']/tbody/tr/td/input[@type='button']")
letters = ''.join([x.get_attribute("value") for x in buttons])

anagrams = get_anagrams(letters)

clock = driver.find_element_by_id("clock")
ans_input = driver.find_element_by_id("answer")
solve_btn = driver.find_element_by_id("solvenow")

# Start solving
for anagram in sorted(anagrams, key=len, reverse=True):
    ans_input.send_keys(anagram)
    entered = ans_input.get_attribute("value")

    if entered.lower() != anagram.lower():
        ans_input.clear()
    else:
        ans_input.send_keys(Keys.RETURN)

    if clock.get_attribute("value") == " :0:01":
        break

print("Finished")
solve_btn.click()
