profit = [
[6, 9, 7, 5, 9],
[4, 7, 3, 10, 9],
[7, 5, 4, 2, 8],
[2, 7, 10, 9, 5],
[2, 5, 2, 6, 1],
[4, 9, 4, 10, 6],
[2, 2, 4, 8, 7],
[4, 10, 2, 7, 4]]
quarantine_time = [3,1,1,1,1]


def column(matrix, i):
    return [row[i] for row in matrix]

print(sum(column(profit[:2],1)))


def get_best_town(profit, quarantine_time, cities, col_totals, cur=0, day=0):
    highest = 0
    total = - 1
    

def best_itinerary(profit, quarantine_time, home):
    # calculate column sum
    col_totals = [ sum(x) for x in zip(*profit) ]
    total = 0
    days = len(profit)
    cities = len(quarantine_time)
    # for i in days:
    get_best_town(profit, quarantine_time, cities, col_totals, home,1)




best_itinerary(profit, quarantine_time, 0)