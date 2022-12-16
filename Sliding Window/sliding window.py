def maximum_sum_subarray_of_size_k(arr, k):
    windowStart = 0
    sum = 0.0
    result = []

    for windowEnd in range(len(arr)):
        sum += arr[windowEnd]

        if windowEnd >= k-1:
            result.append(sum)
            sum -= arr[windowStart]
            windowStart += 1

    return max(result)

def smallest_subarray_with_a_greater_sum(arr, s):
    window_size_min = float('inf')
    window_start = 0
    sum = 0

    for window_end in range(len(arr)):
        sum += arr[window_end]

        while sum >= s:
            window_size_min = min(window_size_min, window_end - window_start + 1)
            sum -= arr[window_start]
            window_start += 1

    return window_size_min

def longest_substring_with_k_distinct_characters(arr, k):
    window_start = 0
    longest_substring = 0
    char_frequency = {}

    for window_end in range(len(arr)):
        if arr[window_end] not in char_frequency:
            char_frequency[arr[window_end]] = 0
        char_frequency[arr[window_end]] += 1

        while len(char_frequency) > k:
            char_frequency[arr[window_start]] -= 1
            if char_frequency[arr[window_start]] == 0:
                del char_frequency[arr[window_start]]
            window_start += 1

        longest_substring = max(longest_substring, window_end - window_start + 1)
    return longest_substring

def fruits_into_baskets(fruit_row):
    window_start = 0
    max_number_of_fruits = 0
    baskets_in_use = {}

    for window_end in range(len(fruit_row)):

        right_pointer = fruit_row[window_end]
        if right_pointer not in baskets_in_use:
            baskets_in_use[right_pointer] = True

        while len(baskets_in_use) > 2:
            left_pointer = fruit_row[window_start]
            del baskets_in_use[left_pointer]
            window_start = window_end - 1

        max_number_of_fruits = max(window_end - window_start + 1, max_number_of_fruits)

    return max_number_of_fruits

def longest_substring_with_distinct_characters(string):
    window_start = 0
    max_number_of_distinct_characters = 0
    characters = {}

    for window_end in range(len(string)):
        current_character = string[window_end]
        if current_character not in characters:
            characters[current_character] = window_end
        else:
            window_start = characters[current_character] + 1
            characters[current_character] = window_end

        max_number_of_distinct_characters = max(max_number_of_distinct_characters, window_end - window_start + 1)
    return max_number_of_distinct_characters

def longest_substring_with_same_letters_after_replacement(string, k):
    window_start = 0
    max_window_size = 0
    character_tracker = {}

    for window_end in range(len(string)):
        right = string[window_end]
        if right not in character_tracker:
            character_tracker[right] = 0
        character_tracker[right] += 1

        left = string[window_start]
        if character_tracker[left] < window_end - window_start + 1 - k:
            character_tracker[left] = 0
            window_start = window_end - k

        max_window_size = max(max_window_size, window_end - window_start + 1)

    return max_window_size

def longest_subarray_with_ones_after_replacement(array, k):
    window_start = 0
    longest_subarray = 0
    zero_tracker = 0

    for window_end in range(len(array)):
        right = array[window_end]

        if right == 0:
            zero_tracker += 1

        while zero_tracker > k:
            left = array[window_start]
            if left == 0:
                zero_tracker -= 1
            window_start += 1
        longest_subarray = max(longest_subarray, window_end - window_start + 1)
    return longest_subarray

def permutation_in_a_string(string, pattern):
    window_start = 0
    hashmap_for_pattern = {}

    # Creates Hashmap containing frequency of values in the desired pattern
    for character in pattern:
        if character not in hashmap_for_pattern:
            hashmap_for_pattern[character] = 0
        hashmap_for_pattern[character] += 1

    # Sliding window algorithm
    for window_end in range(len(string)):
        right = string[window_end]

        if right in hashmap_for_pattern:
            hashmap_for_pattern[right] -= 1

        if sum(hashmap_for_pattern.values()) == 0:
            return True

        if window_end >= len(pattern) - 1:
            left = string[window_start]

            if left in hashmap_for_pattern:
                hashmap_for_pattern[left] += 1
            window_start += 1
    return False

def string_anagrams(string, pattern):
    window_start, matched = 0, 0
    hashmap_for_pattern = {}
    list_of_indices = []

    # Creates Hashmap containing frequency of values in the desired pattern
    for character in pattern:
        if character not in hashmap_for_pattern:
            hashmap_for_pattern[character] = 0
        hashmap_for_pattern[character] += 1

    # Sliding window algorithm
    for window_end in range(len(string)):
        right = string[window_end]

        if right in hashmap_for_pattern:
            hashmap_for_pattern[right] -= 1
            if hashmap_for_pattern[right] == 0:
                matched += 1

        if matched == len(pattern):
            list_of_indices.append(window_start)

        if window_end >= len(pattern) - 1:
            left = string[window_start]

            if left in hashmap_for_pattern:
                if hashmap_for_pattern[left] == 0:
                    matched -= 1
                hashmap_for_pattern[left] += 1
            window_start += 1
    return list_of_indices

# TODO Main part of code
print(permutation_in_a_string("oidbcaf", "abc"))





