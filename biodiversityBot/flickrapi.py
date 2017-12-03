import json
import requests
import flickr_config

endpoint = "https://api.flickr.com/services/rest/"
api_key = flickr_config.api_key
method = "flickr.photos.search"
format = "json"
tags = "bookcollectionbiodiversity"  
per_page = 500
sort="interestingness-asc"

params = {
    "api_key": api_key,
    "method": method,
    "format": format,
    "tags": tags,
    "per_page": per_page,
    "sort": sort
    }

photo_url_template = "https://farm{farm_id}.staticflickr.com/{server_id}/{id}_{secret}.jpg"

r = requests.get(endpoint, params=params)
if r.status_code == 200:
    try:
        response_text = r.text[14:-1]
        data = json.loads(response_text)
        photos = data["photos"]["photo"]
        allPhoto = []


        for photo in photos:
            photo_url = photo_url_template.format(
                id=photo["id"],
                server_id=photo["server"],
                farm_id=photo["farm"],
                secret=photo["secret"],
                time = photo["title"]
            )
            photo["url"] = photo_url
            wanted_keys = ["title", "url"]
            photo = {k: photo[k] for k in set(wanted_keys) & set(photo.keys())}
            allPhoto.append(photo)

        with open('biodiv.json', 'w') as out:
            json.dump(allPhoto, out)

    except ValueError:
        print('Catching ValueError...')
        print('Request URL: ', r.url)
        print('Encoding: ', r.encoding)
        print('Content type: ', r.headers['content-type'])
        with open('bad_output.txt', 'w') as out:
            json.dump(r.text, out)
else:
    print('Bad status code: ', r.status_code)
    print('Request URL: ', r.url)