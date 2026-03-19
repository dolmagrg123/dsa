def identify_popular_creators(nft_collection):

    popular_count ={}
    list_names =[]

    for di in nft_collection:
        creator_name = di["creator"]

        if creator_name in popular_count:
            popular_count[creator_name] += 1
        else:
            popular_count[creator_name] = 1

    for creator in popular_count:
        if popular_count[creator] > 1:
            list_names.append(creator)
            
    return list_names

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))
    


    

