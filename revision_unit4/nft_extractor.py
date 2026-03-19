

def extract_nft_names(nft_collection:list) -> list:
 
    names = [] #create a new list
    for n in nft_collection:
        values = n["name"]  #extract all the names in the dictionary
        names.append(values)
    return names


nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]
print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))
#Time O(n)

#Space O(n)