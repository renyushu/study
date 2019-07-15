# word = 'friends'
# find_evil = word[0] + word[2:6]
# print(find_evil)

word = 'friends'
find_the_evil_in_your_friends = word[0] + word[2:4] + word[-3:-1]
print(find_the_evil_in_your_friends)

phone_number = '144-1444-4444'
hiding_number = phone_number.replace(phone_number[0:9], '*' * 9)
print(hiding_number)
phone_number.find()