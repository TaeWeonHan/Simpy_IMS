# Log simulation events
DAILY_EVENTS = []

# Log daily repots: Inventory level for each item; daily change for each item; Remaining demand (demand - product level)
DAILY_REPORTS = []
COST_LOG = []
DEMAND_LOG = []
DAILY_COST_REPORT = {
    'Holding cost': 0,
    'Process cost': 0,
    'Delivery cost': 0,
    'Order cost': 0,
    'Shortage cost': 0
}
ORDER_HISTORY = []
