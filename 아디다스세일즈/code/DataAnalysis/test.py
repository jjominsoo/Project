
d = 'Men\'s Street FootWear'
temp_d = d.lower()
if 'women' in temp_d:
    if 'footwear' in temp_d:
        if 'athletic' in temp_d:
            new_d = "waf"
        else:
            new_d = "wsf"
    else:
        new_d = "wa"
else:
    if 'footwear' in temp_d:
        if 'athletic' in temp_d:
            new_d = "maf"
        else:
            new_d = "msf"
    else:
        new_d = "ma"

print(new_d)