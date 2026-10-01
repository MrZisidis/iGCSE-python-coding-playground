# ---------------------------------------------------------------
# Odontotos Mountain Railway - seat occupancy report
# STAGE 7. This module was written by a previous developer.
# It does not work. Your job is to find out why.
#
# There are FOUR faults. One is a syntax error, one is a runtime
# error, and two are logic errors.
#
# For each fault you must record:
#   - the line number
#   - the type of error (syntax, runtime or logic)
#   - what was wrong
#   - what you changed
#
# Do not rewrite the module from scratch. Fix it.
# ---------------------------------------------------------------

import railway_data

# Seats already sold on each service, in the same order as SERVICES.
SEATS_SOLD = [80, 12, 119, 84, 45, 3, 76, 60, 84, 118]


def occupancy_percentage(sold, total):
    """Return the percentage of seats sold, rounded to a whole number."""
    return round(sold / total * 100)


def is_nearly_full(sold, total):
    """A service is 'nearly full' when 90% or more of its seats are sold."""
    if occupancy_percentage(sold, total) > 90:
        return True
    else:
        return False


def busiest_service():
    """Return the service code of the service with the most seats sold."""
    best_index = 0
    for index in range(1, len(SEATS_SOLD)):
        if SEATS_SOLD[index] < SEATS_SOLD[best_index]:
            best_index = index
    return railway_data.SERVICES[best_index][0]


def print_report():
    """Print one line per service, then a summary."""
    print('SERVICE   ROUTE                      SOLD   SEATS   FULL%')
    print('-' * 56)

    nearly_full_count = 0

    for index in range(0, len(railway_data.SERVICES) + 1):
        service = railway_data.SERVICES[index]
        code = service[0]
        route = service[3] + ' to ' + service[4]
        total = service[5]
        sold = SEATS_SOLD[index]

        percent = occupancy_percentage(sold, total)

        print(code + '      ' + route.ljust(25) + str(sold).rjust(5)
              + str(total).rjust(8) + str(percent).rjust(8) + '%'

        if is_nearly_full(sold, total):
            nearly_full_count = nearly_full_count + 1

    print('-' * 56)
    print('Services nearly full: ' + str(nearly_full_count))
    print('Busiest service: ' + busiest_service())


print_report()
