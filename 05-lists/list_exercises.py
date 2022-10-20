# TODO: Edit the function
def percentage_growth(num_users, yrs_ago):
    target_year = num_users[len(num_users) - 1 - yrs_ago]
    print("target year: ", target_year)
    growth = (num_users[len(num_users)-1] - target_year) / target_year
    # num_users[len(num_users)-yrs_ago])/num_users[len(num_users)-2]
    #print("last year", num_users[len(num_users)-1])
    return growth


# Do not change: Variable for calculating some test examples
num_users_test = [920344, 1043553, 1204334, 1458996,
                  1503323, 1593432, 1623463, 1843064, 1930992, 2001078]

# Do not change: Should return .036
# print(percentage_growth(num_users_test, 1))

# Do not change: Should return 0.66
print(percentage_growth(num_users_test, 7))

'''
def percentage_liked(ratings):
    list_liked = [i >= 4 for i in ratings]
    print(list_liked)
    # TODO: Complete the function
    percentage_liked = list_liked.count(True) / len(list_liked)
    return percentage_liked

# Do not change: should return 0.5
percentage_liked([1, 2, 3, 4, 5, 4, 5, 1])

print(percentage_liked([1, 2, 3, 4, 5, 4, 5, 1]))
'''
