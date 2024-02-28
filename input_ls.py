import attlist as att
import webscrapping as ws
import re
def features(url, webcon):
    x = [[]]
    
    try:
        # URL_LENGTH
        x[0].append(len(url))
        
        # WHOIS_REG_YEAR
        reg_year = int(webcon[5][14:18])
        x[0].append(reg_year)

        # UPDATE_YEAR
        update_year = int(webcon[4][14:18])
        x[0].append(update_year)

    except (ValueError, IndexError) as e:
        # If the conversion to int fails due to empty values or IndexError, handle the exception
        # Return a special code (e.g., -1) to signify the error
        x[0].append(-1)  # URL_LENGTH
        x[0].append(-1)  # WHOIS_REG_YEAR
        x[0].append(-1)  # UPDATE_YEAR
        return x

    # WHOIS_COUNTRY
    country_found = False
    for line in webcon:
        try:
            if att.r_country.match(line):
                temp = line.split(': ')
                string = 'WHOIS_COUNTRY--' + temp[1]
                country_found = True
                break
        except AttributeError:
            pass
    
    if country_found:
        for i in range(3, 46):
            if att.li[i] == string:
                x[0].append(1)
            else:
                x[0].append(0)
    else:
        # If the country is not found, fill with zeros
        x[0].extend([0] * 43)

    # WHOIS_STATE_CITY
    state_found = False
    for line in webcon:
        try:
            if att.r_state.match(line):
                temp = line.split(': ')
                string = 'WHOIS_STATE_CITY--' + temp[1]
                state_found = True
                break
        except AttributeError:
            pass
    
    if state_found:
        for i in range(46, 206):
            if att.li[i] == string:
                x[0].append(1)
            else:
                x[0].append(0)
    else:
        # If the state/city is not found, fill with zeros
        x[0].extend([0] * 160)

    # DOMAIN_NAME
    string = 'DOMAIN_NAME--' + url
    for i in range(206, 1139):
        if att.li[i] == string:
            x[0].append(1)
        else:
            x[0].append(0)

    return x
