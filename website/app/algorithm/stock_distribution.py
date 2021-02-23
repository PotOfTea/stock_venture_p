import json


def prorated(allocation_amount: str, average_amount: str, total: float) -> float:
    return float(allocation_amount) * (float(average_amount) / float(total))


def actual_investment(prorated_stock: float, requested_stock: float) -> float:
    if prorated_stock >= requested_stock:
        return requested_stock
    else:
        return prorated_stock


def distribute_stocks(json_data: json) -> json:
    """Calculate stock distribution
    1. Investors are divided in 2 groups:
        * Group A who request stock less or equal amount then they can have©
        * Group B who request more stock then they have
    2. Group A stock allocation is calculated and subtracted from overall pool
    3. Group B stock allocation is calculated on remaining stocks

    This method should run in O(N) linear time
    """

    allocation_amount = json_data["allocation_amount"]
    basis_total = 0
    investors_more_list = []
    investors_match_list = []
    investors_more_basis_total = 0
    processed_stocks = 0
    results = {}

    """
    Investors division in to group A/B
    """
    for investor in json_data["investor_amounts"]:
        basis_total += investor["average_amount"]
        if investor["requested_amount"] > investor["average_amount"]:
            investors_more_list.append(investor)
            investors_more_basis_total += investor["average_amount"]
        else:
            investors_match_list.append(investor)

    """
    Group A stock calculations
    """
    for inv in investors_match_list:
        prorated_value = prorated(allocation_amount, inv["average_amount"], basis_total)

        stock_results = actual_investment(prorated_value, inv["requested_amount"])

        results[inv["name"]] = stock_results

        processed_stocks += stock_results

    allocation_amount -= processed_stocks

    """
    Group B remaining stock calculation
    """
    for inv in investors_more_list:
        prorated_value = prorated(allocation_amount, inv["average_amount"], investors_more_basis_total)
        stock_results = actual_investment(prorated_value, inv["requested_amount"])
        results[inv["name"]] = stock_results

    return results
