def return_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    char_count = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def list_sort(dict):
    list_dict = [{'character': key, 'count': value} for key, value in dict.items()]
    sorted_dict = sorted(list_dict, key=lambda x: x['count'], reverse=True)
    return sorted_dict