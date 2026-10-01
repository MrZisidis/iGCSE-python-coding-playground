# ---------------------------------------------------------------
# Odontotos Mountain Railway - booking system
# GIVEN DATA FILE. Do not change anything in this file.
# Import it into your own program with:  import railway_data
# ---------------------------------------------------------------
# The timetable below is simplified and invented for this task.
# It is not the real published timetable. Do not use it to plan a
# day out, unless you enjoy standing on an empty platform.
# ---------------------------------------------------------------

# Each service is a row:
#   [0] service code
#   [1] departure time (24 hour, as a string)
#   [2] arrival time
#   [3] from
#   [4] to
#   [5] seats on the train
SERVICES = [
    ['OD01', '07:15', '08:20', 'Diakofto',  'Kalavryta', 84],
    ['OD02', '09:05', '10:10', 'Diakofto',  'Kalavryta', 84],
    ['OD03', '11:00', '12:05', 'Diakofto',  'Kalavryta', 120],
    ['OD04', '13:40', '14:45', 'Diakofto',  'Kalavryta', 84],
    ['OD05', '16:20', '17:25', 'Diakofto',  'Kalavryta', 120],
    ['OD06', '08:40', '09:45', 'Kalavryta', 'Diakofto',  84],
    ['OD07', '10:30', '11:35', 'Kalavryta', 'Diakofto',  84],
    ['OD08', '12:25', '13:30', 'Kalavryta', 'Diakofto',  120],
    ['OD09', '15:10', '16:15', 'Kalavryta', 'Diakofto',  84],
    ['OD10', '17:45', '18:50', 'Kalavryta', 'Diakofto',  120],
]

# Ticket prices in euros, by ticket type.
PRICES = [
    ['adult',   14.00],
    ['child',    7.00],
    ['senior',  10.50],
    ['family',  38.00],
]

# The two stations on the line, plus the request stop in the gorge.
STATIONS = ['Diakofto', 'Zachlorou', 'Kalavryta']

# Maximum passengers on one booking.
MAX_PARTY_SIZE = 6
