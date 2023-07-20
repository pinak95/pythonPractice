class Solution:
    def possible_speed(self, dist: List[int], hour: float, speed: int) -> bool:
        total_time = 0

        for i in range(len(dist) - 1):
            total_time += (dist[i] + speed - 1) // speed

        total_time += dist[-1] / speed

        return total_time <= hour

    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        k = int(1e7)
        left, right = 1, k

        while left <= right:
            mid = (left + right) // 2

            if self.possible_speed(dist, hour, mid):
                right = mid - 1
            else:
                left = mid + 1

        return left if left <= k else -1
