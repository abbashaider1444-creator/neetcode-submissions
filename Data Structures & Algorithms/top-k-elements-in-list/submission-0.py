class Solution:
    def topKFrequent(self, nums, k: int):   

        individual_freq = {}
        for num in nums:
            if num not in individual_freq:
                individual_freq[num] = 0
            individual_freq[num] += 1

        biggest_freq = 0
        grouped_freq = {}
        for num in individual_freq:
            if individual_freq[num] not in grouped_freq:
                grouped_freq[individual_freq[num]] = []
            grouped_freq[individual_freq[num]].append(num)

            if individual_freq[num] > biggest_freq:
                biggest_freq = individual_freq[num]

        groups_list = [0] * (biggest_freq + 1)
        for group in grouped_freq:
            groups_list[group] = grouped_freq[group]

        res = []
        for item in reversed(groups_list):
            if len(res) == k:
                return res
            if item != 0:
                res += item   