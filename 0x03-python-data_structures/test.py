#!/usr/bin/python3

class Solution:
    def can_send_request(self, age_x, age_y):
        return not (age_y <= 0.5 * age_x + 7 or age_y > age_x or (age_y > 100 and age_x < 100))

    def num_friend_requests(self, ages):
        total_requests = 0
        for i in range(len(ages)):
            for j in range(len(ages)):
                if i != j and self.can_send_request(ages[i], ages[j]):
                    total_requests += 1
        return total_requests

# Example usage
ages = [16, 16]
solution = Solution()
result = solution.num_friend_requests(ages)
print(result)  # Output will vary based on input data
