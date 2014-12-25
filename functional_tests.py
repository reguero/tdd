from selenium import webdriver

browser = webdriver.Firefox()

# Edith has heard about a cool new online to-do app. She goes
# to check out its homepage
browser.get('http://localhost:8000')

# She notices the page title and header mention to-do lists
assert 'To-Do' in browser.title

# She is invited to enter a to-do list straight away.

# She types "Buy peacock feathers" into a text bos (Edith's hobby
# is tying fly-fishing lures)

# When she its enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list

# Edith wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for here -- there is some
# explanatoryu text to that effect.

# She visits that URL - her to-do list is still there.

# Satisfied, she goes back to sleep

browser.quit()
