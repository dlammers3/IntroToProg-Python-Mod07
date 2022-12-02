# ----------------------------------------------------------- #
# Title: FavCookie
# Description: Favorite cookie survey program that utilizes pickling and structured error handling
# Changelog: (Who, When, What)
# DLammers, 11/29/2022, created the script
# DLammers, 12/2/2022, finalized script
# ----------------------------------------------------------- #

import pickle

"""
Favorite Cookie Tally
Define the variables that will be used
Read the data
Ask the user for input
Display the user input back to the user
Save the data to the .pkl file (on reload the previous save data needs to be visible)
"""
# --- Data
cookiejar_init = {'Chocolate Chip': 0 , 'Peanut Butter': 0 , 'Oatmeal': 0} # initial cookie tally
file_name = 'cookies.pickle' # pickled file that will store the tally dictionary

try:
    # --- Read in the data
    file_in = open(file_name, 'rb')
    cookie_counter = pickle.load(file_in)
    file_in.close()
except FileNotFoundError:
    # --- Reinitialization
    file_out = open(file_name, 'wb')
    pickle.dump(cookiejar_init, file_out)
    file_out.close()

# --- Read in the data
file_in = open(file_name, 'rb')
cookie_counter = pickle.load(file_in)
file_in.close()

# --- User Input
print("This survey is collecting data on everyone's favorite cookie... \n  between the three choices given "
      "at least ;) \n\nThink of the best versions of each of these cookies that you have ever had. \nThink of "
      "the smell, the taste, the texture, \nthe feeling you had while you were eating it. Now...")
print()  # printing a blank line to make it pretty
cookie = input('\nBetween the three cookie options,\n    Chocolate Chip [1] \n    Peanut Butter [2] \n    '
               'Oatmeal [3]'
               '\n\nWhich cookie is your favorite? (Enter the corresponding number): ')

# --- Processing
if cookie == '1':
    count = int(cookie_counter['Chocolate Chip'])
    count += 1
    cookie_counter['Chocolate Chip'] = count
elif cookie == '2':
    count = int(cookie_counter['Peanut Butter'])
    count += 1
    cookie_counter['Peanut Butter'] = count
elif cookie == '3':
    count = int(cookie_counter['Oatmeal'])
    count += 1
    cookie_counter['Oatmeal'] = count
else: print('You have entered an option that does not exist, try again.')

# --- Show user the output
print()  # printing a blank line to make it pretty
print('So far the tally is: ')
print(cookie_counter)
print()  # printing a blank line to make it pretty
print("Thank you for participating in the survey. Now go get a cookie!")

# --- Save Data To File
file_out = open(file_name, 'wb')
pickle.dump(cookie_counter, file_out)
file_out.close()



