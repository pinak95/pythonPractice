class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        answer = []

        for incoming in asteroids:

            while answer and incoming < 0 and answer[-1] > 0:
                diff = incoming + answer[-1]
                if diff < 0:
                    answer.pop()
                elif diff > 0:
                    incoming = 0
                else:
                    incoming = 0
                    answer.pop()
            if incoming:
                answer.append(incoming)
        return answer
