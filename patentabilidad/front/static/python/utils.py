def parse_input(request_input):
    query_input =  request_input.get("query_input", None)
    search_parameters = {
        "patents": bool(request_input.get("patents", None)),
        "papers": bool(request_input.get("papers", None)),
        }
    return query_input, search_parameters

    