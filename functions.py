from pandas import DataFrame

def best_matches(data=None, markets_to_be_matched=None, id_variable=None, date_variable=None,
                          matching_variable=None, parallel=TRUE, warping_limit=1, start_match_period=None,
                          end_match_period=None, matches=5, dtw_emphasis=1):
    ## Nulling to avoid angry notes
    match = None
    id = None
    date = None
    shortest_distances = None
    market_id = None
    matching_metric = None
    data = DataFrame()
    return shortest_distances, data, market_id, matching_metric, date 


def lagp(x, p):
    """

    :param x: ???
    :param p: ???
    :return:
    """
    #return (c(rep(0, p), x[1:(length(x) - p)]))


def cmean(b):
    """
    TODO: See if there is an existing function for this
    
    :param b: ??? Great naming.... 
    :return: 
    """
    if len(b) > 0:
        return mean(b)
    return 0


def calculate_distances(all_markets, data, id, i, warping_limit, matches, dtw_emphasis):
    skip = None
    relative_distance = None
    correlation = None
    w = None
    distance_rank = None
    correlation_rank = None
    combined_rank = None
    

def check_inputs(data, id, matching_variable, date):
    """
    Probably not needed
    :param data:
    :param id:
    :param matching_variable:
    :param date:
    :return:
    """
    return


def dw(y, yhat):
    """

    :param y:
    :param yhat:
    :return:
    """
    result = y - yhat
    lagres = lagp(result, 1)
    #r < - stats::cor(res[2:length(res)], lagres[2:length(lagres)])
    return (2 * (1-r))